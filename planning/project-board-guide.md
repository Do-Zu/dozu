# Dozu local-first desktop delivery

The board manages 44 linked GitHub issues: 4 tickets and 40 implementation/verification tasks. The full Next.js frontend, Express backend, PostgreSQL/pgvector, files/jobs and FastAPI run locally. Genuine third-party integrations may use the internet; no central Dozu backend, cloud database or synchronization is required.

## Fields
| Field | Meaning |
| --- | --- |
| Status | Existing workflow columns, preserved |
| Priority | P0 architecture/foundation unblockers; P1 required features/integrations/release; P2 supporting work later; P3 optional/future only if explicitly added |
| Complexity | S contained; M moderate; L cross-system/native/security; XL umbrella/uncertain work to break down |
| Phase | Delivery phase |
| Depends on | Linked prerequisite issues |
| Blocker | Specific unresolved decision/impediment, or None |
| Labels | Task/ticket type and detailed issue status (ready/waiting/review, etc.) |
| Assignees | Actual owner; unassigned until somebody takes the work |

Complexity estimates are provisional, not days or deadlines. Priority does not remove required features from release scope.

## Status columns
- Todo: planned, ready or waiting on normal prerequisites. Issue labels distinguish ready/waiting/backlog.
- Need Clarify: available for questions requiring a response.
- In Progress: active implementation or review. The issue label distinguishes in-review.
- Block: a specific impediment/decision prevents progress; read Blocker.
- Done: closed items. Only closed-as-completed issues with acceptance evidence count as completed work; cancellation is not completion.

Task #2 requirements and #3 audit are completed. The user's 2026-11-10 decisions keep #41 payments explicitly blocked/deferred and select LAN participants for #43 classrooms. #43 now waits on normal prerequisites; its topology-choice blocker is resolved. #27 tracks integration proof. Use the [current local dashboard](task-dashboard.md) and live issue labels for ready work.

## Maintenance
Assign an owner when work starts, link implementation/review evidence, and close as completed only after acceptance checks. No owners or dates are invented.

Built-in Labels/Assignees reflect their issues. Custom Status/Priority/Complexity are independent Project fields: they are populated consistently with issue labels, but no automatic two-way synchronization is configured. Update corresponding labels too if using label-based views.

The local populate-project-board.ps1 command adds missing items/fields and preserves existing board values by default. Its -RefreshFromIssues option deliberately replaces board values from current issue labels. It never assigns owners, closes issues, changes views/columns or enables automatic workflows.

[Full roadmap and checklist](https://github.com/Do-Zu/dozu/issues/1).

