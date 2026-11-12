# Reading and updating GitHub task tracking

Use your [Project #6 board](https://github.com/orgs/Do-Zu/projects/6) for day-to-day management, or the [GitHub Issues list](https://github.com/Do-Zu/dozu/issues) for label-based filtering. Each of the 44 issues has:
- Type: `task` or `ticket`.
- Exactly one `status:...` label.
- Exactly one `priority:P0/P1/P2/P3` label.
- Exactly one `complexity:S/M/L/XL` label.
- An Assignee when somebody actively owns the work.
- Explicit prerequisite links and acceptance criteria.

## Live views
| View | Open directly |
| --- | --- |
| Doing now | [In progress](https://github.com/Do-Zu/dozu/issues?q=is%3Aissue%20is%3Aopen%20label%3A%22status%3Ain-progress%22) |
| Review / verification | [In review](https://github.com/Do-Zu/dozu/issues?q=is%3Aissue%20is%3Aopen%20label%3A%22status%3Ain-review%22) |
| Can start | [Ready](https://github.com/Do-Zu/dozu/issues?q=is%3Aissue%20is%3Aopen%20label%3A%22status%3Aready%22) |
| Specific impediment or decision | [Blocked](https://github.com/Do-Zu/dozu/issues?q=is%3Aissue%20is%3Aopen%20label%3A%22status%3Ablocked%22) |
| Ordinary unfinished prerequisites | [Waiting](https://github.com/Do-Zu/dozu/issues?q=is%3Aissue%20is%3Aopen%20label%3A%22status%3Awaiting%22) |
| Highest current priority | [P0](https://github.com/Do-Zu/dozu/issues?q=is%3Aissue%20is%3Aopen%20label%3A%22priority%3AP0%22) |
| Needs breakdown / uncertainty review | [XL](https://github.com/Do-Zu/dozu/issues?q=is%3Aissue%20is%3Aopen%20label%3A%22complexity%3AXL%22) |

These links query GitHub's current issue labels. Your Project #6 additionally has Status, Priority, Complexity, Phase, Depends on and Blocker fields. No background automation or automatic two-way synchronization was installed. Built-in Labels and Assignees reflect their issues, but changing custom board fields does not automatically update issue labels. If you use both views, update their matching values deliberately.

The existing board columns are preserved: Todo contains ready/waiting/backlog items; In Progress contains active/review items; Block contains specific impediments; Done contains closed items. Need Clarify remains available for your use. Issue status labels distinguish Ready from Waiting within Todo, and distinguish completed from other closed items. Do not count a canceled issue as completed work.

The population command adds missing items/fields and preserves populated board values by default:
```powershell
.\planning\populate-project-board.ps1
# Deliberate overwrite from current issue labels, only when wanted:
.\planning\populate-project-board.ps1 -RefreshFromIssues
```

Assignees remain empty until a real owner takes a task; no owners or dates are invented. All original board columns, views and unrelated items are preserved.

## Status
| Label | Meaning |
| --- | --- |
| status:backlog | Planned or umbrella tracking item; not actively being executed |
| status:ready | All declared prerequisites completed; available to start |
| status:waiting | Normal planned prerequisite work remains |
| status:in-progress | Work has actually started; assign a responsible owner |
| status:in-review | Implementation/evidence submitted; review or validation pending |
| status:blocked | A specific unresolved decision/impediment prevents progress; reason required |
| status:done | GitHub issue closed as completed with acceptance evidence |
| status:closed | Closed without verified completion, e.g. not planned; not counted as done |

Waiting is different from blocked. A task waiting for the local database to be implemented is waiting. A payment implementation without a decision on merchant ownership has a blocking decision.

Current explicit blocker context:
- [#41 Payments](https://github.com/Do-Zu/dozu/issues/41): the user explicitly deferred/skipped payment execution during local migration on 2026-11-10. Keep the existing item blocked; reopening requires an explicit user decision and merchant/provider design. Preserve page/history inventory without claiming payment success.

Task #2 requirements are agreed. Classroom #43's topology-choice blocker is resolved: other devices on the same LAN use a user-owned authoritative host. It now waits for ordinary implementation prerequisites; actual LAN/auth/TLS/availability proof is unfinished. These decisions are recorded under #27 and integration-decisions.md. No central cloud backend or sync is authorized.

## Priority — importance and execution order
| Label | Meaning |
| --- | --- |
| priority:P0 | Highest current priority: architecture and foundation work that unblocks implementation |
| priority:P1 | Required feature/integration/release work after prerequisites |
| priority:P2 | Required supporting work scheduled after the core path |
| priority:P3 | Optional/future work only if explicitly added |

Priorities are relative to this migration; P0 does not imply an existing production outage. All 44 planned items remain tracked; the user explicitly deferred payment execution under #41 on 2026-11-10. Other required scope is not removed by priority. P2 does not mean a required feature may be removed. No current item is assigned P3.

## Complexity — scope and uncertainty
| Label | Meaning |
| --- | --- |
| complexity:S | Contained change, small surface area, little uncertainty |
| complexity:M | Moderate/bounded work across several modules or checks |
| complexity:L | Cross-system, native, security-sensitive or broad verification |
| complexity:XL | Umbrella scope or high uncertainty; break into smaller executable tasks first |

These are provisional planning estimates, not days, cost, deadlines or completion percentages. Each issue's Work tracking section gives its initial rationale. Sidebar labels remain authoritative if estimates change. There are currently no S estimates because the backlog contains substantial migration work; do not invent small estimates for appearance.

## Daily workflow
1. Pick the highest-priority ready item. Split XL work into explicit child issues before starting.
2. Assign the actual owner. Replace its current status label with status:in-progress; do not leave both status labels.
3. Add a short progress comment with evidence, completed work and next step. Link the PR when one exists.
4. If a specific impediment appears, replace status with status:blocked and add a description line `Blocked because: <reason, needed decision/action and responsible person or issue>`. Normal dependency waits use status:waiting.
5. When the blocker is resolved, record the resolution and replace status:blocked with ready/waiting as appropriate. Removing the blocker label is deliberate; elapsed time is not resolution.
6. When implementation and checks are ready, set status:in-review and link the PR/test evidence.
7. Close as completed only after acceptance/review. Close as not planned when canceled; that must not count as done.
8. Refresh derived labels/dashboard after dependencies close using the command below.

The Labels picker is on the issue's right sidebar; deselect the previous label in the same family when choosing a new one. Assignees identifies who is doing the work. No owner is assigned simply because an agent published a plan.

## Refresh commands and authority
```powershell
# Offline validation
.\planning\sync-issue-tracking.ps1 -ValidateOnly

# Read current GitHub state, refresh ready/waiting/done,
# verify labels, and regenerate the local snapshot/dashboard
.\planning\sync-issue-tracking.ps1
```

The sync script preserves live priority/complexity labels and active/review/blocked/backlog states. Initial manifest metadata only seeds missing labels. It promotes waiting to ready only when every declared prerequisite is closed **as completed**; canceled/closed-without-completion dependencies do not satisfy the requirement. It never assigns an owner, starts work, closes an issue or silently clears a blocker.

Keep one value in each label family. Conflicting labels, blocked items without a reason, or active items without an owner cause a validation error rather than guessed state. A fresh dependency snapshot is collected each run; GitHub labels/Assignees are the live authority between runs.

The publisher also invokes this sync at the end. Running the tracker alone updates only its generated Work tracking block, metadata labels and current priority header; unrelated issue content/labels/assignees are retained.

[task-dashboard.md](task-dashboard.md) and [tracking-snapshot.json](tracking-snapshot.json) are timestamped local snapshots; they are not continuously updating boards. The task completion count includes audits among the 40 tasks and excludes the four tickets. It does not measure implemented features or effort-weighted progress; closing baseline audit #3 does not complete application implementation.

## References
- [GitHub labels](https://docs.github.com/en/issues/using-labels-and-milestones-to-track-work/managing-labels)
- [GitHub filtering/search and assignees](https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/filtering-and-searching-issues-and-pull-requests)

