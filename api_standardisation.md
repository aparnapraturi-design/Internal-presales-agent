# API Standardisation (Frontend Contract)

This backend generates/refines report sections asynchronously.
The frontend starts a job and then **polls using the same Request-Id**.

> **Important:** Job state is stored **in-memory** only.
> If the backend restarts, all request state is lost.

---

## Base URL
Provided per environment (dev/staging/prod).

---

## Common Response Envelope

All responses follow:

```json
{
  "status": "ok|processing|ready|busy|error",
  "message": "human readable message",
  "data": {}
}
```

### Status meanings
- `processing`: queued or in progress
- `busy`: currently executing (same as processing but explicitly “running”)
- `ready`: completed successfully
- `error`: failed

---

## Required Headers

Every request must include:

1) `X-API-Key`  
   Auth token for the API.

2) `Session-Id`  
   A frontend-generated session identifier.  
   - Must be included even on the *first* request.
   - Same value should be reused for all section calls in the same report workflow.

3) `Request-Id`  
   A frontend-generated request identifier (idempotency + polling).  
   - New `Request-Id` for a new job.
   - Same `Request-Id` reused for polling that job.

Example:

```
X-API-Key: <key>
Session-Id: session_123
Request-Id: req_001
```

---

## Error Format

Errors are returned as:
- HTTP 4xx/5xx
- `status="error"`
- `data.error_code` included

Example:

```json
{
  "status": "error",
  "message": "Session-Id is required",
  "data": {
    "error_code": "BAD_REQUEST",
    "path": "/generate"
  }
}
```

Validation errors (HTTP 422) include `data.details` (Pydantic error list).

---

## Report Sections (Allowed Values)

`section_title` MUST be one of the allowed section titles for the given report `type`.
Backend validates this even if the frontend enforces it.

### Feasibility_report
Allowed `section_title` values (canonical):

- `Executive Summary`
- `Project Overview`
- `Business Requirements`
- `Technical Assessment`
- `Resource Assessment`
- `Cost-Benefit Analysis`
- `Risk Assessment`
- `Alternative Solutions`
- `Timeline Feasibility`
- `Stakeholder Analysis`
- `Recommendations`
- `Appendix`

### Technical_scope
Allowed `section_title` values (canonical):

- `Executive Summary`
- `Company Background`
- `Current State Analysis`
- `Requirements Overview`
- `Proposed Solution`
- `Technology Stack`
- `Integration Points`
- `Security & Compliance`
- `Implementation Timeline`
- `Resource Requirements`
- `Risks & Mitigations`
- `Assumptions & Dependencies`

### Commercial_proposal
Allowed `section_title` values:
- (TBD)

---

## Endpoints

### 1) POST `/generate`

Starts generation of a report section.

**Headers**
- `X-API-Key` (required)
- `Session-Id` (required)
- `Request-Id` (required)

**Body**
```json
{
  "type": "Feasibility_report|Technical_scope|Commercial_proposal",
  "customer_id": "string",
  "opportunity_id": "string",
  "section_title": "string (must be allowed for type)"
}
```

**Response (initial call)**
HTTP 202

```json
{
  "status": "processing",
  "message": "Queued",
  "data": {
    "ready": false,
    "request_id": "req_001",
    "session_id": "session_123"
  }
}
```

#### Polling `/generate`
To poll, **send the same request again** with the same `Request-Id`.
Backend will return one of:

**Busy**
```json
{
  "status": "busy",
  "message": "Request is busy",
  "data": { "ready": false, "request_id": "req_001" }
}
```

**Processing**
```json
{
  "status": "processing",
  "message": "Generating...",
  "data": { "ready": false, "request_id": "req_001" }
}
```

**Ready**
```json
{
  "status": "ready",
  "message": "Draft ready",
  "data": {
    "ready": true,
    "request_id": "string",
    "customer_id": "string",
    "opportunity_id": "string",
    "section_title": "string",
    "generated_section_b64": "string"
  }
  }

```

**Error**
```json
{
  "status": "error",
  "message": "Error message",
  "data": {
    "ready": false,
    "request_id": "req_001",
    "error_code": "INTERNAL_ERROR"
  }
}
```

---

### 2) POST `/refine`

Starts refinement of an existing section.

**Headers**
- `X-API-Key` (required)
- `Session-Id` (required)
- `Request-Id` (required)

**Body**
```json
{
  "type": "Feasibility_report|Technical_scope|Commercial_proposal",
  "customer_id": "string",
  "opportunity_id": "string",
  "section_title": "string (must be allowed for type)",
  "original_text": "string (markdown/text)",
  "prompt": "string"
}
```

**Response**
Same as `/generate` (HTTP 202 initially, then poll by resending with same `Request-Id`).

**Ready response (example)**
```json
{
  "status": "ready",
  "message": "Refined text ready",
  "data": {
    "ready": true,
    "request_id": "string",
    "customer_id": "string",
    "opportunity_id": "string",
    "section_title": "string",
    "refined_section_b64": "string"
  }
}
```

---

## Polling Guidance (Frontend)

- Poll by resending the same POST (`/generate` or `/refine`) with the same `Request-Id`.
- Suggested backoff:
  - Start at 1s, then 2s, 3s, 5s … up to 10s max.
- Suggested timeout:
  - 3–10 minutes depending on model / workload.
- If backend returns 404 / loses job state (restart), treat as expired and re-submit using a new `Request-Id`.

---

## Notes / Gotchas

1) **No persistence:** In-memory only. Restart wipes request state.
2) **Request-Id is the job key:** Reusing it returns the same job status/result.
3) **Session-Id required always:** The first call must include it.
4) **Report type values:** Use exactly:
   - `Feasibility_report`
   - `Technical_scope`
   - `Commercial_proposal`
