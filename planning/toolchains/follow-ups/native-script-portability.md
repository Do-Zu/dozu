<!-- dozu-toolchains-followup:native-script-portability -->
## Outcome
Run #7's actual portable developer/build/website-package scripts on the approved native OS/CPU hosts and fix only demonstrated script/toolchain/path defects. This is a bounded build-tool proof, distinct from the full installable-stack tests in #22/#46/#47.

## Current evidence
Only a Windows developer host has run the imported workspace commands. That host passed production builds/package, compiled aliases, data-path components, a Windows ZIP fixture containing shell metacharacters, and restricted-write website HTTP checks. It does not establish Windows 10/minimum-device, native macOS/Linux or complete native ABI compatibility.

## Acceptance criteria
- [ ] Record native Windows 10 22H2 x64 and Windows 11 x64, macOS 13+ Intel x64 and ARM64, Ubuntu 22.04 x64 and Debian 12 x64 host/toolchain versions and exact source/lock hashes. Every required target must have an explicit result; cross-builds are not native execution.
- [ ] Run pinned toolchain/workspace checks, frozen installation with the reviewed lifecycle policy, API/Next production builds, repeated builds and root website packaging from paths containing spaces and Unicode.
- [ ] Exercise environment handling, compiled and development alias resolution, config-relative migration paths without touching real data, internal standalone links and the portable start wrapper. Verify a relocated website artifact with original workspace reads denied where the host supports that mechanism.
- [ ] Run the Lambda ZIP developer fixture natively on Windows/macOS/Linux, including paths with spaces/brackets/quotes/dollar signs, and inspect exact archive entries. Record required developer ZIP utilities. Never execute deployment scripts.
- [ ] Test data-root overrides/component writes outside a read-only install tree; distinguish Node permission checks from real OS ACL/packaged installation evidence owned by #15/#34/#23.
- [ ] Attach sanitized commands/logs/checksums and precise limitations, fix measured defects and rerun affected checks. Leave unrun native targets unpassed.

## Dependencies and boundaries
- Final validation depends on #48's selected security-reviewed baseline and #6's completed workspace baseline. Existing #7 measured-baseline runs may execute earlier but must be identified separately.
- This issue is a child of #7 and must not wait for #7 closure. No dependency is inferred satisfied from #4/#45 being closed.
- #38 owns shipped runtime/native ABI manifests; #8 owns Python/model packaging; #29 owns real migrations; #22/#23/#46/#47 own complete installer/runtime/workflow/platform acceptance. This issue does not duplicate or replace those broader gates.
- #45 is currently closed while its acceptance list is unchecked; that is not Windows certification. #22 retains the full Windows release gate.

Parent: #7. Roadmap: #1. Phase: 1 Foundation. Priority: P0. Complexity: M. Status: waiting for final upgraded baseline/native hosts. No owner is invented.

Approved scope is unchanged: retain website/UI/text embeddings, PostgreSQL retained/pgvector deferred, Redis retained, email/STT excluded, payments deferred, LAN classrooms. No developer tools may be required by end-user installers; these are developer build checks only.
