# UI source and interaction ledger

AST evidence covers all page/layout imports, TSX components, hooks/providers and navigation sites. Import closure includes types and barrel exports and therefore over-approximates runtime execution. Dynamic component/data navigation requires runtime confirmation. Exact locations, handlers, unresolved imports and per-page reachability are in [ui-workflows.json](ui-workflows.json) and [source-inventory.json](source-inventory.json).

## Layouts

| Source | Rendered component/provider tags |
| --- | --- |
| [dozu-ui-service/src/app/[locale]/admin/layout.tsx:1](<../../dozu-ui-service/src/app/[locale]/admin/layout.tsx#L1>) | ThemeProvider, Sidebar, Topbar, Separator, ScrollArea |
| [dozu-ui-service/src/app/[locale]/class-based/[id]/layout.tsx:1](<../../dozu-ui-service/src/app/[locale]/class-based/[id]/layout.tsx#L1>) | ClassBasedProvider |
| [dozu-ui-service/src/app/[locale]/class-based/[id]/mindmap/[topicId]/layout.tsx:1](<../../dozu-ui-service/src/app/[locale]/class-based/[id]/mindmap/[topicId]/layout.tsx#L1>) | MindMapProvider |
| [dozu-ui-service/src/app/[locale]/feynman/[topicId]/layout.tsx:1](<../../dozu-ui-service/src/app/[locale]/feynman/[topicId]/layout.tsx#L1>) |  |
| [dozu-ui-service/src/app/[locale]/games/brain-chase/layout.tsx:1](<../../dozu-ui-service/src/app/[locale]/games/brain-chase/layout.tsx#L1>) |  |
| [dozu-ui-service/src/app/[locale]/games/memory-match/layout.tsx:1](<../../dozu-ui-service/src/app/[locale]/games/memory-match/layout.tsx#L1>) |  |
| [dozu-ui-service/src/app/[locale]/generate/layout.tsx:1](<../../dozu-ui-service/src/app/[locale]/generate/layout.tsx#L1>) | ReduxProvider |
| [dozu-ui-service/src/app/[locale]/home/layout.tsx:1](<../../dozu-ui-service/src/app/[locale]/home/layout.tsx#L1>) |  |
| [dozu-ui-service/src/app/[locale]/layout.tsx:1](<../../dozu-ui-service/src/app/[locale]/layout.tsx#L1>) | Providers, LocaleFontProvider, DefaultLayout, UpgradePlanModal |
| [dozu-ui-service/src/app/[locale]/mindmap/[topicId]/layout.tsx:1](<../../dozu-ui-service/src/app/[locale]/mindmap/[topicId]/layout.tsx#L1>) | MindMapProvider |
| [dozu-ui-service/src/app/[locale]/mindmap/view/[topicId]/layout.tsx:1](<../../dozu-ui-service/src/app/[locale]/mindmap/view/[topicId]/layout.tsx#L1>) | MindMapProvider |
| [dozu-ui-service/src/app/[locale]/progress/layout.tsx:1](<../../dozu-ui-service/src/app/[locale]/progress/layout.tsx#L1>) | UserTrackingProvider |
| [dozu-ui-service/src/app/[locale]/quiz/layout.tsx:1](<../../dozu-ui-service/src/app/[locale]/quiz/layout.tsx#L1>) | Button, Home, Separator |
| [dozu-ui-service/src/app/[locale]/setting/layout.tsx:1](<../../dozu-ui-service/src/app/[locale]/setting/layout.tsx#L1>) | TooltipProvider, SettingSidebar |
| [dozu-ui-service/src/app/[locale]/teacher/class-based/[id]/generate/layout.tsx:1](<../../dozu-ui-service/src/app/[locale]/teacher/class-based/[id]/generate/layout.tsx#L1>) | ReduxProvider |
| [dozu-ui-service/src/app/[locale]/teacher/class-based/[id]/mindmap/[topicId]/layout.tsx:1](<../../dozu-ui-service/src/app/[locale]/teacher/class-based/[id]/mindmap/[topicId]/layout.tsx#L1>) | MindMapProvider |
| [dozu-ui-service/src/app/[locale]/teacher/class-based/[id]/students/layout.tsx:1](<../../dozu-ui-service/src/app/[locale]/teacher/class-based/[id]/students/layout.tsx#L1>) | GamificationProvider |
| [dozu-ui-service/src/app/[locale]/teacher/home/layout.tsx:1](<../../dozu-ui-service/src/app/[locale]/teacher/home/layout.tsx#L1>) |  |
| [dozu-ui-service/src/app/[locale]/welcome/layout.tsx:1](<../../dozu-ui-service/src/app/[locale]/welcome/layout.tsx#L1>) |  |
| [dozu-ui-service/src/app/layout.tsx:1](<../../dozu-ui-service/src/app/layout.tsx#L1>) | StoreProvider, ThemeProvider, ReactFlowProvider, AuthProvider, ToasterSooner, Toaster |

## Every page

### UI-001 `/[locale]/about`

Read team/profile content.

[dozu-ui-service/src/app/[locale]/about/page.tsx:1](<../../dozu-ui-service/src/app/[locale]/about/page.tsx#L1>)

Inherited layouts: [dozu-ui-service/src/app/[locale]/layout.tsx:1](<../../dozu-ui-service/src/app/[locale]/layout.tsx#L1>), [dozu-ui-service/src/app/layout.tsx:1](<../../dozu-ui-service/src/app/layout.tsx#L1>)

Direct local imports: [dozu-ui-service/src/app/[locale]/about/_components/Profile.tsx:1](<../../dozu-ui-service/src/app/[locale]/about/_components/Profile.tsx#L1>)

Page interaction sites: none in page AST; inspect imported component ledger

Runtime parity: UNVERIFIED. Complete transitive interactions and source consumers are in the matching JSON page row.

### UI-002 `/[locale]/activities/join/[activityId]`

Join quiz activity, show availability/status and start navigation.

[dozu-ui-service/src/app/[locale]/activities/join/[activityId]/page.tsx:1](<../../dozu-ui-service/src/app/[locale]/activities/join/[activityId]/page.tsx#L1>)

Inherited layouts: [dozu-ui-service/src/app/[locale]/layout.tsx:1](<../../dozu-ui-service/src/app/[locale]/layout.tsx#L1>), [dozu-ui-service/src/app/layout.tsx:1](<../../dozu-ui-service/src/app/layout.tsx#L1>)

Direct local imports: [dozu-ui-service/src/components/ui/card.tsx:1](<../../dozu-ui-service/src/components/ui/card.tsx#L1>), [dozu-ui-service/src/components/ui/button.tsx:1](<../../dozu-ui-service/src/components/ui/button.tsx#L1>), [dozu-ui-service/src/components/ui/badge.tsx:1](<../../dozu-ui-service/src/components/ui/badge.tsx#L1>), [dozu-ui-service/src/components/ui/progress.tsx:1](<../../dozu-ui-service/src/components/ui/progress.tsx#L1>), [dozu-ui-service/src/hooks/use-toast.ts:1](<../../dozu-ui-service/src/hooks/use-toast.ts#L1>), [dozu-ui-service/src/types/activity.ts:1](<../../dozu-ui-service/src/types/activity.ts#L1>), [dozu-ui-service/src/services/activity/activity.service.ts:1](<../../dozu-ui-service/src/services/activity/activity.service.ts#L1>), [dozu-ui-service/src/utils/index.ts:1](<../../dozu-ui-service/src/utils/index.ts#L1>)

Page interaction sites: `useRouter` at 31; `useState` at 32; `useState` at 33; `useState` at 34; `useEffect` at 36; `router.push` at 50; `router.push` at 81; `activity.quizType.replace` at 221; `Button.onClick` at 304

Runtime parity: UNVERIFIED. Complete transitive interactions and source consumers are in the matching JSON page row.

### UI-003 `/[locale]/admin/features`

List/create/update/delete subscription features and limits.

[dozu-ui-service/src/app/[locale]/admin/features/page.tsx:1](<../../dozu-ui-service/src/app/[locale]/admin/features/page.tsx#L1>)

Inherited layouts: [dozu-ui-service/src/app/[locale]/admin/layout.tsx:1](<../../dozu-ui-service/src/app/[locale]/admin/layout.tsx#L1>), [dozu-ui-service/src/app/[locale]/layout.tsx:1](<../../dozu-ui-service/src/app/[locale]/layout.tsx#L1>), [dozu-ui-service/src/app/layout.tsx:1](<../../dozu-ui-service/src/app/layout.tsx#L1>)

Direct local imports: [dozu-ui-service/src/hoc/withAuth.tsx:1](<../../dozu-ui-service/src/hoc/withAuth.tsx#L1>), [dozu-ui-service/src/api/api.ts:1](<../../dozu-ui-service/src/api/api.ts#L1>), [dozu-ui-service/src/api/type.ts:1](<../../dozu-ui-service/src/api/type.ts#L1>), [dozu-ui-service/src/types/subscription.ts:1](<../../dozu-ui-service/src/types/subscription.ts#L1>), [dozu-ui-service/src/components/ui/data-table.tsx:1](<../../dozu-ui-service/src/components/ui/data-table.tsx#L1>), [dozu-ui-service/src/app/[locale]/admin/features/components/Columns.tsx:1](<../../dozu-ui-service/src/app/[locale]/admin/features/components/Columns.tsx#L1>), [dozu-ui-service/src/components/ui/button.tsx:1](<../../dozu-ui-service/src/components/ui/button.tsx#L1>), [dozu-ui-service/src/app/[locale]/admin/features/components/CreateFeatureDialog.tsx:1](<../../dozu-ui-service/src/app/[locale]/admin/features/components/CreateFeatureDialog.tsx#L1>)

Page interaction sites: `useState` at 15; `useState` at 16; `useState` at 17; `useState` at 18; `useCallback` at 20; `getRequest` at 25; `useEffect` at 36; `Button.onClick` at 49; `CreateFeatureDialog.onOpenChange` at 63; `CreateFeatureDialog.onSuccess` at 63; `withAuth` at 72

Runtime parity: UNVERIFIED. Complete transitive interactions and source consumers are in the matching JSON page row.

### UI-004 `/[locale]/admin/feedback`

Filter/list feedback and update moderation/status/auto-ignore operations.

[dozu-ui-service/src/app/[locale]/admin/feedback/page.tsx:1](<../../dozu-ui-service/src/app/[locale]/admin/feedback/page.tsx#L1>)

Inherited layouts: [dozu-ui-service/src/app/[locale]/admin/layout.tsx:1](<../../dozu-ui-service/src/app/[locale]/admin/layout.tsx#L1>), [dozu-ui-service/src/app/[locale]/layout.tsx:1](<../../dozu-ui-service/src/app/[locale]/layout.tsx#L1>), [dozu-ui-service/src/app/layout.tsx:1](<../../dozu-ui-service/src/app/layout.tsx#L1>)

Direct local imports: [dozu-ui-service/src/hoc/withAuth.tsx:1](<../../dozu-ui-service/src/hoc/withAuth.tsx#L1>), [dozu-ui-service/src/api/api.ts:1](<../../dozu-ui-service/src/api/api.ts#L1>), [dozu-ui-service/src/api/type.ts:1](<../../dozu-ui-service/src/api/type.ts#L1>), [dozu-ui-service/src/utils/constants/routes.ts:1](<../../dozu-ui-service/src/utils/constants/routes.ts#L1>), [dozu-ui-service/src/components/ui/button.tsx:1](<../../dozu-ui-service/src/components/ui/button.tsx#L1>), [dozu-ui-service/src/components/ui/data-table.tsx:1](<../../dozu-ui-service/src/components/ui/data-table.tsx#L1>), [dozu-ui-service/src/hooks/use-toast.ts:1](<../../dozu-ui-service/src/hooks/use-toast.ts#L1>), [dozu-ui-service/src/types/feedback-admin/feedback.ts:1](<../../dozu-ui-service/src/types/feedback-admin/feedback.ts#L1>), [dozu-ui-service/src/types/feedback-admin/feedback.ts:1](<../../dozu-ui-service/src/types/feedback-admin/feedback.ts#L1>), [dozu-ui-service/src/app/[locale]/admin/feedback/components/filter-bar.tsx:1](<../../dozu-ui-service/src/app/[locale]/admin/feedback/components/filter-bar.tsx#L1>), [dozu-ui-service/src/app/[locale]/admin/feedback/components/Columns.tsx:1](<../../dozu-ui-service/src/app/[locale]/admin/feedback/components/Columns.tsx#L1>)

Page interaction sites: `useState` at 24; `useState` at 25; `useState` at 26; `useState` at 27; `useState` at 28; `useMemo` at 30; `useCallback` at 39; `getRequest` at 42; `useEffect` at 54; `patchRequest` at 60; `postRequest` at 70; `Button.onClick` at 96; `Button.onClick` at 100; `FeedbackFilterBar.onApplySearch` at 106; `FeedbackFilterBar.onReset` at 106; `withAuth` at 126

Runtime parity: UNVERIFIED. Complete transitive interactions and source consumers are in the matching JSON page row.

### UI-005 `/[locale]/admin/llm-api-key-models`

Create/edit/delete key-model associations, priorities and quotas.

[dozu-ui-service/src/app/[locale]/admin/llm-api-key-models/page.tsx:1](<../../dozu-ui-service/src/app/[locale]/admin/llm-api-key-models/page.tsx#L1>)

Inherited layouts: [dozu-ui-service/src/app/[locale]/admin/layout.tsx:1](<../../dozu-ui-service/src/app/[locale]/admin/layout.tsx#L1>), [dozu-ui-service/src/app/[locale]/layout.tsx:1](<../../dozu-ui-service/src/app/[locale]/layout.tsx#L1>), [dozu-ui-service/src/app/layout.tsx:1](<../../dozu-ui-service/src/app/layout.tsx#L1>)

Direct local imports: [dozu-ui-service/src/hoc/withAuth.tsx:1](<../../dozu-ui-service/src/hoc/withAuth.tsx#L1>), [dozu-ui-service/src/api/api.ts:1](<../../dozu-ui-service/src/api/api.ts#L1>), [dozu-ui-service/src/api/type.ts:1](<../../dozu-ui-service/src/api/type.ts#L1>), [dozu-ui-service/src/types/llm-admin/llmApiKeyModel.ts:1](<../../dozu-ui-service/src/types/llm-admin/llmApiKeyModel.ts#L1>), [dozu-ui-service/src/utils/constants/routes.ts:1](<../../dozu-ui-service/src/utils/constants/routes.ts#L1>), [dozu-ui-service/src/components/ui/data-table.tsx:1](<../../dozu-ui-service/src/components/ui/data-table.tsx#L1>), [dozu-ui-service/src/components/ui/button.tsx:1](<../../dozu-ui-service/src/components/ui/button.tsx#L1>), [dozu-ui-service/src/app/[locale]/admin/llm-api-key-models/components/Columns.tsx:1](<../../dozu-ui-service/src/app/[locale]/admin/llm-api-key-models/components/Columns.tsx#L1>), [dozu-ui-service/src/app/[locale]/admin/llm-api-key-models/components/CreateEditLlmApiKeyModelDialog.tsx:1](<../../dozu-ui-service/src/app/[locale]/admin/llm-api-key-models/components/CreateEditLlmApiKeyModelDialog.tsx#L1>)

Page interaction sites: `useState` at 16; `useState` at 17; `useState` at 18; `useState` at 19; `useState` at 20; `useState` at 21; `useState` at 22; `useCallback` at 24; `getRequest` at 40; `useEffect` at 58; `useCallback` at 66; `Button.onClick` at 93; `CreateEditLlmApiKeyModelDialog.onOpenChange` at 107; `CreateEditLlmApiKeyModelDialog.onSuccess` at 107; `withAuth` at 117

Runtime parity: UNVERIFIED. Complete transitive interactions and source consumers are in the matching JSON page row.

### UI-006 `/[locale]/admin/llm-api-keys`

Create/edit/delete/filter provider keys and key status; sensitive DB-backed key handling.

[dozu-ui-service/src/app/[locale]/admin/llm-api-keys/page.tsx:1](<../../dozu-ui-service/src/app/[locale]/admin/llm-api-keys/page.tsx#L1>)

Inherited layouts: [dozu-ui-service/src/app/[locale]/admin/layout.tsx:1](<../../dozu-ui-service/src/app/[locale]/admin/layout.tsx#L1>), [dozu-ui-service/src/app/[locale]/layout.tsx:1](<../../dozu-ui-service/src/app/[locale]/layout.tsx#L1>), [dozu-ui-service/src/app/layout.tsx:1](<../../dozu-ui-service/src/app/layout.tsx#L1>)

Direct local imports: [dozu-ui-service/src/hoc/withAuth.tsx:1](<../../dozu-ui-service/src/hoc/withAuth.tsx#L1>), [dozu-ui-service/src/api/api.ts:1](<../../dozu-ui-service/src/api/api.ts#L1>), [dozu-ui-service/src/api/type.ts:1](<../../dozu-ui-service/src/api/type.ts#L1>), [dozu-ui-service/src/types/llm-admin/llmApiKey.ts:1](<../../dozu-ui-service/src/types/llm-admin/llmApiKey.ts#L1>), [dozu-ui-service/src/utils/constants/routes.ts:1](<../../dozu-ui-service/src/utils/constants/routes.ts#L1>), [dozu-ui-service/src/components/ui/data-table.tsx:1](<../../dozu-ui-service/src/components/ui/data-table.tsx#L1>), [dozu-ui-service/src/components/ui/button.tsx:1](<../../dozu-ui-service/src/components/ui/button.tsx#L1>), [dozu-ui-service/src/app/[locale]/admin/llm-api-keys/components/Columns.tsx:1](<../../dozu-ui-service/src/app/[locale]/admin/llm-api-keys/components/Columns.tsx#L1>), [dozu-ui-service/src/app/[locale]/admin/llm-api-keys/components/CreateEditLlmApiKeyDialog.tsx:1](<../../dozu-ui-service/src/app/[locale]/admin/llm-api-keys/components/CreateEditLlmApiKeyDialog.tsx#L1>)

Page interaction sites: `useState` at 16; `useState` at 17; `useState` at 18; `useState` at 19; `useState` at 20; `useState` at 21; `useState` at 22; `useCallback` at 24; `getRequest` at 40; `useEffect` at 58; `useCallback` at 66; `Button.onClick` at 93; `CreateEditLlmApiKeyDialog.onOpenChange` at 107; `CreateEditLlmApiKeyDialog.onSuccess` at 107; `withAuth` at 117

Runtime parity: UNVERIFIED. Complete transitive interactions and source consumers are in the matching JSON page row.

### UI-007 `/[locale]/admin/llm-models`

Create/edit/delete/filter provider models and availability.

[dozu-ui-service/src/app/[locale]/admin/llm-models/page.tsx:1](<../../dozu-ui-service/src/app/[locale]/admin/llm-models/page.tsx#L1>)

Inherited layouts: [dozu-ui-service/src/app/[locale]/admin/layout.tsx:1](<../../dozu-ui-service/src/app/[locale]/admin/layout.tsx#L1>), [dozu-ui-service/src/app/[locale]/layout.tsx:1](<../../dozu-ui-service/src/app/[locale]/layout.tsx#L1>), [dozu-ui-service/src/app/layout.tsx:1](<../../dozu-ui-service/src/app/layout.tsx#L1>)

Direct local imports: [dozu-ui-service/src/hoc/withAuth.tsx:1](<../../dozu-ui-service/src/hoc/withAuth.tsx#L1>), [dozu-ui-service/src/api/api.ts:1](<../../dozu-ui-service/src/api/api.ts#L1>), [dozu-ui-service/src/api/type.ts:1](<../../dozu-ui-service/src/api/type.ts#L1>), [dozu-ui-service/src/types/llm-admin/llmModel.ts:1](<../../dozu-ui-service/src/types/llm-admin/llmModel.ts#L1>), [dozu-ui-service/src/utils/constants/routes.ts:1](<../../dozu-ui-service/src/utils/constants/routes.ts#L1>), [dozu-ui-service/src/components/ui/data-table.tsx:1](<../../dozu-ui-service/src/components/ui/data-table.tsx#L1>), [dozu-ui-service/src/app/[locale]/admin/llm-models/components/Columns.tsx:1](<../../dozu-ui-service/src/app/[locale]/admin/llm-models/components/Columns.tsx#L1>), [dozu-ui-service/src/components/ui/button.tsx:1](<../../dozu-ui-service/src/components/ui/button.tsx#L1>), [dozu-ui-service/src/app/[locale]/admin/llm-models/components/CreateEditLlmModelDialog.tsx:1](<../../dozu-ui-service/src/app/[locale]/admin/llm-models/components/CreateEditLlmModelDialog.tsx#L1>), [dozu-ui-service/src/app/[locale]/admin/llm-models/components/LlmModelFilter.tsx:1](<../../dozu-ui-service/src/app/[locale]/admin/llm-models/components/LlmModelFilter.tsx#L1>)

Page interaction sites: `useState` at 17; `useState` at 18; `useState` at 19; `useState` at 20; `useState` at 21; `useState` at 22; `useState` at 23; `useCallback` at 25; `getRequest` at 41; `useEffect` at 59; `useCallback` at 67; `Button.onClick` at 94; `LlmModelFilter.onFilterChange` at 100; `CreateEditLlmModelDialog.onOpenChange` at 110; `CreateEditLlmModelDialog.onSuccess` at 110; `withAuth` at 120

Runtime parity: UNVERIFIED. Complete transitive interactions and source consumers are in the matching JSON page row.

### UI-008 `/[locale]/admin/llm-providers`

Create/edit/delete/filter providers, URLs and availability.

[dozu-ui-service/src/app/[locale]/admin/llm-providers/page.tsx:1](<../../dozu-ui-service/src/app/[locale]/admin/llm-providers/page.tsx#L1>)

Inherited layouts: [dozu-ui-service/src/app/[locale]/admin/layout.tsx:1](<../../dozu-ui-service/src/app/[locale]/admin/layout.tsx#L1>), [dozu-ui-service/src/app/[locale]/layout.tsx:1](<../../dozu-ui-service/src/app/[locale]/layout.tsx#L1>), [dozu-ui-service/src/app/layout.tsx:1](<../../dozu-ui-service/src/app/layout.tsx#L1>)

Direct local imports: [dozu-ui-service/src/hoc/withAuth.tsx:1](<../../dozu-ui-service/src/hoc/withAuth.tsx#L1>), [dozu-ui-service/src/api/api.ts:1](<../../dozu-ui-service/src/api/api.ts#L1>), [dozu-ui-service/src/api/type.ts:1](<../../dozu-ui-service/src/api/type.ts#L1>), [dozu-ui-service/src/types/llm-admin/llmProvider.ts:1](<../../dozu-ui-service/src/types/llm-admin/llmProvider.ts#L1>), [dozu-ui-service/src/utils/constants/routes.ts:1](<../../dozu-ui-service/src/utils/constants/routes.ts#L1>), [dozu-ui-service/src/components/ui/data-table.tsx:1](<../../dozu-ui-service/src/components/ui/data-table.tsx#L1>), [dozu-ui-service/src/app/[locale]/admin/llm-providers/components/Columns.tsx:1](<../../dozu-ui-service/src/app/[locale]/admin/llm-providers/components/Columns.tsx#L1>), [dozu-ui-service/src/components/ui/button.tsx:1](<../../dozu-ui-service/src/components/ui/button.tsx#L1>), [dozu-ui-service/src/app/[locale]/admin/llm-providers/components/CreateEditLlmProviderDialog.tsx:1](<../../dozu-ui-service/src/app/[locale]/admin/llm-providers/components/CreateEditLlmProviderDialog.tsx#L1>), [dozu-ui-service/src/app/[locale]/admin/llm-providers/components/LlmProviderFilter.tsx:1](<../../dozu-ui-service/src/app/[locale]/admin/llm-providers/components/LlmProviderFilter.tsx#L1>)

Page interaction sites: `useState` at 17; `useState` at 18; `useState` at 19; `useState` at 20; `useState` at 21; `useState` at 22; `useState` at 23; `useCallback` at 25; `getRequest` at 41; `useEffect` at 59; `useCallback` at 67; `Button.onClick` at 94; `LlmProviderFilter.onFilterChange` at 100; `CreateEditLlmProviderDialog.onOpenChange` at 110; `CreateEditLlmProviderDialog.onSuccess` at 110; `withAuth` at 120

Runtime parity: UNVERIFIED. Complete transitive interactions and source consumers are in the matching JSON page row.

### UI-009 `/[locale]/admin`

Account/role/activity dashboard cards and signup chart.

[dozu-ui-service/src/app/[locale]/admin/page.tsx:1](<../../dozu-ui-service/src/app/[locale]/admin/page.tsx#L1>)

Inherited layouts: [dozu-ui-service/src/app/[locale]/admin/layout.tsx:1](<../../dozu-ui-service/src/app/[locale]/admin/layout.tsx#L1>), [dozu-ui-service/src/app/[locale]/layout.tsx:1](<../../dozu-ui-service/src/app/[locale]/layout.tsx#L1>), [dozu-ui-service/src/app/layout.tsx:1](<../../dozu-ui-service/src/app/layout.tsx#L1>)

Direct local imports: [dozu-ui-service/src/components/ui/card.tsx:1](<../../dozu-ui-service/src/components/ui/card.tsx#L1>), [dozu-ui-service/src/components/ui/separator.tsx:1](<../../dozu-ui-service/src/components/ui/separator.tsx#L1>), [dozu-ui-service/src/app/[locale]/admin/components/Chart.tsx:1](<../../dozu-ui-service/src/app/[locale]/admin/components/Chart.tsx#L1>), [dozu-ui-service/src/app/[locale]/admin/components/RecentActivity.tsx:1](<../../dozu-ui-service/src/app/[locale]/admin/components/RecentActivity.tsx#L1>), [dozu-ui-service/src/api/api.ts:1](<../../dozu-ui-service/src/api/api.ts#L1>), [dozu-ui-service/src/types/user.ts:1](<../../dozu-ui-service/src/types/user.ts#L1>), [dozu-ui-service/src/hooks/use-toast.ts:1](<../../dozu-ui-service/src/hooks/use-toast.ts#L1>), [dozu-ui-service/src/hoc/withAuth.tsx:1](<../../dozu-ui-service/src/hoc/withAuth.tsx#L1>)

Page interaction sites: `useState` at 15; `useEffect` at 17; `getRequest` at 20; `withAuth` at 113

Runtime parity: UNVERIFIED. Complete transitive interactions and source consumers are in the matching JSON page row.

### UI-010 `/[locale]/admin/payments`

Filter/page payment ledger and export CSV.

[dozu-ui-service/src/app/[locale]/admin/payments/page.tsx:1](<../../dozu-ui-service/src/app/[locale]/admin/payments/page.tsx#L1>)

Inherited layouts: [dozu-ui-service/src/app/[locale]/admin/layout.tsx:1](<../../dozu-ui-service/src/app/[locale]/admin/layout.tsx#L1>), [dozu-ui-service/src/app/[locale]/layout.tsx:1](<../../dozu-ui-service/src/app/[locale]/layout.tsx#L1>), [dozu-ui-service/src/app/layout.tsx:1](<../../dozu-ui-service/src/app/layout.tsx#L1>)

Direct local imports: [dozu-ui-service/src/hoc/withAuth.tsx:1](<../../dozu-ui-service/src/hoc/withAuth.tsx#L1>), [dozu-ui-service/src/hooks/helper.ts:1](<../../dozu-ui-service/src/hooks/helper.ts#L1>), [dozu-ui-service/src/api/type.ts:1](<../../dozu-ui-service/src/api/type.ts#L1>), [dozu-ui-service/src/types/payment.ts:1](<../../dozu-ui-service/src/types/payment.ts#L1>), [dozu-ui-service/src/components/ui/data-table.tsx:1](<../../dozu-ui-service/src/components/ui/data-table.tsx#L1>), [dozu-ui-service/src/app/[locale]/admin/payments/components/Columns.tsx:1](<../../dozu-ui-service/src/app/[locale]/admin/payments/components/Columns.tsx#L1>), [dozu-ui-service/src/app/[locale]/admin/payments/components/PaymentFilter.tsx:1](<../../dozu-ui-service/src/app/[locale]/admin/payments/components/PaymentFilter.tsx#L1>), [dozu-ui-service/src/components/ui/button.tsx:1](<../../dozu-ui-service/src/components/ui/button.tsx#L1>), [dozu-ui-service/src/hooks/use-toast.ts:1](<../../dozu-ui-service/src/hooks/use-toast.ts#L1>)

Page interaction sites: `useState` at 16; `useState` at 17; `useState` at 18; `useState` at 19; `useState` at 20; `useCallback` at 22; `useEffect` at 43; `useState` at 56; `Button.onClick` at 105; `PaymentFilter.onFilterChange` at 111; `withAuth` at 132

Runtime parity: UNVERIFIED. Complete transitive interactions and source consumers are in the matching JSON page row.

### UI-011 `/[locale]/admin/plans/[planId]/features`

Assign/edit/remove plan feature access and limits.

[dozu-ui-service/src/app/[locale]/admin/plans/[planId]/features/page.tsx:1](<../../dozu-ui-service/src/app/[locale]/admin/plans/[planId]/features/page.tsx#L1>)

Inherited layouts: [dozu-ui-service/src/app/[locale]/admin/layout.tsx:1](<../../dozu-ui-service/src/app/[locale]/admin/layout.tsx#L1>), [dozu-ui-service/src/app/[locale]/layout.tsx:1](<../../dozu-ui-service/src/app/[locale]/layout.tsx#L1>), [dozu-ui-service/src/app/layout.tsx:1](<../../dozu-ui-service/src/app/layout.tsx#L1>)

Direct local imports: [dozu-ui-service/src/hoc/withAuth.tsx:1](<../../dozu-ui-service/src/hoc/withAuth.tsx#L1>), [dozu-ui-service/src/api/api.ts:1](<../../dozu-ui-service/src/api/api.ts#L1>), [dozu-ui-service/src/api/type.ts:1](<../../dozu-ui-service/src/api/type.ts#L1>), [dozu-ui-service/src/types/subscription.ts:1](<../../dozu-ui-service/src/types/subscription.ts#L1>), [dozu-ui-service/src/components/ui/data-table.tsx:1](<../../dozu-ui-service/src/components/ui/data-table.tsx#L1>), [dozu-ui-service/src/app/[locale]/admin/plans/[planId]/features/components/Columns.tsx:1](<../../dozu-ui-service/src/app/[locale]/admin/plans/[planId]/features/components/Columns.tsx#L1>), [dozu-ui-service/src/components/ui/button.tsx:1](<../../dozu-ui-service/src/components/ui/button.tsx#L1>), [dozu-ui-service/src/app/[locale]/admin/plans/[planId]/features/components/AssignFeatureDialog.tsx:1](<../../dozu-ui-service/src/app/[locale]/admin/plans/[planId]/features/components/AssignFeatureDialog.tsx#L1>)

Page interaction sites: `useParams` at 17; `useRouter` at 18; `useState` at 21; `useState` at 22; `useState` at 23; `useState` at 24; `useState` at 25; `useCallback` at 27; `getRequest` at 33; `getRequest` at 34; `useEffect` at 46; `Link.href` at 57; `Button.onClick` at 70; `AssignFeatureDialog.onOpenChange` at 84; `AssignFeatureDialog.onSuccess` at 84; `withAuth` at 94

Runtime parity: UNVERIFIED. Complete transitive interactions and source consumers are in the matching JSON page row.

### UI-012 `/[locale]/admin/plans`

List/create/edit/delete plans and navigate feature assignment.

[dozu-ui-service/src/app/[locale]/admin/plans/page.tsx:1](<../../dozu-ui-service/src/app/[locale]/admin/plans/page.tsx#L1>)

Inherited layouts: [dozu-ui-service/src/app/[locale]/admin/layout.tsx:1](<../../dozu-ui-service/src/app/[locale]/admin/layout.tsx#L1>), [dozu-ui-service/src/app/[locale]/layout.tsx:1](<../../dozu-ui-service/src/app/[locale]/layout.tsx#L1>), [dozu-ui-service/src/app/layout.tsx:1](<../../dozu-ui-service/src/app/layout.tsx#L1>)

Direct local imports: [dozu-ui-service/src/hoc/withAuth.tsx:1](<../../dozu-ui-service/src/hoc/withAuth.tsx#L1>), [dozu-ui-service/src/api/api.ts:1](<../../dozu-ui-service/src/api/api.ts#L1>), [dozu-ui-service/src/api/type.ts:1](<../../dozu-ui-service/src/api/type.ts#L1>), [dozu-ui-service/src/types/subscription.ts:1](<../../dozu-ui-service/src/types/subscription.ts#L1>), [dozu-ui-service/src/components/ui/data-table.tsx:1](<../../dozu-ui-service/src/components/ui/data-table.tsx#L1>), [dozu-ui-service/src/app/[locale]/admin/plans/components/Columns.tsx:1](<../../dozu-ui-service/src/app/[locale]/admin/plans/components/Columns.tsx#L1>), [dozu-ui-service/src/components/ui/button.tsx:1](<../../dozu-ui-service/src/components/ui/button.tsx#L1>), [dozu-ui-service/src/app/[locale]/admin/plans/components/CreatePlanDialog.tsx:1](<../../dozu-ui-service/src/app/[locale]/admin/plans/components/CreatePlanDialog.tsx#L1>)

Page interaction sites: `useState` at 15; `useState` at 16; `useState` at 17; `useState` at 18; `useCallback` at 20; `getRequest` at 25; `useEffect` at 34; `Button.onClick` at 47; `CreatePlanDialog.onOpenChange` at 61; `CreatePlanDialog.onSuccess` at 61; `withAuth` at 70

Runtime parity: UNVERIFIED. Complete transitive interactions and source consumers are in the matching JSON page row.

### UI-013 `/[locale]/admin/revenue`

Filter revenue and gateway/plan/trend analytics.

[dozu-ui-service/src/app/[locale]/admin/revenue/page.tsx:1](<../../dozu-ui-service/src/app/[locale]/admin/revenue/page.tsx#L1>)

Inherited layouts: [dozu-ui-service/src/app/[locale]/admin/layout.tsx:1](<../../dozu-ui-service/src/app/[locale]/admin/layout.tsx#L1>), [dozu-ui-service/src/app/[locale]/layout.tsx:1](<../../dozu-ui-service/src/app/[locale]/layout.tsx#L1>), [dozu-ui-service/src/app/layout.tsx:1](<../../dozu-ui-service/src/app/layout.tsx#L1>)

Direct local imports: [dozu-ui-service/src/hoc/withAuth.tsx:1](<../../dozu-ui-service/src/hoc/withAuth.tsx#L1>), [dozu-ui-service/src/api/api.ts:1](<../../dozu-ui-service/src/api/api.ts#L1>), [dozu-ui-service/src/api/type.ts:1](<../../dozu-ui-service/src/api/type.ts#L1>), [dozu-ui-service/src/types/revenue.ts:1](<../../dozu-ui-service/src/types/revenue.ts#L1>), [dozu-ui-service/src/components/ui/card.tsx:1](<../../dozu-ui-service/src/components/ui/card.tsx#L1>), [dozu-ui-service/src/app/[locale]/admin/revenue/components/KPICard.tsx:1](<../../dozu-ui-service/src/app/[locale]/admin/revenue/components/KPICard.tsx#L1>), [dozu-ui-service/src/app/[locale]/admin/revenue/components/RevenueTrendChart.tsx:1](<../../dozu-ui-service/src/app/[locale]/admin/revenue/components/RevenueTrendChart.tsx#L1>), [dozu-ui-service/src/app/[locale]/admin/revenue/components/RevenueByGatewayChart.tsx:1](<../../dozu-ui-service/src/app/[locale]/admin/revenue/components/RevenueByGatewayChart.tsx#L1>), [dozu-ui-service/src/app/[locale]/admin/revenue/components/RevenueByPlanChart.tsx:1](<../../dozu-ui-service/src/app/[locale]/admin/revenue/components/RevenueByPlanChart.tsx#L1>), [dozu-ui-service/src/app/[locale]/admin/revenue/components/RevenueFilter.tsx:1](<../../dozu-ui-service/src/app/[locale]/admin/revenue/components/RevenueFilter.tsx#L1>), [dozu-ui-service/src/utils/formatters.ts:1](<../../dozu-ui-service/src/utils/formatters.ts#L1>)

Page interaction sites: `useState` at 19; `useState` at 20; `useState` at 21; `useState` at 22; `useCallback` at 26; `getRequest` at 47; `useCallback` at 56; `useCallback` at 60; `useEffect` at 71; `RevenueFilter.onFiltersChange` at 101; `RevenueFilter.onSearch` at 101; `withAuth` at 222

Runtime parity: UNVERIFIED. Complete transitive interactions and source consumers are in the matching JSON page row.

### UI-014 `/[locale]/admin/stats`

Fetch user statistics and render charts/loading state.

[dozu-ui-service/src/app/[locale]/admin/stats/page.tsx:1](<../../dozu-ui-service/src/app/[locale]/admin/stats/page.tsx#L1>)

Inherited layouts: [dozu-ui-service/src/app/[locale]/admin/layout.tsx:1](<../../dozu-ui-service/src/app/[locale]/admin/layout.tsx#L1>), [dozu-ui-service/src/app/[locale]/layout.tsx:1](<../../dozu-ui-service/src/app/[locale]/layout.tsx#L1>), [dozu-ui-service/src/app/layout.tsx:1](<../../dozu-ui-service/src/app/layout.tsx#L1>)

Direct local imports: [dozu-ui-service/src/hoc/withAuth.tsx:1](<../../dozu-ui-service/src/hoc/withAuth.tsx#L1>), [dozu-ui-service/src/hooks/useFetch.ts:1](<../../dozu-ui-service/src/hooks/useFetch.ts#L1>), [dozu-ui-service/src/components/ui/card.tsx:1](<../../dozu-ui-service/src/components/ui/card.tsx#L1>), [dozu-ui-service/src/components/ui/skeleton.tsx:1](<../../dozu-ui-service/src/components/ui/skeleton.tsx#L1>)

Page interaction sites: `useFetch` at 26; `useMemo` at 34; `useMemo` at 47; `withAuth` at 94

Runtime parity: UNVERIFIED. Complete transitive interactions and source consumers are in the matching JSON page row.

### UI-015 `/[locale]/admin/subscriptions/list`

Filter/page subscription records and administer their states.

[dozu-ui-service/src/app/[locale]/admin/subscriptions/list/page.tsx:1](<../../dozu-ui-service/src/app/[locale]/admin/subscriptions/list/page.tsx#L1>)

Inherited layouts: [dozu-ui-service/src/app/[locale]/admin/layout.tsx:1](<../../dozu-ui-service/src/app/[locale]/admin/layout.tsx#L1>), [dozu-ui-service/src/app/[locale]/layout.tsx:1](<../../dozu-ui-service/src/app/[locale]/layout.tsx#L1>), [dozu-ui-service/src/app/layout.tsx:1](<../../dozu-ui-service/src/app/layout.tsx#L1>)

Direct local imports: [dozu-ui-service/src/hoc/withAuth.tsx:1](<../../dozu-ui-service/src/hoc/withAuth.tsx#L1>), [dozu-ui-service/src/api/api.ts:1](<../../dozu-ui-service/src/api/api.ts#L1>), [dozu-ui-service/src/api/type.ts:1](<../../dozu-ui-service/src/api/type.ts#L1>), [dozu-ui-service/src/types/subscriptionStats.ts:1](<../../dozu-ui-service/src/types/subscriptionStats.ts#L1>), [dozu-ui-service/src/components/ui/data-table.tsx:1](<../../dozu-ui-service/src/components/ui/data-table.tsx#L1>), [dozu-ui-service/src/app/[locale]/admin/subscriptions/list/components/Columns.tsx:1](<../../dozu-ui-service/src/app/[locale]/admin/subscriptions/list/components/Columns.tsx#L1>), [dozu-ui-service/src/app/[locale]/admin/subscriptions/list/components/SubscriptionFilter.tsx:1](<../../dozu-ui-service/src/app/[locale]/admin/subscriptions/list/components/SubscriptionFilter.tsx#L1>), [dozu-ui-service/src/components/ui/button.tsx:1](<../../dozu-ui-service/src/components/ui/button.tsx#L1>)

Page interaction sites: `useSearchParams` at 17; `useState` at 18; `useState` at 19; `useState` at 20; `useState` at 21; `useCallback` at 23; `getRequest` at 36; `useEffect` at 47; `Link.href` at 59; `SubscriptionFilter.onFilterChange` at 72; `withAuth` at 93

Runtime parity: UNVERIFIED. Complete transitive interactions and source consumers are in the matching JSON page row.

### UI-016 `/[locale]/admin/subscriptions`

Subscription KPI/status/monthly charts with links to lists/plans/features.

[dozu-ui-service/src/app/[locale]/admin/subscriptions/page.tsx:1](<../../dozu-ui-service/src/app/[locale]/admin/subscriptions/page.tsx#L1>)

Inherited layouts: [dozu-ui-service/src/app/[locale]/admin/layout.tsx:1](<../../dozu-ui-service/src/app/[locale]/admin/layout.tsx#L1>), [dozu-ui-service/src/app/[locale]/layout.tsx:1](<../../dozu-ui-service/src/app/[locale]/layout.tsx#L1>), [dozu-ui-service/src/app/layout.tsx:1](<../../dozu-ui-service/src/app/layout.tsx#L1>)

Direct local imports: [dozu-ui-service/src/hoc/withAuth.tsx:1](<../../dozu-ui-service/src/hoc/withAuth.tsx#L1>), [dozu-ui-service/src/api/api.ts:1](<../../dozu-ui-service/src/api/api.ts#L1>), [dozu-ui-service/src/api/type.ts:1](<../../dozu-ui-service/src/api/type.ts#L1>), [dozu-ui-service/src/types/subscriptionStats.ts:1](<../../dozu-ui-service/src/types/subscriptionStats.ts#L1>), [dozu-ui-service/src/components/ui/card.tsx:1](<../../dozu-ui-service/src/components/ui/card.tsx#L1>), [dozu-ui-service/src/app/[locale]/admin/subscriptions/components/StatsCard.tsx:1](<../../dozu-ui-service/src/app/[locale]/admin/subscriptions/components/StatsCard.tsx#L1>), [dozu-ui-service/src/app/[locale]/admin/subscriptions/components/StatusBreakdownChart.tsx:1](<../../dozu-ui-service/src/app/[locale]/admin/subscriptions/components/StatusBreakdownChart.tsx#L1>), [dozu-ui-service/src/app/[locale]/admin/subscriptions/components/MonthlyTrendChart.tsx:1](<../../dozu-ui-service/src/app/[locale]/admin/subscriptions/components/MonthlyTrendChart.tsx#L1>), [dozu-ui-service/src/components/ui/button.tsx:1](<../../dozu-ui-service/src/components/ui/button.tsx#L1>)

Page interaction sites: `useState` at 17; `useState` at 18; `useState` at 19; `useCallback` at 21; `getRequest` at 26; `useEffect` at 35; `Link.href` at 64; `Link.href` at 130; `Link.href` at 133; `Link.href` at 136; `Link.href` at 139; `withAuth` at 148

Runtime parity: UNVERIFIED. Complete transitive interactions and source consumers are in the matching JSON page row.

### UI-017 `/[locale]/admin/teacher-requests`

List teacher applications/statuses.

[dozu-ui-service/src/app/[locale]/admin/teacher-requests/page.tsx:1](<../../dozu-ui-service/src/app/[locale]/admin/teacher-requests/page.tsx#L1>)

Inherited layouts: [dozu-ui-service/src/app/[locale]/admin/layout.tsx:1](<../../dozu-ui-service/src/app/[locale]/admin/layout.tsx#L1>), [dozu-ui-service/src/app/[locale]/layout.tsx:1](<../../dozu-ui-service/src/app/[locale]/layout.tsx#L1>), [dozu-ui-service/src/app/layout.tsx:1](<../../dozu-ui-service/src/app/layout.tsx#L1>)

Direct local imports: [dozu-ui-service/src/hooks/useFetch.ts:1](<../../dozu-ui-service/src/hooks/useFetch.ts#L1>), [dozu-ui-service/src/app/[locale]/admin/teacher-requests/components/RequestList.tsx:1](<../../dozu-ui-service/src/app/[locale]/admin/teacher-requests/components/RequestList.tsx#L1>), [dozu-ui-service/src/app/[locale]/admin/teacher-requests/types/teacherRequest.type.ts:1](<../../dozu-ui-service/src/app/[locale]/admin/teacher-requests/types/teacherRequest.type.ts#L1>), [dozu-ui-service/src/app/loading.tsx:1](<../../dozu-ui-service/src/app/loading.tsx#L1>)

Page interaction sites: `useFetch` at 14

Runtime parity: UNVERIFIED. Complete transitive interactions and source consumers are in the matching JSON page row.

### UI-018 `/[locale]/admin/teacher-requests/pending`

Review pending applications and approve/reject.

[dozu-ui-service/src/app/[locale]/admin/teacher-requests/pending/page.tsx:1](<../../dozu-ui-service/src/app/[locale]/admin/teacher-requests/pending/page.tsx#L1>)

Inherited layouts: [dozu-ui-service/src/app/[locale]/admin/layout.tsx:1](<../../dozu-ui-service/src/app/[locale]/admin/layout.tsx#L1>), [dozu-ui-service/src/app/[locale]/layout.tsx:1](<../../dozu-ui-service/src/app/[locale]/layout.tsx#L1>), [dozu-ui-service/src/app/layout.tsx:1](<../../dozu-ui-service/src/app/layout.tsx#L1>)

Direct local imports: [dozu-ui-service/src/hooks/useFetch.ts:1](<../../dozu-ui-service/src/hooks/useFetch.ts#L1>), [dozu-ui-service/src/app/[locale]/admin/teacher-requests/types/teacherRequest.type.ts:1](<../../dozu-ui-service/src/app/[locale]/admin/teacher-requests/types/teacherRequest.type.ts#L1>), [dozu-ui-service/src/app/[locale]/admin/teacher-requests/components/PendingRequestList.tsx:1](<../../dozu-ui-service/src/app/[locale]/admin/teacher-requests/components/PendingRequestList.tsx#L1>), [dozu-ui-service/src/app/loading.tsx:1](<../../dozu-ui-service/src/app/loading.tsx#L1>), [dozu-ui-service/src/hooks/use-toast.ts:1](<../../dozu-ui-service/src/hooks/use-toast.ts#L1>), [dozu-ui-service/src/services/teacher-request/teacherRequest.service.ts:1](<../../dozu-ui-service/src/services/teacher-request/teacherRequest.service.ts#L1>)

Page interaction sites: `useFetch` at 16; `teacherRequestService.approveRequest` at 21; `teacherRequestService.rejectRequest` at 38

Runtime parity: UNVERIFIED. Complete transitive interactions and source consumers are in the matching JSON page row.

### UI-019 `/[locale]/admin/users/[id]/oauth`

Read user linked authentication accounts and provider metadata.

[dozu-ui-service/src/app/[locale]/admin/users/[id]/oauth/page.tsx:1](<../../dozu-ui-service/src/app/[locale]/admin/users/[id]/oauth/page.tsx#L1>)

Inherited layouts: [dozu-ui-service/src/app/[locale]/admin/layout.tsx:1](<../../dozu-ui-service/src/app/[locale]/admin/layout.tsx#L1>), [dozu-ui-service/src/app/[locale]/layout.tsx:1](<../../dozu-ui-service/src/app/[locale]/layout.tsx#L1>), [dozu-ui-service/src/app/layout.tsx:1](<../../dozu-ui-service/src/app/layout.tsx#L1>)

Direct local imports: [dozu-ui-service/src/hooks/useFetch.ts:1](<../../dozu-ui-service/src/hooks/useFetch.ts#L1>), [dozu-ui-service/src/components/ui/card.tsx:1](<../../dozu-ui-service/src/components/ui/card.tsx#L1>), [dozu-ui-service/src/components/ui/skeleton.tsx:1](<../../dozu-ui-service/src/components/ui/skeleton.tsx#L1>), [dozu-ui-service/src/components/ui/badge.tsx:1](<../../dozu-ui-service/src/components/ui/badge.tsx#L1>)

Page interaction sites: `useParams` at 19; `useFetch` at 26

Runtime parity: UNVERIFIED. Complete transitive interactions and source consumers are in the matching JSON page row.

### UI-020 `/[locale]/admin/users`

Filter/page users; activate/deactivate, edit role and inspect OAuth associations.

[dozu-ui-service/src/app/[locale]/admin/users/page.tsx:1](<../../dozu-ui-service/src/app/[locale]/admin/users/page.tsx#L1>)

Inherited layouts: [dozu-ui-service/src/app/[locale]/admin/layout.tsx:1](<../../dozu-ui-service/src/app/[locale]/admin/layout.tsx#L1>), [dozu-ui-service/src/app/[locale]/layout.tsx:1](<../../dozu-ui-service/src/app/[locale]/layout.tsx#L1>), [dozu-ui-service/src/app/layout.tsx:1](<../../dozu-ui-service/src/app/layout.tsx#L1>)

Direct local imports: [dozu-ui-service/src/hoc/withAuth.tsx:1](<../../dozu-ui-service/src/hoc/withAuth.tsx#L1>), [dozu-ui-service/src/api/api.ts:1](<../../dozu-ui-service/src/api/api.ts#L1>), [dozu-ui-service/src/api/type.ts:1](<../../dozu-ui-service/src/api/type.ts#L1>), [dozu-ui-service/src/types/user.ts:1](<../../dozu-ui-service/src/types/user.ts#L1>), [dozu-ui-service/src/app/[locale]/admin/users/components/Columns.tsx:1](<../../dozu-ui-service/src/app/[locale]/admin/users/components/Columns.tsx#L1>), [dozu-ui-service/src/components/ui/data-table.tsx:1](<../../dozu-ui-service/src/components/ui/data-table.tsx#L1>), [dozu-ui-service/src/app/[locale]/admin/users/components/UserFilter.tsx:1](<../../dozu-ui-service/src/app/[locale]/admin/users/components/UserFilter.tsx#L1>)

Page interaction sites: `useState` at 13; `useState` at 14; `useState` at 15; `useState` at 16; `useCallback` at 18; `getRequest` at 27; `useEffect` at 52; `useMemo` at 61; `UserFilter.onFilterChange` at 69; `withAuth` at 82

Runtime parity: UNVERIFIED. Complete transitive interactions and source consumers are in the matching JSON page row.

### UI-021 `/[locale]/auth/changePassword`

Validate email/code query and submit new password.

[dozu-ui-service/src/app/[locale]/auth/changePassword/page.tsx:1](<../../dozu-ui-service/src/app/[locale]/auth/changePassword/page.tsx#L1>)

Inherited layouts: [dozu-ui-service/src/app/[locale]/layout.tsx:1](<../../dozu-ui-service/src/app/[locale]/layout.tsx#L1>), [dozu-ui-service/src/app/layout.tsx:1](<../../dozu-ui-service/src/app/layout.tsx#L1>)

Direct local imports: [dozu-ui-service/src/components/auth/CentralCard.tsx:1](<../../dozu-ui-service/src/components/auth/CentralCard.tsx#L1>), [dozu-ui-service/src/components/ui/button.tsx:1](<../../dozu-ui-service/src/components/ui/button.tsx#L1>), [dozu-ui-service/src/components/ui/card.tsx:1](<../../dozu-ui-service/src/components/ui/card.tsx#L1>), [dozu-ui-service/src/components/ui/input.tsx:1](<../../dozu-ui-service/src/components/ui/input.tsx#L1>), [dozu-ui-service/src/components/ui/label.tsx:1](<../../dozu-ui-service/src/components/ui/label.tsx#L1>), [dozu-ui-service/src/hooks/usePost.ts:1](<../../dozu-ui-service/src/hooks/usePost.ts#L1>), [dozu-ui-service/src/utils/toast.helper.ts:1](<../../dozu-ui-service/src/utils/toast.helper.ts#L1>), [dozu-ui-service/src/contexts/auth/AuthContext.tsx:1](<../../dozu-ui-service/src/contexts/auth/AuthContext.tsx#L1>), [dozu-ui-service/src/types/auth.ts:1](<../../dozu-ui-service/src/types/auth.ts#L1>), [dozu-ui-service/src/api/type.ts:1](<../../dozu-ui-service/src/api/type.ts#L1>)

Page interaction sites: `useRouter` at 28; `useSearchParams` at 30; `useAuth` at 38; `useTranslations` at 40; `useState` at 41; `useState` at 42; `usePost` at 56; `router.push` at 62; `sendChangePasswordRequest` at 70; `useEffect` at 78; `router.replace` at 81; `Input.onChange` at 99; `Input.onChange` at 112; `Button.onClick` at 122

Runtime parity: UNVERIFIED. Complete transitive interactions and source consumers are in the matching JSON page row.

### UI-022 `/[locale]/auth/changePasswordEmailSent`

Show delivery guidance and return navigation; not proof of email delivery.

[dozu-ui-service/src/app/[locale]/auth/changePasswordEmailSent/page.tsx:1](<../../dozu-ui-service/src/app/[locale]/auth/changePasswordEmailSent/page.tsx#L1>)

Inherited layouts: [dozu-ui-service/src/app/[locale]/layout.tsx:1](<../../dozu-ui-service/src/app/[locale]/layout.tsx#L1>), [dozu-ui-service/src/app/layout.tsx:1](<../../dozu-ui-service/src/app/layout.tsx#L1>)

Direct local imports: [dozu-ui-service/src/components/auth/CentralCard.tsx:1](<../../dozu-ui-service/src/components/auth/CentralCard.tsx#L1>), [dozu-ui-service/src/components/ui/button.tsx:1](<../../dozu-ui-service/src/components/ui/button.tsx#L1>), [dozu-ui-service/src/components/ui/card.tsx:1](<../../dozu-ui-service/src/components/ui/card.tsx#L1>)

Page interaction sites: `useTranslations` at 11; `useRouter` at 13; `router.push` at 16; `Button.onClick` at 31

Runtime parity: UNVERIFIED. Complete transitive interactions and source consumers are in the matching JSON page row.

### UI-023 `/[locale]/auth/forgotPassword`

Request password-change email and show sent/error state.

[dozu-ui-service/src/app/[locale]/auth/forgotPassword/page.tsx:1](<../../dozu-ui-service/src/app/[locale]/auth/forgotPassword/page.tsx#L1>)

Inherited layouts: [dozu-ui-service/src/app/[locale]/layout.tsx:1](<../../dozu-ui-service/src/app/[locale]/layout.tsx#L1>), [dozu-ui-service/src/app/layout.tsx:1](<../../dozu-ui-service/src/app/layout.tsx#L1>)

Direct local imports: [dozu-ui-service/src/components/auth/CentralCard.tsx:1](<../../dozu-ui-service/src/components/auth/CentralCard.tsx#L1>), [dozu-ui-service/src/components/ui/button.tsx:1](<../../dozu-ui-service/src/components/ui/button.tsx#L1>), [dozu-ui-service/src/components/ui/card.tsx:1](<../../dozu-ui-service/src/components/ui/card.tsx#L1>), [dozu-ui-service/src/components/ui/input.tsx:1](<../../dozu-ui-service/src/components/ui/input.tsx#L1>), [dozu-ui-service/src/components/ui/label.tsx:1](<../../dozu-ui-service/src/components/ui/label.tsx#L1>), [dozu-ui-service/src/hooks/usePost.ts:1](<../../dozu-ui-service/src/hooks/usePost.ts#L1>), [dozu-ui-service/src/utils/toast.helper.ts:1](<../../dozu-ui-service/src/utils/toast.helper.ts#L1>)

Page interaction sites: `useTranslations` at 21; `useState` at 22; `useRouter` at 23; `router.push` at 26; `usePost` at 38; `router.push` at 43; `sendChangePasswordRequest` at 48; `Input.onChange` at 65; `Button.onClick` at 76; `Button.onClick` at 82

Runtime parity: UNVERIFIED. Complete transitive interactions and source consumers are in the matching JSON page row.

### UI-024 `/[locale]/auth/login`

Password sign-in; real Google code redirect; preserve redirect destination and error/loading states.

[dozu-ui-service/src/app/[locale]/auth/login/page.tsx:1](<../../dozu-ui-service/src/app/[locale]/auth/login/page.tsx#L1>)

Inherited layouts: [dozu-ui-service/src/app/[locale]/layout.tsx:1](<../../dozu-ui-service/src/app/[locale]/layout.tsx#L1>), [dozu-ui-service/src/app/layout.tsx:1](<../../dozu-ui-service/src/app/layout.tsx#L1>)

Direct local imports: [dozu-ui-service/src/components/ui/input.tsx:1](<../../dozu-ui-service/src/components/ui/input.tsx#L1>), [dozu-ui-service/src/components/ui/button.tsx:1](<../../dozu-ui-service/src/components/ui/button.tsx#L1>), [dozu-ui-service/src/components/ui/card.tsx:1](<../../dozu-ui-service/src/components/ui/card.tsx#L1>), [dozu-ui-service/src/components/ui/label.tsx:1](<../../dozu-ui-service/src/components/ui/label.tsx#L1>), [dozu-ui-service/src/components/guards/RouteGuard.tsx:1](<../../dozu-ui-service/src/components/guards/RouteGuard.tsx#L1>), [dozu-ui-service/src/app/[locale]/auth/hooks/useLogin.ts:1](<../../dozu-ui-service/src/app/[locale]/auth/hooks/useLogin.ts#L1>), [dozu-ui-service/src/app/[locale]/auth/hooks/useGoogleAuth.ts:1](<../../dozu-ui-service/src/app/[locale]/auth/hooks/useGoogleAuth.ts#L1>), [dozu-ui-service/src/app/loading.tsx:1](<../../dozu-ui-service/src/app/loading.tsx#L1>), [dozu-ui-service/src/components/auth/CentralCard.tsx:1](<../../dozu-ui-service/src/components/auth/CentralCard.tsx#L1>)

Page interaction sites: `useRouter` at 21; `useState` at 22; `useTranslations` at 27; `useLogin` at 29; `useGoogleAuth` at 30; `router.push` at 42; `LoginForm.onInputChange` at 57; `LoginForm.onSubmit` at 57; `LoginForm.onGoogleLogin` at 57; `LoginForm.onForgetPassword` at 57; `form.onSubmit` at 108; `Input.onChange` at 121; `Input.onChange` at 134; `Button.onClick` at 146; `Button.onClick` at 155; `Button.onClick` at 165; `Link.href` at 181; `Link.href` at 186

Runtime parity: UNVERIFIED. Complete transitive interactions and source consumers are in the matching JSON page row.

### UI-025 `/[locale]/auth/register`

Create account, verification mail, Google sign-in, validation and login link.

[dozu-ui-service/src/app/[locale]/auth/register/page.tsx:1](<../../dozu-ui-service/src/app/[locale]/auth/register/page.tsx#L1>)

Inherited layouts: [dozu-ui-service/src/app/[locale]/layout.tsx:1](<../../dozu-ui-service/src/app/[locale]/layout.tsx#L1>), [dozu-ui-service/src/app/layout.tsx:1](<../../dozu-ui-service/src/app/layout.tsx#L1>)

Direct local imports: [dozu-ui-service/src/components/ui/input.tsx:1](<../../dozu-ui-service/src/components/ui/input.tsx#L1>), [dozu-ui-service/src/components/ui/button.tsx:1](<../../dozu-ui-service/src/components/ui/button.tsx#L1>), [dozu-ui-service/src/components/ui/card.tsx:1](<../../dozu-ui-service/src/components/ui/card.tsx#L1>), [dozu-ui-service/src/components/ui/label.tsx:1](<../../dozu-ui-service/src/components/ui/label.tsx#L1>), [dozu-ui-service/src/hooks/usePost.ts:1](<../../dozu-ui-service/src/hooks/usePost.ts#L1>), [dozu-ui-service/src/hooks/use-toast.ts:1](<../../dozu-ui-service/src/hooks/use-toast.ts#L1>), [dozu-ui-service/src/components/guards/RouteGuard.tsx:1](<../../dozu-ui-service/src/components/guards/RouteGuard.tsx#L1>), [dozu-ui-service/src/app/[locale]/auth/hooks/useGoogleAuth.ts:1](<../../dozu-ui-service/src/app/[locale]/auth/hooks/useGoogleAuth.ts#L1>), [dozu-ui-service/src/components/auth/CentralCard.tsx:1](<../../dozu-ui-service/src/components/auth/CentralCard.tsx#L1>), [dozu-ui-service/src/utils/toast.helper.ts:1](<../../dozu-ui-service/src/utils/toast.helper.ts#L1>), [dozu-ui-service/src/utils/constants/routes.ts:1](<../../dozu-ui-service/src/utils/constants/routes.ts#L1>)

Page interaction sites: `useTranslations` at 24; `useRouter` at 25; `useGoogleAuth` at 27; `useState` at 36; `useState` at 37; `useState` at 38; `usePost` at 41; `router.push` at 48; `form.onSubmit` at 72; `Input.onChange` at 75; `Input.onChange` at 88; `Input.onChange` at 103; `Button.onClick` at 122; `Link.href` at 135

Runtime parity: UNVERIFIED. Complete transitive interactions and source consumers are in the matching JSON page row.

### UI-026 `/[locale]/auth/testBackEnd`

Developer authentication/Redux test surface; preserve source, classify for release.

[dozu-ui-service/src/app/[locale]/auth/testBackEnd/page.tsx:1](<../../dozu-ui-service/src/app/[locale]/auth/testBackEnd/page.tsx#L1>)

Inherited layouts: [dozu-ui-service/src/app/[locale]/layout.tsx:1](<../../dozu-ui-service/src/app/[locale]/layout.tsx#L1>), [dozu-ui-service/src/app/layout.tsx:1](<../../dozu-ui-service/src/app/layout.tsx#L1>)

Direct local imports: [dozu-ui-service/src/api/api.ts:1](<../../dozu-ui-service/src/api/api.ts#L1>), [dozu-ui-service/src/api/axios.ts:1](<../../dozu-ui-service/src/api/axios.ts#L1>), [dozu-ui-service/src/stores/features/auth/authSlice.ts:1](<../../dozu-ui-service/src/stores/features/auth/authSlice.ts#L1>), [dozu-ui-service/src/stores/hooks.tsx:1](<../../dozu-ui-service/src/stores/hooks.tsx#L1>)

Page interaction sites: `useAppDispatch` at 10; `useEffect` at 11; `button.onClick` at 27

Runtime parity: UNVERIFIED. Complete transitive interactions and source consumers are in the matching JSON page row.

### UI-027 `/[locale]/auth/verifyEmail`

Read email/code query, verify with backend, update session and navigate.

[dozu-ui-service/src/app/[locale]/auth/verifyEmail/page.tsx:1](<../../dozu-ui-service/src/app/[locale]/auth/verifyEmail/page.tsx#L1>)

Inherited layouts: [dozu-ui-service/src/app/[locale]/layout.tsx:1](<../../dozu-ui-service/src/app/[locale]/layout.tsx#L1>), [dozu-ui-service/src/app/layout.tsx:1](<../../dozu-ui-service/src/app/layout.tsx#L1>)

Direct local imports: [dozu-ui-service/src/components/ui/card.tsx:1](<../../dozu-ui-service/src/components/ui/card.tsx#L1>), [dozu-ui-service/src/components/ui/spinner.tsx:1](<../../dozu-ui-service/src/components/ui/spinner.tsx#L1>), [dozu-ui-service/src/contexts/auth/AuthContext.tsx:1](<../../dozu-ui-service/src/contexts/auth/AuthContext.tsx#L1>), [dozu-ui-service/src/hooks/useAuthNavigation.ts:1](<../../dozu-ui-service/src/hooks/useAuthNavigation.ts#L1>), [dozu-ui-service/src/hooks/usePost.ts:1](<../../dozu-ui-service/src/hooks/usePost.ts#L1>), [dozu-ui-service/src/services/auth/auth.service.ts:1](<../../dozu-ui-service/src/services/auth/auth.service.ts#L1>), [dozu-ui-service/src/types/auth.ts:1](<../../dozu-ui-service/src/types/auth.ts#L1>), [dozu-ui-service/src/utils/toast.helper.ts:1](<../../dozu-ui-service/src/utils/toast.helper.ts#L1>)

Page interaction sites: `useAuth` at 17; `useAuthNavigation` at 18; `useTranslations` at 19; `useRouter` at 20; `useSearchParams` at 21; `usePost` at 30; `router.push` at 33; `router.push` at 38; `useEffect` at 42; `router.push` at 45

Runtime parity: UNVERIFIED. Complete transitive interactions and source consumers are in the matching JSON page row.

### UI-028 `/[locale]/blogs`

Render Blog Page heading; placeholder, no blog CRUD.

[dozu-ui-service/src/app/[locale]/blogs/page.tsx:1](<../../dozu-ui-service/src/app/[locale]/blogs/page.tsx#L1>)

Inherited layouts: [dozu-ui-service/src/app/[locale]/layout.tsx:1](<../../dozu-ui-service/src/app/[locale]/layout.tsx#L1>), [dozu-ui-service/src/app/layout.tsx:1](<../../dozu-ui-service/src/app/layout.tsx#L1>)

Direct local imports: none

Page interaction sites: none in page AST; inspect imported component ledger

Runtime parity: UNVERIFIED. Complete transitive interactions and source consumers are in the matching JSON page row.

### UI-029 `/[locale]/class-based/[id]/assignments/[assignmentId]/details`

Read assignment/attachments/comments; student uploads/replaces/submits work and reads private feedback.

[dozu-ui-service/src/app/[locale]/class-based/[id]/assignments/[assignmentId]/details/page.tsx:1](<../../dozu-ui-service/src/app/[locale]/class-based/[id]/assignments/[assignmentId]/details/page.tsx#L1>)

Inherited layouts: [dozu-ui-service/src/app/[locale]/class-based/[id]/layout.tsx:1](<../../dozu-ui-service/src/app/[locale]/class-based/[id]/layout.tsx#L1>), [dozu-ui-service/src/app/[locale]/layout.tsx:1](<../../dozu-ui-service/src/app/[locale]/layout.tsx#L1>), [dozu-ui-service/src/app/layout.tsx:1](<../../dozu-ui-service/src/app/layout.tsx#L1>)

Direct local imports: [dozu-ui-service/src/app/[locale]/class-based/(classwork)/components/common/details/ContentSection.tsx:1](<../../dozu-ui-service/src/app/[locale]/class-based/(classwork)/components/common/details/ContentSection.tsx#L1>), [dozu-ui-service/src/app/[locale]/class-based/(classwork)/components/common/details/AttachmentsViewSection.tsx:1](<../../dozu-ui-service/src/app/[locale]/class-based/(classwork)/components/common/details/AttachmentsViewSection.tsx#L1>), [dozu-ui-service/src/components/ui/separator.tsx:1](<../../dozu-ui-service/src/components/ui/separator.tsx#L1>), [dozu-ui-service/src/hooks/useFetch.ts:1](<../../dozu-ui-service/src/hooks/useFetch.ts#L1>), [dozu-ui-service/src/app/[locale]/class-based/(assignment)/types/assignment.type.ts:1](<../../dozu-ui-service/src/app/[locale]/class-based/(assignment)/types/assignment.type.ts#L1>), [dozu-ui-service/src/app/[locale]/class-based/(assignment)/service/assignment.service.ts:1](<../../dozu-ui-service/src/app/[locale]/class-based/(assignment)/service/assignment.service.ts#L1>), [dozu-ui-service/src/app/loading.tsx:1](<../../dozu-ui-service/src/app/loading.tsx#L1>), [dozu-ui-service/src/components/ui/dropdown-menu.tsx:1](<../../dozu-ui-service/src/components/ui/dropdown-menu.tsx#L1>), [dozu-ui-service/src/app/[locale]/class-based/[id]/assignments/[assignmentId]/details/components/SubmissionCard.tsx:1](<../../dozu-ui-service/src/app/[locale]/class-based/[id]/assignments/[assignmentId]/details/components/SubmissionCard.tsx#L1>), [dozu-ui-service/src/app/[locale]/teacher/class-based/[id]/assignments/[assignmentId]/details/components/CommentSection.tsx:1](<../../dozu-ui-service/src/app/[locale]/teacher/class-based/[id]/assignments/[assignmentId]/details/components/CommentSection.tsx#L1>), [dozu-ui-service/src/app/[locale]/class-based/(assignment)/types/assignmentSubmission.type.ts:1](<../../dozu-ui-service/src/app/[locale]/class-based/(assignment)/types/assignmentSubmission.type.ts#L1>), [dozu-ui-service/src/app/[locale]/class-based/(assignment)/service/assignmentSubmission.service.ts:1](<../../dozu-ui-service/src/app/[locale]/class-based/(assignment)/service/assignmentSubmission.service.ts#L1>), [dozu-ui-service/src/hooks/usePost.ts:1](<../../dozu-ui-service/src/hooks/usePost.ts#L1>), [dozu-ui-service/src/utils/toast.helper.ts:1](<../../dozu-ui-service/src/utils/toast.helper.ts#L1>), [dozu-ui-service/src/app/[locale]/class-based/(classwork)/types/attachment.type.ts:1](<../../dozu-ui-service/src/app/[locale]/class-based/(classwork)/types/attachment.type.ts#L1>), [dozu-ui-service/src/hooks/upload/useUploadAttachmentFiles.tsx:1](<../../dozu-ui-service/src/hooks/upload/useUploadAttachmentFiles.tsx#L1>), [dozu-ui-service/src/app/[locale]/generate/constants/resource.ts:1](<../../dozu-ui-service/src/app/[locale]/generate/constants/resource.ts#L1>)

Page interaction sites: `useParams` at 37; `useRouter` at 56; `useTranslations` at 57; `useFetch` at 65; `useFetch` at 74; `usePost` at 79; `useUploadAttachmentFiles` at 99; `SubmissionCard.onSubmit` at 178

Runtime parity: UNVERIFIED. Complete transitive interactions and source consumers are in the matching JSON page row.

### UI-030 `/[locale]/class-based/[id]/class-quiz/[classQuizId]/history`

List/review student attempt history with answers and timing.

[dozu-ui-service/src/app/[locale]/class-based/[id]/class-quiz/[classQuizId]/history/page.tsx:1](<../../dozu-ui-service/src/app/[locale]/class-based/[id]/class-quiz/[classQuizId]/history/page.tsx#L1>)

Inherited layouts: [dozu-ui-service/src/app/[locale]/class-based/[id]/layout.tsx:1](<../../dozu-ui-service/src/app/[locale]/class-based/[id]/layout.tsx#L1>), [dozu-ui-service/src/app/[locale]/layout.tsx:1](<../../dozu-ui-service/src/app/[locale]/layout.tsx#L1>), [dozu-ui-service/src/app/layout.tsx:1](<../../dozu-ui-service/src/app/layout.tsx#L1>)

Direct local imports: [dozu-ui-service/src/app/[locale]/class-based/(class-quiz)/services/classQuizStudent.service.ts:1](<../../dozu-ui-service/src/app/[locale]/class-based/(class-quiz)/services/classQuizStudent.service.ts#L1>), [dozu-ui-service/src/app/loading.tsx:1](<../../dozu-ui-service/src/app/loading.tsx#L1>), [dozu-ui-service/src/app/[locale]/class-based/(class-quiz)/types/classQuiz.type.ts:1](<../../dozu-ui-service/src/app/[locale]/class-based/(class-quiz)/types/classQuiz.type.ts#L1>), [dozu-ui-service/src/app/[locale]/quiz/components/QuizQuestion.tsx:1](<../../dozu-ui-service/src/app/[locale]/quiz/components/QuizQuestion.tsx#L1>), [dozu-ui-service/src/components/ui/button.tsx:1](<../../dozu-ui-service/src/components/ui/button.tsx#L1>), [dozu-ui-service/src/components/ui/card.tsx:1](<../../dozu-ui-service/src/components/ui/card.tsx#L1>)

Page interaction sites: `useParams` at 13; `useRouter` at 14; `useSearchParams` at 15; `useState` at 20; `useState` at 21; `useState` at 22; `useEffect` at 25; `useEffect` at 33; `Button.onClick` at 80; `router.push` at 84; `Button.onClick` at 169; `router.push` at 172; `QuizQuestion.onAnswerSelect` at 184

Runtime parity: UNVERIFIED. Complete transitive interactions and source consumers are in the matching JSON page row.

### UI-031 `/[locale]/class-based/[id]/class-quiz/[classQuizId]/start`

Student start timed attempt, autosave answers, receive quiz activity and confirm submit.

[dozu-ui-service/src/app/[locale]/class-based/[id]/class-quiz/[classQuizId]/start/page.tsx:1](<../../dozu-ui-service/src/app/[locale]/class-based/[id]/class-quiz/[classQuizId]/start/page.tsx#L1>)

Inherited layouts: [dozu-ui-service/src/app/[locale]/class-based/[id]/layout.tsx:1](<../../dozu-ui-service/src/app/[locale]/class-based/[id]/layout.tsx#L1>), [dozu-ui-service/src/app/[locale]/layout.tsx:1](<../../dozu-ui-service/src/app/[locale]/layout.tsx#L1>), [dozu-ui-service/src/app/layout.tsx:1](<../../dozu-ui-service/src/app/layout.tsx#L1>)

Direct local imports: [dozu-ui-service/src/utils/constants/routes.ts:1](<../../dozu-ui-service/src/utils/constants/routes.ts#L1>), [dozu-ui-service/src/app/loading.tsx:1](<../../dozu-ui-service/src/app/loading.tsx#L1>), [dozu-ui-service/src/app/[locale]/class-based/(class-quiz)/services/classQuizStudent.service.ts:1](<../../dozu-ui-service/src/app/[locale]/class-based/(class-quiz)/services/classQuizStudent.service.ts#L1>), [dozu-ui-service/src/app/[locale]/class-based/(class-quiz)/types/classQuiz.type.ts:1](<../../dozu-ui-service/src/app/[locale]/class-based/(class-quiz)/types/classQuiz.type.ts#L1>), [dozu-ui-service/src/components/ui/button.tsx:1](<../../dozu-ui-service/src/components/ui/button.tsx#L1>), [dozu-ui-service/src/app/[locale]/quiz/components/QuizQuestion.tsx:1](<../../dozu-ui-service/src/app/[locale]/quiz/components/QuizQuestion.tsx#L1>), [dozu-ui-service/src/hooks/use-toast.ts:1](<../../dozu-ui-service/src/hooks/use-toast.ts#L1>), [dozu-ui-service/src/app/[locale]/auth/hooks/useUserSession.ts:1](<../../dozu-ui-service/src/app/[locale]/auth/hooks/useUserSession.ts#L1>), [dozu-ui-service/src/hooks/useQuizActivityWebSocket.ts:1](<../../dozu-ui-service/src/hooks/useQuizActivityWebSocket.ts#L1>), [dozu-ui-service/src/components/ui/alert-dialog.tsx:1](<../../dozu-ui-service/src/components/ui/alert-dialog.tsx#L1>)

Page interaction sites: `useParams` at 48; `useRouter` at 52; `useParams` at 53; `useUserSession` at 54; `useState` at 58; `useState` at 59; `useState` at 60; `useState` at 61; `useState` at 63; `useState` at 64; `useState` at 65; `useState` at 68; `useState` at 71; `useRef` at 72; `useRef` at 73; `useQuizActivityWebSocket` at 75; `useMemo` at 82; `window.localStorage.getItem` at 90; `window.localStorage.setItem` at 96; `window.localStorage.removeItem` at 101; `useRef` at 105; `useEffect` at 106; `useEffect` at 129; `useEffect` at 137; `router.push` at 250; `useEffect` at 272; `Button.onClick` at 327; `Button.onClick` at 359; `button.onClick` at 391; `button.onClick` at 422; `QuizQuestion.onAnswerSelect` at 440; `Button.onClick` at 456; `Button.onClick` at 464; `AlertDialog.onOpenChange` at 483; `AlertDialogAction.onClick` at 494

Runtime parity: UNVERIFIED. Complete transitive interactions and source consumers are in the matching JSON page row.

### UI-032 `/[locale]/class-based/[id]/class-quiz/[classQuizId]/submit`

Submit/review attempt and show result; preserve deadline/retry semantics.

[dozu-ui-service/src/app/[locale]/class-based/[id]/class-quiz/[classQuizId]/submit/page.tsx:1](<../../dozu-ui-service/src/app/[locale]/class-based/[id]/class-quiz/[classQuizId]/submit/page.tsx#L1>)

Inherited layouts: [dozu-ui-service/src/app/[locale]/class-based/[id]/layout.tsx:1](<../../dozu-ui-service/src/app/[locale]/class-based/[id]/layout.tsx#L1>), [dozu-ui-service/src/app/[locale]/layout.tsx:1](<../../dozu-ui-service/src/app/[locale]/layout.tsx#L1>), [dozu-ui-service/src/app/layout.tsx:1](<../../dozu-ui-service/src/app/layout.tsx#L1>)

Direct local imports: [dozu-ui-service/src/app/[locale]/class-based/(class-quiz)/services/classQuizStudent.service.ts:1](<../../dozu-ui-service/src/app/[locale]/class-based/(class-quiz)/services/classQuizStudent.service.ts#L1>), [dozu-ui-service/src/app/loading.tsx:1](<../../dozu-ui-service/src/app/loading.tsx#L1>), [dozu-ui-service/src/app/[locale]/class-based/(class-quiz)/types/classQuiz.type.ts:1](<../../dozu-ui-service/src/app/[locale]/class-based/(class-quiz)/types/classQuiz.type.ts#L1>), [dozu-ui-service/src/app/[locale]/quiz/components/QuizQuestion.tsx:1](<../../dozu-ui-service/src/app/[locale]/quiz/components/QuizQuestion.tsx#L1>), [dozu-ui-service/src/components/ui/button.tsx:1](<../../dozu-ui-service/src/components/ui/button.tsx#L1>), [dozu-ui-service/src/components/ui/card.tsx:1](<../../dozu-ui-service/src/components/ui/card.tsx#L1>), [dozu-ui-service/src/utils/constants/routes.ts:1](<../../dozu-ui-service/src/utils/constants/routes.ts#L1>)

Page interaction sites: `useParams` at 13; `useSearchParams` at 14; `useRouter` at 15; `useState` at 19; `useState` at 20; `useEffect` at 22; `Button.onClick` at 84; `router.push` at 84; `QuizQuestion.onAnswerSelect` at 95

Runtime parity: UNVERIFIED. Complete transitive interactions and source consumers are in the matching JSON page row.

### UI-033 `/[locale]/class-based/[id]/learning-material/[learningMaterialId]/details`

Read material content/attachments/comments; student read/comment actions.

[dozu-ui-service/src/app/[locale]/class-based/[id]/learning-material/[learningMaterialId]/details/page.tsx:1](<../../dozu-ui-service/src/app/[locale]/class-based/[id]/learning-material/[learningMaterialId]/details/page.tsx#L1>)

Inherited layouts: [dozu-ui-service/src/app/[locale]/class-based/[id]/layout.tsx:1](<../../dozu-ui-service/src/app/[locale]/class-based/[id]/layout.tsx#L1>), [dozu-ui-service/src/app/[locale]/layout.tsx:1](<../../dozu-ui-service/src/app/[locale]/layout.tsx#L1>), [dozu-ui-service/src/app/layout.tsx:1](<../../dozu-ui-service/src/app/layout.tsx#L1>)

Direct local imports: [dozu-ui-service/src/app/[locale]/class-based/(classwork)/components/common/details/ContentSection.tsx:1](<../../dozu-ui-service/src/app/[locale]/class-based/(classwork)/components/common/details/ContentSection.tsx#L1>), [dozu-ui-service/src/app/[locale]/class-based/(classwork)/components/common/details/AttachmentsViewSection.tsx:1](<../../dozu-ui-service/src/app/[locale]/class-based/(classwork)/components/common/details/AttachmentsViewSection.tsx#L1>), [dozu-ui-service/src/components/ui/separator.tsx:1](<../../dozu-ui-service/src/components/ui/separator.tsx#L1>), [dozu-ui-service/src/hooks/useFetch.ts:1](<../../dozu-ui-service/src/hooks/useFetch.ts#L1>), [dozu-ui-service/src/app/loading.tsx:1](<../../dozu-ui-service/src/app/loading.tsx#L1>), [dozu-ui-service/src/components/ui/dropdown-menu.tsx:1](<../../dozu-ui-service/src/components/ui/dropdown-menu.tsx#L1>), [dozu-ui-service/src/app/[locale]/class-based/(learning-material)/types/learningMaterial.type.ts:1](<../../dozu-ui-service/src/app/[locale]/class-based/(learning-material)/types/learningMaterial.type.ts#L1>), [dozu-ui-service/src/app/[locale]/class-based/(learning-material)/service/learningMaterial.service.ts:1](<../../dozu-ui-service/src/app/[locale]/class-based/(learning-material)/service/learningMaterial.service.ts#L1>), [dozu-ui-service/src/app/[locale]/class-based/[id]/learning-material/[learningMaterialId]/details/components/LearningMaterialCommentSection.tsx:1](<../../dozu-ui-service/src/app/[locale]/class-based/[id]/learning-material/[learningMaterialId]/details/components/LearningMaterialCommentSection.tsx#L1>)

Page interaction sites: `useParams` at 22; `useRouter` at 41; `useTranslations` at 42; `useFetch` at 49

Runtime parity: UNVERIFIED. Complete transitive interactions and source consumers are in the matching JSON page row.

### UI-034 `/[locale]/class-based/[id]/mindmap/[topicId]`

Class topic ReactFlow mindmap, source and flashcard sheets, export; student read-only access.

[dozu-ui-service/src/app/[locale]/class-based/[id]/mindmap/[topicId]/page.tsx:1](<../../dozu-ui-service/src/app/[locale]/class-based/[id]/mindmap/[topicId]/page.tsx#L1>)

Inherited layouts: [dozu-ui-service/src/app/[locale]/class-based/[id]/layout.tsx:1](<../../dozu-ui-service/src/app/[locale]/class-based/[id]/layout.tsx#L1>), [dozu-ui-service/src/app/[locale]/class-based/[id]/mindmap/[topicId]/layout.tsx:1](<../../dozu-ui-service/src/app/[locale]/class-based/[id]/mindmap/[topicId]/layout.tsx#L1>), [dozu-ui-service/src/app/[locale]/layout.tsx:1](<../../dozu-ui-service/src/app/[locale]/layout.tsx#L1>), [dozu-ui-service/src/app/layout.tsx:1](<../../dozu-ui-service/src/app/layout.tsx#L1>)

Direct local imports: [dozu-ui-service/src/stores/hooks.tsx:1](<../../dozu-ui-service/src/stores/hooks.tsx#L1>), [dozu-ui-service/src/components/ui/button.tsx:1](<../../dozu-ui-service/src/components/ui/button.tsx#L1>), [dozu-ui-service/src/utils/routerService.ts:1](<../../dozu-ui-service/src/utils/routerService.ts#L1>), [dozu-ui-service/src/components/generative/GeneratingSkeleton.tsx:1](<../../dozu-ui-service/src/components/generative/GeneratingSkeleton.tsx#L1>), [dozu-ui-service/src/hooks/use-toast.ts:1](<../../dozu-ui-service/src/hooks/use-toast.ts#L1>), [dozu-ui-service/src/app/[locale]/flashcards/components/FlashcardEditor.tsx:1](<../../dozu-ui-service/src/app/[locale]/flashcards/components/FlashcardEditor.tsx#L1>), [dozu-ui-service/src/app/[locale]/generate/components/ContentGenerationPreview.tsx:1](<../../dozu-ui-service/src/app/[locale]/generate/components/ContentGenerationPreview.tsx#L1>), [dozu-ui-service/src/app/[locale]/generate/hooks/useContentGeneration.ts:1](<../../dozu-ui-service/src/app/[locale]/generate/hooks/useContentGeneration.ts#L1>), [dozu-ui-service/src/components/mindmap/button/DownloadButton.tsx:1](<../../dozu-ui-service/src/components/mindmap/button/DownloadButton.tsx#L1>), [dozu-ui-service/src/components/mindmap/button/ViewFileButton.tsx:1](<../../dozu-ui-service/src/components/mindmap/button/ViewFileButton.tsx#L1>), [dozu-ui-service/src/app/[locale]/mindmap/components/FileSheet.tsx:1](<../../dozu-ui-service/src/app/[locale]/mindmap/components/FileSheet.tsx#L1>), [dozu-ui-service/src/app/[locale]/mindmap/components/FloatingEdge.tsx:1](<../../dozu-ui-service/src/app/[locale]/mindmap/components/FloatingEdge.tsx#L1>), [dozu-ui-service/src/app/[locale]/mindmap/components/NodeSheetViewOnly.tsx:1](<../../dozu-ui-service/src/app/[locale]/mindmap/components/NodeSheetViewOnly.tsx#L1>), [dozu-ui-service/src/app/[locale]/mindmap/components/ReactFlowNodeInClass.tsx:1](<../../dozu-ui-service/src/app/[locale]/mindmap/components/ReactFlowNodeInClass.tsx#L1>), [dozu-ui-service/src/app/[locale]/mindmap/context/MindMapContext.tsx:1](<../../dozu-ui-service/src/app/[locale]/mindmap/context/MindMapContext.tsx#L1>), [dozu-ui-service/src/app/loading.tsx:1](<../../dozu-ui-service/src/app/loading.tsx#L1>), [dozu-ui-service/src/services/flashcard/flashcard.service.ts:1](<../../dozu-ui-service/src/services/flashcard/flashcard.service.ts#L1>)

Page interaction sites: `useRouter` at 43; `useMindMapContext` at 57; `useState` at 59; `useContentGeneration` at 61; `useAppSelector` at 63; `useEffect` at 65; `useEffect` at 69; `router.push` at 117; `ContentGenerationPreview.onSave` at 126; `Button.onClick` at 134; `ReactFlow.onNodesChange` at 144; `ReactFlow.onEdgesChange` at 144

Runtime parity: UNVERIFIED. Complete transitive interactions and source consumers are in the matching JSON page row.

### UI-035 `/[locale]/class-based/[id]`

Student dashboard tabs: topics, feed, classwork/materials, assignments and quizzes.

[dozu-ui-service/src/app/[locale]/class-based/[id]/page.tsx:1](<../../dozu-ui-service/src/app/[locale]/class-based/[id]/page.tsx#L1>)

Inherited layouts: [dozu-ui-service/src/app/[locale]/class-based/[id]/layout.tsx:1](<../../dozu-ui-service/src/app/[locale]/class-based/[id]/layout.tsx#L1>), [dozu-ui-service/src/app/[locale]/layout.tsx:1](<../../dozu-ui-service/src/app/[locale]/layout.tsx#L1>), [dozu-ui-service/src/app/layout.tsx:1](<../../dozu-ui-service/src/app/layout.tsx#L1>)

Direct local imports: [dozu-ui-service/src/contexts/class-based/index.ts:1](<../../dozu-ui-service/src/contexts/class-based/index.ts#L1>), [dozu-ui-service/src/app/[locale]/class-based/[id]/dashboard/StudentClassDashboard.tsx:1](<../../dozu-ui-service/src/app/[locale]/class-based/[id]/dashboard/StudentClassDashboard.tsx#L1>)

Page interaction sites: `useClassBased` at 7

Runtime parity: UNVERIFIED. Complete transitive interactions and source consumers are in the matching JSON page row.

### UI-036 `/[locale]/class-based/[id]/topics/[topicId]`

Class context wraps shared topic workspace and mindmap provider; preserve teacher/student permissions across tabs.

[dozu-ui-service/src/app/[locale]/class-based/[id]/topics/[topicId]/page.tsx:1](<../../dozu-ui-service/src/app/[locale]/class-based/[id]/topics/[topicId]/page.tsx#L1>)

Inherited layouts: [dozu-ui-service/src/app/[locale]/class-based/[id]/layout.tsx:1](<../../dozu-ui-service/src/app/[locale]/class-based/[id]/layout.tsx#L1>), [dozu-ui-service/src/app/[locale]/layout.tsx:1](<../../dozu-ui-service/src/app/[locale]/layout.tsx#L1>), [dozu-ui-service/src/app/layout.tsx:1](<../../dozu-ui-service/src/app/layout.tsx#L1>)

Direct local imports: [dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/context/TopicWorkspaceContext.tsx:1](<../../dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/context/TopicWorkspaceContext.tsx#L1>), [dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/workspace/TopicWorkspace.tsx:1](<../../dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/workspace/TopicWorkspace.tsx#L1>), [dozu-ui-service/src/app/[locale]/mindmap/context/MindMapContext.tsx:1](<../../dozu-ui-service/src/app/[locale]/mindmap/context/MindMapContext.tsx#L1>)

Page interaction sites: `useParams` at 10

Runtime parity: UNVERIFIED. Complete transitive interactions and source consumers are in the matching JSON page row.

### UI-037 `/[locale]/class-based`

Student class library, invitation/join and class navigation.

[dozu-ui-service/src/app/[locale]/class-based/page.tsx:1](<../../dozu-ui-service/src/app/[locale]/class-based/page.tsx#L1>)

Inherited layouts: [dozu-ui-service/src/app/[locale]/layout.tsx:1](<../../dozu-ui-service/src/app/[locale]/layout.tsx#L1>), [dozu-ui-service/src/app/layout.tsx:1](<../../dozu-ui-service/src/app/layout.tsx#L1>)

Direct local imports: [dozu-ui-service/src/app/[locale]/class-based/components/ui/class/StudentClassLibrary.tsx:1](<../../dozu-ui-service/src/app/[locale]/class-based/components/ui/class/StudentClassLibrary.tsx#L1>), [dozu-ui-service/src/components/common/BackgroundGradient.tsx:1](<../../dozu-ui-service/src/components/common/BackgroundGradient.tsx#L1>)

Page interaction sites: none in page AST; inspect imported component ledger

Runtime parity: UNVERIFIED. Complete transitive interactions and source consumers are in the matching JSON page row.

### UI-038 `/[locale]/feynman/[topicId]`

Read mission/source, write explanation, request genuine AI questions/review, view history and save learning progress.

[dozu-ui-service/src/app/[locale]/feynman/[topicId]/page.tsx:1](<../../dozu-ui-service/src/app/[locale]/feynman/[topicId]/page.tsx#L1>)

Inherited layouts: [dozu-ui-service/src/app/[locale]/feynman/[topicId]/layout.tsx:1](<../../dozu-ui-service/src/app/[locale]/feynman/[topicId]/layout.tsx#L1>), [dozu-ui-service/src/app/[locale]/layout.tsx:1](<../../dozu-ui-service/src/app/[locale]/layout.tsx#L1>), [dozu-ui-service/src/app/layout.tsx:1](<../../dozu-ui-service/src/app/layout.tsx#L1>)

Direct local imports: [dozu-ui-service/src/hooks/generate/useGenerate.tsx:1](<../../dozu-ui-service/src/hooks/generate/useGenerate.tsx#L1>), [dozu-ui-service/src/hooks/useFetch.ts:1](<../../dozu-ui-service/src/hooks/useFetch.ts#L1>), [dozu-ui-service/src/services/flashcard/flashcard.service.ts:1](<../../dozu-ui-service/src/services/flashcard/flashcard.service.ts#L1>), [dozu-ui-service/src/app/loading.tsx:1](<../../dozu-ui-service/src/app/loading.tsx#L1>), [dozu-ui-service/src/components/ui/skeleton.tsx:1](<../../dozu-ui-service/src/components/ui/skeleton.tsx#L1>), [dozu-ui-service/src/components/ui/button.tsx:1](<../../dozu-ui-service/src/components/ui/button.tsx#L1>), [dozu-ui-service/src/components/feynman/FeynmanEditor.tsx:1](<../../dozu-ui-service/src/components/feynman/FeynmanEditor.tsx#L1>), [dozu-ui-service/src/components/feynman/ActionBar.tsx:1](<../../dozu-ui-service/src/components/feynman/ActionBar.tsx#L1>), [dozu-ui-service/src/components/ui/card.tsx:1](<../../dozu-ui-service/src/components/ui/card.tsx#L1>), [dozu-ui-service/src/utils/index.ts:1](<../../dozu-ui-service/src/utils/index.ts#L1>), [dozu-ui-service/src/components/feynman/ReviewedDialog.tsx:1](<../../dozu-ui-service/src/components/feynman/ReviewedDialog.tsx#L1>), [dozu-ui-service/src/components/feynman/types.ts:1](<../../dozu-ui-service/src/components/feynman/types.ts#L1>), [dozu-ui-service/src/components/feynman/config.ts:1](<../../dozu-ui-service/src/components/feynman/config.ts#L1>), [dozu-ui-service/src/app/[locale]/feynman/[topicId]/hooks/useFeynmanService.tsx:1](<../../dozu-ui-service/src/app/[locale]/feynman/[topicId]/hooks/useFeynmanService.tsx#L1>), [dozu-ui-service/src/components/feynman/History.tsx:1](<../../dozu-ui-service/src/components/feynman/History.tsx#L1>), [dozu-ui-service/src/components/feynman/LeftMissionPanel.tsx:1](<../../dozu-ui-service/src/components/feynman/LeftMissionPanel.tsx#L1>), [dozu-ui-service/src/hooks/use-toast.ts:1](<../../dozu-ui-service/src/hooks/use-toast.ts#L1>), [dozu-ui-service/src/hoc/withAuth.tsx:1](<../../dozu-ui-service/src/hoc/withAuth.tsx#L1>)

Page interaction sites: `useTranslations` at 27; `useTranslations` at 28; `useSearchParams` at 30; `useParams` at 31; `useState` at 35; `useState` at 36; `useState` at 37; `useState` at 39; `useState` at 40; `useState` at 41; `useState` at 42; `useState` at 43; `useFeynmanService` at 45; `useFetch` at 55; `useGenerate` at 76; `useGenerate` at 86; `useRef` at 88; `useRef` at 90; `useRef` at 91; `useRef` at 92; `useRef` at 93; `useRef` at 94; `useRef` at 95; `useRef` at 96; `useRef` at 97; `useEffect` at 99; `useEffect` at 102; `useEffect` at 105; `useEffect` at 108; `useEffect` at 111; `useEffect` at 114; `useEffect` at 117; `useEffect` at 120; `useCallback` at 229; `useCallback` at 257; `useMemo` at 309; `useEffect` at 318; `useEffect` at 326; `useEffect` at 330; `useMemo` at 336; `useMemo` at 340; `useMemo` at 344; `LeftMissionPanel.onToggle` at 377; `LeftMissionPanel.onUseAnalogy` at 377; `FeynmanEditor.onChange` at 396; `FeynmanEditor.onChangeHtml` at 396; `ActionBar.onSubmit` at 406; `ActionBar.onGetHints` at 406; `ActionBar.onSave` at 406; `ActionBar.onReset` at 406; `FeynmanReviewDialog.onOpenChange` at 420; `Button.onClick` at 426; `withAuth` at 445

Runtime parity: UNVERIFIED. Complete transitive interactions and source consumers are in the matching JSON page row.

### UI-039 `/[locale]/games/brain-chase`

Flashcard-based game, pause/restart/settings and result/progress integration.

[dozu-ui-service/src/app/[locale]/games/brain-chase/page.tsx:1](<../../dozu-ui-service/src/app/[locale]/games/brain-chase/page.tsx#L1>)

Inherited layouts: [dozu-ui-service/src/app/[locale]/games/brain-chase/layout.tsx:1](<../../dozu-ui-service/src/app/[locale]/games/brain-chase/layout.tsx#L1>), [dozu-ui-service/src/app/[locale]/layout.tsx:1](<../../dozu-ui-service/src/app/[locale]/layout.tsx#L1>), [dozu-ui-service/src/app/layout.tsx:1](<../../dozu-ui-service/src/app/layout.tsx#L1>)

Direct local imports: [dozu-ui-service/src/components/ui/button.tsx:1](<../../dozu-ui-service/src/components/ui/button.tsx#L1>), [dozu-ui-service/src/app/[locale]/games/brain-chase/components/GameArea.tsx:1](<../../dozu-ui-service/src/app/[locale]/games/brain-chase/components/GameArea.tsx#L1>), [dozu-ui-service/src/app/[locale]/games/brain-chase/components/QuestionArea.tsx:1](<../../dozu-ui-service/src/app/[locale]/games/brain-chase/components/QuestionArea.tsx#L1>), [dozu-ui-service/src/app/[locale]/games/brain-chase/components/Setting.tsx:1](<../../dozu-ui-service/src/app/[locale]/games/brain-chase/components/Setting.tsx#L1>), [dozu-ui-service/src/app/[locale]/games/brain-chase/context/brainChaseContext.tsx:1](<../../dozu-ui-service/src/app/[locale]/games/brain-chase/context/brainChaseContext.tsx#L1>), [dozu-ui-service/src/components/ui/tooltip.tsx:1](<../../dozu-ui-service/src/components/ui/tooltip.tsx#L1>)

Page interaction sites: `useTranslations` at 14; `useBrainChase` at 31; `Button.onClick` at 51; `Button.onClick` at 75; `Button.onClick` at 88; `Button.onClick` at 99; `Button.onClick` at 116; `Button.onClick` at 135; `Button.onClick` at 167; `Button.onClick` at 170; `useSearchParams` at 180

Runtime parity: UNVERIFIED. Complete transitive interactions and source consumers are in the matching JSON page row.

### UI-040 `/[locale]/games/memory-match`

Match flashcard pairs, timer/game state and completion behavior.

[dozu-ui-service/src/app/[locale]/games/memory-match/page.tsx:1](<../../dozu-ui-service/src/app/[locale]/games/memory-match/page.tsx#L1>)

Inherited layouts: [dozu-ui-service/src/app/[locale]/games/memory-match/layout.tsx:1](<../../dozu-ui-service/src/app/[locale]/games/memory-match/layout.tsx#L1>), [dozu-ui-service/src/app/[locale]/layout.tsx:1](<../../dozu-ui-service/src/app/[locale]/layout.tsx#L1>), [dozu-ui-service/src/app/layout.tsx:1](<../../dozu-ui-service/src/app/layout.tsx#L1>)

Direct local imports: [dozu-ui-service/src/app/[locale]/games/memory-match/context/MemoryMatchContext.tsx:1](<../../dozu-ui-service/src/app/[locale]/games/memory-match/context/MemoryMatchContext.tsx#L1>), [dozu-ui-service/src/app/[locale]/games/memory-match/components/MemoryMatchGame.tsx:1](<../../dozu-ui-service/src/app/[locale]/games/memory-match/components/MemoryMatchGame.tsx#L1>)

Page interaction sites: `useSearchParams` at 9

Runtime parity: UNVERIFIED. Complete transitive interactions and source consumers are in the matching JSON page row.

### UI-041 `/[locale]/generate`

Choose text/file/URL/YouTube/media input, convert/transcribe, select model/content/difficulty, stream generation, preview/save study content.

[dozu-ui-service/src/app/[locale]/generate/page.tsx:1](<../../dozu-ui-service/src/app/[locale]/generate/page.tsx#L1>)

Inherited layouts: [dozu-ui-service/src/app/[locale]/generate/layout.tsx:1](<../../dozu-ui-service/src/app/[locale]/generate/layout.tsx#L1>), [dozu-ui-service/src/app/[locale]/layout.tsx:1](<../../dozu-ui-service/src/app/[locale]/layout.tsx#L1>), [dozu-ui-service/src/app/layout.tsx:1](<../../dozu-ui-service/src/app/layout.tsx#L1>)

Direct local imports: [dozu-ui-service/src/hoc/withAuth.tsx:1](<../../dozu-ui-service/src/hoc/withAuth.tsx#L1>), [dozu-ui-service/src/utils/constants/common.constant.ts:1](<../../dozu-ui-service/src/utils/constants/common.constant.ts#L1>), [dozu-ui-service/src/app/[locale]/generate/components/GeneratePage.tsx:1](<../../dozu-ui-service/src/app/[locale]/generate/components/GeneratePage.tsx#L1>)

Page interaction sites: `withAuth` at 19

Runtime parity: UNVERIFIED. Complete transitive interactions and source consumers are in the matching JSON page row.

### UI-042 `/[locale]/home`

Guest preview or account library; packages/tree/topics CRUD, current learning, generate actions, learning-mode/admin redirects.

[dozu-ui-service/src/app/[locale]/home/page.tsx:1](<../../dozu-ui-service/src/app/[locale]/home/page.tsx#L1>)

Inherited layouts: [dozu-ui-service/src/app/[locale]/home/layout.tsx:1](<../../dozu-ui-service/src/app/[locale]/home/layout.tsx#L1>), [dozu-ui-service/src/app/[locale]/layout.tsx:1](<../../dozu-ui-service/src/app/[locale]/layout.tsx#L1>), [dozu-ui-service/src/app/layout.tsx:1](<../../dozu-ui-service/src/app/layout.tsx#L1>)

Direct local imports: [dozu-ui-service/src/stores/features/class-based-learning/learningModeSlice.ts:1](<../../dozu-ui-service/src/stores/features/class-based-learning/learningModeSlice.ts#L1>), [dozu-ui-service/src/utils/constants/routes.ts:1](<../../dozu-ui-service/src/utils/constants/routes.ts#L1>), [dozu-ui-service/src/app/[locale]/auth/hooks/useAuthStorage.ts:1](<../../dozu-ui-service/src/app/[locale]/auth/hooks/useAuthStorage.ts#L1>), [dozu-ui-service/src/utils/constants/common.constant.ts:1](<../../dozu-ui-service/src/utils/constants/common.constant.ts#L1>), [dozu-ui-service/src/app/[locale]/topics/components/ui/PersonalTopicLibrary.tsx:1](<../../dozu-ui-service/src/app/[locale]/topics/components/ui/PersonalTopicLibrary.tsx#L1>), [dozu-ui-service/src/app/[locale]/home/components/CurrentProcessLearning.tsx:1](<../../dozu-ui-service/src/app/[locale]/home/components/CurrentProcessLearning.tsx#L1>), [dozu-ui-service/src/app/[locale]/home/components/HeroSection.tsx:1](<../../dozu-ui-service/src/app/[locale]/home/components/HeroSection.tsx#L1>), [dozu-ui-service/src/app/[locale]/home/components/actions/Actions.tsx:1](<../../dozu-ui-service/src/app/[locale]/home/components/actions/Actions.tsx#L1>), [dozu-ui-service/src/app/loading.tsx:1](<../../dozu-ui-service/src/app/loading.tsx#L1>), [dozu-ui-service/src/hooks/useLocalStorage.ts:1](<../../dozu-ui-service/src/hooks/useLocalStorage.ts#L1>), [dozu-ui-service/src/hooks/useRoleChecker.ts:1](<../../dozu-ui-service/src/hooks/useRoleChecker.ts#L1>), [dozu-ui-service/src/components/common/BackgroundGradient.tsx:1](<../../dozu-ui-service/src/components/common/BackgroundGradient.tsx#L1>), [dozu-ui-service/src/app/[locale]/home/components/GuestLibraryPlaceholder.tsx:1](<../../dozu-ui-service/src/app/[locale]/home/components/GuestLibraryPlaceholder.tsx#L1>), [dozu-ui-service/src/app/[locale]/home/components/Title.tsx:1](<../../dozu-ui-service/src/app/[locale]/home/components/Title.tsx#L1>)

Page interaction sites: `useLocalStorage` at 39; `useRouter` at 40; `useAuthStorage` at 41; `useRoleChecker` at 42; `useEffect` at 45; `router.replace` at 47; `useEffect` at 52; `router.push` at 54

Runtime parity: UNVERIFIED. Complete transitive interactions and source consumers are in the matching JSON page row.

### UI-043 `/[locale]/mindmap/[topicId]`

Edit ReactFlow nodes/edges, flashcards/source sheet, generation, roadmap and export/import/save actions.

[dozu-ui-service/src/app/[locale]/mindmap/[topicId]/page.tsx:1](<../../dozu-ui-service/src/app/[locale]/mindmap/[topicId]/page.tsx#L1>)

Inherited layouts: [dozu-ui-service/src/app/[locale]/layout.tsx:1](<../../dozu-ui-service/src/app/[locale]/layout.tsx#L1>), [dozu-ui-service/src/app/[locale]/mindmap/[topicId]/layout.tsx:1](<../../dozu-ui-service/src/app/[locale]/mindmap/[topicId]/layout.tsx#L1>), [dozu-ui-service/src/app/layout.tsx:1](<../../dozu-ui-service/src/app/layout.tsx#L1>)

Direct local imports: [dozu-ui-service/src/stores/hooks.tsx:1](<../../dozu-ui-service/src/stores/hooks.tsx#L1>), [dozu-ui-service/src/hooks/use-toast.ts:1](<../../dozu-ui-service/src/hooks/use-toast.ts#L1>), [dozu-ui-service/src/utils/routerService.ts:1](<../../dozu-ui-service/src/utils/routerService.ts#L1>), [dozu-ui-service/src/components/ui/button.tsx:1](<../../dozu-ui-service/src/components/ui/button.tsx#L1>), [dozu-ui-service/src/components/mindmap/button/ViewFileButton.tsx:1](<../../dozu-ui-service/src/components/mindmap/button/ViewFileButton.tsx#L1>), [dozu-ui-service/src/app/[locale]/mindmap/components/CustomReactFlowNode.tsx:1](<../../dozu-ui-service/src/app/[locale]/mindmap/components/CustomReactFlowNode.tsx#L1>), [dozu-ui-service/src/app/[locale]/mindmap/components/FileSheet.tsx:1](<../../dozu-ui-service/src/app/[locale]/mindmap/components/FileSheet.tsx#L1>), [dozu-ui-service/src/app/[locale]/mindmap/components/FloatingEdge.tsx:1](<../../dozu-ui-service/src/app/[locale]/mindmap/components/FloatingEdge.tsx#L1>), [dozu-ui-service/src/app/[locale]/mindmap/context/MindMapContext.tsx:1](<../../dozu-ui-service/src/app/[locale]/mindmap/context/MindMapContext.tsx#L1>), [dozu-ui-service/src/app/loading.tsx:1](<../../dozu-ui-service/src/app/loading.tsx#L1>), [dozu-ui-service/src/services/flashcard/flashcard.service.ts:1](<../../dozu-ui-service/src/services/flashcard/flashcard.service.ts#L1>), [dozu-ui-service/src/app/[locale]/generate/components/ContentGenerationPreview.tsx:1](<../../dozu-ui-service/src/app/[locale]/generate/components/ContentGenerationPreview.tsx#L1>), [dozu-ui-service/src/components/generative/GeneratingSkeleton.tsx:1](<../../dozu-ui-service/src/components/generative/GeneratingSkeleton.tsx#L1>), [dozu-ui-service/src/app/[locale]/generate/hooks/useContentGeneration.ts:1](<../../dozu-ui-service/src/app/[locale]/generate/hooks/useContentGeneration.ts#L1>), [dozu-ui-service/src/app/[locale]/flashcards/components/FlashcardEditor.tsx:1](<../../dozu-ui-service/src/app/[locale]/flashcards/components/FlashcardEditor.tsx#L1>), [dozu-ui-service/src/app/[locale]/flashcards/types/flashcard.type.ts:1](<../../dozu-ui-service/src/app/[locale]/flashcards/types/flashcard.type.ts#L1>), [dozu-ui-service/src/app/[locale]/mindmap/hooks/useSetCenterOnRoot.ts:1](<../../dozu-ui-service/src/app/[locale]/mindmap/hooks/useSetCenterOnRoot.ts#L1>), [dozu-ui-service/src/app/[locale]/mindmap/components/MindmapButtonsPanel.tsx:1](<../../dozu-ui-service/src/app/[locale]/mindmap/components/MindmapButtonsPanel.tsx#L1>), [dozu-ui-service/src/app/[locale]/mindmap/components/RoadmapButtonPanel.tsx:1](<../../dozu-ui-service/src/app/[locale]/mindmap/components/RoadmapButtonPanel.tsx#L1>)

Page interaction sites: `useTheme` at 54; `useRouter` at 56; `useMindMapContext` at 71; `useContentGeneration` at 73; `useAppSelector` at 75; `useEffect` at 77; `useSetCenterOnRoot` at 81; `useEffect` at 83; `router.push` at 187; `ContentGenerationPreview.onSave` at 202; `Button.onClick` at 210; `ReactFlow.onNodesChange` at 220; `ReactFlow.onEdgesChange` at 220

Runtime parity: UNVERIFIED. Complete transitive interactions and source consumers are in the matching JSON page row.

### UI-044 `/[locale]/mindmap/add-flashcard`

Select flashcards in table and attach to nodes; verify IDs/save integration.

[dozu-ui-service/src/app/[locale]/mindmap/add-flashcard/page.tsx:1](<../../dozu-ui-service/src/app/[locale]/mindmap/add-flashcard/page.tsx#L1>)

Inherited layouts: [dozu-ui-service/src/app/[locale]/layout.tsx:1](<../../dozu-ui-service/src/app/[locale]/layout.tsx#L1>), [dozu-ui-service/src/app/layout.tsx:1](<../../dozu-ui-service/src/app/layout.tsx#L1>)

Direct local imports: [dozu-ui-service/src/api/axios.ts:1](<../../dozu-ui-service/src/api/axios.ts#L1>), [dozu-ui-service/src/components/ui/button.tsx:1](<../../dozu-ui-service/src/components/ui/button.tsx#L1>), [dozu-ui-service/src/components/ui/checkbox.tsx:1](<../../dozu-ui-service/src/components/ui/checkbox.tsx#L1>), [dozu-ui-service/src/components/ui/table.tsx:1](<../../dozu-ui-service/src/components/ui/table.tsx#L1>), [dozu-ui-service/src/utils/constants/api.routes.ts:1](<../../dozu-ui-service/src/utils/constants/api.routes.ts#L1>)

Page interaction sites: `useState` at 22; `useSearchParams` at 23; `useState` at 24; `useState` at 25; `useState` at 30; `useEffect` at 32; `useRouter` at 71; `router.push` at 74; `Button.onClick` at 85; `Checkbox.onCheckedChange` at 105; `Button.onClick` at 122

Runtime parity: UNVERIFIED. Complete transitive interactions and source consumers are in the matching JSON page row.

### UI-045 `/[locale]/mindmap/nodes/[id]/flashcard`

Temporary node flashcard list fetched through raw Axios; loading/empty/error states.

[dozu-ui-service/src/app/[locale]/mindmap/nodes/[id]/flashcard/page.tsx:1](<../../dozu-ui-service/src/app/[locale]/mindmap/nodes/[id]/flashcard/page.tsx#L1>)

Inherited layouts: [dozu-ui-service/src/app/[locale]/layout.tsx:1](<../../dozu-ui-service/src/app/[locale]/layout.tsx#L1>), [dozu-ui-service/src/app/layout.tsx:1](<../../dozu-ui-service/src/app/layout.tsx#L1>)

Direct local imports: [dozu-ui-service/src/api/axios.ts:1](<../../dozu-ui-service/src/api/axios.ts#L1>)

Page interaction sites: `useState` at 19; `useState` at 20; `useParams` at 22; `useEffect` at 27

Runtime parity: UNVERIFIED. Complete transitive interactions and source consumers are in the matching JSON page row.

### UI-046 `/[locale]/mindmap/nodes/[id]`

Mostly empty node page with parameter check; ReactFlow body commented out.

[dozu-ui-service/src/app/[locale]/mindmap/nodes/[id]/page.tsx:1](<../../dozu-ui-service/src/app/[locale]/mindmap/nodes/[id]/page.tsx#L1>)

Inherited layouts: [dozu-ui-service/src/app/[locale]/layout.tsx:1](<../../dozu-ui-service/src/app/[locale]/layout.tsx#L1>), [dozu-ui-service/src/app/layout.tsx:1](<../../dozu-ui-service/src/app/layout.tsx#L1>)

Direct local imports: [dozu-ui-service/src/api/axios.ts:1](<../../dozu-ui-service/src/api/axios.ts#L1>), [dozu-ui-service/src/components/ui/button.tsx:1](<../../dozu-ui-service/src/components/ui/button.tsx#L1>)

Page interaction sites: `useState` at 23; `useParams` at 24

Runtime parity: UNVERIFIED. Complete transitive interactions and source consumers are in the matching JSON page row.

### UI-047 `/[locale]/mindmap/view/[topicId]`

View-only ReactFlow source/node sheets and export/download.

[dozu-ui-service/src/app/[locale]/mindmap/view/[topicId]/page.tsx:1](<../../dozu-ui-service/src/app/[locale]/mindmap/view/[topicId]/page.tsx#L1>)

Inherited layouts: [dozu-ui-service/src/app/[locale]/layout.tsx:1](<../../dozu-ui-service/src/app/[locale]/layout.tsx#L1>), [dozu-ui-service/src/app/[locale]/mindmap/view/[topicId]/layout.tsx:1](<../../dozu-ui-service/src/app/[locale]/mindmap/view/[topicId]/layout.tsx#L1>), [dozu-ui-service/src/app/layout.tsx:1](<../../dozu-ui-service/src/app/layout.tsx#L1>)

Direct local imports: [dozu-ui-service/src/components/ui/button.tsx:1](<../../dozu-ui-service/src/components/ui/button.tsx#L1>), [dozu-ui-service/src/utils/routerService.ts:1](<../../dozu-ui-service/src/utils/routerService.ts#L1>), [dozu-ui-service/src/components/generative/GeneratingSkeleton.tsx:1](<../../dozu-ui-service/src/components/generative/GeneratingSkeleton.tsx#L1>), [dozu-ui-service/src/hooks/use-toast.ts:1](<../../dozu-ui-service/src/hooks/use-toast.ts#L1>), [dozu-ui-service/src/components/mindmap/button/DownloadButton.tsx:1](<../../dozu-ui-service/src/components/mindmap/button/DownloadButton.tsx#L1>), [dozu-ui-service/src/app/[locale]/mindmap/components/FileSheet.tsx:1](<../../dozu-ui-service/src/app/[locale]/mindmap/components/FileSheet.tsx#L1>), [dozu-ui-service/src/app/[locale]/mindmap/components/FloatingEdge.tsx:1](<../../dozu-ui-service/src/app/[locale]/mindmap/components/FloatingEdge.tsx#L1>), [dozu-ui-service/src/app/[locale]/mindmap/context/MindMapContext.tsx:1](<../../dozu-ui-service/src/app/[locale]/mindmap/context/MindMapContext.tsx#L1>), [dozu-ui-service/src/components/mindmap/button/ViewFileButton.tsx:1](<../../dozu-ui-service/src/components/mindmap/button/ViewFileButton.tsx#L1>), [dozu-ui-service/src/app/[locale]/flashcards/types/flashcard.type.ts:1](<../../dozu-ui-service/src/app/[locale]/flashcards/types/flashcard.type.ts#L1>), [dozu-ui-service/src/app/loading.tsx:1](<../../dozu-ui-service/src/app/loading.tsx#L1>), [dozu-ui-service/src/services/flashcard/flashcard.service.ts:1](<../../dozu-ui-service/src/services/flashcard/flashcard.service.ts#L1>), [dozu-ui-service/src/stores/hooks.tsx:1](<../../dozu-ui-service/src/stores/hooks.tsx#L1>), [dozu-ui-service/src/app/[locale]/flashcards/components/FlashcardEditor.tsx:1](<../../dozu-ui-service/src/app/[locale]/flashcards/components/FlashcardEditor.tsx#L1>), [dozu-ui-service/src/app/[locale]/generate/components/ContentGenerationPreview.tsx:1](<../../dozu-ui-service/src/app/[locale]/generate/components/ContentGenerationPreview.tsx#L1>), [dozu-ui-service/src/app/[locale]/generate/hooks/useContentGeneration.ts:1](<../../dozu-ui-service/src/app/[locale]/generate/hooks/useContentGeneration.ts#L1>), [dozu-ui-service/src/app/[locale]/mindmap/components/NodeSheetViewOnly.tsx:1](<../../dozu-ui-service/src/app/[locale]/mindmap/components/NodeSheetViewOnly.tsx#L1>), [dozu-ui-service/src/app/[locale]/mindmap/components/ReactFlowNodeInClass.tsx:1](<../../dozu-ui-service/src/app/[locale]/mindmap/components/ReactFlowNodeInClass.tsx#L1>)

Page interaction sites: `useTheme` at 47; `useRouter` at 49; `useState` at 50; `useMindMapContext` at 64; `useContentGeneration` at 66; `useAppSelector` at 68; `useEffect` at 70; `useEffect` at 74; `router.push` at 182; `ContentGenerationPreview.onSave` at 197; `Button.onClick` at 205; `ReactFlow.onNodesChange` at 215; `ReactFlow.onEdgesChange` at 215

Runtime parity: UNVERIFIED. Complete transitive interactions and source consumers are in the matching JSON page row.

### UI-048 `/[locale]/onboarding`

Step through topic tags, duration and learning-method preferences; persist completion.

[dozu-ui-service/src/app/[locale]/onboarding/page.tsx:1](<../../dozu-ui-service/src/app/[locale]/onboarding/page.tsx#L1>)

Inherited layouts: [dozu-ui-service/src/app/[locale]/layout.tsx:1](<../../dozu-ui-service/src/app/[locale]/layout.tsx#L1>), [dozu-ui-service/src/app/layout.tsx:1](<../../dozu-ui-service/src/app/layout.tsx#L1>)

Direct local imports: [dozu-ui-service/src/app/[locale]/onboarding/components/WelcomeStepCard.tsx:1](<../../dozu-ui-service/src/app/[locale]/onboarding/components/WelcomeStepCard.tsx#L1>), [dozu-ui-service/src/app/[locale]/onboarding/components/TopicTagStepCard.tsx:1](<../../dozu-ui-service/src/app/[locale]/onboarding/components/TopicTagStepCard.tsx#L1>), [dozu-ui-service/src/app/[locale]/onboarding/components/StudyDurationStepCard.tsx:1](<../../dozu-ui-service/src/app/[locale]/onboarding/components/StudyDurationStepCard.tsx#L1>), [dozu-ui-service/src/app/[locale]/onboarding/components/StudyMethodStepCard.tsx:1](<../../dozu-ui-service/src/app/[locale]/onboarding/components/StudyMethodStepCard.tsx#L1>), [dozu-ui-service/src/app/[locale]/onboarding/components/OnboardingCompleteCard.tsx:1](<../../dozu-ui-service/src/app/[locale]/onboarding/components/OnboardingCompleteCard.tsx#L1>), [dozu-ui-service/src/hooks/usePost.ts:1](<../../dozu-ui-service/src/hooks/usePost.ts#L1>), [dozu-ui-service/src/app/loading.tsx:1](<../../dozu-ui-service/src/app/loading.tsx#L1>), [dozu-ui-service/src/components/ui/auth-skeleton.tsx:1](<../../dozu-ui-service/src/components/ui/auth-skeleton.tsx#L1>), [dozu-ui-service/src/hooks/useAuthNavigation.ts:1](<../../dozu-ui-service/src/hooks/useAuthNavigation.ts#L1>)

Page interaction sites: `useAuthNavigation` at 15; `useState` at 17; `useState` at 18; `useState` at 19; `useState` at 20; `usePost` at 59

Runtime parity: UNVERIFIED. Complete transitive interactions and source consumers are in the matching JSON page row.

### UI-049 `/[locale]`

Choose redirect by account/onboarding state; show auth loading.

[dozu-ui-service/src/app/[locale]/page.tsx:1](<../../dozu-ui-service/src/app/[locale]/page.tsx#L1>)

Inherited layouts: [dozu-ui-service/src/app/[locale]/layout.tsx:1](<../../dozu-ui-service/src/app/[locale]/layout.tsx#L1>), [dozu-ui-service/src/app/layout.tsx:1](<../../dozu-ui-service/src/app/layout.tsx#L1>)

Direct local imports: [dozu-ui-service/src/components/ui/auth-skeleton.tsx:1](<../../dozu-ui-service/src/components/ui/auth-skeleton.tsx#L1>), [dozu-ui-service/src/contexts/auth/AuthContext.tsx:1](<../../dozu-ui-service/src/contexts/auth/AuthContext.tsx#L1>), [dozu-ui-service/src/hooks/useLocalStorage.ts:1](<../../dozu-ui-service/src/hooks/useLocalStorage.ts#L1>), [dozu-ui-service/src/hooks/useRoleChecker.ts:1](<../../dozu-ui-service/src/hooks/useRoleChecker.ts#L1>), [dozu-ui-service/src/stores/features/class-based-learning/learningModeSlice.ts:1](<../../dozu-ui-service/src/stores/features/class-based-learning/learningModeSlice.ts#L1>), [dozu-ui-service/src/utils/constants/common.constant.ts:1](<../../dozu-ui-service/src/utils/constants/common.constant.ts#L1>), [dozu-ui-service/src/utils/constants/routes.ts:1](<../../dozu-ui-service/src/utils/constants/routes.ts#L1>)

Page interaction sites: `useAuth` at 15; `useRouter` at 16; `useLocalStorage` at 18; `useRoleChecker` at 19; `useDispatch` at 20; `useEffect` at 22; `router.push` at 24; `router.push` at 29; `router.push` at 35; `router.push` at 41

Runtime parity: UNVERIFIED. Complete transitive interactions and source consumers are in the matching JSON page row.

### UI-050 `/[locale]/payment`

Select plan/payment method, genuine checkout/QR, cancel/return, realtime result and transaction status/history.

[dozu-ui-service/src/app/[locale]/payment/page.tsx:1](<../../dozu-ui-service/src/app/[locale]/payment/page.tsx#L1>)

Inherited layouts: [dozu-ui-service/src/app/[locale]/layout.tsx:1](<../../dozu-ui-service/src/app/[locale]/layout.tsx#L1>), [dozu-ui-service/src/app/layout.tsx:1](<../../dozu-ui-service/src/app/layout.tsx#L1>)

Direct local imports: [dozu-ui-service/src/app/[locale]/payment/hooks/usePayment.ts:1](<../../dozu-ui-service/src/app/[locale]/payment/hooks/usePayment.ts#L1>), [dozu-ui-service/src/hoc/withAuth.tsx:1](<../../dozu-ui-service/src/hoc/withAuth.tsx#L1>), [dozu-ui-service/src/components/ui/badge.tsx:1](<../../dozu-ui-service/src/components/ui/badge.tsx#L1>), [dozu-ui-service/src/components/ui/button.tsx:1](<../../dozu-ui-service/src/components/ui/button.tsx#L1>), [dozu-ui-service/src/components/ui/card.tsx:1](<../../dozu-ui-service/src/components/ui/card.tsx#L1>), [dozu-ui-service/src/components/ui/skeleton.tsx:1](<../../dozu-ui-service/src/components/ui/skeleton.tsx#L1>), [dozu-ui-service/src/components/ui/separator.tsx:1](<../../dozu-ui-service/src/components/ui/separator.tsx#L1>), [dozu-ui-service/src/components/ui/tabs.tsx:1](<../../dozu-ui-service/src/components/ui/tabs.tsx#L1>), [dozu-ui-service/src/components/ui/qr-code.tsx:1](<../../dozu-ui-service/src/components/ui/qr-code.tsx#L1>), [dozu-ui-service/src/hooks/use-toast.ts:1](<../../dozu-ui-service/src/hooks/use-toast.ts#L1>), [dozu-ui-service/src/utils/constants/routes.ts:1](<../../dozu-ui-service/src/utils/constants/routes.ts#L1>), [dozu-ui-service/src/services/payment/index.ts:1](<../../dozu-ui-service/src/services/payment/index.ts#L1>), [dozu-ui-service/src/app/[locale]/payment/utils/constants.ts:1](<../../dozu-ui-service/src/app/[locale]/payment/utils/constants.ts#L1>), [dozu-ui-service/src/app/loading.tsx:1](<../../dozu-ui-service/src/app/loading.tsx#L1>), [dozu-ui-service/src/utils/constants/roles.ts:1](<../../dozu-ui-service/src/utils/constants/roles.ts#L1>), [dozu-ui-service/src/utils/index.ts:1](<../../dozu-ui-service/src/utils/index.ts#L1>)

Page interaction sites: `useRouter` at 31; `useSearchParams` at 32; `useTranslations` at 33; `useState` at 35; `usePayment` at 45; `useEffect` at 67; `router.push` at 86; `Button.onClick` at 117; `Button.onClick` at 138; `Button.onClick` at 184; `router.push` at 184; `Button.onClick` at 230; `Button.onClick` at 252; `Button.onClick` at 353; `withAuth` at 406

Runtime parity: UNVERIFIED. Complete transitive interactions and source consumers are in the matching JSON page row.

### UI-051 `/[locale]/profile`

Load/update personal information, avatar and notification/settings tabs.

[dozu-ui-service/src/app/[locale]/profile/page.tsx:1](<../../dozu-ui-service/src/app/[locale]/profile/page.tsx#L1>)

Inherited layouts: [dozu-ui-service/src/app/[locale]/layout.tsx:1](<../../dozu-ui-service/src/app/[locale]/layout.tsx#L1>), [dozu-ui-service/src/app/layout.tsx:1](<../../dozu-ui-service/src/app/layout.tsx#L1>)

Direct local imports: [dozu-ui-service/src/hoc/withAuth.tsx:1](<../../dozu-ui-service/src/hoc/withAuth.tsx#L1>), [dozu-ui-service/src/app/[locale]/profile/components/index.ts:1](<../../dozu-ui-service/src/app/[locale]/profile/components/index.ts#L1>), [dozu-ui-service/src/types/profile.ts:1](<../../dozu-ui-service/src/types/profile.ts#L1>), [dozu-ui-service/src/services/profile/profileService.ts:1](<../../dozu-ui-service/src/services/profile/profileService.ts#L1>), [dozu-ui-service/src/hooks/useProfile.ts:1](<../../dozu-ui-service/src/hooks/useProfile.ts#L1>), [dozu-ui-service/src/hooks/use-toast.ts:1](<../../dozu-ui-service/src/hooks/use-toast.ts#L1>), [dozu-ui-service/src/utils/index.ts:1](<../../dozu-ui-service/src/utils/index.ts#L1>), [dozu-ui-service/src/components/errors/DataStatus.tsx:1](<../../dozu-ui-service/src/components/errors/DataStatus.tsx#L1>)

Page interaction sites: `useProfile` at 14; `ProfileHeader.onProfileUpdate` at 82; `ProfileHeader.onAvatarUpdate` at 82; `ProfileHeader.onAvatarRemove` at 82; `SettingsTab.onPasswordChange` at 90; `SettingsTab.onSettingsChange` at 90; `SettingsTab.onDeleteAccount` at 90; `withAuth` at 102

Runtime parity: UNVERIFIED. Complete transitive interactions and source consumers are in the matching JSON page row.

### UI-052 `/[locale]/progress`

Progress dashboard with study totals and topic/method progress.

[dozu-ui-service/src/app/[locale]/progress/page.tsx:1](<../../dozu-ui-service/src/app/[locale]/progress/page.tsx#L1>)

Inherited layouts: [dozu-ui-service/src/app/[locale]/layout.tsx:1](<../../dozu-ui-service/src/app/[locale]/layout.tsx#L1>), [dozu-ui-service/src/app/[locale]/progress/layout.tsx:1](<../../dozu-ui-service/src/app/[locale]/progress/layout.tsx#L1>), [dozu-ui-service/src/app/layout.tsx:1](<../../dozu-ui-service/src/app/layout.tsx#L1>)

Direct local imports: [dozu-ui-service/src/components/ui/tabs.tsx:1](<../../dozu-ui-service/src/components/ui/tabs.tsx#L1>), [dozu-ui-service/src/app/[locale]/progress/components/index.ts:1](<../../dozu-ui-service/src/app/[locale]/progress/components/index.ts#L1>), [dozu-ui-service/src/hoc/withAuth.tsx:1](<../../dozu-ui-service/src/hoc/withAuth.tsx#L1>)

Page interaction sites: `useState` at 10; `useTranslations` at 11; `withAuth` at 28

Runtime parity: UNVERIFIED. Complete transitive interactions and source consumers are in the matching JSON page row.

### UI-053 `/[locale]/question/edit/[topicId]`

Question editor: change questions/answers/options and persist topic quiz bank.

[dozu-ui-service/src/app/[locale]/question/edit/[topicId]/page.tsx:1](<../../dozu-ui-service/src/app/[locale]/question/edit/[topicId]/page.tsx#L1>)

Inherited layouts: [dozu-ui-service/src/app/[locale]/layout.tsx:1](<../../dozu-ui-service/src/app/[locale]/layout.tsx#L1>), [dozu-ui-service/src/app/layout.tsx:1](<../../dozu-ui-service/src/app/layout.tsx#L1>)

Direct local imports: [dozu-ui-service/src/hooks/useFetch.ts:1](<../../dozu-ui-service/src/hooks/useFetch.ts#L1>), [dozu-ui-service/src/app/[locale]/question/components/QuestionEditor.tsx:1](<../../dozu-ui-service/src/app/[locale]/question/components/QuestionEditor.tsx#L1>), [dozu-ui-service/src/app/[locale]/question/types/question.type.ts:1](<../../dozu-ui-service/src/app/[locale]/question/types/question.type.ts#L1>), [dozu-ui-service/src/app/loading.tsx:1](<../../dozu-ui-service/src/app/loading.tsx#L1>), [dozu-ui-service/src/app/[locale]/question/utils/handleConvertToQuestionsEdited.ts:1](<../../dozu-ui-service/src/app/[locale]/question/utils/handleConvertToQuestionsEdited.ts#L1>)

Page interaction sites: `useParams` at 29; `useFetch` at 38; `useState` at 39; `useEffect` at 42

Runtime parity: UNVERIFIED. Complete transitive interactions and source consumers are in the matching JSON page row.

### UI-054 `/[locale]/quiz/[topicId]/doing`

Answer quiz, navigate questions, confirm submission and persist results.

[dozu-ui-service/src/app/[locale]/quiz/[topicId]/doing/page.tsx:1](<../../dozu-ui-service/src/app/[locale]/quiz/[topicId]/doing/page.tsx#L1>)

Inherited layouts: [dozu-ui-service/src/app/[locale]/layout.tsx:1](<../../dozu-ui-service/src/app/[locale]/layout.tsx#L1>), [dozu-ui-service/src/app/[locale]/quiz/layout.tsx:1](<../../dozu-ui-service/src/app/[locale]/quiz/layout.tsx#L1>), [dozu-ui-service/src/app/layout.tsx:1](<../../dozu-ui-service/src/app/layout.tsx#L1>)

Direct local imports: [dozu-ui-service/src/app/[locale]/quiz/services/quiz.service.ts:1](<../../dozu-ui-service/src/app/[locale]/quiz/services/quiz.service.ts#L1>), [dozu-ui-service/src/components/ui/button.tsx:1](<../../dozu-ui-service/src/components/ui/button.tsx#L1>), [dozu-ui-service/src/app/[locale]/quiz/components/ConfirmSubmitDialog.tsx:1](<../../dozu-ui-service/src/app/[locale]/quiz/components/ConfirmSubmitDialog.tsx#L1>), [dozu-ui-service/src/app/[locale]/quiz/components/QuizQuestion.tsx:1](<../../dozu-ui-service/src/app/[locale]/quiz/components/QuizQuestion.tsx#L1>), [dozu-ui-service/src/hooks/useStreakProgress.ts:1](<../../dozu-ui-service/src/hooks/useStreakProgress.ts#L1>), [dozu-ui-service/src/hooks/use-toast.ts:1](<../../dozu-ui-service/src/hooks/use-toast.ts#L1>), [dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/hooks/useQuizWorkspace.tsx:1](<../../dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/hooks/useQuizWorkspace.tsx#L1>)

Page interaction sites: `useState` at 38; `useState` at 39; `useState` at 40; `useState` at 41; `useRouter` at 42; `useSearchParams` at 43; `useQuizStreakTracking` at 44; `useState` at 45; `useState` at 46; `useEffect` at 63; `localStorage.getItem` at 146; `router.push` at 173; `QuizQuestion.onAnswerSelect` at 220; `Button.onClick` at 234; `ConfirmSubmitDialog.onCancel` at 238; `ConfirmSubmitDialog.onConfirm` at 238

Runtime parity: UNVERIFIED. Complete transitive interactions and source consumers are in the matching JSON page row.

### UI-055 `/[locale]/quiz/[topicId]/history/[quizResultId]`

Read historical attempt questions/answers and scoring details.

[dozu-ui-service/src/app/[locale]/quiz/[topicId]/history/[quizResultId]/page.tsx:1](<../../dozu-ui-service/src/app/[locale]/quiz/[topicId]/history/[quizResultId]/page.tsx#L1>)

Inherited layouts: [dozu-ui-service/src/app/[locale]/layout.tsx:1](<../../dozu-ui-service/src/app/[locale]/layout.tsx#L1>), [dozu-ui-service/src/app/[locale]/quiz/layout.tsx:1](<../../dozu-ui-service/src/app/[locale]/quiz/layout.tsx#L1>), [dozu-ui-service/src/app/layout.tsx:1](<../../dozu-ui-service/src/app/layout.tsx#L1>)

Direct local imports: [dozu-ui-service/src/app/[locale]/quiz/services/quiz.service.ts:1](<../../dozu-ui-service/src/app/[locale]/quiz/services/quiz.service.ts#L1>), [dozu-ui-service/src/app/[locale]/quiz/components/QuizResultDetail.tsx:1](<../../dozu-ui-service/src/app/[locale]/quiz/components/QuizResultDetail.tsx#L1>)

Page interaction sites: `useState` at 8; `useEffect` at 10

Runtime parity: UNVERIFIED. Complete transitive interactions and source consumers are in the matching JSON page row.

### UI-056 `/[locale]/quiz/[topicId]/history`

List attempts and open result/history details.

[dozu-ui-service/src/app/[locale]/quiz/[topicId]/history/page.tsx:1](<../../dozu-ui-service/src/app/[locale]/quiz/[topicId]/history/page.tsx#L1>)

Inherited layouts: [dozu-ui-service/src/app/[locale]/layout.tsx:1](<../../dozu-ui-service/src/app/[locale]/layout.tsx#L1>), [dozu-ui-service/src/app/[locale]/quiz/layout.tsx:1](<../../dozu-ui-service/src/app/[locale]/quiz/layout.tsx#L1>), [dozu-ui-service/src/app/layout.tsx:1](<../../dozu-ui-service/src/app/layout.tsx#L1>)

Direct local imports: [dozu-ui-service/src/app/[locale]/quiz/services/quiz.service.ts:1](<../../dozu-ui-service/src/app/[locale]/quiz/services/quiz.service.ts#L1>), [dozu-ui-service/src/app/[locale]/quiz/components/QuizCard.tsx:1](<../../dozu-ui-service/src/app/[locale]/quiz/components/QuizCard.tsx#L1>), [dozu-ui-service/src/components/ui/button.tsx:1](<../../dozu-ui-service/src/components/ui/button.tsx#L1>)

Page interaction sites: `useState` at 19; `useState` at 20; `useState` at 21; `useRouter` at 22; `useCallback` at 24; `useEffect` at 59; `Button.onClick` at 76; `QuizCard.onClick` at 89; `router.push` at 96

Runtime parity: UNVERIFIED. Complete transitive interactions and source consumers are in the matching JSON page row.

### UI-057 `/[locale]/quiz/[topicId]/result/[quizResultId]`

Display saved result and review answers.

[dozu-ui-service/src/app/[locale]/quiz/[topicId]/result/[quizResultId]/page.tsx:1](<../../dozu-ui-service/src/app/[locale]/quiz/[topicId]/result/[quizResultId]/page.tsx#L1>)

Inherited layouts: [dozu-ui-service/src/app/[locale]/layout.tsx:1](<../../dozu-ui-service/src/app/[locale]/layout.tsx#L1>), [dozu-ui-service/src/app/[locale]/quiz/layout.tsx:1](<../../dozu-ui-service/src/app/[locale]/quiz/layout.tsx#L1>), [dozu-ui-service/src/app/layout.tsx:1](<../../dozu-ui-service/src/app/layout.tsx#L1>)

Direct local imports: [dozu-ui-service/src/app/[locale]/quiz/services/quiz.service.ts:1](<../../dozu-ui-service/src/app/[locale]/quiz/services/quiz.service.ts#L1>), [dozu-ui-service/src/app/[locale]/quiz/components/QuizResult.tsx:1](<../../dozu-ui-service/src/app/[locale]/quiz/components/QuizResult.tsx#L1>)

Page interaction sites: `useState` at 8; `useEffect` at 10

Runtime parity: UNVERIFIED. Complete transitive interactions and source consumers are in the matching JSON page row.

### UI-058 `/[locale]/quiz/local`

Browser-storage quiz draft/answers plus streak update; shared DB authority requires explicit transfer contract.

[dozu-ui-service/src/app/[locale]/quiz/local/page.tsx:1](<../../dozu-ui-service/src/app/[locale]/quiz/local/page.tsx#L1>)

Inherited layouts: [dozu-ui-service/src/app/[locale]/layout.tsx:1](<../../dozu-ui-service/src/app/[locale]/layout.tsx#L1>), [dozu-ui-service/src/app/[locale]/quiz/layout.tsx:1](<../../dozu-ui-service/src/app/[locale]/quiz/layout.tsx#L1>), [dozu-ui-service/src/app/layout.tsx:1](<../../dozu-ui-service/src/app/layout.tsx#L1>)

Direct local imports: [dozu-ui-service/src/app/[locale]/quiz/utils/localQuiz.storage.ts:1](<../../dozu-ui-service/src/app/[locale]/quiz/utils/localQuiz.storage.ts#L1>), [dozu-ui-service/src/app/[locale]/quiz/components/QuizQuestion.tsx:1](<../../dozu-ui-service/src/app/[locale]/quiz/components/QuizQuestion.tsx#L1>), [dozu-ui-service/src/components/ui/button.tsx:1](<../../dozu-ui-service/src/components/ui/button.tsx#L1>), [dozu-ui-service/src/hooks/useStreakProgress.ts:1](<../../dozu-ui-service/src/hooks/useStreakProgress.ts#L1>)

Page interaction sites: `useRouter` at 13; `useSearchParams` at 14; `useQuizStreakTracking` at 17; `useState` at 19; `useState` at 20; `useState` at 21; `useState` at 22; `useEffect` at 24; `router.replace` at 29; `useMemo` at 37; `localStorage.getItem` at 50; `router.replace` at 88; `QuizQuestion.onAnswerSelect` at 104; `Button.onClick` at 117; `Button.onClick` at 157

Runtime parity: UNVERIFIED. Complete transitive interactions and source consumers are in the matching JSON page row.

### UI-059 `/[locale]/request-teacher`

Read request status or submit teacher application.

[dozu-ui-service/src/app/[locale]/request-teacher/page.tsx:1](<../../dozu-ui-service/src/app/[locale]/request-teacher/page.tsx#L1>)

Inherited layouts: [dozu-ui-service/src/app/[locale]/layout.tsx:1](<../../dozu-ui-service/src/app/[locale]/layout.tsx#L1>), [dozu-ui-service/src/app/layout.tsx:1](<../../dozu-ui-service/src/app/layout.tsx#L1>)

Direct local imports: [dozu-ui-service/src/hooks/use-toast.ts:1](<../../dozu-ui-service/src/hooks/use-toast.ts#L1>), [dozu-ui-service/src/services/teacher-request/teacherRequest.service.ts:1](<../../dozu-ui-service/src/services/teacher-request/teacherRequest.service.ts#L1>), [dozu-ui-service/src/app/[locale]/admin/teacher-requests/types/teacherRequest.type.ts:1](<../../dozu-ui-service/src/app/[locale]/admin/teacher-requests/types/teacherRequest.type.ts#L1>), [dozu-ui-service/src/hooks/useFetch.ts:1](<../../dozu-ui-service/src/hooks/useFetch.ts#L1>), [dozu-ui-service/src/app/loading.tsx:1](<../../dozu-ui-service/src/app/loading.tsx#L1>), [dozu-ui-service/src/app/[locale]/request-teacher/components/RequestStatus.tsx:1](<../../dozu-ui-service/src/app/[locale]/request-teacher/components/RequestStatus.tsx#L1>), [dozu-ui-service/src/app/[locale]/request-teacher/components/RequestForm.tsx:1](<../../dozu-ui-service/src/app/[locale]/request-teacher/components/RequestForm.tsx#L1>)

Page interaction sites: `useState` at 13; `useFetch` at 19; `teacherRequestService.sendRequest` at 31; `setMyRequest` at 35

Runtime parity: UNVERIFIED. Complete transitive interactions and source consumers are in the matching JSON page row.

### UI-060 `/[locale]/request-teacher/reapply`

Edit/resubmit teacher application after rejection.

[dozu-ui-service/src/app/[locale]/request-teacher/reapply/page.tsx:1](<../../dozu-ui-service/src/app/[locale]/request-teacher/reapply/page.tsx#L1>)

Inherited layouts: [dozu-ui-service/src/app/[locale]/layout.tsx:1](<../../dozu-ui-service/src/app/[locale]/layout.tsx#L1>), [dozu-ui-service/src/app/layout.tsx:1](<../../dozu-ui-service/src/app/layout.tsx#L1>)

Direct local imports: [dozu-ui-service/src/hooks/use-toast.ts:1](<../../dozu-ui-service/src/hooks/use-toast.ts#L1>), [dozu-ui-service/src/services/teacher-request/teacherRequest.service.ts:1](<../../dozu-ui-service/src/services/teacher-request/teacherRequest.service.ts#L1>), [dozu-ui-service/src/app/[locale]/admin/teacher-requests/types/teacherRequest.type.ts:1](<../../dozu-ui-service/src/app/[locale]/admin/teacher-requests/types/teacherRequest.type.ts#L1>), [dozu-ui-service/src/hooks/useFetch.ts:1](<../../dozu-ui-service/src/hooks/useFetch.ts#L1>), [dozu-ui-service/src/app/loading.tsx:1](<../../dozu-ui-service/src/app/loading.tsx#L1>), [dozu-ui-service/src/app/[locale]/request-teacher/components/RequestStatus.tsx:1](<../../dozu-ui-service/src/app/[locale]/request-teacher/components/RequestStatus.tsx#L1>), [dozu-ui-service/src/app/[locale]/request-teacher/components/RequestForm.tsx:1](<../../dozu-ui-service/src/app/[locale]/request-teacher/components/RequestForm.tsx#L1>)

Page interaction sites: `useRouter` at 14; `useState` at 15; `teacherRequestService.sendRequest` at 27; `router.push` at 31

Runtime parity: UNVERIFIED. Complete transitive interactions and source consumers are in the matching JSON page row.

### UI-061 `/[locale]/schedule`

Calendar/list views, recommended slots and learning progress interactions.

[dozu-ui-service/src/app/[locale]/schedule/page.tsx:1](<../../dozu-ui-service/src/app/[locale]/schedule/page.tsx#L1>)

Inherited layouts: [dozu-ui-service/src/app/[locale]/layout.tsx:1](<../../dozu-ui-service/src/app/[locale]/layout.tsx#L1>), [dozu-ui-service/src/app/layout.tsx:1](<../../dozu-ui-service/src/app/layout.tsx#L1>)

Direct local imports: [dozu-ui-service/src/components/ui/full-calendar.tsx:1](<../../dozu-ui-service/src/components/ui/full-calendar.tsx#L1>), [dozu-ui-service/src/hoc/withAuth.tsx:1](<../../dozu-ui-service/src/hoc/withAuth.tsx#L1>), [dozu-ui-service/src/app/[locale]/schedule/components/CalendarView.tsx:1](<../../dozu-ui-service/src/app/[locale]/schedule/components/CalendarView.tsx#L1>)

Page interaction sites: `withAuth` at 15

Runtime parity: UNVERIFIED. Complete transitive interactions and source consumers are in the matching JSON page row.

### UI-062 `/[locale]/setting/profile`

Authenticated wrapper reusing profile page.

[dozu-ui-service/src/app/[locale]/setting/profile/page.tsx:1](<../../dozu-ui-service/src/app/[locale]/setting/profile/page.tsx#L1>)

Inherited layouts: [dozu-ui-service/src/app/[locale]/layout.tsx:1](<../../dozu-ui-service/src/app/[locale]/layout.tsx#L1>), [dozu-ui-service/src/app/[locale]/setting/layout.tsx:1](<../../dozu-ui-service/src/app/[locale]/setting/layout.tsx#L1>), [dozu-ui-service/src/app/layout.tsx:1](<../../dozu-ui-service/src/app/layout.tsx#L1>)

Direct local imports: [dozu-ui-service/src/hoc/withAuth.tsx:1](<../../dozu-ui-service/src/hoc/withAuth.tsx#L1>), [dozu-ui-service/src/app/[locale]/profile/page.tsx:1](<../../dozu-ui-service/src/app/[locale]/profile/page.tsx#L1>), [dozu-ui-service/src/components/ui/button.tsx:1](<../../dozu-ui-service/src/components/ui/button.tsx#L1>)

Page interaction sites: `useRouter` at 11; `router.push` at 14; `withAuth` at 30

Runtime parity: UNVERIFIED. Complete transitive interactions and source consumers are in the matching JSON page row.

### UI-063 `/[locale]/setting/schedule-setup`

Configure study availability, frequency, methods and schedule preferences.

[dozu-ui-service/src/app/[locale]/setting/schedule-setup/page.tsx:1](<../../dozu-ui-service/src/app/[locale]/setting/schedule-setup/page.tsx#L1>)

Inherited layouts: [dozu-ui-service/src/app/[locale]/layout.tsx:1](<../../dozu-ui-service/src/app/[locale]/layout.tsx#L1>), [dozu-ui-service/src/app/[locale]/setting/layout.tsx:1](<../../dozu-ui-service/src/app/[locale]/setting/layout.tsx#L1>), [dozu-ui-service/src/app/layout.tsx:1](<../../dozu-ui-service/src/app/layout.tsx#L1>)

Direct local imports: [dozu-ui-service/src/app/[locale]/setting/schedule-setup/components/SetupForm.tsx:1](<../../dozu-ui-service/src/app/[locale]/setting/schedule-setup/components/SetupForm.tsx#L1>)

Page interaction sites: `useRouter` at 8; `useTranslations` at 9; `SetupForm.onComplete` at 20

Runtime parity: UNVERIFIED. Complete transitive interactions and source consumers are in the matching JSON page row.

### UI-064 `/[locale]/stats`

LearningProgress component; verify supplied data and API use before claiming analytics.

[dozu-ui-service/src/app/[locale]/stats/page.tsx:1](<../../dozu-ui-service/src/app/[locale]/stats/page.tsx#L1>)

Inherited layouts: [dozu-ui-service/src/app/[locale]/layout.tsx:1](<../../dozu-ui-service/src/app/[locale]/layout.tsx#L1>), [dozu-ui-service/src/app/layout.tsx:1](<../../dozu-ui-service/src/app/layout.tsx#L1>)

Direct local imports: [dozu-ui-service/src/app/[locale]/stats/components/LearningProgress.tsx:1](<../../dozu-ui-service/src/app/[locale]/stats/components/LearningProgress.tsx#L1>)

Page interaction sites: `useState` at 10

Runtime parity: UNVERIFIED. Complete transitive interactions and source consumers are in the matching JSON page row.

### UI-065 `/[locale]/teacher/class-based/[id]/activities/[activityId]`

Teacher live quiz monitoring tabs, participation/answer events, refresh and XLSX results export.

[dozu-ui-service/src/app/[locale]/teacher/class-based/[id]/activities/[activityId]/page.tsx:1](<../../dozu-ui-service/src/app/[locale]/teacher/class-based/[id]/activities/[activityId]/page.tsx#L1>)

Inherited layouts: [dozu-ui-service/src/app/[locale]/layout.tsx:1](<../../dozu-ui-service/src/app/[locale]/layout.tsx#L1>), [dozu-ui-service/src/app/layout.tsx:1](<../../dozu-ui-service/src/app/layout.tsx#L1>)

Direct local imports: [dozu-ui-service/src/components/ui/card.tsx:1](<../../dozu-ui-service/src/components/ui/card.tsx#L1>), [dozu-ui-service/src/components/ui/button.tsx:1](<../../dozu-ui-service/src/components/ui/button.tsx#L1>), [dozu-ui-service/src/components/ui/badge.tsx:1](<../../dozu-ui-service/src/components/ui/badge.tsx#L1>), [dozu-ui-service/src/components/ui/progress.tsx:1](<../../dozu-ui-service/src/components/ui/progress.tsx#L1>), [dozu-ui-service/src/components/ui/tabs.tsx:1](<../../dozu-ui-service/src/components/ui/tabs.tsx#L1>), [dozu-ui-service/src/hooks/use-toast.ts:1](<../../dozu-ui-service/src/hooks/use-toast.ts#L1>), [dozu-ui-service/src/types/activity.ts:1](<../../dozu-ui-service/src/types/activity.ts#L1>), [dozu-ui-service/src/app/[locale]/activities/utils/excelGenerator.ts:1](<../../dozu-ui-service/src/app/[locale]/activities/utils/excelGenerator.ts#L1>), [dozu-ui-service/src/services/activity/activity.service.ts:1](<../../dozu-ui-service/src/services/activity/activity.service.ts#L1>), [dozu-ui-service/src/services/class-based-learning/quizClass.service.ts:1](<../../dozu-ui-service/src/services/class-based-learning/quizClass.service.ts#L1>), [dozu-ui-service/src/app/[locale]/activities/utils/dataAdapter.ts:1](<../../dozu-ui-service/src/app/[locale]/activities/utils/dataAdapter.ts#L1>), [dozu-ui-service/src/app/[locale]/activities/components/ActivitySummaryTab.tsx:1](<../../dozu-ui-service/src/app/[locale]/activities/components/ActivitySummaryTab.tsx#L1>), [dozu-ui-service/src/app/[locale]/activities/components/StudentSummaryTab.tsx:1](<../../dozu-ui-service/src/app/[locale]/activities/components/StudentSummaryTab.tsx#L1>), [dozu-ui-service/src/app/[locale]/activities/components/TermProgressTab.tsx:1](<../../dozu-ui-service/src/app/[locale]/activities/components/TermProgressTab.tsx#L1>), [dozu-ui-service/src/app/[locale]/activities/components/StudentResultsTab.tsx:1](<../../dozu-ui-service/src/app/[locale]/activities/components/StudentResultsTab.tsx#L1>), [dozu-ui-service/src/hooks/useQuizActivityWebSocket.ts:1](<../../dozu-ui-service/src/hooks/useQuizActivityWebSocket.ts#L1>)

Page interaction sites: `useTranslations` at 31; `useState` at 32; `useState` at 33; `useState` at 34; `useCallback` at 38; `useCallback` at 185; `useCallback` at 209; `useCallback` at 238; `useQuizActivityWebSocket` at 250; `useEffect` at 256; `Button.onClick` at 431; `Button.onClick` at 446

Runtime parity: UNVERIFIED. Complete transitive interactions and source consumers are in the matching JSON page row.

### UI-066 `/[locale]/teacher/class-based/[id]/assignments/[assignmentId]/details`

Read assignment/attachments/comments; teacher reviews/grades submissions and edits/deletes assignment.

[dozu-ui-service/src/app/[locale]/teacher/class-based/[id]/assignments/[assignmentId]/details/page.tsx:1](<../../dozu-ui-service/src/app/[locale]/teacher/class-based/[id]/assignments/[assignmentId]/details/page.tsx#L1>)

Inherited layouts: [dozu-ui-service/src/app/[locale]/layout.tsx:1](<../../dozu-ui-service/src/app/[locale]/layout.tsx#L1>), [dozu-ui-service/src/app/layout.tsx:1](<../../dozu-ui-service/src/app/layout.tsx#L1>)

Direct local imports: [dozu-ui-service/src/app/[locale]/class-based/(classwork)/components/common/details/ContentSection.tsx:1](<../../dozu-ui-service/src/app/[locale]/class-based/(classwork)/components/common/details/ContentSection.tsx#L1>), [dozu-ui-service/src/app/[locale]/class-based/(classwork)/components/common/details/AttachmentsViewSection.tsx:1](<../../dozu-ui-service/src/app/[locale]/class-based/(classwork)/components/common/details/AttachmentsViewSection.tsx#L1>), [dozu-ui-service/src/components/ui/separator.tsx:1](<../../dozu-ui-service/src/components/ui/separator.tsx#L1>), [dozu-ui-service/src/hooks/useFetch.ts:1](<../../dozu-ui-service/src/hooks/useFetch.ts#L1>), [dozu-ui-service/src/app/[locale]/class-based/(assignment)/types/assignment.type.ts:1](<../../dozu-ui-service/src/app/[locale]/class-based/(assignment)/types/assignment.type.ts#L1>), [dozu-ui-service/src/app/[locale]/class-based/(assignment)/service/assignment.service.ts:1](<../../dozu-ui-service/src/app/[locale]/class-based/(assignment)/service/assignment.service.ts#L1>), [dozu-ui-service/src/app/loading.tsx:1](<../../dozu-ui-service/src/app/loading.tsx#L1>), [dozu-ui-service/src/components/ui/dropdown-menu.tsx:1](<../../dozu-ui-service/src/components/ui/dropdown-menu.tsx#L1>), [dozu-ui-service/src/utils/constants/routes.ts:1](<../../dozu-ui-service/src/utils/constants/routes.ts#L1>), [dozu-ui-service/src/hooks/usePost.ts:1](<../../dozu-ui-service/src/hooks/usePost.ts#L1>), [dozu-ui-service/src/utils/toast.helper.ts:1](<../../dozu-ui-service/src/utils/toast.helper.ts#L1>), [dozu-ui-service/src/app/[locale]/class-based/(assignment)/components/DeleteAssignmentModal.tsx:1](<../../dozu-ui-service/src/app/[locale]/class-based/(assignment)/components/DeleteAssignmentModal.tsx#L1>), [dozu-ui-service/src/app/[locale]/class-based/[id]/utils/class.constant.ts:1](<../../dozu-ui-service/src/app/[locale]/class-based/[id]/utils/class.constant.ts#L1>), [dozu-ui-service/src/contexts/auth/AuthContext.tsx:1](<../../dozu-ui-service/src/contexts/auth/AuthContext.tsx#L1>), [dozu-ui-service/src/components/ui/tabs.tsx:1](<../../dozu-ui-service/src/components/ui/tabs.tsx#L1>), [dozu-ui-service/src/app/[locale]/teacher/class-based/[id]/assignments/[assignmentId]/details/components/SubmissionsPage.tsx:1](<../../dozu-ui-service/src/app/[locale]/teacher/class-based/[id]/assignments/[assignmentId]/details/components/SubmissionsPage.tsx#L1>), [dozu-ui-service/src/app/[locale]/teacher/class-based/[id]/assignments/[assignmentId]/details/components/CommentSection.tsx:1](<../../dozu-ui-service/src/app/[locale]/teacher/class-based/[id]/assignments/[assignmentId]/details/components/CommentSection.tsx#L1>), [dozu-ui-service/src/app/[locale]/class-based/(assignment)/types/assignmentSubmission.type.ts:1](<../../dozu-ui-service/src/app/[locale]/class-based/(assignment)/types/assignmentSubmission.type.ts#L1>), [dozu-ui-service/src/app/[locale]/class-based/(assignment)/service/assignmentSubmission.service.ts:1](<../../dozu-ui-service/src/app/[locale]/class-based/(assignment)/service/assignmentSubmission.service.ts#L1>)

Page interaction sites: `useParams` at 80; `useAuth` at 99; `useRouter` at 100; `useTranslations` at 101; `useFetch` at 108; `useFetch` at 118; `usePost` at 123; `useState` at 145; `usePost` at 147; `router.push` at 157; `router.push` at 162; `DropdownMenuItem.onClick` at 218; `DropdownMenuItem.onClick` at 223; `DeleteAssignmentModal.onSubmit` at 237; `SubmissionsPage.onGradeSubmit` at 249

Runtime parity: UNVERIFIED. Complete transitive interactions and source consumers are in the matching JSON page row.

### UI-067 `/[locale]/teacher/class-based/[id]/assignments/[assignmentId]/edit`

Load/edit assignment, topics, rich text, attachments and scheduling.

[dozu-ui-service/src/app/[locale]/teacher/class-based/[id]/assignments/[assignmentId]/edit/page.tsx:1](<../../dozu-ui-service/src/app/[locale]/teacher/class-based/[id]/assignments/[assignmentId]/edit/page.tsx#L1>)

Inherited layouts: [dozu-ui-service/src/app/[locale]/layout.tsx:1](<../../dozu-ui-service/src/app/[locale]/layout.tsx#L1>), [dozu-ui-service/src/app/layout.tsx:1](<../../dozu-ui-service/src/app/layout.tsx#L1>)

Direct local imports: [dozu-ui-service/src/app/[locale]/class-based/(assignment)/components/EditAssignment.tsx:1](<../../dozu-ui-service/src/app/[locale]/class-based/(assignment)/components/EditAssignment.tsx#L1>), [dozu-ui-service/src/app/[locale]/class-based/(assignment)/service/assignment.service.ts:1](<../../dozu-ui-service/src/app/[locale]/class-based/(assignment)/service/assignment.service.ts#L1>), [dozu-ui-service/src/app/[locale]/class-based/(assignment)/types/assignment.type.ts:1](<../../dozu-ui-service/src/app/[locale]/class-based/(assignment)/types/assignment.type.ts#L1>), [dozu-ui-service/src/app/[locale]/class-based/(classwork)/types/attachment.type.ts:1](<../../dozu-ui-service/src/app/[locale]/class-based/(classwork)/types/attachment.type.ts#L1>), [dozu-ui-service/src/app/[locale]/class-based/[id]/utils/class.constant.ts:1](<../../dozu-ui-service/src/app/[locale]/class-based/[id]/utils/class.constant.ts#L1>), [dozu-ui-service/src/app/[locale]/class-based/types/class.type.ts:1](<../../dozu-ui-service/src/app/[locale]/class-based/types/class.type.ts#L1>), [dozu-ui-service/src/app/[locale]/generate/constants/resource.ts:1](<../../dozu-ui-service/src/app/[locale]/generate/constants/resource.ts#L1>), [dozu-ui-service/src/app/[locale]/topics/hooks/useTopics.tsx:1](<../../dozu-ui-service/src/app/[locale]/topics/hooks/useTopics.tsx#L1>), [dozu-ui-service/src/app/loading.tsx:1](<../../dozu-ui-service/src/app/loading.tsx#L1>), [dozu-ui-service/src/hooks/upload/useUploadAttachmentFiles.tsx:1](<../../dozu-ui-service/src/hooks/upload/useUploadAttachmentFiles.tsx#L1>), [dozu-ui-service/src/hooks/useFetch.ts:1](<../../dozu-ui-service/src/hooks/useFetch.ts#L1>), [dozu-ui-service/src/hooks/usePost.ts:1](<../../dozu-ui-service/src/hooks/usePost.ts#L1>), [dozu-ui-service/src/services/class-based-learning/teacher/teacherClass.service.ts:1](<../../dozu-ui-service/src/services/class-based-learning/teacher/teacherClass.service.ts#L1>), [dozu-ui-service/src/utils/constants/routes.ts:1](<../../dozu-ui-service/src/utils/constants/routes.ts#L1>), [dozu-ui-service/src/utils/toast.helper.ts:1](<../../dozu-ui-service/src/utils/toast.helper.ts#L1>)

Page interaction sites: `useParams` at 26; `useRouter` at 45; `useFetch` at 52; `useTopics` at 55; `useFetch` at 67; `usePost` at 72; `router.push` at 81; `useUploadAttachmentFiles` at 86; `EditAssignment.onSubmit` at 135

Runtime parity: UNVERIFIED. Complete transitive interactions and source consumers are in the matching JSON page row.

### UI-068 `/[locale]/teacher/class-based/[id]/assignments`

Create assignment, choose class/topics, rich text, attachments and scheduling; persist and return to class.

[dozu-ui-service/src/app/[locale]/teacher/class-based/[id]/assignments/page.tsx:1](<../../dozu-ui-service/src/app/[locale]/teacher/class-based/[id]/assignments/page.tsx#L1>)

Inherited layouts: [dozu-ui-service/src/app/[locale]/layout.tsx:1](<../../dozu-ui-service/src/app/[locale]/layout.tsx#L1>), [dozu-ui-service/src/app/layout.tsx:1](<../../dozu-ui-service/src/app/layout.tsx#L1>)

Direct local imports: [dozu-ui-service/src/app/[locale]/class-based/(assignment)/components/CreateAssignment.tsx:1](<../../dozu-ui-service/src/app/[locale]/class-based/(assignment)/components/CreateAssignment.tsx#L1>), [dozu-ui-service/src/app/[locale]/class-based/(assignment)/service/assignment.service.ts:1](<../../dozu-ui-service/src/app/[locale]/class-based/(assignment)/service/assignment.service.ts#L1>), [dozu-ui-service/src/app/[locale]/class-based/(assignment)/types/assignment.type.ts:1](<../../dozu-ui-service/src/app/[locale]/class-based/(assignment)/types/assignment.type.ts#L1>), [dozu-ui-service/src/app/[locale]/class-based/(classwork)/types/attachment.type.ts:1](<../../dozu-ui-service/src/app/[locale]/class-based/(classwork)/types/attachment.type.ts#L1>), [dozu-ui-service/src/app/[locale]/class-based/[id]/utils/class.constant.ts:1](<../../dozu-ui-service/src/app/[locale]/class-based/[id]/utils/class.constant.ts#L1>), [dozu-ui-service/src/app/[locale]/class-based/types/class.type.ts:1](<../../dozu-ui-service/src/app/[locale]/class-based/types/class.type.ts#L1>), [dozu-ui-service/src/app/[locale]/generate/constants/resource.ts:1](<../../dozu-ui-service/src/app/[locale]/generate/constants/resource.ts#L1>), [dozu-ui-service/src/app/[locale]/topics/hooks/useTopics.tsx:1](<../../dozu-ui-service/src/app/[locale]/topics/hooks/useTopics.tsx#L1>), [dozu-ui-service/src/app/loading.tsx:1](<../../dozu-ui-service/src/app/loading.tsx#L1>), [dozu-ui-service/src/hooks/upload/useUploadAttachmentFiles.tsx:1](<../../dozu-ui-service/src/hooks/upload/useUploadAttachmentFiles.tsx#L1>), [dozu-ui-service/src/hooks/useFetch.ts:1](<../../dozu-ui-service/src/hooks/useFetch.ts#L1>), [dozu-ui-service/src/hooks/usePost.ts:1](<../../dozu-ui-service/src/hooks/usePost.ts#L1>), [dozu-ui-service/src/services/class-based-learning/teacher/teacherClass.service.ts:1](<../../dozu-ui-service/src/services/class-based-learning/teacher/teacherClass.service.ts#L1>), [dozu-ui-service/src/utils/constants/routes.ts:1](<../../dozu-ui-service/src/utils/constants/routes.ts#L1>), [dozu-ui-service/src/utils/toast.helper.ts:1](<../../dozu-ui-service/src/utils/toast.helper.ts#L1>)

Page interaction sites: `useParams` at 24; `useRouter` at 36; `useFetch` at 43; `useTopics` at 46; `usePost` at 54; `router.push` at 67; `useUploadAttachmentFiles` at 73; `CreateAssignment.onSubmit` at 110

Runtime parity: UNVERIFIED. Complete transitive interactions and source consumers are in the matching JSON page row.

### UI-069 `/[locale]/teacher/class-based/[id]/class-quiz/[classQuizId]/edit`

Edit quiz draft/questions/settings and publish/schedule/close lifecycle.

[dozu-ui-service/src/app/[locale]/teacher/class-based/[id]/class-quiz/[classQuizId]/edit/page.tsx:1](<../../dozu-ui-service/src/app/[locale]/teacher/class-based/[id]/class-quiz/[classQuizId]/edit/page.tsx#L1>)

Inherited layouts: [dozu-ui-service/src/app/[locale]/layout.tsx:1](<../../dozu-ui-service/src/app/[locale]/layout.tsx#L1>), [dozu-ui-service/src/app/layout.tsx:1](<../../dozu-ui-service/src/app/layout.tsx#L1>)

Direct local imports: [dozu-ui-service/src/app/[locale]/class-based/(class-quiz)/components/ClassQuizDraftEditor.tsx:1](<../../dozu-ui-service/src/app/[locale]/class-based/(class-quiz)/components/ClassQuizDraftEditor.tsx#L1>), [dozu-ui-service/src/app/[locale]/class-based/(class-quiz)/services/classQuizTeacher.service.ts:1](<../../dozu-ui-service/src/app/[locale]/class-based/(class-quiz)/services/classQuizTeacher.service.ts#L1>), [dozu-ui-service/src/app/[locale]/class-based/(class-quiz)/types/classQuiz.type.ts:1](<../../dozu-ui-service/src/app/[locale]/class-based/(class-quiz)/types/classQuiz.type.ts#L1>), [dozu-ui-service/src/hooks/use-toast.ts:1](<../../dozu-ui-service/src/hooks/use-toast.ts#L1>), [dozu-ui-service/src/utils/constants/routes.ts:1](<../../dozu-ui-service/src/utils/constants/routes.ts#L1>)

Page interaction sites: `useParams` at 12; `useRouter` at 13; `useState` at 16; `useState` at 17; `useState` at 18; `useState` at 19; `useState` at 20; `useState` at 21; `useState` at 22; `useEffect` at 25; `router.push` at 68; `ClassQuizDraftEditor.onSaved` at 82; `ClassQuizDraftEditor.onPublished` at 82

Runtime parity: UNVERIFIED. Complete transitive interactions and source consumers are in the matching JSON page row.

### UI-070 `/[locale]/teacher/class-based/[id]/class-quiz`

List teacher quiz drafts/publications and navigate editing.

[dozu-ui-service/src/app/[locale]/teacher/class-based/[id]/class-quiz/page.tsx:1](<../../dozu-ui-service/src/app/[locale]/teacher/class-based/[id]/class-quiz/page.tsx#L1>)

Inherited layouts: [dozu-ui-service/src/app/[locale]/layout.tsx:1](<../../dozu-ui-service/src/app/[locale]/layout.tsx#L1>), [dozu-ui-service/src/app/layout.tsx:1](<../../dozu-ui-service/src/app/layout.tsx#L1>)

Direct local imports: [dozu-ui-service/src/hooks/useFetch.ts:1](<../../dozu-ui-service/src/hooks/useFetch.ts#L1>), [dozu-ui-service/src/app/loading.tsx:1](<../../dozu-ui-service/src/app/loading.tsx#L1>), [dozu-ui-service/src/app/[locale]/class-based/(class-quiz)/services/classQuizTeacher.service.ts:1](<../../dozu-ui-service/src/app/[locale]/class-based/(class-quiz)/services/classQuizTeacher.service.ts#L1>), [dozu-ui-service/src/app/[locale]/class-based/(class-quiz)/types/classQuiz.type.ts:1](<../../dozu-ui-service/src/app/[locale]/class-based/(class-quiz)/types/classQuiz.type.ts#L1>), [dozu-ui-service/src/app/[locale]/class-based/(class-quiz)/components/ClassQuizItem.tsx:1](<../../dozu-ui-service/src/app/[locale]/class-based/(class-quiz)/components/ClassQuizItem.tsx#L1>), [dozu-ui-service/src/utils/constants/roles.ts:1](<../../dozu-ui-service/src/utils/constants/roles.ts#L1>)

Page interaction sites: `useParams` at 11; `useFetch` at 13; `ClassQuizItem.role` at 25

Runtime parity: UNVERIFIED. Complete transitive interactions and source consumers are in the matching JSON page row.

### UI-071 `/[locale]/teacher/class-based/[id]/generate`

Teacher generation reuses full GeneratePage for class/topic content.

[dozu-ui-service/src/app/[locale]/teacher/class-based/[id]/generate/page.tsx:1](<../../dozu-ui-service/src/app/[locale]/teacher/class-based/[id]/generate/page.tsx#L1>)

Inherited layouts: [dozu-ui-service/src/app/[locale]/layout.tsx:1](<../../dozu-ui-service/src/app/[locale]/layout.tsx#L1>), [dozu-ui-service/src/app/[locale]/teacher/class-based/[id]/generate/layout.tsx:1](<../../dozu-ui-service/src/app/[locale]/teacher/class-based/[id]/generate/layout.tsx#L1>), [dozu-ui-service/src/app/layout.tsx:1](<../../dozu-ui-service/src/app/layout.tsx#L1>)

Direct local imports: [dozu-ui-service/src/hoc/withAuth.tsx:1](<../../dozu-ui-service/src/hoc/withAuth.tsx#L1>), [dozu-ui-service/src/utils/constants/common.constant.ts:1](<../../dozu-ui-service/src/utils/constants/common.constant.ts#L1>), [dozu-ui-service/src/utils/constants/roles.ts:1](<../../dozu-ui-service/src/utils/constants/roles.ts#L1>), [dozu-ui-service/src/app/[locale]/generate/components/GeneratePage.tsx:1](<../../dozu-ui-service/src/app/[locale]/generate/components/GeneratePage.tsx#L1>)

Page interaction sites: `withAuth` at 23; `useParams` at 26

Runtime parity: UNVERIFIED. Complete transitive interactions and source consumers are in the matching JSON page row.

### UI-072 `/[locale]/teacher/class-based/[id]/learning-material/[learningMaterialId]/details`

Read material content/attachments/comments; teacher edit/delete actions.

[dozu-ui-service/src/app/[locale]/teacher/class-based/[id]/learning-material/[learningMaterialId]/details/page.tsx:1](<../../dozu-ui-service/src/app/[locale]/teacher/class-based/[id]/learning-material/[learningMaterialId]/details/page.tsx#L1>)

Inherited layouts: [dozu-ui-service/src/app/[locale]/layout.tsx:1](<../../dozu-ui-service/src/app/[locale]/layout.tsx#L1>), [dozu-ui-service/src/app/layout.tsx:1](<../../dozu-ui-service/src/app/layout.tsx#L1>)

Direct local imports: [dozu-ui-service/src/app/[locale]/class-based/(classwork)/components/common/details/ContentSection.tsx:1](<../../dozu-ui-service/src/app/[locale]/class-based/(classwork)/components/common/details/ContentSection.tsx#L1>), [dozu-ui-service/src/app/[locale]/class-based/(classwork)/components/common/details/AttachmentsViewSection.tsx:1](<../../dozu-ui-service/src/app/[locale]/class-based/(classwork)/components/common/details/AttachmentsViewSection.tsx#L1>), [dozu-ui-service/src/components/ui/separator.tsx:1](<../../dozu-ui-service/src/components/ui/separator.tsx#L1>), [dozu-ui-service/src/hooks/useFetch.ts:1](<../../dozu-ui-service/src/hooks/useFetch.ts#L1>), [dozu-ui-service/src/app/[locale]/class-based/(assignment)/types/assignment.type.ts:1](<../../dozu-ui-service/src/app/[locale]/class-based/(assignment)/types/assignment.type.ts#L1>), [dozu-ui-service/src/app/[locale]/class-based/(assignment)/service/assignment.service.ts:1](<../../dozu-ui-service/src/app/[locale]/class-based/(assignment)/service/assignment.service.ts#L1>), [dozu-ui-service/src/app/loading.tsx:1](<../../dozu-ui-service/src/app/loading.tsx#L1>), [dozu-ui-service/src/components/ui/dropdown-menu.tsx:1](<../../dozu-ui-service/src/components/ui/dropdown-menu.tsx#L1>), [dozu-ui-service/src/utils/constants/routes.ts:1](<../../dozu-ui-service/src/utils/constants/routes.ts#L1>), [dozu-ui-service/src/hooks/usePost.ts:1](<../../dozu-ui-service/src/hooks/usePost.ts#L1>), [dozu-ui-service/src/utils/toast.helper.ts:1](<../../dozu-ui-service/src/utils/toast.helper.ts#L1>), [dozu-ui-service/src/app/[locale]/class-based/(assignment)/components/DeleteAssignmentModal.tsx:1](<../../dozu-ui-service/src/app/[locale]/class-based/(assignment)/components/DeleteAssignmentModal.tsx#L1>), [dozu-ui-service/src/app/[locale]/class-based/[id]/utils/class.constant.ts:1](<../../dozu-ui-service/src/app/[locale]/class-based/[id]/utils/class.constant.ts#L1>), [dozu-ui-service/src/contexts/auth/AuthContext.tsx:1](<../../dozu-ui-service/src/contexts/auth/AuthContext.tsx#L1>), [dozu-ui-service/src/components/ui/tabs.tsx:1](<../../dozu-ui-service/src/components/ui/tabs.tsx#L1>), [dozu-ui-service/src/app/[locale]/class-based/(assignment)/types/assignmentSubmission.type.ts:1](<../../dozu-ui-service/src/app/[locale]/class-based/(assignment)/types/assignmentSubmission.type.ts#L1>), [dozu-ui-service/src/app/[locale]/class-based/(assignment)/service/assignmentSubmission.service.ts:1](<../../dozu-ui-service/src/app/[locale]/class-based/(assignment)/service/assignmentSubmission.service.ts#L1>), [dozu-ui-service/src/app/[locale]/class-based/(learning-material)/types/learningMaterial.type.ts:1](<../../dozu-ui-service/src/app/[locale]/class-based/(learning-material)/types/learningMaterial.type.ts#L1>), [dozu-ui-service/src/app/[locale]/class-based/(learning-material)/service/learningMaterial.service.ts:1](<../../dozu-ui-service/src/app/[locale]/class-based/(learning-material)/service/learningMaterial.service.ts#L1>), [dozu-ui-service/src/app/[locale]/class-based/(learning-material)/components/DeleteLearningMaterialModal.tsx:1](<../../dozu-ui-service/src/app/[locale]/class-based/(learning-material)/components/DeleteLearningMaterialModal.tsx#L1>), [dozu-ui-service/src/app/[locale]/class-based/[id]/learning-material/[learningMaterialId]/details/components/LearningMaterialCommentSection.tsx:1](<../../dozu-ui-service/src/app/[locale]/class-based/[id]/learning-material/[learningMaterialId]/details/components/LearningMaterialCommentSection.tsx#L1>)

Page interaction sites: `useParams` at 44; `useAuth` at 63; `useRouter` at 64; `useTranslations` at 65; `useFetch` at 72; `useState` at 109; `usePost` at 125; `router.push` at 136; `router.push` at 142; `DropdownMenuItem.onClick` at 188; `DropdownMenuItem.onClick` at 193; `DeleteLearningMaterialModal.onSubmit` at 207

Runtime parity: UNVERIFIED. Complete transitive interactions and source consumers are in the matching JSON page row.

### UI-073 `/[locale]/teacher/class-based/[id]/learning-material/[learningMaterialId]/edit`

Load/edit teaching material, content, attachments and associated topics.

[dozu-ui-service/src/app/[locale]/teacher/class-based/[id]/learning-material/[learningMaterialId]/edit/page.tsx:1](<../../dozu-ui-service/src/app/[locale]/teacher/class-based/[id]/learning-material/[learningMaterialId]/edit/page.tsx#L1>)

Inherited layouts: [dozu-ui-service/src/app/[locale]/layout.tsx:1](<../../dozu-ui-service/src/app/[locale]/layout.tsx#L1>), [dozu-ui-service/src/app/layout.tsx:1](<../../dozu-ui-service/src/app/layout.tsx#L1>)

Direct local imports: [dozu-ui-service/src/app/[locale]/class-based/(assignment)/components/EditAssignment.tsx:1](<../../dozu-ui-service/src/app/[locale]/class-based/(assignment)/components/EditAssignment.tsx#L1>), [dozu-ui-service/src/app/[locale]/class-based/(assignment)/service/assignment.service.ts:1](<../../dozu-ui-service/src/app/[locale]/class-based/(assignment)/service/assignment.service.ts#L1>), [dozu-ui-service/src/app/[locale]/class-based/(assignment)/types/assignment.type.ts:1](<../../dozu-ui-service/src/app/[locale]/class-based/(assignment)/types/assignment.type.ts#L1>), [dozu-ui-service/src/app/[locale]/class-based/(classwork)/types/attachment.type.ts:1](<../../dozu-ui-service/src/app/[locale]/class-based/(classwork)/types/attachment.type.ts#L1>), [dozu-ui-service/src/app/[locale]/class-based/(learning-material)/components/EditLearningMaterial.tsx:1](<../../dozu-ui-service/src/app/[locale]/class-based/(learning-material)/components/EditLearningMaterial.tsx#L1>), [dozu-ui-service/src/app/[locale]/class-based/(learning-material)/service/learningMaterial.service.ts:1](<../../dozu-ui-service/src/app/[locale]/class-based/(learning-material)/service/learningMaterial.service.ts#L1>), [dozu-ui-service/src/app/[locale]/class-based/(learning-material)/types/learningMaterial.type.ts:1](<../../dozu-ui-service/src/app/[locale]/class-based/(learning-material)/types/learningMaterial.type.ts#L1>), [dozu-ui-service/src/app/[locale]/class-based/[id]/utils/class.constant.ts:1](<../../dozu-ui-service/src/app/[locale]/class-based/[id]/utils/class.constant.ts#L1>), [dozu-ui-service/src/app/[locale]/class-based/types/class.type.ts:1](<../../dozu-ui-service/src/app/[locale]/class-based/types/class.type.ts#L1>), [dozu-ui-service/src/app/[locale]/generate/constants/resource.ts:1](<../../dozu-ui-service/src/app/[locale]/generate/constants/resource.ts#L1>), [dozu-ui-service/src/app/[locale]/topics/hooks/useTopics.tsx:1](<../../dozu-ui-service/src/app/[locale]/topics/hooks/useTopics.tsx#L1>), [dozu-ui-service/src/app/loading.tsx:1](<../../dozu-ui-service/src/app/loading.tsx#L1>), [dozu-ui-service/src/hooks/upload/useUploadAttachmentFiles.tsx:1](<../../dozu-ui-service/src/hooks/upload/useUploadAttachmentFiles.tsx#L1>), [dozu-ui-service/src/hooks/useFetch.ts:1](<../../dozu-ui-service/src/hooks/useFetch.ts#L1>), [dozu-ui-service/src/hooks/usePost.ts:1](<../../dozu-ui-service/src/hooks/usePost.ts#L1>), [dozu-ui-service/src/services/class-based-learning/teacher/teacherClass.service.ts:1](<../../dozu-ui-service/src/services/class-based-learning/teacher/teacherClass.service.ts#L1>), [dozu-ui-service/src/utils/constants/routes.ts:1](<../../dozu-ui-service/src/utils/constants/routes.ts#L1>), [dozu-ui-service/src/utils/toast.helper.ts:1](<../../dozu-ui-service/src/utils/toast.helper.ts#L1>)

Page interaction sites: `useParams` at 34; `useRouter` at 53; `useFetch` at 60; `useTopics` at 63; `useFetch` at 75; `usePost` at 80; `router.push` at 89; `useUploadAttachmentFiles` at 94; `EditLearningMaterial.onSubmit` at 143

Runtime parity: UNVERIFIED. Complete transitive interactions and source consumers are in the matching JSON page row.

### UI-074 `/[locale]/teacher/class-based/[id]/learning-material/[learningMaterialId]`

Read/download learning-material attachment from backend.

[dozu-ui-service/src/app/[locale]/teacher/class-based/[id]/learning-material/[learningMaterialId]/page.tsx:1](<../../dozu-ui-service/src/app/[locale]/teacher/class-based/[id]/learning-material/[learningMaterialId]/page.tsx#L1>)

Inherited layouts: [dozu-ui-service/src/app/[locale]/layout.tsx:1](<../../dozu-ui-service/src/app/[locale]/layout.tsx#L1>), [dozu-ui-service/src/app/layout.tsx:1](<../../dozu-ui-service/src/app/layout.tsx#L1>)

Direct local imports: [dozu-ui-service/src/components/ui/card.tsx:1](<../../dozu-ui-service/src/components/ui/card.tsx#L1>), [dozu-ui-service/src/components/ui/button.tsx:1](<../../dozu-ui-service/src/components/ui/button.tsx#L1>), [dozu-ui-service/src/hooks/useFetch.ts:1](<../../dozu-ui-service/src/hooks/useFetch.ts#L1>)

Page interaction sites: `useTranslations` at 43; `useFetch` at 46; `a.href` at 76

Runtime parity: UNVERIFIED. Complete transitive interactions and source consumers are in the matching JSON page row.

### UI-075 `/[locale]/teacher/class-based/[id]/learning-material`

Create teaching material with topic/content/attachment selection.

[dozu-ui-service/src/app/[locale]/teacher/class-based/[id]/learning-material/page.tsx:1](<../../dozu-ui-service/src/app/[locale]/teacher/class-based/[id]/learning-material/page.tsx#L1>)

Inherited layouts: [dozu-ui-service/src/app/[locale]/layout.tsx:1](<../../dozu-ui-service/src/app/[locale]/layout.tsx#L1>), [dozu-ui-service/src/app/layout.tsx:1](<../../dozu-ui-service/src/app/layout.tsx#L1>)

Direct local imports: [dozu-ui-service/src/app/[locale]/class-based/types/class.type.ts:1](<../../dozu-ui-service/src/app/[locale]/class-based/types/class.type.ts#L1>), [dozu-ui-service/src/app/[locale]/topics/hooks/useTopics.tsx:1](<../../dozu-ui-service/src/app/[locale]/topics/hooks/useTopics.tsx#L1>), [dozu-ui-service/src/app/loading.tsx:1](<../../dozu-ui-service/src/app/loading.tsx#L1>), [dozu-ui-service/src/hooks/useFetch.ts:1](<../../dozu-ui-service/src/hooks/useFetch.ts#L1>), [dozu-ui-service/src/services/class-based-learning/teacher/teacherClass.service.ts:1](<../../dozu-ui-service/src/services/class-based-learning/teacher/teacherClass.service.ts#L1>), [dozu-ui-service/src/app/[locale]/teacher/class-based/[id]/learning-material/components/CreateLearningMaterial.tsx:1](<../../dozu-ui-service/src/app/[locale]/teacher/class-based/[id]/learning-material/components/CreateLearningMaterial.tsx#L1>)

Page interaction sites: `useParams` at 14; `useFetch` at 31; `useTopics` at 34

Runtime parity: UNVERIFIED. Complete transitive interactions and source consumers are in the matching JSON page row.

### UI-076 `/[locale]/teacher/class-based/[id]/mindmap/[topicId]`

Class topic ReactFlow mindmap, source and flashcard sheets, export; teacher edit/save/generate actions.

[dozu-ui-service/src/app/[locale]/teacher/class-based/[id]/mindmap/[topicId]/page.tsx:1](<../../dozu-ui-service/src/app/[locale]/teacher/class-based/[id]/mindmap/[topicId]/page.tsx#L1>)

Inherited layouts: [dozu-ui-service/src/app/[locale]/layout.tsx:1](<../../dozu-ui-service/src/app/[locale]/layout.tsx#L1>), [dozu-ui-service/src/app/[locale]/teacher/class-based/[id]/mindmap/[topicId]/layout.tsx:1](<../../dozu-ui-service/src/app/[locale]/teacher/class-based/[id]/mindmap/[topicId]/layout.tsx#L1>), [dozu-ui-service/src/app/layout.tsx:1](<../../dozu-ui-service/src/app/layout.tsx#L1>)

Direct local imports: [dozu-ui-service/src/stores/hooks.tsx:1](<../../dozu-ui-service/src/stores/hooks.tsx#L1>), [dozu-ui-service/src/hooks/use-toast.ts:1](<../../dozu-ui-service/src/hooks/use-toast.ts#L1>), [dozu-ui-service/src/utils/routerService.ts:1](<../../dozu-ui-service/src/utils/routerService.ts#L1>), [dozu-ui-service/src/components/ui/button.tsx:1](<../../dozu-ui-service/src/components/ui/button.tsx#L1>), [dozu-ui-service/src/components/mindmap/button/DownloadButton.tsx:1](<../../dozu-ui-service/src/components/mindmap/button/DownloadButton.tsx#L1>), [dozu-ui-service/src/app/loading.tsx:1](<../../dozu-ui-service/src/app/loading.tsx#L1>), [dozu-ui-service/src/services/flashcard/flashcard.service.ts:1](<../../dozu-ui-service/src/services/flashcard/flashcard.service.ts#L1>), [dozu-ui-service/src/components/generative/GeneratingSkeleton.tsx:1](<../../dozu-ui-service/src/components/generative/GeneratingSkeleton.tsx#L1>), [dozu-ui-service/src/app/[locale]/generate/hooks/useContentGeneration.ts:1](<../../dozu-ui-service/src/app/[locale]/generate/hooks/useContentGeneration.ts#L1>), [dozu-ui-service/src/app/[locale]/flashcards/types/flashcard.type.ts:1](<../../dozu-ui-service/src/app/[locale]/flashcards/types/flashcard.type.ts#L1>), [dozu-ui-service/src/components/mindmap/button/ViewFileButton.tsx:1](<../../dozu-ui-service/src/components/mindmap/button/ViewFileButton.tsx#L1>), [dozu-ui-service/src/app/[locale]/mindmap/components/CustomReactFlowNode.tsx:1](<../../dozu-ui-service/src/app/[locale]/mindmap/components/CustomReactFlowNode.tsx#L1>), [dozu-ui-service/src/app/[locale]/mindmap/components/FileSheet.tsx:1](<../../dozu-ui-service/src/app/[locale]/mindmap/components/FileSheet.tsx#L1>), [dozu-ui-service/src/app/[locale]/mindmap/components/FloatingEdge.tsx:1](<../../dozu-ui-service/src/app/[locale]/mindmap/components/FloatingEdge.tsx#L1>), [dozu-ui-service/src/app/[locale]/generate/components/ContentGenerationPreview.tsx:1](<../../dozu-ui-service/src/app/[locale]/generate/components/ContentGenerationPreview.tsx#L1>), [dozu-ui-service/src/app/[locale]/mindmap/context/MindMapContext.tsx:1](<../../dozu-ui-service/src/app/[locale]/mindmap/context/MindMapContext.tsx#L1>), [dozu-ui-service/src/app/[locale]/flashcards/components/FlashcardEditor.tsx:1](<../../dozu-ui-service/src/app/[locale]/flashcards/components/FlashcardEditor.tsx#L1>), [dozu-ui-service/src/components/mindmap/TeacherNodeSheet.tsx:1](<../../dozu-ui-service/src/components/mindmap/TeacherNodeSheet.tsx#L1>)

Page interaction sites: `useRouter` at 53; `useParams` at 54; `useState` at 57; `useMindMapContext` at 70; `useContentGeneration` at 72; `useAppSelector` at 74; `useEffect` at 76; `useEffect` at 80; `router.push` at 184; `ContentGenerationPreview.onSave` at 199; `Button.onClick` at 207; `ReactFlow.onNodesChange` at 217; `ReactFlow.onEdgesChange` at 217; `Button.onClick` at 231

Runtime parity: UNVERIFIED. Complete transitive interactions and source consumers are in the matching JSON page row.

### UI-077 `/[locale]/teacher/class-based/[id]`

Teacher class dashboard, topics/feed/classwork tabs, create/edit/archive and access management.

[dozu-ui-service/src/app/[locale]/teacher/class-based/[id]/page.tsx:1](<../../dozu-ui-service/src/app/[locale]/teacher/class-based/[id]/page.tsx#L1>)

Inherited layouts: [dozu-ui-service/src/app/[locale]/layout.tsx:1](<../../dozu-ui-service/src/app/[locale]/layout.tsx#L1>), [dozu-ui-service/src/app/layout.tsx:1](<../../dozu-ui-service/src/app/layout.tsx#L1>)

Direct local imports: [dozu-ui-service/src/app/[locale]/class-based/[id]/utils/class.utils.ts:1](<../../dozu-ui-service/src/app/[locale]/class-based/[id]/utils/class.utils.ts#L1>), [dozu-ui-service/src/app/[locale]/teacher/class-based/[id]/dashboard/TeacherClassDashboard.tsx:1](<../../dozu-ui-service/src/app/[locale]/teacher/class-based/[id]/dashboard/TeacherClassDashboard.tsx#L1>), [dozu-ui-service/src/hoc/withAuth.tsx:1](<../../dozu-ui-service/src/hoc/withAuth.tsx#L1>), [dozu-ui-service/src/utils/constants/roles.ts:1](<../../dozu-ui-service/src/utils/constants/roles.ts#L1>), [dozu-ui-service/src/app/[locale]/class-based/[id]/utils/class.constant.ts:1](<../../dozu-ui-service/src/app/[locale]/class-based/[id]/utils/class.constant.ts#L1>)

Page interaction sites: `withAuth` at 10; `useParams` at 13; `useSearchParams` at 15

Runtime parity: UNVERIFIED. Complete transitive interactions and source consumers are in the matching JSON page row.

### UI-078 `/[locale]/teacher/class-based/[id]/students`

List/search student enrollment, profile modal and enrollment management.

[dozu-ui-service/src/app/[locale]/teacher/class-based/[id]/students/page.tsx:1](<../../dozu-ui-service/src/app/[locale]/teacher/class-based/[id]/students/page.tsx#L1>)

Inherited layouts: [dozu-ui-service/src/app/[locale]/layout.tsx:1](<../../dozu-ui-service/src/app/[locale]/layout.tsx#L1>), [dozu-ui-service/src/app/[locale]/teacher/class-based/[id]/students/layout.tsx:1](<../../dozu-ui-service/src/app/[locale]/teacher/class-based/[id]/students/layout.tsx#L1>), [dozu-ui-service/src/app/layout.tsx:1](<../../dozu-ui-service/src/app/layout.tsx#L1>)

Direct local imports: [dozu-ui-service/src/hooks/useFetch.ts:1](<../../dozu-ui-service/src/hooks/useFetch.ts#L1>), [dozu-ui-service/src/app/[locale]/class-based/types/class.type.ts:1](<../../dozu-ui-service/src/app/[locale]/class-based/types/class.type.ts#L1>), [dozu-ui-service/src/app/loading.tsx:1](<../../dozu-ui-service/src/app/loading.tsx#L1>), [dozu-ui-service/src/app/[locale]/teacher/class-based/[id]/students/components/StudentList.tsx:1](<../../dozu-ui-service/src/app/[locale]/teacher/class-based/[id]/students/components/StudentList.tsx#L1>), [dozu-ui-service/src/hooks/use-toast.ts:1](<../../dozu-ui-service/src/hooks/use-toast.ts#L1>), [dozu-ui-service/src/services/class-based-learning/teacher/teacherClass.service.ts:1](<../../dozu-ui-service/src/services/class-based-learning/teacher/teacherClass.service.ts#L1>), [dozu-ui-service/src/types/profile.ts:1](<../../dozu-ui-service/src/types/profile.ts#L1>), [dozu-ui-service/src/hooks/usePost.ts:1](<../../dozu-ui-service/src/hooks/usePost.ts#L1>), [dozu-ui-service/src/utils/toast.helper.ts:1](<../../dozu-ui-service/src/utils/toast.helper.ts#L1>), [dozu-ui-service/src/app/[locale]/teacher/class-based/[id]/students/components/StudentProfileModal.tsx:1](<../../dozu-ui-service/src/app/[locale]/teacher/class-based/[id]/students/components/StudentProfileModal.tsx#L1>), [dozu-ui-service/src/components/toolbar/LanguageSwitcher.tsx:1](<../../dozu-ui-service/src/components/toolbar/LanguageSwitcher.tsx#L1>), [dozu-ui-service/src/hoc/withAuth.tsx:1](<../../dozu-ui-service/src/hoc/withAuth.tsx#L1>), [dozu-ui-service/src/utils/constants/roles.ts:1](<../../dozu-ui-service/src/utils/constants/roles.ts#L1>)

Page interaction sites: `useTranslations` at 24; `useTranslations` at 25; `useTranslations` at 26; `useState` at 29; `useState` at 30; `useState` at 31; `useFetch` at 38; `useFetch` at 45; `usePost` at 47; `StudentProfileModal.onClose` at 145; `withAuth` at 156; `useParams` at 159

Runtime parity: UNVERIFIED. Complete transitive interactions and source consumers are in the matching JSON page row.

### UI-079 `/[locale]/teacher/class-based/[id]/topics/[topicId]`

Class context wraps shared topic workspace and mindmap provider; preserve teacher/student permissions across tabs.

[dozu-ui-service/src/app/[locale]/teacher/class-based/[id]/topics/[topicId]/page.tsx:1](<../../dozu-ui-service/src/app/[locale]/teacher/class-based/[id]/topics/[topicId]/page.tsx#L1>)

Inherited layouts: [dozu-ui-service/src/app/[locale]/layout.tsx:1](<../../dozu-ui-service/src/app/[locale]/layout.tsx#L1>), [dozu-ui-service/src/app/layout.tsx:1](<../../dozu-ui-service/src/app/layout.tsx#L1>)

Direct local imports: [dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/context/TopicWorkspaceContext.tsx:1](<../../dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/context/TopicWorkspaceContext.tsx#L1>), [dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/workspace/TopicWorkspace.tsx:1](<../../dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/workspace/TopicWorkspace.tsx#L1>), [dozu-ui-service/src/app/[locale]/mindmap/context/MindMapContext.tsx:1](<../../dozu-ui-service/src/app/[locale]/mindmap/context/MindMapContext.tsx#L1>)

Page interaction sites: `useParams` at 10

Runtime parity: UNVERIFIED. Complete transitive interactions and source consumers are in the matching JSON page row.

### UI-080 `/[locale]/teacher/home`

Teacher class library and class management/navigation.

[dozu-ui-service/src/app/[locale]/teacher/home/page.tsx:1](<../../dozu-ui-service/src/app/[locale]/teacher/home/page.tsx#L1>)

Inherited layouts: [dozu-ui-service/src/app/[locale]/layout.tsx:1](<../../dozu-ui-service/src/app/[locale]/layout.tsx#L1>), [dozu-ui-service/src/app/[locale]/teacher/home/layout.tsx:1](<../../dozu-ui-service/src/app/[locale]/teacher/home/layout.tsx#L1>), [dozu-ui-service/src/app/layout.tsx:1](<../../dozu-ui-service/src/app/layout.tsx#L1>)

Direct local imports: [dozu-ui-service/src/app/[locale]/teacher/home/components/ui/TeacherClassLibrary.tsx:1](<../../dozu-ui-service/src/app/[locale]/teacher/home/components/ui/TeacherClassLibrary.tsx#L1>), [dozu-ui-service/src/hoc/withAuth.tsx:1](<../../dozu-ui-service/src/hoc/withAuth.tsx#L1>), [dozu-ui-service/src/utils/constants/roles.ts:1](<../../dozu-ui-service/src/utils/constants/roles.ts#L1>), [dozu-ui-service/src/components/common/BackgroundGradient.tsx:1](<../../dozu-ui-service/src/components/common/BackgroundGradient.tsx#L1>)

Page interaction sites: `withAuth` at 9

Runtime parity: UNVERIFIED. Complete transitive interactions and source consumers are in the matching JSON page row.

### UI-081 `/[locale]/tests/class/comment`

Empty developer route; not implemented comment UI.

[dozu-ui-service/src/app/[locale]/tests/class/comment/page.tsx:1](<../../dozu-ui-service/src/app/[locale]/tests/class/comment/page.tsx#L1>)

Inherited layouts: [dozu-ui-service/src/app/[locale]/layout.tsx:1](<../../dozu-ui-service/src/app/[locale]/layout.tsx#L1>), [dozu-ui-service/src/app/layout.tsx:1](<../../dozu-ui-service/src/app/layout.tsx#L1>)

Direct local imports: none

Page interaction sites: none in page AST; inspect imported component ledger

Runtime parity: UNVERIFIED. Complete transitive interactions and source consumers are in the matching JSON page row.

### UI-082 `/[locale]/topics/[topicId]`

Topic workspace tabs for flashcards, quiz, mindmap, notes and media; generation/edit/learning and source-linked context.

[dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/page.tsx:1](<../../dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/page.tsx#L1>)

Inherited layouts: [dozu-ui-service/src/app/[locale]/layout.tsx:1](<../../dozu-ui-service/src/app/[locale]/layout.tsx#L1>), [dozu-ui-service/src/app/layout.tsx:1](<../../dozu-ui-service/src/app/layout.tsx#L1>)

Direct local imports: [dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/workspace/TopicWorkspace.tsx:1](<../../dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/workspace/TopicWorkspace.tsx#L1>), [dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/context/TopicWorkspaceContext.tsx:1](<../../dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/context/TopicWorkspaceContext.tsx#L1>), [dozu-ui-service/src/hoc/withAuth.tsx:1](<../../dozu-ui-service/src/hoc/withAuth.tsx#L1>), [dozu-ui-service/src/app/[locale]/mindmap/context/MindMapContext.tsx:1](<../../dozu-ui-service/src/app/[locale]/mindmap/context/MindMapContext.tsx#L1>)

Page interaction sites: `useParams` at 11; `withAuth` at 31

Runtime parity: UNVERIFIED. Complete transitive interactions and source consumers are in the matching JSON page row.

### UI-083 `/[locale]/topics/[topicId]/settings/anki`

Select/create/update/delete Anki preset, edit parameters, assign to topic and reset defaults.

[dozu-ui-service/src/app/[locale]/topics/[topicId]/settings/anki/page.tsx:1](<../../dozu-ui-service/src/app/[locale]/topics/[topicId]/settings/anki/page.tsx#L1>)

Inherited layouts: [dozu-ui-service/src/app/[locale]/layout.tsx:1](<../../dozu-ui-service/src/app/[locale]/layout.tsx#L1>), [dozu-ui-service/src/app/layout.tsx:1](<../../dozu-ui-service/src/app/layout.tsx#L1>)

Direct local imports: [dozu-ui-service/src/components/ui/button.tsx:1](<../../dozu-ui-service/src/components/ui/button.tsx#L1>), [dozu-ui-service/src/components/ui/input.tsx:1](<../../dozu-ui-service/src/components/ui/input.tsx#L1>), [dozu-ui-service/src/components/ui/label.tsx:1](<../../dozu-ui-service/src/components/ui/label.tsx#L1>), [dozu-ui-service/src/components/ui/card.tsx:1](<../../dozu-ui-service/src/components/ui/card.tsx#L1>), [dozu-ui-service/src/components/ui/separator.tsx:1](<../../dozu-ui-service/src/components/ui/separator.tsx#L1>), [dozu-ui-service/src/components/ui/tooltip.tsx:1](<../../dozu-ui-service/src/components/ui/tooltip.tsx#L1>), [dozu-ui-service/src/hooks/useFetch.ts:1](<../../dozu-ui-service/src/hooks/useFetch.ts#L1>), [dozu-ui-service/src/services/anki-setting/ankiSetting.service.ts:1](<../../dozu-ui-service/src/services/anki-setting/ankiSetting.service.ts#L1>), [dozu-ui-service/src/app/loading.tsx:1](<../../dozu-ui-service/src/app/loading.tsx#L1>), [dozu-ui-service/src/types/anki-setting/ankiSetting.type.ts:1](<../../dozu-ui-service/src/types/anki-setting/ankiSetting.type.ts#L1>), [dozu-ui-service/src/hooks/usePost.ts:1](<../../dozu-ui-service/src/hooks/usePost.ts#L1>), [dozu-ui-service/src/utils/toast.helper.ts:1](<../../dozu-ui-service/src/utils/toast.helper.ts#L1>), [dozu-ui-service/src/components/ui/select.tsx:1](<../../dozu-ui-service/src/components/ui/select.tsx#L1>), [dozu-ui-service/src/services/topic/topic.service.ts:1](<../../dozu-ui-service/src/services/topic/topic.service.ts#L1>), [dozu-ui-service/src/app/[locale]/topics/types/topic.type.ts:1](<../../dozu-ui-service/src/app/[locale]/topics/types/topic.type.ts#L1>), [dozu-ui-service/src/app/[locale]/topics/[topicId]/settings/anki/utils/ankiSetting.util.ts:1](<../../dozu-ui-service/src/app/[locale]/topics/[topicId]/settings/anki/utils/ankiSetting.util.ts#L1>), [dozu-ui-service/src/app/[locale]/topics/[topicId]/settings/anki/components/CreateSettingModal.tsx:1](<../../dozu-ui-service/src/app/[locale]/topics/[topicId]/settings/anki/components/CreateSettingModal.tsx#L1>), [dozu-ui-service/src/components/ui/dropdown-menu.tsx:1](<../../dozu-ui-service/src/components/ui/dropdown-menu.tsx#L1>), [dozu-ui-service/src/app/[locale]/topics/[topicId]/settings/anki/components/UpdateSettingModal.tsx:1](<../../dozu-ui-service/src/app/[locale]/topics/[topicId]/settings/anki/components/UpdateSettingModal.tsx#L1>), [dozu-ui-service/src/app/[locale]/topics/[topicId]/settings/anki/components/DeleteSettingModal.tsx:1](<../../dozu-ui-service/src/app/[locale]/topics/[topicId]/settings/anki/components/DeleteSettingModal.tsx#L1>), [dozu-ui-service/src/services/anki-setting/constant.ts:1](<../../dozu-ui-service/src/services/anki-setting/constant.ts#L1>), [dozu-ui-service/src/app/[locale]/topics/[topicId]/settings/anki/components/ResetToDefaultModal.tsx:1](<../../dozu-ui-service/src/app/[locale]/topics/[topicId]/settings/anki/components/ResetToDefaultModal.tsx#L1>)

Page interaction sites: `useParams` at 68; `useTranslations` at 75; `useFetch` at 81; `useFetch` at 88; `usePost` at 92; `usePost` at 111; `usePost` at 130; `useState` at 159; `useState` at 160; `useState` at 163; `useState` at 166; `useState` at 167; `useState` at 170; `useState` at 171; `useState` at 174; `useState` at 177; `useState` at 178; `useEffect` at 180; `useEffect` at 186; `useEffect` at 192; `Select.onValueChange` at 332; `DropdownMenuItem.onSelect` at 358; `DropdownMenuItem.onSelect` at 362; `Button.onClick` at 370; `CreateSettingModal.onSubmit` at 375; `UpdateSettingModal.onSubmit` at 382; `DeleteSettingModal.onSubmit` at 390; `Input.onChange` at 413; `Input.onBlur` at 413; `Input.onChange` at 424; `Input.onChange` at 435; `Input.onChange` at 456; `Input.onChange` at 468; `Input.onChange` at 480; `Input.onChange` at 492; `Input.onChange` at 506; `Input.onChange` at 517; `Input.onChange` at 540; `Input.onBlur` at 540; `Input.onChange` at 551; `Input.onChange` at 573; `Input.onChange` at 584; `Button.onClick` at 596; `Button.onClick` at 599; `ResetToDefaultModal.onSubmit` at 603

Runtime parity: UNVERIFIED. Complete transitive interactions and source consumers are in the matching JSON page row.

### UI-084 `/[locale]/welcome`

Browse landing/FAQ, change language/theme and enter sign-in/onboarding.

[dozu-ui-service/src/app/[locale]/welcome/page.tsx:1](<../../dozu-ui-service/src/app/[locale]/welcome/page.tsx#L1>)

Inherited layouts: [dozu-ui-service/src/app/[locale]/layout.tsx:1](<../../dozu-ui-service/src/app/[locale]/layout.tsx#L1>), [dozu-ui-service/src/app/[locale]/welcome/layout.tsx:1](<../../dozu-ui-service/src/app/[locale]/welcome/layout.tsx#L1>), [dozu-ui-service/src/app/layout.tsx:1](<../../dozu-ui-service/src/app/layout.tsx#L1>)

Direct local imports: [dozu-ui-service/src/components/ui/button.tsx:1](<../../dozu-ui-service/src/components/ui/button.tsx#L1>), [dozu-ui-service/src/contexts/auth/AuthContext.tsx:1](<../../dozu-ui-service/src/contexts/auth/AuthContext.tsx#L1>), [dozu-ui-service/src/hooks/useAuthNavigation.ts:1](<../../dozu-ui-service/src/hooks/useAuthNavigation.ts#L1>), [dozu-ui-service/src/components/react-bits/Threads.tsx:1](<../../dozu-ui-service/src/components/react-bits/Threads.tsx#L1>), [dozu-ui-service/src/components/react-bits/TextType.tsx:1](<../../dozu-ui-service/src/components/react-bits/TextType.tsx#L1>), [dozu-ui-service/src/components/react-bits/StarBorder.tsx:1](<../../dozu-ui-service/src/components/react-bits/StarBorder.tsx#L1>), [dozu-ui-service/src/components/react-bits/CardSwap.tsx:1](<../../dozu-ui-service/src/components/react-bits/CardSwap.tsx#L1>), [dozu-ui-service/src/components/react-bits/Particles.tsx:1](<../../dozu-ui-service/src/components/react-bits/Particles.tsx#L1>), [dozu-ui-service/src/components/react-bits/SplitText.tsx:1](<../../dozu-ui-service/src/components/react-bits/SplitText.tsx#L1>)

Page interaction sites: `useAuth` at 31; `useAuthNavigation` at 32; `useTranslations` at 37; `useEffect` at 68; `StarBorder.onClick` at 163; `motion.button.onClick` at 176; `a.href` at 470; `a.href` at 477; `a.href` at 484; `a.href` at 491; `a.href` at 506; `a.href` at 514; `a.href` at 522; `a.href` at 530; `a.href` at 545; `a.href` at 553; `a.href` at 561; `a.href` at 569; `a.href` at 584; `a.href` at 592; `a.href` at 600; `a.href` at 608; `useState` at 654; `button.onClick` at 664

Runtime parity: UNVERIFIED. Complete transitive interactions and source consumers are in the matching JSON page row.

## All non-entry TSX components

Scope includes 164 src/components TSX files and all route-scoped TSX plus supporting providers/layout helpers. Unreferenced components remain inventoried; no dead-code deletion is authorized.

| Source | Declared symbols | Page reachability |
| --- | --- | --- |
| [dozu-ui-service/src/app/Providers.tsx:1](<../../dozu-ui-service/src/app/Providers.tsx#L1>) | Providers | 84 source closures; see JSON |
| [dozu-ui-service/src/app/StoreProvider.tsx:1](<../../dozu-ui-service/src/app/StoreProvider.tsx#L1>) | StoreProvider | 84 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/about/_components/Profile.tsx:1](<../../dozu-ui-service/src/app/[locale]/about/_components/Profile.tsx#L1>) | Profile | 1 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/activities/components/ActivitySummaryTab.tsx:1](<../../dozu-ui-service/src/app/[locale]/activities/components/ActivitySummaryTab.tsx#L1>) | ActivitySummaryTab | 1 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/activities/components/CircularProgressChart.tsx:1](<../../dozu-ui-service/src/app/[locale]/activities/components/CircularProgressChart.tsx#L1>) | CircularProgressChart | 1 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/activities/components/JoinActivityLink.tsx:1](<../../dozu-ui-service/src/app/[locale]/activities/components/JoinActivityLink.tsx#L1>) | JoinActivityLink | 1 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/activities/components/PerformanceBreakdown.tsx:1](<../../dozu-ui-service/src/app/[locale]/activities/components/PerformanceBreakdown.tsx#L1>) | PerformanceBreakdown | 0 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/activities/components/QuestionDetailList.tsx:1](<../../dozu-ui-service/src/app/[locale]/activities/components/QuestionDetailList.tsx#L1>) | QuestionDetailList | 1 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/activities/components/StudentProgressCard.tsx:1](<../../dozu-ui-service/src/app/[locale]/activities/components/StudentProgressCard.tsx#L1>) | StudentProgressCard | 1 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/activities/components/StudentResultsTab.tsx:1](<../../dozu-ui-service/src/app/[locale]/activities/components/StudentResultsTab.tsx#L1>) | StudentResultsTab | 1 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/activities/components/StudentSummaryTab.tsx:1](<../../dozu-ui-service/src/app/[locale]/activities/components/StudentSummaryTab.tsx#L1>) | StudentSummaryTab | 1 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/activities/components/TermProgressTab.tsx:1](<../../dozu-ui-service/src/app/[locale]/activities/components/TermProgressTab.tsx#L1>) | TermProgressTab | 1 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/admin/components/Chart.tsx:1](<../../dozu-ui-service/src/app/[locale]/admin/components/Chart.tsx#L1>) | UserSignupChart | 1 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/admin/components/RecentActivity.tsx:1](<../../dozu-ui-service/src/app/[locale]/admin/components/RecentActivity.tsx#L1>) | RecentActivity | 1 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/admin/features/components/Columns.tsx:1](<../../dozu-ui-service/src/app/[locale]/admin/features/components/Columns.tsx#L1>) | FeatureTypeBadge, CategoryBadge, ActionButtons | 1 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/admin/features/components/CreateFeatureDialog.tsx:1](<../../dozu-ui-service/src/app/[locale]/admin/features/components/CreateFeatureDialog.tsx#L1>) | CreateFeatureDialog | 1 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/admin/features/components/DeleteFeatureDialog.tsx:1](<../../dozu-ui-service/src/app/[locale]/admin/features/components/DeleteFeatureDialog.tsx#L1>) | DeleteFeatureDialog | 1 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/admin/feedback/components/Columns.tsx:1](<../../dozu-ui-service/src/app/[locale]/admin/feedback/components/Columns.tsx#L1>) | (anonymous/local declarations) | 1 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/admin/feedback/components/category-select.tsx:1](<../../dozu-ui-service/src/app/[locale]/admin/feedback/components/category-select.tsx#L1>) | CategorySelect | 1 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/admin/feedback/components/feedback-content-cell.tsx:1](<../../dozu-ui-service/src/app/[locale]/admin/feedback/components/feedback-content-cell.tsx#L1>) | FeedbackContentCell | 1 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/admin/feedback/components/filter-bar.tsx:1](<../../dozu-ui-service/src/app/[locale]/admin/feedback/components/filter-bar.tsx#L1>) | FeedbackFilterBar | 1 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/admin/feedback/components/image-cell.tsx:1](<../../dozu-ui-service/src/app/[locale]/admin/feedback/components/image-cell.tsx#L1>) | ImageCell | 1 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/admin/feedback/components/row-actions.tsx:1](<../../dozu-ui-service/src/app/[locale]/admin/feedback/components/row-actions.tsx#L1>) | FeedbackRowActions | 1 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/admin/feedback/components/score-cell.tsx:1](<../../dozu-ui-service/src/app/[locale]/admin/feedback/components/score-cell.tsx#L1>) | ScoreCell | 1 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/admin/feedback/components/status-select.tsx:1](<../../dozu-ui-service/src/app/[locale]/admin/feedback/components/status-select.tsx#L1>) | StatusSelect | 1 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/admin/llm-api-key-models/components/Columns.tsx:1](<../../dozu-ui-service/src/app/[locale]/admin/llm-api-key-models/components/Columns.tsx#L1>) | ActionButtons | 1 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/admin/llm-api-key-models/components/CreateEditLlmApiKeyModelDialog.tsx:1](<../../dozu-ui-service/src/app/[locale]/admin/llm-api-key-models/components/CreateEditLlmApiKeyModelDialog.tsx#L1>) | CreateEditLlmApiKeyModelDialog | 1 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/admin/llm-api-key-models/components/DeleteApiKeyModelDialog.tsx:1](<../../dozu-ui-service/src/app/[locale]/admin/llm-api-key-models/components/DeleteApiKeyModelDialog.tsx#L1>) | DeleteApiKeyModelDialog | 1 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/admin/llm-api-keys/components/Columns.tsx:1](<../../dozu-ui-service/src/app/[locale]/admin/llm-api-keys/components/Columns.tsx#L1>) | ActionButtons | 1 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/admin/llm-api-keys/components/CreateEditLlmApiKeyDialog.tsx:1](<../../dozu-ui-service/src/app/[locale]/admin/llm-api-keys/components/CreateEditLlmApiKeyDialog.tsx#L1>) | CreateEditLlmApiKeyDialog | 1 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/admin/llm-api-keys/components/DeleteApiKeyDialog.tsx:1](<../../dozu-ui-service/src/app/[locale]/admin/llm-api-keys/components/DeleteApiKeyDialog.tsx#L1>) | DeleteApiKeyDialog | 1 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/admin/llm-models/components/Columns.tsx:1](<../../dozu-ui-service/src/app/[locale]/admin/llm-models/components/Columns.tsx#L1>) | ActionButtons | 1 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/admin/llm-models/components/CreateEditLlmModelDialog.tsx:1](<../../dozu-ui-service/src/app/[locale]/admin/llm-models/components/CreateEditLlmModelDialog.tsx#L1>) | CreateEditLlmModelDialog | 1 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/admin/llm-models/components/DeleteModelDialog.tsx:1](<../../dozu-ui-service/src/app/[locale]/admin/llm-models/components/DeleteModelDialog.tsx#L1>) | DeleteModelDialog | 1 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/admin/llm-models/components/LlmModelFilter.tsx:1](<../../dozu-ui-service/src/app/[locale]/admin/llm-models/components/LlmModelFilter.tsx#L1>) | LlmModelFilter | 1 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/admin/llm-providers/components/Columns.tsx:1](<../../dozu-ui-service/src/app/[locale]/admin/llm-providers/components/Columns.tsx#L1>) | ActionButtons | 1 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/admin/llm-providers/components/CreateEditLlmProviderDialog.tsx:1](<../../dozu-ui-service/src/app/[locale]/admin/llm-providers/components/CreateEditLlmProviderDialog.tsx#L1>) | CreateEditLlmProviderDialog | 1 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/admin/llm-providers/components/DeleteProviderDialog.tsx:1](<../../dozu-ui-service/src/app/[locale]/admin/llm-providers/components/DeleteProviderDialog.tsx#L1>) | DeleteProviderDialog | 1 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/admin/llm-providers/components/LlmProviderFilter.tsx:1](<../../dozu-ui-service/src/app/[locale]/admin/llm-providers/components/LlmProviderFilter.tsx#L1>) | LlmProviderFilter | 1 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/admin/payments/components/Columns.tsx:1](<../../dozu-ui-service/src/app/[locale]/admin/payments/components/Columns.tsx#L1>) | StatusBadge, GatewayBadge, ActionButtons | 1 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/admin/payments/components/PaymentFilter.tsx:1](<../../dozu-ui-service/src/app/[locale]/admin/payments/components/PaymentFilter.tsx#L1>) | PaymentFilter | 1 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/admin/payments/components/RefundDialog.tsx:1](<../../dozu-ui-service/src/app/[locale]/admin/payments/components/RefundDialog.tsx#L1>) | RefundDialog | 1 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/admin/plans/[planId]/features/components/AssignFeatureDialog.tsx:1](<../../dozu-ui-service/src/app/[locale]/admin/plans/[planId]/features/components/AssignFeatureDialog.tsx#L1>) | AssignFeatureDialog | 1 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/admin/plans/[planId]/features/components/Columns.tsx:1](<../../dozu-ui-service/src/app/[locale]/admin/plans/[planId]/features/components/Columns.tsx#L1>) | FeatureTypeBadge, CategoryBadge, FeatureValue, ActionButtons | 1 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/admin/plans/[planId]/features/components/RemoveFeatureDialog.tsx:1](<../../dozu-ui-service/src/app/[locale]/admin/plans/[planId]/features/components/RemoveFeatureDialog.tsx#L1>) | RemoveFeatureDialog | 1 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/admin/plans/components/Columns.tsx:1](<../../dozu-ui-service/src/app/[locale]/admin/plans/components/Columns.tsx#L1>) | PlanTypeBadge, BillingBadge, ActiveBadge, ActionButtons | 1 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/admin/plans/components/CreatePlanDialog.tsx:1](<../../dozu-ui-service/src/app/[locale]/admin/plans/components/CreatePlanDialog.tsx#L1>) | CreatePlanDialog | 1 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/admin/plans/components/DeletePlanDialog.tsx:1](<../../dozu-ui-service/src/app/[locale]/admin/plans/components/DeletePlanDialog.tsx#L1>) | DeletePlanDialog | 1 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/admin/revenue/components/KPICard.tsx:1](<../../dozu-ui-service/src/app/[locale]/admin/revenue/components/KPICard.tsx#L1>) | KPICard | 1 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/admin/revenue/components/PeriodSelector.tsx:1](<../../dozu-ui-service/src/app/[locale]/admin/revenue/components/PeriodSelector.tsx#L1>) | PeriodSelector | 1 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/admin/revenue/components/RevenueByGatewayChart.tsx:1](<../../dozu-ui-service/src/app/[locale]/admin/revenue/components/RevenueByGatewayChart.tsx#L1>) | RevenueByGatewayChart | 1 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/admin/revenue/components/RevenueByPlanChart.tsx:1](<../../dozu-ui-service/src/app/[locale]/admin/revenue/components/RevenueByPlanChart.tsx#L1>) | RevenueByPlanChart | 1 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/admin/revenue/components/RevenueFilter.tsx:1](<../../dozu-ui-service/src/app/[locale]/admin/revenue/components/RevenueFilter.tsx#L1>) | RevenueFilter | 1 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/admin/revenue/components/RevenueTrendChart.tsx:1](<../../dozu-ui-service/src/app/[locale]/admin/revenue/components/RevenueTrendChart.tsx#L1>) | RevenueTrendChart | 1 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/admin/subscriptions/components/MonthlyTrendChart.tsx:1](<../../dozu-ui-service/src/app/[locale]/admin/subscriptions/components/MonthlyTrendChart.tsx#L1>) | MonthlyTrendChart | 1 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/admin/subscriptions/components/StatsCard.tsx:1](<../../dozu-ui-service/src/app/[locale]/admin/subscriptions/components/StatsCard.tsx#L1>) | StatsCard | 1 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/admin/subscriptions/components/StatusBreakdownChart.tsx:1](<../../dozu-ui-service/src/app/[locale]/admin/subscriptions/components/StatusBreakdownChart.tsx#L1>) | StatusBreakdownChart | 1 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/admin/subscriptions/list/components/Columns.tsx:1](<../../dozu-ui-service/src/app/[locale]/admin/subscriptions/list/components/Columns.tsx#L1>) | StatusBadge, PlanBadge | 1 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/admin/subscriptions/list/components/SubscriptionFilter.tsx:1](<../../dozu-ui-service/src/app/[locale]/admin/subscriptions/list/components/SubscriptionFilter.tsx#L1>) | SubscriptionFilter | 1 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/admin/teacher-requests/components/PendingRequestList.tsx:1](<../../dozu-ui-service/src/app/[locale]/admin/teacher-requests/components/PendingRequestList.tsx#L1>) | PendingRequestList | 1 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/admin/teacher-requests/components/RequestList.tsx:1](<../../dozu-ui-service/src/app/[locale]/admin/teacher-requests/components/RequestList.tsx#L1>) | RequestList | 1 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/admin/users/components/Columns.tsx:1](<../../dozu-ui-service/src/app/[locale]/admin/users/components/Columns.tsx#L1>) | RoleBadge, ActiveBadge, PlanBadge, ActionButtons | 1 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/admin/users/components/UserFilter.tsx:1](<../../dozu-ui-service/src/app/[locale]/admin/users/components/UserFilter.tsx#L1>) | UserFilter | 1 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/class-based/(assignment)/components/CreateAssignment.tsx:1](<../../dozu-ui-service/src/app/[locale]/class-based/(assignment)/components/CreateAssignment.tsx#L1>) | CreateAssignment | 1 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/class-based/(assignment)/components/DeleteAssignmentModal.tsx:1](<../../dozu-ui-service/src/app/[locale]/class-based/(assignment)/components/DeleteAssignmentModal.tsx#L1>) | DeleteAssignmentModal | 4 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/class-based/(assignment)/components/EditAssignment.tsx:1](<../../dozu-ui-service/src/app/[locale]/class-based/(assignment)/components/EditAssignment.tsx#L1>) | EditAssignment | 2 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/class-based/(class-quiz)/components/ClassQuizDraftEditor.tsx:1](<../../dozu-ui-service/src/app/[locale]/class-based/(class-quiz)/components/ClassQuizDraftEditor.tsx#L1>) | ClassQuizDraftEditor | 1 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/class-based/(class-quiz)/components/ClassQuizItem.tsx:1](<../../dozu-ui-service/src/app/[locale]/class-based/(class-quiz)/components/ClassQuizItem.tsx#L1>) | ClassQuizItem | 3 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/class-based/(class-quiz)/components/QuestionCardClass.tsx:1](<../../dozu-ui-service/src/app/[locale]/class-based/(class-quiz)/components/QuestionCardClass.tsx#L1>) | QuestionCardClass | 1 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/class-based/(classwork)/components/ClassworkList.tsx:1](<../../dozu-ui-service/src/app/[locale]/class-based/(classwork)/components/ClassworkList.tsx#L1>) | AssignmentItem, LearningMaterialItem, ClassworkList | 2 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/class-based/(classwork)/components/common/AttachmentItem.tsx:1](<../../dozu-ui-service/src/app/[locale]/class-based/(classwork)/components/common/AttachmentItem.tsx#L1>) | AttachmentItem | 6 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/class-based/(classwork)/components/common/AttachmentItemWithDownload.tsx:1](<../../dozu-ui-service/src/app/[locale]/class-based/(classwork)/components/common/AttachmentItemWithDownload.tsx#L1>) | AttachmentItemWithDownload | 4 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/class-based/(classwork)/components/common/AttachmentItemWithUrl.tsx:1](<../../dozu-ui-service/src/app/[locale]/class-based/(classwork)/components/common/AttachmentItemWithUrl.tsx#L1>) | AttachmentItemWithUrl | 4 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/class-based/(classwork)/components/common/AttachmentsSection.tsx:1](<../../dozu-ui-service/src/app/[locale]/class-based/(classwork)/components/common/AttachmentsSection.tsx#L1>) | AttachmentsSection | 4 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/class-based/(classwork)/components/common/ContentSection.tsx:1](<../../dozu-ui-service/src/app/[locale]/class-based/(classwork)/components/common/ContentSection.tsx#L1>) | ContentSection | 4 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/class-based/(classwork)/components/common/DetailsPanel.tsx:1](<../../dozu-ui-service/src/app/[locale]/class-based/(classwork)/components/common/DetailsPanel.tsx#L1>) | DetailsPanel | 4 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/class-based/(classwork)/components/common/FileItem.tsx:1](<../../dozu-ui-service/src/app/[locale]/class-based/(classwork)/components/common/FileItem.tsx#L1>) | FileItem | 5 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/class-based/(classwork)/components/common/LearningMaterialItem.tsx:1](<../../dozu-ui-service/src/app/[locale]/class-based/(classwork)/components/common/LearningMaterialItem.tsx#L1>) | LearningMaterialItem | 0 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/class-based/(classwork)/components/common/UrlAttachmentItem.tsx:1](<../../dozu-ui-service/src/app/[locale]/class-based/(classwork)/components/common/UrlAttachmentItem.tsx#L1>) | UrlAttachmentItem | 6 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/class-based/(classwork)/components/common/UrlAttachmentModal.tsx:1](<../../dozu-ui-service/src/app/[locale]/class-based/(classwork)/components/common/UrlAttachmentModal.tsx#L1>) | UrlAttachmentModal | 5 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/class-based/(classwork)/components/common/details/AttachmentsViewSection.tsx:1](<../../dozu-ui-service/src/app/[locale]/class-based/(classwork)/components/common/details/AttachmentsViewSection.tsx#L1>) | AttachmentsViewSection | 4 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/class-based/(classwork)/components/common/details/ContentSection.tsx:1](<../../dozu-ui-service/src/app/[locale]/class-based/(classwork)/components/common/details/ContentSection.tsx#L1>) | ContentSection | 4 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/class-based/(classwork)/components/old_ver/ClassworkList.tsx:1](<../../dozu-ui-service/src/app/[locale]/class-based/(classwork)/components/old_ver/ClassworkList.tsx#L1>) | ClassworkItem, LearningMaterialItem, ClassworkList | 0 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/class-based/(classwork)/components/old_ver/ClassworkListCopy.tsx:1](<../../dozu-ui-service/src/app/[locale]/class-based/(classwork)/components/old_ver/ClassworkListCopy.tsx#L1>) | ClassworkItem, ClassworkListCopy | 0 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/class-based/(learning-material)/components/DeleteLearningMaterialModal.tsx:1](<../../dozu-ui-service/src/app/[locale]/class-based/(learning-material)/components/DeleteLearningMaterialModal.tsx#L1>) | DeleteLearningMaterialModal | 3 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/class-based/(learning-material)/components/EditLearningMaterial.tsx:1](<../../dozu-ui-service/src/app/[locale]/class-based/(learning-material)/components/EditLearningMaterial.tsx#L1>) | EditLearningMaterial | 1 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/class-based/[id]/assignments/[assignmentId]/details/components/SubmissionCard.tsx:1](<../../dozu-ui-service/src/app/[locale]/class-based/[id]/assignments/[assignmentId]/details/components/SubmissionCard.tsx#L1>) | SubmissionCard, PrivateCommentsCard, ClassCommentsCard | 1 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/class-based/[id]/dashboard/StudentClassDashboard.tsx:1](<../../dozu-ui-service/src/app/[locale]/class-based/[id]/dashboard/StudentClassDashboard.tsx#L1>) | StudentClassDashboard | 1 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/class-based/[id]/learning-material/[learningMaterialId]/details/components/LearningMaterialCommentSection.tsx:1](<../../dozu-ui-service/src/app/[locale]/class-based/[id]/learning-material/[learningMaterialId]/details/components/LearningMaterialCommentSection.tsx#L1>) | LearningMaterialCommentSection | 2 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/class-based/components/comment/CommentCard.tsx:1](<../../dozu-ui-service/src/app/[locale]/class-based/components/comment/CommentCard.tsx#L1>) | CommentCard | 9 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/class-based/components/comment/CommentInput.tsx:1](<../../dozu-ui-service/src/app/[locale]/class-based/components/comment/CommentInput.tsx#L1>) | CommentInput | 9 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/class-based/components/comment/CommentThread.tsx:1](<../../dozu-ui-service/src/app/[locale]/class-based/components/comment/CommentThread.tsx#L1>) | CommentThread, PAGE_SIZE | 9 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/class-based/components/comment/SkeletonCard.tsx:1](<../../dozu-ui-service/src/app/[locale]/class-based/components/comment/SkeletonCard.tsx#L1>) | CommentSkeleton, CommentListSkeleton, CommentThreadSkeleton | 9 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/class-based/components/common/class/ClassCard.tsx:1](<../../dozu-ui-service/src/app/[locale]/class-based/components/common/class/ClassCard.tsx#L1>) | ClassCard | 2 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/class-based/components/common/class/ClassLibrary.tsx:1](<../../dozu-ui-service/src/app/[locale]/class-based/components/common/class/ClassLibrary.tsx#L1>) | ClassLibrary | 2 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/class-based/components/modal/JoinClassModal.tsx:1](<../../dozu-ui-service/src/app/[locale]/class-based/components/modal/JoinClassModal.tsx#L1>) | JoinClassModal | 1 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/class-based/components/modal/LeaveClassModal.tsx:1](<../../dozu-ui-service/src/app/[locale]/class-based/components/modal/LeaveClassModal.tsx#L1>) | LeaveClassModal | 1 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/class-based/components/ui/class/StudentClassLibrary.tsx:1](<../../dozu-ui-service/src/app/[locale]/class-based/components/ui/class/StudentClassLibrary.tsx#L1>) | StudentClassLibrary | 1 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/class-based/components/ui/classFeed/ClassFeedCard.tsx:1](<../../dozu-ui-service/src/app/[locale]/class-based/components/ui/classFeed/ClassFeedCard.tsx#L1>) | ClassFeedCard | 2 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/class-based/components/ui/classFeed/ClassFeedGroupByTime.tsx:1](<../../dozu-ui-service/src/app/[locale]/class-based/components/ui/classFeed/ClassFeedGroupByTime.tsx#L1>) | ClassFeedGroupedByTime | 2 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/feynman/[topicId]/hooks/useFeynmanService.tsx:1](<../../dozu-ui-service/src/app/[locale]/feynman/[topicId]/hooks/useFeynmanService.tsx#L1>) | (anonymous/local declarations) | 1 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/flashcards/components/BackButton.tsx:1](<../../dozu-ui-service/src/app/[locale]/flashcards/components/BackButton.tsx#L1>) | BackButton | 84 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/flashcards/components/FlashcardEditor.tsx:1](<../../dozu-ui-service/src/app/[locale]/flashcards/components/FlashcardEditor.tsx#L1>) | FlashcardEditor | 84 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/flashcards/components/ImagesPreview.tsx:1](<../../dozu-ui-service/src/app/[locale]/flashcards/components/ImagesPreview.tsx#L1>) | ImagesPreview, ImagesPreviewModal | 84 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/flashcards/learning/components/BacklogCTA.tsx:1](<../../dozu-ui-service/src/app/[locale]/flashcards/learning/components/BacklogCTA.tsx#L1>) | BacklogCTA | 84 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/flashcards/learning/components/NoFlashcardsMessage.tsx:1](<../../dozu-ui-service/src/app/[locale]/flashcards/learning/components/NoFlashcardsMessage.tsx#L1>) | NoFlashcardsMessage | 0 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/flashcards/learning/components/QuickQuizPrompt.tsx:1](<../../dozu-ui-service/src/app/[locale]/flashcards/learning/components/QuickQuizPrompt.tsx#L1>) | QuickQuizPrompt | 84 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/games/brain-chase/components/AnswerBox.tsx:1](<../../dozu-ui-service/src/app/[locale]/games/brain-chase/components/AnswerBox.tsx#L1>) | BASE_SPEED, AnswerBox | 84 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/games/brain-chase/components/GameArea.tsx:1](<../../dozu-ui-service/src/app/[locale]/games/brain-chase/components/GameArea.tsx#L1>) | GameArea | 84 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/games/brain-chase/components/QuestionArea.tsx:1](<../../dozu-ui-service/src/app/[locale]/games/brain-chase/components/QuestionArea.tsx#L1>) | QuestionArea | 84 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/games/brain-chase/components/Setting.tsx:1](<../../dozu-ui-service/src/app/[locale]/games/brain-chase/components/Setting.tsx#L1>) | Setting | 84 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/games/brain-chase/context/brainChaseContext.tsx:1](<../../dozu-ui-service/src/app/[locale]/games/brain-chase/context/brainChaseContext.tsx#L1>) | DEFAULT_SETTINGS, BrainChaseContext, BrainChaseProvider | 84 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/games/memory-match/components/GameStats.tsx:1](<../../dozu-ui-service/src/app/[locale]/games/memory-match/components/GameStats.tsx#L1>) | GameStats | 84 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/games/memory-match/components/GameStatsModal.tsx:1](<../../dozu-ui-service/src/app/[locale]/games/memory-match/components/GameStatsModal.tsx#L1>) | GameStatsModal | 84 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/games/memory-match/components/MemoryCard.tsx:1](<../../dozu-ui-service/src/app/[locale]/games/memory-match/components/MemoryCard.tsx#L1>) | MemoryCard | 84 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/games/memory-match/components/MemoryGameBoard.tsx:1](<../../dozu-ui-service/src/app/[locale]/games/memory-match/components/MemoryGameBoard.tsx#L1>) | MemoryGameBoard | 84 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/games/memory-match/components/MemoryMatchGame.tsx:1](<../../dozu-ui-service/src/app/[locale]/games/memory-match/components/MemoryMatchGame.tsx#L1>) | MemoryMatchGame | 1 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/games/memory-match/context/MemoryMatchContext.tsx:1](<../../dozu-ui-service/src/app/[locale]/games/memory-match/context/MemoryMatchContext.tsx#L1>) | DEFAULT_SETTINGS, DEFAULT_STATS, DEFAULT_BATCH_STRATEGY, MemoryMatchContext, MemoryMatchProvider | 84 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/generate/components/CardImport.tsx:1](<../../dozu-ui-service/src/app/[locale]/generate/components/CardImport.tsx#L1>) | CardImport | 84 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/generate/components/ContentGenerationPreview.tsx:1](<../../dozu-ui-service/src/app/[locale]/generate/components/ContentGenerationPreview.tsx#L1>) | ContentGenerationPreview | 84 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/generate/components/ContentRender.tsx:1](<../../dozu-ui-service/src/app/[locale]/generate/components/ContentRender.tsx#L1>) | ContentRender, FlashcardRenderer, QuestionRenderer, MindmapRenderer | 84 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/generate/components/GeneratePage.tsx:1](<../../dozu-ui-service/src/app/[locale]/generate/components/GeneratePage.tsx#L1>) | GeneratePage | 84 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/generate/components/ImportPanel.tsx:1](<../../dozu-ui-service/src/app/[locale]/generate/components/ImportPanel.tsx#L1>) | CHUNK_SIZE, ImportPanel | 0 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/generate/components/detail-extract/ContentDetailView.tsx:1](<../../dozu-ui-service/src/app/[locale]/generate/components/detail-extract/ContentDetailView.tsx#L1>) | ContentDetailView | 0 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/generate/components/detail-extract/WebsiteView.tsx:1](<../../dozu-ui-service/src/app/[locale]/generate/components/detail-extract/WebsiteView.tsx#L1>) | WebsiteView | 0 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/generate/components/import/Import.tsx:1](<../../dozu-ui-service/src/app/[locale]/generate/components/import/Import.tsx#L1>) | Import | 84 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/generate/components/import/components/FileTab.tsx:1](<../../dozu-ui-service/src/app/[locale]/generate/components/import/components/FileTab.tsx#L1>) | FileTab | 84 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/generate/components/import/components/FileUploadArea.tsx:1](<../../dozu-ui-service/src/app/[locale]/generate/components/import/components/FileUploadArea.tsx#L1>) | FileUploadArea | 84 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/generate/components/import/components/LoadingOverlay.tsx:1](<../../dozu-ui-service/src/app/[locale]/generate/components/import/components/LoadingOverlay.tsx#L1>) | LoadingOverlay | 84 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/generate/components/import/components/MediaTab.tsx:1](<../../dozu-ui-service/src/app/[locale]/generate/components/import/components/MediaTab.tsx#L1>) | MediaTab | 84 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/generate/components/import/components/TextUrlContentTab.tsx:1](<../../dozu-ui-service/src/app/[locale]/generate/components/import/components/TextUrlContentTab.tsx#L1>) | TabContent | 84 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/generate/components/process/NavigationAlertDialog.tsx:1](<../../dozu-ui-service/src/app/[locale]/generate/components/process/NavigationAlertDialog.tsx#L1>) | NavigationAlertDialog | 0 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/generate/components/process/Process.tsx:1](<../../dozu-ui-service/src/app/[locale]/generate/components/process/Process.tsx#L1>) | Process | 0 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/generate/components/process/ProcessGenerate.tsx:1](<../../dozu-ui-service/src/app/[locale]/generate/components/process/ProcessGenerate.tsx#L1>) | ProcessGenerate | 0 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/generate/components/steps/Final.tsx:1](<../../dozu-ui-service/src/app/[locale]/generate/components/steps/Final.tsx#L1>) | Final | 0 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/generate/components/steps/FlashcardViewer.tsx:1](<../../dozu-ui-service/src/app/[locale]/generate/components/steps/FlashcardViewer.tsx#L1>) | FlashcardViewer | 0 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/generate/components/steps/SelectMethod.tsx:1](<../../dozu-ui-service/src/app/[locale]/generate/components/steps/SelectMethod.tsx#L1>) | SelectMethod | 84 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/generate/components/steps/SelectMethodImport.tsx:1](<../../dozu-ui-service/src/app/[locale]/generate/components/steps/SelectMethodImport.tsx#L1>) | SelectMethodImport | 0 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/generate/detail-extract/components/ContentDetailView.tsx:1](<../../dozu-ui-service/src/app/[locale]/generate/detail-extract/components/ContentDetailView.tsx#L1>) | ContentDetailView | 84 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/generate/detail-extract/components/WebsiteView.tsx:1](<../../dozu-ui-service/src/app/[locale]/generate/detail-extract/components/WebsiteView.tsx#L1>) | WebsiteView | 0 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/generate/hooks/useReaderFile.tsx:1](<../../dozu-ui-service/src/app/[locale]/generate/hooks/useReaderFile.tsx#L1>) | (anonymous/local declarations) | 84 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/generate/hooks/useReduxStore.tsx:1](<../../dozu-ui-service/src/app/[locale]/generate/hooks/useReduxStore.tsx#L1>) | (anonymous/local declarations) | 84 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/generate/hooks/useUploadConvertFileFormat.tsx:1](<../../dozu-ui-service/src/app/[locale]/generate/hooks/useUploadConvertFileFormat.tsx#L1>) | (anonymous/local declarations) | 84 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/home/components/ContentCard.tsx:1](<../../dozu-ui-service/src/app/[locale]/home/components/ContentCard.tsx#L1>) | ContentCard | 0 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/home/components/CoreActionCards.tsx:1](<../../dozu-ui-service/src/app/[locale]/home/components/CoreActionCards.tsx#L1>) | CoreActionCards, IconComponent | 0 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/home/components/CurrentProcessLearning.tsx:1](<../../dozu-ui-service/src/app/[locale]/home/components/CurrentProcessLearning.tsx#L1>) | CurrentProcessLearning | 1 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/home/components/GuestLibraryPlaceholder.tsx:1](<../../dozu-ui-service/src/app/[locale]/home/components/GuestLibraryPlaceholder.tsx#L1>) | GuestLibraryPlaceholder | 1 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/home/components/HeroSection.tsx:1](<../../dozu-ui-service/src/app/[locale]/home/components/HeroSection.tsx#L1>) | HeroSection | 1 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/home/components/SuggestContent.tsx:1](<../../dozu-ui-service/src/app/[locale]/home/components/SuggestContent.tsx#L1>) | SuggestContent, RecommendationCard | 0 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/home/components/Title.tsx:1](<../../dozu-ui-service/src/app/[locale]/home/components/Title.tsx#L1>) | Title | 1 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/home/components/actions/Actions.tsx:1](<../../dozu-ui-service/src/app/[locale]/home/components/actions/Actions.tsx#L1>) | ActionsContent, Actions | 1 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/home/components/actions/MediaModal.tsx:1](<../../dozu-ui-service/src/app/[locale]/home/components/actions/MediaModal.tsx#L1>) | MediaModal | 1 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/home/components/actions/PasteLinkModal.tsx:1](<../../dozu-ui-service/src/app/[locale]/home/components/actions/PasteLinkModal.tsx#L1>) | PasteLinkModal, DEFAULT_TITLE | 1 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/home/components/actions/UploadModal.tsx:1](<../../dozu-ui-service/src/app/[locale]/home/components/actions/UploadModal.tsx#L1>) | UploadModal | 1 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/home/components/actions/components/FileUploadArea.tsx:1](<../../dozu-ui-service/src/app/[locale]/home/components/actions/components/FileUploadArea.tsx#L1>) | FileUploadArea | 0 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/home/components/actions/components/record/RecordTab.tsx:1](<../../dozu-ui-service/src/app/[locale]/home/components/actions/components/record/RecordTab.tsx#L1>) | AcquiringMedia, AUDIO_RECORD_EXT, RecordTab | 1 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/home/components/actions/components/upload/RenderProgress.tsx:1](<../../dozu-ui-service/src/app/[locale]/home/components/actions/components/upload/RenderProgress.tsx#L1>) | RenderProgress | 1 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/home/components/actions/components/upload/UploadMediaFileInput.tsx:1](<../../dozu-ui-service/src/app/[locale]/home/components/actions/components/upload/UploadMediaFileInput.tsx#L1>) | UploadMediaFileInput | 1 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/home/components/actions/context/ActionContext.tsx:1](<../../dozu-ui-service/src/app/[locale]/home/components/actions/context/ActionContext.tsx#L1>) | ActionContext, ActionProvider | 1 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/home/components/actions/hooks/useToastManager.tsx:1](<../../dozu-ui-service/src/app/[locale]/home/components/actions/hooks/useToastManager.tsx#L1>) | (anonymous/local declarations) | 1 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/home/components/actions/hooks/useUploadConvertFileFormat.tsx:1](<../../dozu-ui-service/src/app/[locale]/home/components/actions/hooks/useUploadConvertFileFormat.tsx#L1>) | (anonymous/local declarations) | 1 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/home/components/actions/hooks/useUploadMediaFile.tsx:1](<../../dozu-ui-service/src/app/[locale]/home/components/actions/hooks/useUploadMediaFile.tsx#L1>) | (anonymous/local declarations) | 1 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/home/components/package/ListTopicUnAssign.tsx:1](<../../dozu-ui-service/src/app/[locale]/home/components/package/ListTopicUnAssign.tsx#L1>) | DEFAULT_LIMIT, INIT_OFFSET, ListTopicUnAssign | 84 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/home/components/package/TreeView.tsx:1](<../../dozu-ui-service/src/app/[locale]/home/components/package/TreeView.tsx#L1>) | TreeView | 84 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/mindmap/components/CustomReactFlowNode.tsx:1](<../../dozu-ui-service/src/app/[locale]/mindmap/components/CustomReactFlowNode.tsx#L1>) | CustomReactFlowNode | 5 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/mindmap/components/CustomReactFlowPreviewNode.tsx:1](<../../dozu-ui-service/src/app/[locale]/mindmap/components/CustomReactFlowPreviewNode.tsx#L1>) | CustomReactFlowPreviewNode | 84 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/mindmap/components/FileSheet.tsx:1](<../../dozu-ui-service/src/app/[locale]/mindmap/components/FileSheet.tsx#L1>) | FileSheet | 4 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/mindmap/components/FloatingConnectionLine.tsx:1](<../../dozu-ui-service/src/app/[locale]/mindmap/components/FloatingConnectionLine.tsx#L1>) | FloatingConnectionLine | 0 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/mindmap/components/FloatingEdge.tsx:1](<../../dozu-ui-service/src/app/[locale]/mindmap/components/FloatingEdge.tsx#L1>) | FloatingEdge | 84 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/mindmap/components/GenerateMindmapCard.tsx:1](<../../dozu-ui-service/src/app/[locale]/mindmap/components/GenerateMindmapCard.tsx#L1>) | GenerateMindmapCard | 84 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/mindmap/components/MindmapButtonsPanel.tsx:1](<../../dozu-ui-service/src/app/[locale]/mindmap/components/MindmapButtonsPanel.tsx#L1>) | MindmapButtonsPanel | 4 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/mindmap/components/NodeSheetViewOnly.tsx:1](<../../dozu-ui-service/src/app/[locale]/mindmap/components/NodeSheetViewOnly.tsx#L1>) | NodeSheetViewOnly | 2 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/mindmap/components/PreviewMindmap.tsx:1](<../../dozu-ui-service/src/app/[locale]/mindmap/components/PreviewMindmap.tsx#L1>) | PreviewMindmap | 84 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/mindmap/components/ReactFlowNodeInClass.tsx:1](<../../dozu-ui-service/src/app/[locale]/mindmap/components/ReactFlowNodeInClass.tsx#L1>) | ReactFlowNodeInClass | 2 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/mindmap/components/ReferenceDocumentViaPage.tsx:1](<../../dozu-ui-service/src/app/[locale]/mindmap/components/ReferenceDocumentViaPage.tsx#L1>) | ReferenceDocumentViaPage | 3 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/mindmap/components/RoadmapButtonPanel.tsx:1](<../../dozu-ui-service/src/app/[locale]/mindmap/components/RoadmapButtonPanel.tsx#L1>) | RoadmapButtonPanel | 4 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/mindmap/components/RoadmapItem.tsx:1](<../../dozu-ui-service/src/app/[locale]/mindmap/components/RoadmapItem.tsx#L1>) | RoadmapItem | 3 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/mindmap/components/RoadmapList.tsx:1](<../../dozu-ui-service/src/app/[locale]/mindmap/components/RoadmapList.tsx#L1>) | RoadmapList | 3 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/mindmap/components/SimpleFloatingEdge.tsx:1](<../../dozu-ui-service/src/app/[locale]/mindmap/components/SimpleFloatingEdge.tsx#L1>) | SimpleFloatingEdge | 0 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/mindmap/components/buttons/AddChildNodeButton.tsx:1](<../../dozu-ui-service/src/app/[locale]/mindmap/components/buttons/AddChildNodeButton.tsx#L1>) | AddChildNodeButton | 5 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/mindmap/components/buttons/DeleteNodeButton.tsx:1](<../../dozu-ui-service/src/app/[locale]/mindmap/components/buttons/DeleteNodeButton.tsx#L1>) | DeleteNodeButton | 5 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/mindmap/components/buttons/ExportToCSVButton.tsx:1](<../../dozu-ui-service/src/app/[locale]/mindmap/components/buttons/ExportToCSVButton.tsx#L1>) | ExportToCSVButton | 4 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/mindmap/components/buttons/ImportButton.tsx:1](<../../dozu-ui-service/src/app/[locale]/mindmap/components/buttons/ImportButton.tsx#L1>) | ImportButton | 4 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/mindmap/components/buttons/OutlineTree.tsx:1](<../../dozu-ui-service/src/app/[locale]/mindmap/components/buttons/OutlineTree.tsx#L1>) | OutlineTree | 0 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/mindmap/components/buttons/PaletteButton.tsx:1](<../../dozu-ui-service/src/app/[locale]/mindmap/components/buttons/PaletteButton.tsx#L1>) | PaletteButton | 5 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/mindmap/components/buttons/RoadmapButton.tsx:1](<../../dozu-ui-service/src/app/[locale]/mindmap/components/buttons/RoadmapButton.tsx#L1>) | RoadmapButton | 0 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/mindmap/context/MindMapContext.tsx:1](<../../dozu-ui-service/src/app/[locale]/mindmap/context/MindMapContext.tsx#L1>) | MindMapContext, MindMapProvider | 84 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/onboarding/components/OnboardingCompleteCard.tsx:1](<../../dozu-ui-service/src/app/[locale]/onboarding/components/OnboardingCompleteCard.tsx#L1>) | OnboardingCompleteCard | 1 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/onboarding/components/SchedulingMethodStepCard.tsx:1](<../../dozu-ui-service/src/app/[locale]/onboarding/components/SchedulingMethodStepCard.tsx#L1>) | SchedulingMethodStepCard | 0 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/onboarding/components/StudyDurationStepCard.tsx:1](<../../dozu-ui-service/src/app/[locale]/onboarding/components/StudyDurationStepCard.tsx#L1>) | StudyDurationStepCard | 1 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/onboarding/components/StudyMethodStepCard.tsx:1](<../../dozu-ui-service/src/app/[locale]/onboarding/components/StudyMethodStepCard.tsx#L1>) | StudyMethodStepCard | 1 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/onboarding/components/TopicTagStepCard.tsx:1](<../../dozu-ui-service/src/app/[locale]/onboarding/components/TopicTagStepCard.tsx#L1>) | TopicTagStepCard | 1 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/onboarding/components/WelcomeStepCard.tsx:1](<../../dozu-ui-service/src/app/[locale]/onboarding/components/WelcomeStepCard.tsx#L1>) | WelcomeStepCard | 1 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/profile/components/AccountSettings.tsx:1](<../../dozu-ui-service/src/app/[locale]/profile/components/AccountSettings.tsx#L1>) | AccountSettings | 2 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/profile/components/AvatarManager.tsx:1](<../../dozu-ui-service/src/app/[locale]/profile/components/AvatarManager.tsx#L1>) | AvatarManager | 2 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/profile/components/ChangePassword.tsx:1](<../../dozu-ui-service/src/app/[locale]/profile/components/ChangePassword.tsx#L1>) | ChangePassword | 2 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/profile/components/LoadingState.tsx:1](<../../dozu-ui-service/src/app/[locale]/profile/components/LoadingState.tsx#L1>) | LoadingState | 2 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/profile/components/ProfileHeader.tsx:1](<../../dozu-ui-service/src/app/[locale]/profile/components/ProfileHeader.tsx#L1>) | ProfileHeader | 2 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/profile/components/ProfilePage.tsx:1](<../../dozu-ui-service/src/app/[locale]/profile/components/ProfilePage.tsx#L1>) | ProfilePage | 0 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/profile/components/SettingsTab.tsx:1](<../../dozu-ui-service/src/app/[locale]/profile/components/SettingsTab.tsx#L1>) | SettingsTab | 2 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/profile/components/TransactionHistory.tsx:1](<../../dozu-ui-service/src/app/[locale]/profile/components/TransactionHistory.tsx#L1>) | TransactionHistory | 2 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/progress/components/DailyStudyBarChart.tsx:1](<../../dozu-ui-service/src/app/[locale]/progress/components/DailyStudyBarChart.tsx#L1>) | DailyStudyBarChart | 1 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/progress/components/LearningMethodsPieChart.tsx:1](<../../dozu-ui-service/src/app/[locale]/progress/components/LearningMethodsPieChart.tsx#L1>) | COLORS, LearningMethodsPieChart | 1 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/progress/components/ProgressDashboard.tsx:1](<../../dozu-ui-service/src/app/[locale]/progress/components/ProgressDashboard.tsx#L1>) | ProgressDashboard, XLSX | 1 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/progress/components/ProgressManager.tsx:1](<../../dozu-ui-service/src/app/[locale]/progress/components/ProgressManager.tsx#L1>) | ProgressManager | 0 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/question/components/QuestionCard.tsx:1](<../../dozu-ui-service/src/app/[locale]/question/components/QuestionCard.tsx#L1>) | QUESTION_TYPES, QuestionCard | 84 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/question/components/QuestionEditor.tsx:1](<../../dozu-ui-service/src/app/[locale]/question/components/QuestionEditor.tsx#L1>) | QuestionEditor | 84 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/quiz/components/ConfirmSubmitDialog.tsx:1](<../../dozu-ui-service/src/app/[locale]/quiz/components/ConfirmSubmitDialog.tsx#L1>) | ConfirmSubmitDialog | 1 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/quiz/components/CreateQuizModal.tsx:1](<../../dozu-ui-service/src/app/[locale]/quiz/components/CreateQuizModal.tsx#L1>) | CreateQuizModal | 0 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/quiz/components/QuizCard.tsx:1](<../../dozu-ui-service/src/app/[locale]/quiz/components/QuizCard.tsx#L1>) | QuizCard | 1 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/quiz/components/QuizOnboarding.tsx:1](<../../dozu-ui-service/src/app/[locale]/quiz/components/QuizOnboarding.tsx#L1>) | QuizOnboarding, QuizTypeRow | 0 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/quiz/components/QuizQuestion.tsx:1](<../../dozu-ui-service/src/app/[locale]/quiz/components/QuizQuestion.tsx#L1>) | QuizQuestion | 5 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/quiz/components/QuizResult.tsx:1](<../../dozu-ui-service/src/app/[locale]/quiz/components/QuizResult.tsx#L1>) | QuizResult | 1 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/quiz/components/QuizResultDetail.tsx:1](<../../dozu-ui-service/src/app/[locale]/quiz/components/QuizResultDetail.tsx#L1>) | QuizResultDetail | 4 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/quiz/components/QuizTypeSelector.tsx:1](<../../dozu-ui-service/src/app/[locale]/quiz/components/QuizTypeSelector.tsx#L1>) | QuizTypeSelector | 0 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/request-teacher/components/RequestForm.tsx:1](<../../dozu-ui-service/src/app/[locale]/request-teacher/components/RequestForm.tsx#L1>) | RequestForm | 2 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/request-teacher/components/RequestStatus.tsx:1](<../../dozu-ui-service/src/app/[locale]/request-teacher/components/RequestStatus.tsx#L1>) | TeacherRequestStatus | 2 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/schedule/components/CalendarView.tsx:1](<../../dozu-ui-service/src/app/[locale]/schedule/components/CalendarView.tsx#L1>) | CalendarView | 4 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/schedule/components/EditDialog.tsx:1](<../../dozu-ui-service/src/app/[locale]/schedule/components/EditDialog.tsx#L1>) | EditDialog | 0 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/setting/components/SettingSidebar.tsx:1](<../../dozu-ui-service/src/app/[locale]/setting/components/SettingSidebar.tsx#L1>) | SettingSidebar | 2 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/setting/schedule-setup/components/SetupForm.tsx:1](<../../dozu-ui-service/src/app/[locale]/setting/schedule-setup/components/SetupForm.tsx#L1>) | SetupForm | 1 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/stats/components/DailyStudyChart.tsx:1](<../../dozu-ui-service/src/app/[locale]/stats/components/DailyStudyChart.tsx#L1>) | DailyStudyChart | 1 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/stats/components/KeyMetricCard.tsx:1](<../../dozu-ui-service/src/app/[locale]/stats/components/KeyMetricCard.tsx#L1>) | KeyMetricCard | 1 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/stats/components/LearningMethodsChart.tsx:1](<../../dozu-ui-service/src/app/[locale]/stats/components/LearningMethodsChart.tsx#L1>) | LearningMethodsChart | 1 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/stats/components/LearningProgress.tsx:1](<../../dozu-ui-service/src/app/[locale]/stats/components/LearningProgress.tsx#L1>) | LearningProgress | 1 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/stats/components/ProgressStatistics.tsx:1](<../../dozu-ui-service/src/app/[locale]/stats/components/ProgressStatistics.tsx#L1>) | ProgressStatistics | 0 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/stats/components/ReportFooter.tsx:1](<../../dozu-ui-service/src/app/[locale]/stats/components/ReportFooter.tsx#L1>) | ReportFooter | 1 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/stats/components/StatsLearningMethods.tsx:1](<../../dozu-ui-service/src/app/[locale]/stats/components/StatsLearningMethods.tsx#L1>) | StatsLearningMethods | 1 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/stats/components/StatsOverview.tsx:1](<../../dozu-ui-service/src/app/[locale]/stats/components/StatsOverview.tsx#L1>) | StatsOverview | 1 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/stats/components/WeeklyComparison.tsx:1](<../../dozu-ui-service/src/app/[locale]/stats/components/WeeklyComparison.tsx#L1>) | WeeklyComparison | 0 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/teacher/class-based/[id]/assignments/[assignmentId]/details/components/CommentInput.tsx:1](<../../dozu-ui-service/src/app/[locale]/teacher/class-based/[id]/assignments/[assignmentId]/details/components/CommentInput.tsx#L1>) | CommentInput | 4 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/teacher/class-based/[id]/assignments/[assignmentId]/details/components/CommentList.tsx:1](<../../dozu-ui-service/src/app/[locale]/teacher/class-based/[id]/assignments/[assignmentId]/details/components/CommentList.tsx#L1>) | (anonymous/local declarations) | 0 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/teacher/class-based/[id]/assignments/[assignmentId]/details/components/CommentSection.tsx:1](<../../dozu-ui-service/src/app/[locale]/teacher/class-based/[id]/assignments/[assignmentId]/details/components/CommentSection.tsx#L1>) | CommentSection | 2 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/teacher/class-based/[id]/assignments/[assignmentId]/details/components/PrivateCommentSection.tsx:1](<../../dozu-ui-service/src/app/[locale]/teacher/class-based/[id]/assignments/[assignmentId]/details/components/PrivateCommentSection.tsx#L1>) | TeacherPrivateCommentSection | 1 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/teacher/class-based/[id]/assignments/[assignmentId]/details/components/SubmissionsPage.tsx:1](<../../dozu-ui-service/src/app/[locale]/teacher/class-based/[id]/assignments/[assignmentId]/details/components/SubmissionsPage.tsx#L1>) | StudentItem, SubmissionsOverview, SubmissionItem, SubmissionsPage | 1 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/teacher/class-based/[id]/dashboard/TeacherClassDashboard.tsx:1](<../../dozu-ui-service/src/app/[locale]/teacher/class-based/[id]/dashboard/TeacherClassDashboard.tsx#L1>) | TeacherClassDashboard | 1 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/teacher/class-based/[id]/learning-material/components/CreateLearningMaterial.tsx:1](<../../dozu-ui-service/src/app/[locale]/teacher/class-based/[id]/learning-material/components/CreateLearningMaterial.tsx#L1>) | DEFAULT_TOTAL_GRADE, DEFAULT_ASSIGNMENT_STATUS, CreateLearningMaterial | 1 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/teacher/class-based/[id]/students/components/StreakStatusBadge.tsx:1](<../../dozu-ui-service/src/app/[locale]/teacher/class-based/[id]/students/components/StreakStatusBadge.tsx#L1>) | StreakStatusBadge | 1 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/teacher/class-based/[id]/students/components/StudentList.tsx:1](<../../dozu-ui-service/src/app/[locale]/teacher/class-based/[id]/students/components/StudentList.tsx#L1>) | StudentList | 1 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/teacher/class-based/[id]/students/components/StudentProfileModal.tsx:1](<../../dozu-ui-service/src/app/[locale]/teacher/class-based/[id]/students/components/StudentProfileModal.tsx#L1>) | StudentProfileModal | 1 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/teacher/feeds/components/modals/CreateFeedModal.tsx:1](<../../dozu-ui-service/src/app/[locale]/teacher/feeds/components/modals/CreateFeedModal.tsx#L1>) | CreateFeedModal | 84 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/teacher/feeds/components/modals/DeleteFeedModal.tsx:1](<../../dozu-ui-service/src/app/[locale]/teacher/feeds/components/modals/DeleteFeedModal.tsx#L1>) | DeleteFeedModal | 1 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/teacher/feeds/components/modals/UpdateFeedModal.tsx:1](<../../dozu-ui-service/src/app/[locale]/teacher/feeds/components/modals/UpdateFeedModal.tsx#L1>) | UpdateFeedModal | 84 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/teacher/feeds/hooks/useCreateFeed.tsx:1](<../../dozu-ui-service/src/app/[locale]/teacher/feeds/hooks/useCreateFeed.tsx#L1>) | (anonymous/local declarations) | 84 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/teacher/feeds/hooks/useDeleteFeed.tsx:1](<../../dozu-ui-service/src/app/[locale]/teacher/feeds/hooks/useDeleteFeed.tsx#L1>) | (anonymous/local declarations) | 84 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/teacher/feeds/hooks/useFeeds.tsx:1](<../../dozu-ui-service/src/app/[locale]/teacher/feeds/hooks/useFeeds.tsx#L1>) | (anonymous/local declarations) | 84 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/teacher/feeds/hooks/useUpdateFeed.tsx:1](<../../dozu-ui-service/src/app/[locale]/teacher/feeds/hooks/useUpdateFeed.tsx#L1>) | (anonymous/local declarations) | 84 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/teacher/home/components/modal/CreateClassModal.tsx:1](<../../dozu-ui-service/src/app/[locale]/teacher/home/components/modal/CreateClassModal.tsx#L1>) | CreateClassModal | 1 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/teacher/home/components/modal/UpdateClassModal.tsx:1](<../../dozu-ui-service/src/app/[locale]/teacher/home/components/modal/UpdateClassModal.tsx#L1>) | UpdateClassModal | 1 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/teacher/home/components/ui/TeacherClassLibrary.tsx:1](<../../dozu-ui-service/src/app/[locale]/teacher/home/components/ui/TeacherClassLibrary.tsx#L1>) | TeacherClassLibrary | 1 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/common/LoadingNode.tsx:1](<../../dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/common/LoadingNode.tsx#L1>) | LoadingNode | 4 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/flashcard/Flashcard.tsx:1](<../../dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/flashcard/Flashcard.tsx#L1>) | Flashcard | 84 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/flashcard/FlashcardContent.tsx:1](<../../dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/flashcard/FlashcardContent.tsx#L1>) | FlashcardContent | 84 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/flashcard/FlashcardDetailsModal.tsx:1](<../../dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/flashcard/FlashcardDetailsModal.tsx#L1>) | FlashcardDetailsModal | 84 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/flashcard/browse/FlashcardStreamPreview.tsx:1](<../../dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/flashcard/browse/FlashcardStreamPreview.tsx#L1>) | FlashcardStreamPreview | 84 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/flashcard/browse/FlashcardsBrowse.tsx:1](<../../dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/flashcard/browse/FlashcardsBrowse.tsx#L1>) | FlashcardsBrowse | 84 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/flashcard/browse/GenerateFlashcards.tsx:1](<../../dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/flashcard/browse/GenerateFlashcards.tsx#L1>) | GenerateFlashcards | 84 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/flashcard/browse/StudyControls.tsx:1](<../../dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/flashcard/browse/StudyControls.tsx#L1>) | StudyControls | 84 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/flashcard/browse/TopicFlashcardsBrowse.tsx:1](<../../dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/flashcard/browse/TopicFlashcardsBrowse.tsx#L1>) | TopicFlashcardsBrowse | 84 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/flashcard/browse/ViewModeToggle.tsx:1](<../../dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/flashcard/browse/ViewModeToggle.tsx#L1>) | ViewModeToggle | 84 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/flashcard/edit/FlashcardsEdit.tsx:1](<../../dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/flashcard/edit/FlashcardsEdit.tsx#L1>) | FlashcardsEdit | 84 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/flashcard/edit/TopicFlashcardsEdit.tsx:1](<../../dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/flashcard/edit/TopicFlashcardsEdit.tsx#L1>) | TopicFlashcardsEdit | 84 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/flashcard/flashcard-image/EditImage.tsx:1](<../../dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/flashcard/flashcard-image/EditImage.tsx#L1>) | SelectImage, EditImage | 84 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/flashcard/flashcard-image/EditImageModal.tsx:1](<../../dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/flashcard/flashcard-image/EditImageModal.tsx#L1>) | EditImageModal | 84 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/flashcard/flashcard-image/SearchTab.tsx:1](<../../dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/flashcard/flashcard-image/SearchTab.tsx#L1>) | QueryItem, SearchTab | 84 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/flashcard/flashcard-image/UploadTab.tsx:1](<../../dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/flashcard/flashcard-image/UploadTab.tsx#L1>) | UploadTab | 84 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/flashcard/import/FlashcardImportCsv.tsx:1](<../../dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/flashcard/import/FlashcardImportCsv.tsx#L1>) | FlashcardImportCsv | 84 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/flashcard/import/FlashcardImportModal.tsx:1](<../../dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/flashcard/import/FlashcardImportModal.tsx#L1>) | FlashcardImportModal | 84 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/flashcard/import/FlashcardImportText.tsx:1](<../../dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/flashcard/import/FlashcardImportText.tsx#L1>) | FlashcardImportText | 84 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/flashcard/import/FlashcardPreview.tsx:1](<../../dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/flashcard/import/FlashcardPreview.tsx#L1>) | FlashcardsPreview | 84 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/flashcard/learning/LearningCard.tsx:1](<../../dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/flashcard/learning/LearningCard.tsx#L1>) | LearningCard | 84 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/flashcard/learning/LearningFlashcards.tsx:1](<../../dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/flashcard/learning/LearningFlashcards.tsx#L1>) | LearningFlashcards | 84 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/flashcard/learning/LearningFlashcardsEmptyState.tsx:1](<../../dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/flashcard/learning/LearningFlashcardsEmptyState.tsx#L1>) | LearningFlashcardsEmptyState | 84 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/flashcard/node/EmptyNodeFlashcards.tsx:1](<../../dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/flashcard/node/EmptyNodeFlashcards.tsx#L1>) | EmptyNodeFlashcards | 3 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/flashcard/node/FlashcardsPanelControls.tsx:1](<../../dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/flashcard/node/FlashcardsPanelControls.tsx#L1>) | FlashcardsPanelControls | 84 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/flashcard/node/MultiNodeFlashcardsPreview.tsx:1](<../../dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/flashcard/node/MultiNodeFlashcardsPreview.tsx#L1>) | MultiNodeFlashcardsPreview | 3 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/flashcard/node/MultiNodeGeneratePanel.tsx:1](<../../dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/flashcard/node/MultiNodeGeneratePanel.tsx#L1>) | MultiNodeGeneratePanel | 3 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/flashcard/node/NodeFlashcardsBrowse.tsx:1](<../../dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/flashcard/node/NodeFlashcardsBrowse.tsx#L1>) | NodeFlashcardsBrowse | 3 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/flashcard/node/NodeFlashcardsEdit.tsx:1](<../../dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/flashcard/node/NodeFlashcardsEdit.tsx#L1>) | NodeFlashcardsEdit | 3 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/flashcard/node/NodeFlashcardsLearning.tsx:1](<../../dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/flashcard/node/NodeFlashcardsLearning.tsx#L1>) | NodeFlashcardsLearning | 3 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/flashcard/node/NodeFlashcardsLinker.tsx:1](<../../dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/flashcard/node/NodeFlashcardsLinker.tsx#L1>) | NodeFlashcardsLinker | 3 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/flashcard/node/reference/MediaSegmentReferenceEdit.tsx:1](<../../dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/flashcard/node/reference/MediaSegmentReferenceEdit.tsx#L1>) | MediaSegmentReferenceItem, MediaSegmentReferenceEdit | 3 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/flashcard/node/reference/PdfReferenceEdit.tsx:1](<../../dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/flashcard/node/reference/PdfReferenceEdit.tsx#L1>) | PdfReferenceItem, PdfReferenceEdit | 3 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/flashcard/node/reference/ReferenceEdit.tsx:1](<../../dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/flashcard/node/reference/ReferenceEdit.tsx#L1>) | ReferenceEdit | 3 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/flashcard/settings/FlashcardSettings.tsx:1](<../../dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/flashcard/settings/FlashcardSettings.tsx#L1>) | SettingsField, FlashcardSettings | 84 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/games/BrainChaseGame.tsx:1](<../../dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/games/BrainChaseGame.tsx#L1>) | BrainChaseGame | 84 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/games/GamesContent.tsx:1](<../../dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/games/GamesContent.tsx#L1>) | GamesContent | 84 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/games/MemoryMatchGame.tsx:1](<../../dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/games/MemoryMatchGame.tsx#L1>) | MemoryMatchGame | 84 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/generate/CustomizeProperties.tsx:1](<../../dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/generate/CustomizeProperties.tsx#L1>) | CustomizeProperties, TypeButton, DifficultyButton | 84 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/generate/DefaultGenerateButton.tsx:1](<../../dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/generate/DefaultGenerateButton.tsx#L1>) | DefaultGenerateButton | 3 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/generate/Generate.tsx:1](<../../dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/generate/Generate.tsx#L1>) | DEFAULT_METHOD, GenerateContent, LoadingDefault, Generate | 84 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/material/LearningMaterial.tsx:1](<../../dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/material/LearningMaterial.tsx#L1>) | LearningMaterial | 3 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/material/SelectMenu.tsx:1](<../../dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/material/SelectMenu.tsx#L1>) | SelectMenu | 3 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/material/common/transcript/TranscriptViewer.tsx:1](<../../dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/material/common/transcript/TranscriptViewer.tsx#L1>) | TranscriptViewer | 3 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/material/media/AudioLearningMaterial.tsx:1](<../../dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/material/media/AudioLearningMaterial.tsx#L1>) | AudioLearningMaterial | 3 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/material/media/video/VideoLearningMaterial.tsx:1](<../../dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/material/media/video/VideoLearningMaterial.tsx#L1>) | VideoLearningMaterial | 3 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/material/media/video/VideoPlayer.tsx:1](<../../dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/material/media/video/VideoPlayer.tsx#L1>) | VideoPlayer | 3 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/material/pdf/CustomPDFViewer.tsx:1](<../../dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/material/pdf/CustomPDFViewer.tsx#L1>) | PdfToolbar, CustomPDFViewer | 3 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/material/pdf/PDFLearningMaterial.tsx:1](<../../dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/material/pdf/PDFLearningMaterial.tsx#L1>) | PDFLearningMaterial | 3 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/material/youtube/YoutubeLearningMaterial.tsx:1](<../../dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/material/youtube/YoutubeLearningMaterial.tsx#L1>) | YoutubeLearningMaterial | 3 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/material/youtube/YoutubePlayer.tsx:1](<../../dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/material/youtube/YoutubePlayer.tsx#L1>) | YoutubePlayer | 3 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/mindmap/MindmapContent.tsx:1](<../../dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/mindmap/MindmapContent.tsx#L1>) | MindmapContent | 3 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/mindmap/components/ColorThemeSelection.tsx:1](<../../dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/mindmap/components/ColorThemeSelection.tsx#L1>) | ThemeItem, ColorThemeSelection | 4 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/mindmap/components/CustomizedGenerateOptions.tsx:1](<../../dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/mindmap/components/CustomizedGenerateOptions.tsx#L1>) | CustomizedGenerateOptions | 3 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/mindmap/components/MindmapGenerate.tsx:1](<../../dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/mindmap/components/MindmapGenerate.tsx#L1>) | MindmapGenerate | 3 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/mindmap/components/Roadmap.tsx:1](<../../dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/mindmap/components/Roadmap.tsx#L1>) | Roadmap | 3 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/mindmap/node/NodeDetails.tsx:1](<../../dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/mindmap/node/NodeDetails.tsx#L1>) | NodeDetails | 3 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/note/CommandsView.tsx:1](<../../dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/note/CommandsView.tsx#L1>) | CommandsView | 3 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/note/CustomBubbleMenu.tsx:1](<../../dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/note/CustomBubbleMenu.tsx#L1>) | CustomBubbleMenu | 3 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/note/MenuBar.tsx:1](<../../dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/note/MenuBar.tsx#L1>) | MenuBar | 0 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/note/NoteSegmentRenderer.tsx:1](<../../dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/note/NoteSegmentRenderer.tsx#L1>) | NoteSegmentRenderer | 0 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/note/ReferenceNodeView.tsx:1](<../../dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/note/ReferenceNodeView.tsx#L1>) | ReferenceNodeView | 3 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/note/RichTextEditor.tsx:1](<../../dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/note/RichTextEditor.tsx#L1>) | RichTextEditor | 3 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/overview/TopicOverview.tsx:1](<../../dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/overview/TopicOverview.tsx#L1>) | StatCard, TopicOverview | 3 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/quiz/context/QuizWorkspaceContext.tsx:1](<../../dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/quiz/context/QuizWorkspaceContext.tsx#L1>) | QuizWorkspaceContext, QuizWorkspaceProvider | 84 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/quiz/import/QuestionImportModal.tsx:1](<../../dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/quiz/import/QuestionImportModal.tsx#L1>) | QuestionImportModal | 84 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/quiz/import/QuestionImportText.tsx:1](<../../dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/quiz/import/QuestionImportText.tsx#L1>) | QuestionImportText | 84 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/quiz/import/QuestionPreview.tsx:1](<../../dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/quiz/import/QuestionPreview.tsx#L1>) | QuestionPreview | 84 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/quiz/quiz-edit/QuizEditTab.tsx:1](<../../dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/quiz/quiz-edit/QuizEditTab.tsx#L1>) | QuizEditTab | 3 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/quiz/quiz-generate/QuizCreateModal.tsx:1](<../../dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/quiz/quiz-generate/QuizCreateModal.tsx#L1>) | CreateQuizModal | 3 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/quiz/quiz-generate/QuizGenerateTab.tsx:1](<../../dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/quiz/quiz-generate/QuizGenerateTab.tsx#L1>) | DEFAULT_CHECK_TYPE, QUIZ_TYPES, QuizGenerateTab | 3 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/quiz/quiz-generate/QuizOnboarding.tsx:1](<../../dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/quiz/quiz-generate/QuizOnboarding.tsx#L1>) | QuizOnboarding, SectionTitle, Divider, StepBlock, InfoRow | 3 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/quiz/quiz-generate/QuizStatisticsChart.tsx:1](<../../dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/quiz/quiz-generate/QuizStatisticsChart.tsx#L1>) | QuizStatisticsChart | 3 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/quiz/quiz-generate/QuizTypeAccordion.tsx:1](<../../dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/quiz/quiz-generate/QuizTypeAccordion.tsx#L1>) | COLORS, QuizTypeAccordion | 3 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/quiz/quiz-generate/QuizTypeSelector.tsx:1](<../../dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/quiz/quiz-generate/QuizTypeSelector.tsx#L1>) | LABEL_MAP, TYPE_META, QuizTypeSelector | 3 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/quiz/quiz-generate/RecommendationCard.tsx:1](<../../dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/quiz/quiz-generate/RecommendationCard.tsx#L1>) | LABEL_MAP, COLOR_MAP, RecommendationCard | 3 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/quiz/quiz-generate/quiz-doing/ConfirmSubmitDialog.tsx:1](<../../dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/quiz/quiz-generate/quiz-doing/ConfirmSubmitDialog.tsx#L1>) | ConfirmSubmitDialog | 3 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/quiz/quiz-generate/quiz-doing/QuizDoingPanel.tsx:1](<../../dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/quiz/quiz-generate/quiz-doing/QuizDoingPanel.tsx#L1>) | QuizDoingPanel | 3 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/quiz/quiz-generate/quiz-doing/QuizFooterNavigator.tsx:1](<../../dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/quiz/quiz-generate/quiz-doing/QuizFooterNavigator.tsx#L1>) | QuizFooterNavigator | 3 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/quiz/quiz-generate/quiz-doing/QuizHeaderProgress.tsx:1](<../../dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/quiz/quiz-generate/quiz-doing/QuizHeaderProgress.tsx#L1>) | QuizHeaderProgress | 3 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/quiz/quiz-generate/quiz-doing/QuizQuestionIndividual.tsx:1](<../../dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/quiz/quiz-generate/quiz-doing/QuizQuestionIndividual.tsx#L1>) | QuizQuestionIndividual | 3 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/quiz/quiz-generate/quiz-doing/components/QuizConfidenceSelector.tsx:1](<../../dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/quiz/quiz-generate/quiz-doing/components/QuizConfidenceSelector.tsx#L1>) | CONFIDENCE_OPTIONS, QuizConfidenceSelector, LEVELS | 3 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/quiz/quiz-generate/quiz-doing/components/QuizResultFeedback.tsx:1](<../../dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/quiz/quiz-generate/quiz-doing/components/QuizResultFeedback.tsx#L1>) | RESULT_STATUS, QuizResultFeedback, Icon | 3 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/quiz/quiz-healthy/HealthBadge.tsx:1](<../../dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/quiz/quiz-healthy/HealthBadge.tsx#L1>) | HealthBadge | 3 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/quiz/quiz-healthy/QuestionHealthCard.tsx:1](<../../dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/quiz/quiz-healthy/QuestionHealthCard.tsx#L1>) | QuestionHealthCard | 3 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/quiz/quiz-healthy/QuizHealthyTab.tsx:1](<../../dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/quiz/quiz-healthy/QuizHealthyTab.tsx#L1>) | FILTERS, QuizHealthyTab | 3 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/quiz/quiz-history/QuizHistoryList.tsx:1](<../../dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/quiz/quiz-history/QuizHistoryList.tsx#L1>) | QuizHistoryList | 3 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/quiz/quiz-history/QuizHistoryTab.tsx:1](<../../dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/quiz/quiz-history/QuizHistoryTab.tsx#L1>) | QuizHistoryTab, ITEMS_PER_PAGE | 3 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/quiz/quiz-history/QuizResultDetailPanel.tsx:1](<../../dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/quiz/quiz-history/QuizResultDetailPanel.tsx#L1>) | QuizResultDetailPanel | 3 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/quiz/ui/FilterBar.tsx:1](<../../dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/quiz/ui/FilterBar.tsx#L1>) | FilterBar | 3 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/quiz/ui/QuizCard.tsx:1](<../../dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/quiz/ui/QuizCard.tsx#L1>) | QuizCard | 3 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/reference/Reference.tsx:1](<../../dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/reference/Reference.tsx#L1>) | DEFAULT_TYPE_EMBEDDING_MAPPING, Reference, Body, Footer, Cancel, ReferenceItem, YouTubeReferenceItem, FileReferenceItem | 84 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/schedule/ScheduleDialog.tsx:1](<../../dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/schedule/ScheduleDialog.tsx#L1>) | ScheduleDialog | 3 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/tabs/FlashCardTab.tsx:1](<../../dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/tabs/FlashCardTab.tsx#L1>) | FlashCardTab | 3 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/tabs/MindMapTab.tsx:1](<../../dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/tabs/MindMapTab.tsx#L1>) | MindmapTab | 3 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/tabs/NoteTab.tsx:1](<../../dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/tabs/NoteTab.tsx#L1>) | NoteTab | 3 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/tabs/OverViewTab.tsx:1](<../../dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/tabs/OverViewTab.tsx#L1>) | OverViewTab | 3 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/tabs/QuizTab.tsx:1](<../../dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/tabs/QuizTab.tsx#L1>) | QuizTabContent, QuizTab | 3 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/ui/ActiveDot.tsx:1](<../../dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/ui/ActiveDot.tsx#L1>) | ActiveDot | 3 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/workspace/TopicWorkspace.tsx:1](<../../dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/workspace/TopicWorkspace.tsx#L1>) | TopicWorkspace | 3 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/context/GenerateContext.tsx:1](<../../dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/context/GenerateContext.tsx#L1>) | GenerateContext, GenerateProvider, DEFAULT_LIST_TYPE, DEFAULT_DIFFICULT, DEFAULT_NUMBER_OF_ITEM | 84 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/context/TopicWorkspaceContext.tsx:1](<../../dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/context/TopicWorkspaceContext.tsx#L1>) | TopicWorkspaceContext, DEFAULT_TAB, ALLOWED_TABS, TopicWorkspaceProvider | 84 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/context/useRequireFlashcardContent.tsx:1](<../../dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/context/useRequireFlashcardContent.tsx#L1>) | (anonymous/local declarations) | 84 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/context/useRequireTopic.tsx:1](<../../dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/context/useRequireTopic.tsx#L1>) | (anonymous/local declarations) | 84 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/hooks/flashcard/useBatchFlashcardsForNode.tsx:1](<../../dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/hooks/flashcard/useBatchFlashcardsForNode.tsx#L1>) | (anonymous/local declarations) | 3 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/hooks/flashcard/useBatchFlashcardsForTopic.tsx:1](<../../dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/hooks/flashcard/useBatchFlashcardsForTopic.tsx#L1>) | (anonymous/local declarations) | 84 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/hooks/media/useMediaPlayer.tsx:1](<../../dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/hooks/media/useMediaPlayer.tsx#L1>) | (anonymous/local declarations) | 84 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/hooks/tiptap/useCommandOptions.tsx:1](<../../dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/hooks/tiptap/useCommandOptions.tsx#L1>) | (anonymous/local declarations) | 3 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/hooks/tiptap/useTiptapOptions.tsx:1](<../../dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/hooks/tiptap/useTiptapOptions.tsx#L1>) | (anonymous/local declarations) | 3 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/hooks/useAnkiSettings.tsx:1](<../../dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/hooks/useAnkiSettings.tsx#L1>) | (anonymous/local declarations) | 84 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/hooks/useFlashCardWorkSpace.tsx:1](<../../dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/hooks/useFlashCardWorkSpace.tsx#L1>) | (anonymous/local declarations) | 84 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/hooks/useGamesWorkSpace.tsx:1](<../../dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/hooks/useGamesWorkSpace.tsx#L1>) | (anonymous/local declarations) | 84 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/hooks/useLearningOptions.tsx:1](<../../dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/hooks/useLearningOptions.tsx#L1>) | (anonymous/local declarations) | 84 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/hooks/useMultiNodeFlashcardsGenerate.tsx:1](<../../dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/hooks/useMultiNodeFlashcardsGenerate.tsx#L1>) | (anonymous/local declarations) | 3 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/hooks/useNote.tsx:1](<../../dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/hooks/useNote.tsx#L1>) | (anonymous/local declarations) | 3 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/hooks/useNoteWorkspace.tsx:1](<../../dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/hooks/useNoteWorkspace.tsx#L1>) | (anonymous/local declarations) | 84 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/hooks/usePdfMaterial.tsx:1](<../../dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/hooks/usePdfMaterial.tsx#L1>) | (anonymous/local declarations) | 84 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/hooks/useQuizWorkspace.tsx:1](<../../dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/hooks/useQuizWorkspace.tsx#L1>) | (anonymous/local declarations) | 84 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/hooks/useSelectMenu.tsx:1](<../../dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/hooks/useSelectMenu.tsx#L1>) | GenerateFlashcards, GenerateFlashcardsComponent, GenerateQuizComponent, AddToNoteComponent | 3 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/layout/config.layout.tsx:1](<../../dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/layout/config.layout.tsx#L1>) | TOPIC_WORKSPACE_TABS | 3 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/topics/[topicId]/settings/anki/components/CreateSettingModal.tsx:1](<../../dozu-ui-service/src/app/[locale]/topics/[topicId]/settings/anki/components/CreateSettingModal.tsx#L1>) | CreateSettingModal | 84 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/topics/[topicId]/settings/anki/components/DeleteSettingModal.tsx:1](<../../dozu-ui-service/src/app/[locale]/topics/[topicId]/settings/anki/components/DeleteSettingModal.tsx#L1>) | DeleteSettingModal | 84 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/topics/[topicId]/settings/anki/components/ResetToDefaultModal.tsx:1](<../../dozu-ui-service/src/app/[locale]/topics/[topicId]/settings/anki/components/ResetToDefaultModal.tsx#L1>) | ResetToDefaultModal | 84 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/topics/[topicId]/settings/anki/components/UpdateSettingModal.tsx:1](<../../dozu-ui-service/src/app/[locale]/topics/[topicId]/settings/anki/components/UpdateSettingModal.tsx#L1>) | UpdateSettingModal | 84 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/topics/components/common/LearningSpace.tsx:1](<../../dozu-ui-service/src/app/[locale]/topics/components/common/LearningSpace.tsx#L1>) | LearningSpace | 3 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/topics/components/common/Metric.tsx:1](<../../dozu-ui-service/src/app/[locale]/topics/components/common/Metric.tsx#L1>) | Metric | 1 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/topics/components/common/TopicCard.tsx:1](<../../dozu-ui-service/src/app/[locale]/topics/components/common/TopicCard.tsx#L1>) | TopicCard | 3 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/topics/components/modals/CreateTopicModal.tsx:1](<../../dozu-ui-service/src/app/[locale]/topics/components/modals/CreateTopicModal.tsx#L1>) | CreateTopicModal | 84 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/topics/components/modals/DeleteTopicModal.tsx:1](<../../dozu-ui-service/src/app/[locale]/topics/components/modals/DeleteTopicModal.tsx#L1>) | DeleteTopicModal | 10 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/topics/components/modals/StudentProfileModal.tsx:1](<../../dozu-ui-service/src/app/[locale]/topics/components/modals/StudentProfileModal.tsx#L1>) | StudentProfileModal | 1 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/topics/components/modals/TopicDetailsModal.tsx:1](<../../dozu-ui-service/src/app/[locale]/topics/components/modals/TopicDetailsModal.tsx#L1>) | TopicDetails, TopicDetailsModal | 10 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/topics/components/modals/UpdateTopicModal.tsx:1](<../../dozu-ui-service/src/app/[locale]/topics/components/modals/UpdateTopicModal.tsx#L1>) | UpdateTopicModal | 10 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/topics/components/ui/ActivityTab.tsx:1](<../../dozu-ui-service/src/app/[locale]/topics/components/ui/ActivityTab.tsx#L1>) | ActivityTab | 1 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/topics/components/ui/LessonCompletionTracker.tsx:1](<../../dozu-ui-service/src/app/[locale]/topics/components/ui/LessonCompletionTracker.tsx#L1>) | LessonCompletionTracker | 0 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/topics/components/ui/ListPackage.tsx:1](<../../dozu-ui-service/src/app/[locale]/topics/components/ui/ListPackage.tsx#L1>) | ListPackage | 1 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/topics/components/ui/PersonalTopicLibrary.tsx:1](<../../dozu-ui-service/src/app/[locale]/topics/components/ui/PersonalTopicLibrary.tsx#L1>) | PersonalTopicLibrary | 1 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/topics/components/ui/modals/EditActivityModal.tsx:1](<../../dozu-ui-service/src/app/[locale]/topics/components/ui/modals/EditActivityModal.tsx#L1>) | EditActivityModal | 1 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/topics/hooks/useCreateTopic.tsx:1](<../../dozu-ui-service/src/app/[locale]/topics/hooks/useCreateTopic.tsx#L1>) | (anonymous/local declarations) | 10 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/topics/hooks/useDeleteTopic.tsx:1](<../../dozu-ui-service/src/app/[locale]/topics/hooks/useDeleteTopic.tsx#L1>) | (anonymous/local declarations) | 10 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/topics/hooks/useSelectPackageForTopic.tsx:1](<../../dozu-ui-service/src/app/[locale]/topics/hooks/useSelectPackageForTopic.tsx#L1>) | (anonymous/local declarations) | 10 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/topics/hooks/useTopicDetails.tsx:1](<../../dozu-ui-service/src/app/[locale]/topics/hooks/useTopicDetails.tsx#L1>) | (anonymous/local declarations) | 10 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/topics/hooks/useTopics.tsx:1](<../../dozu-ui-service/src/app/[locale]/topics/hooks/useTopics.tsx#L1>) | (anonymous/local declarations) | 10 source closures; see JSON |
| [dozu-ui-service/src/app/[locale]/topics/hooks/useUpdateTopic.tsx:1](<../../dozu-ui-service/src/app/[locale]/topics/hooks/useUpdateTopic.tsx#L1>) | (anonymous/local declarations) | 10 source closures; see JSON |
| [dozu-ui-service/src/app/global-error.tsx:1](<../../dozu-ui-service/src/app/global-error.tsx#L1>) | GlobalError | 0 source closures; see JSON |
| [dozu-ui-service/src/app/loading.tsx:1](<../../dozu-ui-service/src/app/loading.tsx#L1>) | AnimationLoading, Z_INDEX_OVERLAY, LoadingPage | 84 source closures; see JSON |
| [dozu-ui-service/src/app/not-found.tsx:1](<../../dozu-ui-service/src/app/not-found.tsx#L1>) | NotFoundPage | 0 source closures; see JSON |
| [dozu-ui-service/src/components/admin/DeleteConfirmationDialog.tsx:1](<../../dozu-ui-service/src/components/admin/DeleteConfirmationDialog.tsx#L1>) | DeleteConfirmationDialog | 4 source closures; see JSON |
| [dozu-ui-service/src/components/admin/Sidebar.tsx:1](<../../dozu-ui-service/src/components/admin/Sidebar.tsx#L1>) | Sidebar, Icon | 18 source closures; see JSON |
| [dozu-ui-service/src/components/admin/StatusBadges.tsx:1](<../../dozu-ui-service/src/components/admin/StatusBadges.tsx#L1>) | AvailabilityBadge, DefaultBadge | 2 source closures; see JSON |
| [dozu-ui-service/src/components/admin/Topbar.tsx:1](<../../dozu-ui-service/src/components/admin/Topbar.tsx#L1>) | THEMES, Topbar, CurrentIcon | 18 source closures; see JSON |
| [dozu-ui-service/src/components/animations/Animation404.tsx:1](<../../dozu-ui-service/src/components/animations/Animation404.tsx#L1>) | Animation404 | 0 source closures; see JSON |
| [dozu-ui-service/src/components/animations/AnimationLoading.tsx:1](<../../dozu-ui-service/src/components/animations/AnimationLoading.tsx#L1>) | AnimationLoading | 84 source closures; see JSON |
| [dozu-ui-service/src/components/auth/CentralCard.tsx:1](<../../dozu-ui-service/src/components/auth/CentralCard.tsx#L1>) | CentralCard | 5 source closures; see JSON |
| [dozu-ui-service/src/components/class/InviteStudentsModal.tsx:1](<../../dozu-ui-service/src/components/class/InviteStudentsModal.tsx#L1>) | InviteStudentsModal | 1 source closures; see JSON |
| [dozu-ui-service/src/components/class/PendingInvitesList.tsx:1](<../../dozu-ui-service/src/components/class/PendingInvitesList.tsx#L1>) | PendingInvitesList | 1 source closures; see JSON |
| [dozu-ui-service/src/components/class/QRCodeGenerator.tsx:1](<../../dozu-ui-service/src/components/class/QRCodeGenerator.tsx#L1>) | QRCodeGenerator | 1 source closures; see JSON |
| [dozu-ui-service/src/components/comments/CommentItem/CommentActions.tsx:1](<../../dozu-ui-service/src/components/comments/CommentItem/CommentActions.tsx#L1>) | CommentActions | 4 source closures; see JSON |
| [dozu-ui-service/src/components/comments/CommentItem/CommentContent.tsx:1](<../../dozu-ui-service/src/components/comments/CommentItem/CommentContent.tsx#L1>) | CommentContent | 4 source closures; see JSON |
| [dozu-ui-service/src/components/comments/CommentItem/CommentItem.tsx:1](<../../dozu-ui-service/src/components/comments/CommentItem/CommentItem.tsx#L1>) | CommentItem | 4 source closures; see JSON |
| [dozu-ui-service/src/components/comments/CommentItem/ReplyInput.tsx:1](<../../dozu-ui-service/src/components/comments/CommentItem/ReplyInput.tsx#L1>) | ReplyInput | 4 source closures; see JSON |
| [dozu-ui-service/src/components/comments/CommentList.tsx:1](<../../dozu-ui-service/src/components/comments/CommentList.tsx#L1>) | CommentList | 4 source closures; see JSON |
| [dozu-ui-service/src/components/comments/PrivateCommentSection.tsx:1](<../../dozu-ui-service/src/components/comments/PrivateCommentSection.tsx#L1>) | PrivateCommentSection | 2 source closures; see JSON |
| [dozu-ui-service/src/components/comments/PublicCommentSection.tsx:1](<../../dozu-ui-service/src/components/comments/PublicCommentSection.tsx#L1>) | PublicCommentSection | 4 source closures; see JSON |
| [dozu-ui-service/src/components/common/BackgroundGradient.tsx:1](<../../dozu-ui-service/src/components/common/BackgroundGradient.tsx#L1>) | BackgroundGradient | 3 source closures; see JSON |
| [dozu-ui-service/src/components/common/BackgroundGradientCard.tsx:1](<../../dozu-ui-service/src/components/common/BackgroundGradientCard.tsx#L1>) | BackgroundGradientCard | 2 source closures; see JSON |
| [dozu-ui-service/src/components/common/ErrorPage.tsx:1](<../../dozu-ui-service/src/components/common/ErrorPage.tsx#L1>) | ErrorPage | 0 source closures; see JSON |
| [dozu-ui-service/src/components/common/FetchBoundary.tsx:1](<../../dozu-ui-service/src/components/common/FetchBoundary.tsx#L1>) | FetchBoundary | 0 source closures; see JSON |
| [dozu-ui-service/src/components/common/FetchBoundary2.tsx:1](<../../dozu-ui-service/src/components/common/FetchBoundary2.tsx#L1>) | FetchBoundary | 0 source closures; see JSON |
| [dozu-ui-service/src/components/common/HeaderSection.tsx:1](<../../dozu-ui-service/src/components/common/HeaderSection.tsx#L1>) | HeaderSection | 2 source closures; see JSON |
| [dozu-ui-service/src/components/customs/cap-table.tsx:1](<../../dozu-ui-service/src/components/customs/cap-table.tsx#L1>) | CapTable | 0 source closures; see JSON |
| [dozu-ui-service/src/components/customs/error.component.tsx:1](<../../dozu-ui-service/src/components/customs/error.component.tsx#L1>) | Error | 0 source closures; see JSON |
| [dozu-ui-service/src/components/customs/markdown-content.tsx:1](<../../dozu-ui-service/src/components/customs/markdown-content.tsx#L1>) | MarkdownContent | 84 source closures; see JSON |
| [dozu-ui-service/src/components/customs/spinner.tsx:1](<../../dozu-ui-service/src/components/customs/spinner.tsx#L1>) | Spinner | 0 source closures; see JSON |
| [dozu-ui-service/src/components/customs/wrapper.component.tsx:1](<../../dozu-ui-service/src/components/customs/wrapper.component.tsx#L1>) | (anonymous/local declarations) | 0 source closures; see JSON |
| [dozu-ui-service/src/components/demo/SurveyQuiz.tsx:1](<../../dozu-ui-service/src/components/demo/SurveyQuiz.tsx#L1>) | SurveyQuiz | 0 source closures; see JSON |
| [dozu-ui-service/src/components/demo/dataTableDemo.tsx:1](<../../dozu-ui-service/src/components/demo/dataTableDemo.tsx#L1>) | DataTableDemo | 0 source closures; see JSON |
| [dozu-ui-service/src/components/errors/DataStatus.tsx:1](<../../dozu-ui-service/src/components/errors/DataStatus.tsx#L1>) | DataStatus | 84 source closures; see JSON |
| [dozu-ui-service/src/components/errors/ErrorPageFallback.tsx:1](<../../dozu-ui-service/src/components/errors/ErrorPageFallback.tsx#L1>) | ErrorPageFallback | 0 source closures; see JSON |
| [dozu-ui-service/src/components/errors/NotFoundView.tsx:1](<../../dozu-ui-service/src/components/errors/NotFoundView.tsx#L1>) | NotFoundView | 0 source closures; see JSON |
| [dozu-ui-service/src/components/feedback/FeedbackDialog.tsx:1](<../../dozu-ui-service/src/components/feedback/FeedbackDialog.tsx#L1>) | FeedbackDialog | 84 source closures; see JSON |
| [dozu-ui-service/src/components/feynman/ActionBar.tsx:1](<../../dozu-ui-service/src/components/feynman/ActionBar.tsx#L1>) | ActionBar | 1 source closures; see JSON |
| [dozu-ui-service/src/components/feynman/FeynmanEditor.tsx:1](<../../dozu-ui-service/src/components/feynman/FeynmanEditor.tsx#L1>) | JARGON_COLORS, FeynmanEditor, JargonHighlighter | 1 source closures; see JSON |
| [dozu-ui-service/src/components/feynman/HintPanel.tsx:1](<../../dozu-ui-service/src/components/feynman/HintPanel.tsx#L1>) | HintPanel | 0 source closures; see JSON |
| [dozu-ui-service/src/components/feynman/History.tsx:1](<../../dozu-ui-service/src/components/feynman/History.tsx#L1>) | History | 1 source closures; see JSON |
| [dozu-ui-service/src/components/feynman/LeftMissionPanel.tsx:1](<../../dozu-ui-service/src/components/feynman/LeftMissionPanel.tsx#L1>) | LeftMissionPanel | 1 source closures; see JSON |
| [dozu-ui-service/src/components/feynman/MenuEditorBar.tsx:1](<../../dozu-ui-service/src/components/feynman/MenuEditorBar.tsx#L1>) | MenuBar | 1 source closures; see JSON |
| [dozu-ui-service/src/components/feynman/ReviewedDialog.tsx:1](<../../dozu-ui-service/src/components/feynman/ReviewedDialog.tsx#L1>) | FeynmanReviewDialog | 1 source closures; see JSON |
| [dozu-ui-service/src/components/flashcard/StarButton.tsx:1](<../../dozu-ui-service/src/components/flashcard/StarButton.tsx#L1>) | StarButton | 84 source closures; see JSON |
| [dozu-ui-service/src/components/flashcard/VolumeButton.tsx:1](<../../dozu-ui-service/src/components/flashcard/VolumeButton.tsx#L1>) | VolumeButton | 84 source closures; see JSON |
| [dozu-ui-service/src/components/gamification/GamificationDashboard.tsx:1](<../../dozu-ui-service/src/components/gamification/GamificationDashboard.tsx#L1>) | GamificationDashboard | 0 source closures; see JSON |
| [dozu-ui-service/src/components/gamification/Leaderboard.tsx:1](<../../dozu-ui-service/src/components/gamification/Leaderboard.tsx#L1>) | Leaderboard | 0 source closures; see JSON |
| [dozu-ui-service/src/components/gamification/PointSystem.tsx:1](<../../dozu-ui-service/src/components/gamification/PointSystem.tsx#L1>) | PointSystem | 0 source closures; see JSON |
| [dozu-ui-service/src/components/gamification/StreakDisplay.tsx:1](<../../dozu-ui-service/src/components/gamification/StreakDisplay.tsx#L1>) | StreakDisplay, MILESTONE_THRESHOLDS, MilestoneIcon | 0 source closures; see JSON |
| [dozu-ui-service/src/components/generative/GenerateStreaming.tsx:1](<../../dozu-ui-service/src/components/generative/GenerateStreaming.tsx#L1>) | GenerateStreaming | 0 source closures; see JSON |
| [dozu-ui-service/src/components/generative/GeneratingSkeleton.tsx:1](<../../dozu-ui-service/src/components/generative/GeneratingSkeleton.tsx#L1>) | GeneratingSkeleton | 84 source closures; see JSON |
| [dozu-ui-service/src/components/generative/UploadProgressComponent.tsx:1](<../../dozu-ui-service/src/components/generative/UploadProgressComponent.tsx#L1>) | UploadProgressComponent | 0 source closures; see JSON |
| [dozu-ui-service/src/components/guards/RouteGuard.tsx:1](<../../dozu-ui-service/src/components/guards/RouteGuard.tsx#L1>) | RouteGuard | 2 source closures; see JSON |
| [dozu-ui-service/src/components/loading/LoadingOverLay.tsx:1](<../../dozu-ui-service/src/components/loading/LoadingOverLay.tsx#L1>) | LoadingOverlay | 84 source closures; see JSON |
| [dozu-ui-service/src/components/mindmap/ProgressDialog.tsx:1](<../../dozu-ui-service/src/components/mindmap/ProgressDialog.tsx#L1>) | ProgressDialog | 1 source closures; see JSON |
| [dozu-ui-service/src/components/mindmap/TeacherNodeSheet.tsx:1](<../../dozu-ui-service/src/components/mindmap/TeacherNodeSheet.tsx#L1>) | TeacherNodeSheet | 1 source closures; see JSON |
| [dozu-ui-service/src/components/mindmap/button/ChangeColorThemeButton.tsx:1](<../../dozu-ui-service/src/components/mindmap/button/ChangeColorThemeButton.tsx#L1>) | ChangeColorThemeButton | 4 source closures; see JSON |
| [dozu-ui-service/src/components/mindmap/button/CustomizeMindmapLayoutOptionsButton.tsx:1](<../../dozu-ui-service/src/components/mindmap/button/CustomizeMindmapLayoutOptionsButton.tsx#L1>) | CustomizeMindmapLayoutOptionsButton | 4 source closures; see JSON |
| [dozu-ui-service/src/components/mindmap/button/DeleteMindmapButton.tsx:1](<../../dozu-ui-service/src/components/mindmap/button/DeleteMindmapButton.tsx#L1>) | DeleteMindmapButton | 4 source closures; see JSON |
| [dozu-ui-service/src/components/mindmap/button/DownloadButton.tsx:1](<../../dozu-ui-service/src/components/mindmap/button/DownloadButton.tsx#L1>) | DownloadButton | 7 source closures; see JSON |
| [dozu-ui-service/src/components/mindmap/button/EditMindmapButton.tsx:1](<../../dozu-ui-service/src/components/mindmap/button/EditMindmapButton.tsx#L1>) | EditMindmapButton | 4 source closures; see JSON |
| [dozu-ui-service/src/components/mindmap/button/HorizontalLayoutButton.tsx:1](<../../dozu-ui-service/src/components/mindmap/button/HorizontalLayoutButton.tsx#L1>) | HorizontalLayoutButton | 4 source closures; see JSON |
| [dozu-ui-service/src/components/mindmap/button/MindmapLayoutButton.tsx:1](<../../dozu-ui-service/src/components/mindmap/button/MindmapLayoutButton.tsx#L1>) | MindmapLayoutButton | 4 source closures; see JSON |
| [dozu-ui-service/src/components/mindmap/button/RadialLayoutButton.tsx:1](<../../dozu-ui-service/src/components/mindmap/button/RadialLayoutButton.tsx#L1>) | RadialLayoutButton | 4 source closures; see JSON |
| [dozu-ui-service/src/components/mindmap/button/SelectMultipleButton.tsx:1](<../../dozu-ui-service/src/components/mindmap/button/SelectMultipleButton.tsx#L1>) | SelectMultipleButton | 4 source closures; see JSON |
| [dozu-ui-service/src/components/mindmap/button/VerticalLayoutButton.tsx:1](<../../dozu-ui-service/src/components/mindmap/button/VerticalLayoutButton.tsx#L1>) | VerticalLayoutButton | 4 source closures; see JSON |
| [dozu-ui-service/src/components/mindmap/button/ViewFileButton.tsx:1](<../../dozu-ui-service/src/components/mindmap/button/ViewFileButton.tsx#L1>) | ViewFileButton | 4 source closures; see JSON |
| [dozu-ui-service/src/components/modal/DeleteComfirmationModal.tsx:1](<../../dozu-ui-service/src/components/modal/DeleteComfirmationModal.tsx#L1>) | DeleteConfirmationModal | 84 source closures; see JSON |
| [dozu-ui-service/src/components/modal/Modal.tsx:1](<../../dozu-ui-service/src/components/modal/Modal.tsx#L1>) | Modal | 84 source closures; see JSON |
| [dozu-ui-service/src/components/permission/AuthGuard.tsx:1](<../../dozu-ui-service/src/components/permission/AuthGuard.tsx#L1>) | AuthGuard | 84 source closures; see JSON |
| [dozu-ui-service/src/components/permission/PermissionGate.tsx:1](<../../dozu-ui-service/src/components/permission/PermissionGate.tsx#L1>) | PermissionGate | 0 source closures; see JSON |
| [dozu-ui-service/src/components/pomodoro/Pomodoro.tsx:1](<../../dozu-ui-service/src/components/pomodoro/Pomodoro.tsx#L1>) | DEFAULT_MINUTE_COUNT_DOWN, DEFAULT_MINUTE_BREAK_TIME_COUNT_DOWN, DEFAULT_TIME_SUB_COUNT_DOWN, Pomodoro, LS_SOUNDS_KEY, LS_SELECTED_SOUND_KEY, LS_VOLUME_KEY, LS_PLAY_BREAK_KEY, LS_DEFAULT_TIME_COUNT_DOWN, LS_BREAK_SPECIFIC_ENABLED, LS_BREAK_AMBIENT_ID, MAX_CUSTOM_SOUND_SIZE_MB, LARGE_FILE_THRESHOLD_MB | 84 source closures; see JSON |
| [dozu-ui-service/src/components/providers/GamificationWrapper.tsx:1](<../../dozu-ui-service/src/components/providers/GamificationWrapper.tsx#L1>) | GamificationWrapper | 0 source closures; see JSON |
| [dozu-ui-service/src/components/react-bits/CardSwap.tsx:1](<../../dozu-ui-service/src/components/react-bits/CardSwap.tsx#L1>) | Card, CardSwap | 1 source closures; see JSON |
| [dozu-ui-service/src/components/react-bits/Particles.tsx:1](<../../dozu-ui-service/src/components/react-bits/Particles.tsx#L1>) | Particles | 1 source closures; see JSON |
| [dozu-ui-service/src/components/react-bits/SplitText.tsx:1](<../../dozu-ui-service/src/components/react-bits/SplitText.tsx#L1>) | SplitText | 1 source closures; see JSON |
| [dozu-ui-service/src/components/react-bits/StarBorder.tsx:1](<../../dozu-ui-service/src/components/react-bits/StarBorder.tsx#L1>) | StarBorder, Component | 1 source closures; see JSON |
| [dozu-ui-service/src/components/react-bits/TextType.tsx:1](<../../dozu-ui-service/src/components/react-bits/TextType.tsx#L1>) | TextType | 1 source closures; see JSON |
| [dozu-ui-service/src/components/react-bits/Threads.tsx:1](<../../dozu-ui-service/src/components/react-bits/Threads.tsx#L1>) | Threads | 1 source closures; see JSON |
| [dozu-ui-service/src/components/schedule/CalendarDayView.tsx:1](<../../dozu-ui-service/src/components/schedule/CalendarDayView.tsx#L1>) | CalendarDayView | 4 source closures; see JSON |
| [dozu-ui-service/src/components/schedule/CalendarWeekView.tsx:1](<../../dozu-ui-service/src/components/schedule/CalendarWeekView.tsx#L1>) | CalendarWeekView | 4 source closures; see JSON |
| [dozu-ui-service/src/components/schedule/DayEventsContainer.tsx:1](<../../dozu-ui-service/src/components/schedule/DayEventsContainer.tsx#L1>) | DayEventsContainer | 4 source closures; see JSON |
| [dozu-ui-service/src/components/schedule/DroppableTimeSlot.tsx:1](<../../dozu-ui-service/src/components/schedule/DroppableTimeSlot.tsx#L1>) | DroppableTimeSlot | 4 source closures; see JSON |
| [dozu-ui-service/src/components/schedule/EventCard.tsx:1](<../../dozu-ui-service/src/components/schedule/EventCard.tsx#L1>) | EventCard | 4 source closures; see JSON |
| [dozu-ui-service/src/components/schedule/EventGroup.tsx:1](<../../dozu-ui-service/src/components/schedule/EventGroup.tsx#L1>) | EventGroup | 4 source closures; see JSON |
| [dozu-ui-service/src/components/schedule/FreeTimeSelector.tsx:1](<../../dozu-ui-service/src/components/schedule/FreeTimeSelector.tsx#L1>) | FreeTimeSelector | 1 source closures; see JSON |
| [dozu-ui-service/src/components/schedule/PrioritySelector.tsx:1](<../../dozu-ui-service/src/components/schedule/PrioritySelector.tsx#L1>) | PrioritySelector | 0 source closures; see JSON |
| [dozu-ui-service/src/components/schedule/SaveBar.tsx:1](<../../dozu-ui-service/src/components/schedule/SaveBar.tsx#L1>) | SaveBar | 4 source closures; see JSON |
| [dozu-ui-service/src/components/schedule/StudyPreference.tsx:1](<../../dozu-ui-service/src/components/schedule/StudyPreference.tsx#L1>) | StudyPreference, StudyPreferenceInDate | 1 source closures; see JSON |
| [dozu-ui-service/src/components/schedule/SubjectListInput.tsx:1](<../../dozu-ui-service/src/components/schedule/SubjectListInput.tsx#L1>) | SubjectListInput | 0 source closures; see JSON |
| [dozu-ui-service/src/components/schedule/TimeTable.tsx:1](<../../dozu-ui-service/src/components/schedule/TimeTable.tsx#L1>) | TimeTable | 4 source closures; see JSON |
| [dozu-ui-service/src/components/side-bar/SideBar.tsx:1](<../../dozu-ui-service/src/components/side-bar/SideBar.tsx#L1>) | NAME_CONVERSION_PLAN_UPGRADE, AppSidebar | 84 source closures; see JSON |
| [dozu-ui-service/src/components/stats/DailyStudyChart.tsx:1](<../../dozu-ui-service/src/components/stats/DailyStudyChart.tsx#L1>) | (anonymous/local declarations) | 0 source closures; see JSON |
| [dozu-ui-service/src/components/stats/KeyMetricCard.tsx:1](<../../dozu-ui-service/src/components/stats/KeyMetricCard.tsx#L1>) | (anonymous/local declarations) | 0 source closures; see JSON |
| [dozu-ui-service/src/components/stats/LearningMethodsChart.tsx:1](<../../dozu-ui-service/src/components/stats/LearningMethodsChart.tsx#L1>) | (anonymous/local declarations) | 0 source closures; see JSON |
| [dozu-ui-service/src/components/stats/LearningProgress.tsx:1](<../../dozu-ui-service/src/components/stats/LearningProgress.tsx#L1>) | (anonymous/local declarations) | 0 source closures; see JSON |
| [dozu-ui-service/src/components/stats/StatsLearningMethods.tsx:1](<../../dozu-ui-service/src/components/stats/StatsLearningMethods.tsx#L1>) | (anonymous/local declarations) | 0 source closures; see JSON |
| [dozu-ui-service/src/components/stats/StatsOverview.tsx:1](<../../dozu-ui-service/src/components/stats/StatsOverview.tsx#L1>) | (anonymous/local declarations) | 0 source closures; see JSON |
| [dozu-ui-service/src/components/tiptap-icons/close-icon.tsx:1](<../../dozu-ui-service/src/components/tiptap-icons/close-icon.tsx#L1>) | CloseIcon | 3 source closures; see JSON |
| [dozu-ui-service/src/components/tiptap-icons/image-plus-icon.tsx:1](<../../dozu-ui-service/src/components/tiptap-icons/image-plus-icon.tsx#L1>) | ImagePlusIcon | 3 source closures; see JSON |
| [dozu-ui-service/src/components/tiptap-node/image-upload-node/image-upload-node.tsx:1](<../../dozu-ui-service/src/components/tiptap-node/image-upload-node/image-upload-node.tsx#L1>) | CloudUploadIcon, FileIcon, FileCornerIcon, ImageUploadDragArea, ImageUploadPreview, DropZoneContent, ImageUploadNode | 3 source closures; see JSON |
| [dozu-ui-service/src/components/tiptap-node/image-upload-node/index.tsx:1](<../../dozu-ui-service/src/components/tiptap-node/image-upload-node/index.tsx#L1>) | (anonymous/local declarations) | 3 source closures; see JSON |
| [dozu-ui-service/src/components/tiptap-ui-primitive/badge/badge.tsx:1](<../../dozu-ui-service/src/components/tiptap-ui-primitive/badge/badge.tsx#L1>) | Badge | 3 source closures; see JSON |
| [dozu-ui-service/src/components/tiptap-ui-primitive/badge/index.tsx:1](<../../dozu-ui-service/src/components/tiptap-ui-primitive/badge/index.tsx#L1>) | (anonymous/local declarations) | 3 source closures; see JSON |
| [dozu-ui-service/src/components/tiptap-ui-primitive/button/button.tsx:1](<../../dozu-ui-service/src/components/tiptap-ui-primitive/button/button.tsx#L1>) | ShortcutDisplay, Button, ButtonGroup | 3 source closures; see JSON |
| [dozu-ui-service/src/components/tiptap-ui-primitive/button/index.tsx:1](<../../dozu-ui-service/src/components/tiptap-ui-primitive/button/index.tsx#L1>) | (anonymous/local declarations) | 3 source closures; see JSON |
| [dozu-ui-service/src/components/tiptap-ui-primitive/tooltip/index.tsx:1](<../../dozu-ui-service/src/components/tiptap-ui-primitive/tooltip/index.tsx#L1>) | (anonymous/local declarations) | 3 source closures; see JSON |
| [dozu-ui-service/src/components/tiptap-ui-primitive/tooltip/tooltip.tsx:1](<../../dozu-ui-service/src/components/tiptap-ui-primitive/tooltip/tooltip.tsx#L1>) | TooltipContext, Tooltip, TooltipTrigger, TooltipContent | 3 source closures; see JSON |
| [dozu-ui-service/src/components/tiptap-ui/image-upload-button/image-upload-button.tsx:1](<../../dozu-ui-service/src/components/tiptap-ui/image-upload-button/image-upload-button.tsx#L1>) | ImageShortcutBadge, ImageUploadButton, RenderIcon | 3 source closures; see JSON |
| [dozu-ui-service/src/components/tiptap-ui/image-upload-button/index.tsx:1](<../../dozu-ui-service/src/components/tiptap-ui/image-upload-button/index.tsx#L1>) | (anonymous/local declarations) | 3 source closures; see JSON |
| [dozu-ui-service/src/components/toolbar/AuthButton.tsx:1](<../../dozu-ui-service/src/components/toolbar/AuthButton.tsx#L1>) | AuthButton | 84 source closures; see JSON |
| [dozu-ui-service/src/components/toolbar/LanguageSwitcher.tsx:1](<../../dozu-ui-service/src/components/toolbar/LanguageSwitcher.tsx#L1>) | LanguageSwitcher | 84 source closures; see JSON |
| [dozu-ui-service/src/components/toolbar/LearningModeSelect.tsx:1](<../../dozu-ui-service/src/components/toolbar/LearningModeSelect.tsx#L1>) | Personal, ClassBased, LearningModeSelect | 84 source closures; see JSON |
| [dozu-ui-service/src/components/toolbar/Navbar.tsx:1](<../../dozu-ui-service/src/components/toolbar/Navbar.tsx#L1>) | Navbar | 84 source closures; see JSON |
| [dozu-ui-service/src/components/toolbar/ThemeToggle.tsx:1](<../../dozu-ui-service/src/components/toolbar/ThemeToggle.tsx#L1>) | ThemeToggle, Icon | 84 source closures; see JSON |
| [dozu-ui-service/src/components/toolbar/UserMenu.tsx:1](<../../dozu-ui-service/src/components/toolbar/UserMenu.tsx#L1>) | UserMenu, Icon | 84 source closures; see JSON |
| [dozu-ui-service/src/components/ui/AvatarWithStreak.tsx:1](<../../dozu-ui-service/src/components/ui/AvatarWithStreak.tsx#L1>) | AvatarWithStreak | 1 source closures; see JSON |
| [dozu-ui-service/src/components/ui/LocaleFontProvider.tsx:1](<../../dozu-ui-service/src/components/ui/LocaleFontProvider.tsx#L1>) | LocaleFontProvider | 84 source closures; see JSON |
| [dozu-ui-service/src/components/ui/ShowIf.tsx:1](<../../dozu-ui-service/src/components/ui/ShowIf.tsx#L1>) | ShowIf | 84 source closures; see JSON |
| [dozu-ui-service/src/components/ui/StreakFreezeModal.tsx:1](<../../dozu-ui-service/src/components/ui/StreakFreezeModal.tsx#L1>) | StreakFreezeModal | 0 source closures; see JSON |
| [dozu-ui-service/src/components/ui/StreakTracker.tsx:1](<../../dozu-ui-service/src/components/ui/StreakTracker.tsx#L1>) | StreakTracker | 0 source closures; see JSON |
| [dozu-ui-service/src/components/ui/accordion.tsx:1](<../../dozu-ui-service/src/components/ui/accordion.tsx#L1>) | Accordion, AccordionItem, AccordionTrigger, AccordionContent | 0 source closures; see JSON |
| [dozu-ui-service/src/components/ui/alert-dialog.tsx:1](<../../dozu-ui-service/src/components/ui/alert-dialog.tsx#L1>) | AlertDialog, AlertDialogTrigger, AlertDialogPortal, AlertDialogOverlay, AlertDialogContent, AlertDialogHeader, AlertDialogFooter, AlertDialogTitle, AlertDialogDescription, AlertDialogAction, AlertDialogCancel | 84 source closures; see JSON |
| [dozu-ui-service/src/components/ui/alert.tsx:1](<../../dozu-ui-service/src/components/ui/alert.tsx#L1>) | Alert, AlertTitle, AlertDescription | 15 source closures; see JSON |
| [dozu-ui-service/src/components/ui/aspect-ratio.tsx:1](<../../dozu-ui-service/src/components/ui/aspect-ratio.tsx#L1>) | AspectRatio | 0 source closures; see JSON |
| [dozu-ui-service/src/components/ui/auth-skeleton.tsx:1](<../../dozu-ui-service/src/components/ui/auth-skeleton.tsx#L1>) | AuthSkeleton | 2 source closures; see JSON |
| [dozu-ui-service/src/components/ui/avatar.tsx:1](<../../dozu-ui-service/src/components/ui/avatar.tsx#L1>) | Avatar, AvatarImage, AvatarFallback | 84 source closures; see JSON |
| [dozu-ui-service/src/components/ui/badge.tsx:1](<../../dozu-ui-service/src/components/ui/badge.tsx#L1>) | Badge | 84 source closures; see JSON |
| [dozu-ui-service/src/components/ui/button.tsx:1](<../../dozu-ui-service/src/components/ui/button.tsx#L1>) | Button, Comp | 84 source closures; see JSON |
| [dozu-ui-service/src/components/ui/calendar.tsx:1](<../../dozu-ui-service/src/components/ui/calendar.tsx#L1>) | Calendar | 6 source closures; see JSON |
| [dozu-ui-service/src/components/ui/card.tsx:1](<../../dozu-ui-service/src/components/ui/card.tsx#L1>) | Card, CardHeader, CardTitle, CardDescription, CardContent, CardFooter | 84 source closures; see JSON |
| [dozu-ui-service/src/components/ui/carousel.tsx:1](<../../dozu-ui-service/src/components/ui/carousel.tsx#L1>) | CarouselContext, Carousel, CarouselContent, CarouselItem, CarouselPrevious, CarouselNext | 1 source closures; see JSON |
| [dozu-ui-service/src/components/ui/checkbox.tsx:1](<../../dozu-ui-service/src/components/ui/checkbox.tsx#L1>) | Checkbox | 84 source closures; see JSON |
| [dozu-ui-service/src/components/ui/collapsible.tsx:1](<../../dozu-ui-service/src/components/ui/collapsible.tsx#L1>) | Collapsible, CollapsibleTrigger, CollapsibleContent | 4 source closures; see JSON |
| [dozu-ui-service/src/components/ui/command.tsx:1](<../../dozu-ui-service/src/components/ui/command.tsx#L1>) | Command, CommandDialog, CommandInput, CommandList, CommandEmpty, CommandGroup, CommandSeparator, CommandItem, CommandShortcut | 3 source closures; see JSON |
| [dozu-ui-service/src/components/ui/data-table.tsx:1](<../../dozu-ui-service/src/components/ui/data-table.tsx#L1>) | DataTable | 11 source closures; see JSON |
| [dozu-ui-service/src/components/ui/dialog.tsx:1](<../../dozu-ui-service/src/components/ui/dialog.tsx#L1>) | Dialog, DialogTrigger, DialogPortal, DialogClose, DialogOverlay, DialogContent, DialogHeader, DialogFooter, DialogTitle, DialogDescription | 84 source closures; see JSON |
| [dozu-ui-service/src/components/ui/dropdown-menu.tsx:1](<../../dozu-ui-service/src/components/ui/dropdown-menu.tsx#L1>) | DropdownMenu, DropdownMenuTrigger, DropdownMenuGroup, DropdownMenuPortal, DropdownMenuSub, DropdownMenuRadioGroup, DropdownMenuSubTrigger, DropdownMenuSubContent, DropdownMenuContent, DropdownMenuItem, DropdownMenuCheckboxItem, DropdownMenuRadioItem, DropdownMenuLabel, DropdownMenuSeparator, DropdownMenuShortcut | 84 source closures; see JSON |
| [dozu-ui-service/src/components/ui/full-calendar.tsx:1](<../../dozu-ui-service/src/components/ui/full-calendar.tsx#L1>) | Context, Calendar, CalendarViewTrigger, CalendarNextTrigger, CalendarPrevTrigger, CalendarTodayTrigger, CalendarCurrentDate, TimeTable | 4 source closures; see JSON |
| [dozu-ui-service/src/components/ui/hover-card.tsx:1](<../../dozu-ui-service/src/components/ui/hover-card.tsx#L1>) | HoverCard, HoverCardTrigger, HoverCardContent | 0 source closures; see JSON |
| [dozu-ui-service/src/components/ui/input.tsx:1](<../../dozu-ui-service/src/components/ui/input.tsx#L1>) | Input | 84 source closures; see JSON |
| [dozu-ui-service/src/components/ui/label.tsx:1](<../../dozu-ui-service/src/components/ui/label.tsx#L1>) | Label | 84 source closures; see JSON |
| [dozu-ui-service/src/components/ui/popover.tsx:1](<../../dozu-ui-service/src/components/ui/popover.tsx#L1>) | Popover, PopoverTrigger, PopoverContent, PopoverAnchor | 12 source closures; see JSON |
| [dozu-ui-service/src/components/ui/progress.tsx:1](<../../dozu-ui-service/src/components/ui/progress.tsx#L1>) | Progress | 84 source closures; see JSON |
| [dozu-ui-service/src/components/ui/qr-code.tsx:1](<../../dozu-ui-service/src/components/ui/qr-code.tsx#L1>) | QRCodeComponent | 1 source closures; see JSON |
| [dozu-ui-service/src/components/ui/radio-group.tsx:1](<../../dozu-ui-service/src/components/ui/radio-group.tsx#L1>) | RadioGroup, RadioGroupItem | 84 source closures; see JSON |
| [dozu-ui-service/src/components/ui/resizable.tsx:1](<../../dozu-ui-service/src/components/ui/resizable.tsx#L1>) | ResizablePanelGroup, ResizablePanel, ResizableHandle | 3 source closures; see JSON |
| [dozu-ui-service/src/components/ui/scroll-area.tsx:1](<../../dozu-ui-service/src/components/ui/scroll-area.tsx#L1>) | ScrollArea, ScrollBar | 84 source closures; see JSON |
| [dozu-ui-service/src/components/ui/select.tsx:1](<../../dozu-ui-service/src/components/ui/select.tsx#L1>) | Select, SelectGroup, SelectValue, SelectTrigger, SelectScrollUpButton, SelectScrollDownButton, SelectContent, SelectLabel, SelectItem, SelectSeparator | 84 source closures; see JSON |
| [dozu-ui-service/src/components/ui/separator.tsx:1](<../../dozu-ui-service/src/components/ui/separator.tsx#L1>) | Separator | 84 source closures; see JSON |
| [dozu-ui-service/src/components/ui/sheet.tsx:1](<../../dozu-ui-service/src/components/ui/sheet.tsx#L1>) | Sheet, SheetTrigger, SheetClose, SheetPortal, SheetOverlay, SheetContent, SheetHeader, SheetFooter, SheetTitle, SheetDescription | 84 source closures; see JSON |
| [dozu-ui-service/src/components/ui/sidebar.tsx:1](<../../dozu-ui-service/src/components/ui/sidebar.tsx#L1>) | SIDEBAR_COOKIE_NAME, SIDEBAR_COOKIE_MAX_AGE, SIDEBAR_WIDTH, SIDEBAR_WIDTH_MOBILE, SIDEBAR_WIDTH_ICON, SIDEBAR_KEYBOARD_SHORTCUT, SidebarContext, SidebarProvider, Sidebar, SidebarTrigger, SidebarRail, SidebarInset, SidebarInput, SidebarHeader, SidebarFooter, SidebarSeparator, SidebarContent, SidebarGroup, SidebarGroupLabel, Comp, SidebarGroupAction, SidebarGroupContent, SidebarMenu, SidebarMenuItem, SidebarMenuButton, SidebarMenuAction, SidebarMen | 84 source closures; see JSON |
| [dozu-ui-service/src/components/ui/skeleton.tsx:1](<../../dozu-ui-service/src/components/ui/skeleton.tsx#L1>) | Skeleton | 84 source closures; see JSON |
| [dozu-ui-service/src/components/ui/slider.tsx:1](<../../dozu-ui-service/src/components/ui/slider.tsx#L1>) | Slider | 84 source closures; see JSON |
| [dozu-ui-service/src/components/ui/sonner.tsx:1](<../../dozu-ui-service/src/components/ui/sonner.tsx#L1>) | Toaster | 84 source closures; see JSON |
| [dozu-ui-service/src/components/ui/spinner.tsx:1](<../../dozu-ui-service/src/components/ui/spinner.tsx#L1>) | Spinner | 84 source closures; see JSON |
| [dozu-ui-service/src/components/ui/switch.tsx:1](<../../dozu-ui-service/src/components/ui/switch.tsx#L1>) | Switch | 84 source closures; see JSON |
| [dozu-ui-service/src/components/ui/table.tsx:1](<../../dozu-ui-service/src/components/ui/table.tsx#L1>) | Table, TableHeader, TableBody, TableFooter, TableRow, TableHead, TableCell, TableCaption | 84 source closures; see JSON |
| [dozu-ui-service/src/components/ui/tabs.tsx:1](<../../dozu-ui-service/src/components/ui/tabs.tsx#L1>) | Tabs, TabsList, TabsTrigger, TabsContent | 84 source closures; see JSON |
| [dozu-ui-service/src/components/ui/textarea.tsx:1](<../../dozu-ui-service/src/components/ui/textarea.tsx#L1>) | Textarea | 84 source closures; see JSON |
| [dozu-ui-service/src/components/ui/toast.tsx:1](<../../dozu-ui-service/src/components/ui/toast.tsx#L1>) | ToastProvider, ToastViewport, Toast, ToastAction, ToastClose, ToastTitle, ToastDescription | 84 source closures; see JSON |
| [dozu-ui-service/src/components/ui/toaster.tsx:1](<../../dozu-ui-service/src/components/ui/toaster.tsx#L1>) | Toaster | 84 source closures; see JSON |
| [dozu-ui-service/src/components/ui/toggle.tsx:1](<../../dozu-ui-service/src/components/ui/toggle.tsx#L1>) | Toggle | 3 source closures; see JSON |
| [dozu-ui-service/src/components/ui/tooltip.tsx:1](<../../dozu-ui-service/src/components/ui/tooltip.tsx#L1>) | TooltipProvider, Tooltip, TooltipTrigger, TooltipContent | 84 source closures; see JSON |
| [dozu-ui-service/src/components/upgrade-plan/UpgradePlanModal.tsx:1](<../../dozu-ui-service/src/components/upgrade-plan/UpgradePlanModal.tsx#L1>) | UpgradePlanModal | 84 source closures; see JSON |
| [dozu-ui-service/src/components/upload/DialogImportFile.tsx:1](<../../dozu-ui-service/src/components/upload/DialogImportFile.tsx#L1>) | MAX_FILE_SIZE_MB, ALLOWED_FILE_TYPES, ALLOWED_MIME_TYPES, DialogImportFile | 0 source closures; see JSON |
| [dozu-ui-service/src/contexts/auth/AuthContext.tsx:1](<../../dozu-ui-service/src/contexts/auth/AuthContext.tsx#L1>) | AuthContext, AuthProvider | 84 source closures; see JSON |
| [dozu-ui-service/src/contexts/class-based/ClassBasedContext.tsx:1](<../../dozu-ui-service/src/contexts/class-based/ClassBasedContext.tsx#L1>) | ClassBasedContext, ClassBasedProvider | 8 source closures; see JSON |
| [dozu-ui-service/src/contexts/gamification/GamificationContext.tsx:1](<../../dozu-ui-service/src/contexts/gamification/GamificationContext.tsx#L1>) | GamificationContext, GamificationProvider | 1 source closures; see JSON |
| [dozu-ui-service/src/contexts/tracking/UserTrackingContext.tsx:1](<../../dozu-ui-service/src/contexts/tracking/UserTrackingContext.tsx#L1>) | UserTrackingContext, UserTrackingProvider | 84 source closures; see JSON |
| [dozu-ui-service/src/core/ErrorBoundary.tsx:1](<../../dozu-ui-service/src/core/ErrorBoundary.tsx#L1>) | ErrorBoundary | 0 source closures; see JSON |
| [dozu-ui-service/src/core/error/AbstractErrorBoundary.tsx:1](<../../dozu-ui-service/src/core/error/AbstractErrorBoundary.tsx#L1>) | AbstractErrorBoundary | 0 source closures; see JSON |
| [dozu-ui-service/src/core/error/ErrorBoundary.tsx:1](<../../dozu-ui-service/src/core/error/ErrorBoundary.tsx#L1>) | ErrorBoundary | 0 source closures; see JSON |
| [dozu-ui-service/src/hoc/withAuth.tsx:1](<../../dozu-ui-service/src/hoc/withAuth.tsx#L1>) | DEFAULT_REDIRECT, DEFAULT_UNAUTHORIZED, DEFAULT_REDIRECT_BACK | 27 source closures; see JSON |
| [dozu-ui-service/src/hooks/generate/useGenerate.tsx:1](<../../dozu-ui-service/src/hooks/generate/useGenerate.tsx#L1>) | (anonymous/local declarations) | 1 source closures; see JSON |
| [dozu-ui-service/src/hooks/generate/useGenerateStream.tsx:1](<../../dozu-ui-service/src/hooks/generate/useGenerateStream.tsx#L1>) | (anonymous/local declarations) | 84 source closures; see JSON |
| [dozu-ui-service/src/hooks/upload/useUploadAttachmentFiles.tsx:1](<../../dozu-ui-service/src/hooks/upload/useUploadAttachmentFiles.tsx#L1>) | (anonymous/local declarations) | 5 source closures; see JSON |
| [dozu-ui-service/src/hooks/use-mobile.tsx:1](<../../dozu-ui-service/src/hooks/use-mobile.tsx#L1>) | MOBILE_BREAKPOINT | 84 source closures; see JSON |
| [dozu-ui-service/src/hooks/useActivePomodoro.tsx:1](<../../dozu-ui-service/src/hooks/useActivePomodoro.tsx#L1>) | (anonymous/local declarations) | 84 source closures; see JSON |
| [dozu-ui-service/src/hooks/usePdfReader.tsx:1](<../../dozu-ui-service/src/hooks/usePdfReader.tsx#L1>) | (anonymous/local declarations) | 84 source closures; see JSON |
| [dozu-ui-service/src/hooks/useRetry.tsx:1](<../../dozu-ui-service/src/hooks/useRetry.tsx#L1>) | DEFAULT_MAX_RETRIES, DEFAULT_DELAY | 1 source closures; see JSON |
| [dozu-ui-service/src/hooks/useUploadFile.tsx:1](<../../dozu-ui-service/src/hooks/useUploadFile.tsx#L1>) | (anonymous/local declarations) | 0 source closures; see JSON |
| [dozu-ui-service/src/layouts/CustomLayout.tsx:1](<../../dozu-ui-service/src/layouts/CustomLayout.tsx#L1>) | CustomPage | 0 source closures; see JSON |
| [dozu-ui-service/src/layouts/DefaultLayout.tsx:1](<../../dozu-ui-service/src/layouts/DefaultLayout.tsx#L1>) | DefaultLayout | 84 source closures; see JSON |
| [dozu-ui-service/src/layouts/components/Footer.tsx:1](<../../dozu-ui-service/src/layouts/components/Footer.tsx#L1>) | Footer | 84 source closures; see JSON |
| [dozu-ui-service/src/layouts/components/Header.tsx:1](<../../dozu-ui-service/src/layouts/components/Header.tsx#L1>) | Header | 84 source closures; see JSON |
| [dozu-ui-service/src/lib/providers/theme.tsx:1](<../../dozu-ui-service/src/lib/providers/theme.tsx#L1>) | ThemeProvider | 84 source closures; see JSON |
| [dozu-ui-service/src/stores/hooks.tsx:1](<../../dozu-ui-service/src/stores/hooks.tsx#L1>) | (anonymous/local declarations) | 84 source closures; see JSON |
| [dozu-ui-service/src/stores/registry.store.tsx:1](<../../dozu-ui-service/src/stores/registry.store.tsx#L1>) | (anonymous/local declarations) | 84 source closures; see JSON |
| [dozu-ui-service/src/utils/import/flashcardContentConverter.tsx:1](<../../dozu-ui-service/src/utils/import/flashcardContentConverter.tsx#L1>) | FlashcardContentConverter | 84 source closures; see JSON |

## Hooks, contexts and providers

| Source | Declarations | Page reachability |
| --- | --- | --- |
| [dozu-ui-service/src/app/Providers.tsx:1](<../../dozu-ui-service/src/app/Providers.tsx#L1>) | Providers | 84 |
| [dozu-ui-service/src/app/StoreProvider.tsx:1](<../../dozu-ui-service/src/app/StoreProvider.tsx#L1>) | StoreProvider, storeRef | 84 |
| [dozu-ui-service/src/app/[locale]/admin/llm-models/components/CreateEditLlmModelDialog.tsx:1](<../../dozu-ui-service/src/app/[locale]/admin/llm-models/components/CreateEditLlmModelDialog.tsx#L1>) | CreateEditLlmModelDialog, isEditMode, fetchProviders, response, error, resetForm, errorMessage, handleSubmit, selectedProvider, updateData, createData, loading, colors | 1 |
| [dozu-ui-service/src/app/[locale]/admin/llm-providers/components/CreateEditLlmProviderDialog.tsx:1](<../../dozu-ui-service/src/app/[locale]/admin/llm-providers/components/CreateEditLlmProviderDialog.tsx#L1>) | CreateEditLlmProviderDialog, isEditMode, resetForm, errorMessage, handleSubmit, updateData, loading | 1 |
| [dozu-ui-service/src/app/[locale]/admin/llm-providers/components/DeleteProviderDialog.tsx:1](<../../dozu-ui-service/src/app/[locale]/admin/llm-providers/components/DeleteProviderDialog.tsx#L1>) | DeleteProviderDialog, config | 1 |
| [dozu-ui-service/src/app/[locale]/admin/llm-providers/components/LlmProviderFilter.tsx:1](<../../dozu-ui-service/src/app/[locale]/admin/llm-providers/components/LlmProviderFilter.tsx#L1>) | LlmProviderFilter, handleFilterChange, newFilters, clearFilters, clearedFilters, hasActiveFilters, filterValue | 1 |
| [dozu-ui-service/src/app/[locale]/auth/hooks/useAuthStorage.ts:1](<../../dozu-ui-service/src/app/[locale]/auth/hooks/useAuthStorage.ts#L1>) | useAuthStorage, setAuthData, userWithTimestamp, updateUser, markOnboardingComplete, updateLastLogin, clearAuthData, isAuthenticated | 84 |
| [dozu-ui-service/src/app/[locale]/auth/hooks/useGoogleAuth.ts:1](<../../dozu-ui-service/src/app/[locale]/auth/hooks/useGoogleAuth.ts#L1>) | useGoogleAuth, searchParams, code, redirectTo, url, loginWithGoogle, response, userData, error, handleSuccessfulLogin | 2 |
| [dozu-ui-service/src/app/[locale]/auth/hooks/useLogin.ts:1](<../../dozu-ui-service/src/app/[locale]/auth/hooks/useLogin.ts#L1>) | useLogin, t, searchParams, handleSuccessfulLogin, redirectTo, decodedPath, login, response, userData, error | 1 |
| [dozu-ui-service/src/app/[locale]/auth/hooks/useUserSession.ts:1](<../../dozu-ui-service/src/app/[locale]/auth/hooks/useUserSession.ts#L1>) | useUserSession, authStorage, login, logout, updateProfile | 4 |
| [dozu-ui-service/src/app/[locale]/feynman/[topicId]/hooks/useFeynmanService.tsx:1](<../../dozu-ui-service/src/app/[locale]/feynman/[topicId]/hooks/useFeynmanService.tsx#L1>) | useFeynmanService, fetch, update, storage | 1 |
| [dozu-ui-service/src/app/[locale]/flashcards/learning/hooks/useQuizMilestones.ts:1](<../../dozu-ui-service/src/app/[locale]/flashcards/learning/hooks/useQuizMilestones.ts#L1>) | keyBaseline, keyLastRemaining, keyHalf, readNum, raw, n, writeNum, readBaseline, writeBaseline, readLastRemaining, writeLastRemaining, loadStatus, saveStatus, dedupeById, seen, id, normalizeToDue, buildPayloadFromQuizCards, normalized, useQuizMilestones, router, refreshBacklogCount, res, showCatchUp, half, percentLabel, isGenerating, closeSession, ensureBaseline, resetTo, onStudiedProgress, studiedSoFar, hasBaseline, firstSlice, confirmHalfQuiz,  | 84 |
| [dozu-ui-service/src/app/[locale]/games/brain-chase/context/brainChaseContext.tsx:1](<../../dozu-ui-service/src/app/[locale]/games/brain-chase/context/brainChaseContext.tsx#L1>) | sampleQuestions, DEFAULT_SETTINGS, BrainChaseContext, BrainChaseProvider, gameQuestions, wrongAnswers, genericAnswers, available, allAnswers, correctAnswerIdx, generateShuffledQuestions, length, shuffledQuestions, tempFirstCurrentQuestion, index, randomIndex, formattedAnswers, currentQ, correctIndex, currentQuestion, resetStateGame, startGame, handleShuffledQuestionGame, resetGame, onCorrectAnswer, onIncorrectAnswer, newErrorsRemaining, updateSet | 84 |
| [dozu-ui-service/src/app/[locale]/games/memory-match/context/MemoryMatchContext.tsx:1](<../../dozu-ui-service/src/app/[locale]/games/memory-match/context/MemoryMatchContext.tsx#L1>) | DEFAULT_SETTINGS, DEFAULT_STATS, DEFAULT_BATCH_STRATEGY, memoryMatchReducer, MemoryMatchContext, MemoryMatchProvider, gameTimerRef, flipTimeoutRef, gameStatusRef, isLoading, error, pauseGame, resumeGame, resetGame, topicIdNum, endGame, accuracy, canFlipCard, card, flipCard, newSelectedCards, isMatch, newMatchedCount, updateSettings, getGameProgress, startNextBatch, progress, nextBatchFlashcards, newBatch, memoryCards, completeBatch, completedBatc | 84 |
| [dozu-ui-service/src/app/[locale]/games/memory-match/hooks/useGameAnimations.ts:1](<../../dozu-ui-service/src/app/[locale]/games/memory-match/hooks/useGameAnimations.ts#L1>) | useGameAnimations, timersRef, clearCardTimer, existingTimer, setCardAnimation, timer, newMap, triggerMatchAnimation, triggerWrongMatchAnimation, getCardAnimation, flipAnimationStyles, useFadeInAnimation, animationClasses | 0 |
| [dozu-ui-service/src/app/[locale]/generate/hooks/useContentGeneration.ts:1](<../../dozu-ui-service/src/app/[locale]/generate/hooks/useContentGeneration.ts#L1>) | useContentGeneration, router, dispatch, tCommon, tClassFeed, classId, useFeedsHook, createFeed, handleCreateFeedClick, value, handleCancelFeedClick, contentType, isContentReady, handleParseData, handleRedirectAfterGenerateSuccess, handleInsertResourceContent, contentTypeResource, resolvedContentType, file, fileInfo, youtubePayload, websitePayload, textPayload, error, handleOnClickSave, contentData, result, topicInClass, topicId, attached, content | 84 |
| [dozu-ui-service/src/app/[locale]/generate/hooks/useGenerateFromExisting.ts:1](<../../dozu-ui-service/src/app/[locale]/generate/hooks/useGenerateFromExisting.ts#L1>) | useGenerateFromExisting, payloadStatus, regenerate, compressed | 84 |
| [dozu-ui-service/src/app/[locale]/generate/hooks/useReaderFile.tsx:1](<../../dozu-ui-service/src/app/[locale]/generate/hooks/useReaderFile.tsx#L1>) | useReaderFile, dispatch, loadPdfLibrary, error, handleExtractDocxToText, file, reader, arrayBuffer, result, content, err, handleExtractTxtToText, handleExtractPdfToText, pdfGetDocument, pdf, fullText, i, page, textContent, textItems, handleFileChange | 84 |
| [dozu-ui-service/src/app/[locale]/generate/hooks/useReduxStore.tsx:1](<../../dozu-ui-service/src/app/[locale]/generate/hooks/useReduxStore.tsx#L1>) | useCardImportDispatch, useCardImportSelector, useAppStore | 84 |
| [dozu-ui-service/src/app/[locale]/generate/hooks/useUploadConvertFileFormat.tsx:1](<../../dozu-ui-service/src/app/[locale]/generate/hooks/useUploadConvertFileFormat.tsx#L1>) | appendFields, useUploadConvertFile, upload, formData, response, data, error, reset | 84 |
| [dozu-ui-service/src/app/[locale]/generate/hooks/useUrlToPdfConverter.ts:1](<../../dozu-ui-service/src/app/[locale]/generate/hooks/useUrlToPdfConverter.ts#L1>) | API_CONVERT_URL_ENDPOINT, PDF_MIME_TYPE, generateFilename, hostname, timestamp, isValidUrl, createPdfBlob, convertBlobToFile, useUrlToPdfConverter, clearError, fetchPdfFromApi, response, convertUrlToPdf, errorMessage, arrayBuffer, pdfBlob, filename, file, err | 84 |
| [dozu-ui-service/src/app/[locale]/home/components/actions/context/ActionContext.tsx:1](<../../dozu-ui-service/src/app/[locale]/home/components/actions/context/ActionContext.tsx#L1>) | createActionStore, ActionContext, ActionProvider, router, storeRef, useActionStore, store | 1 |
| [dozu-ui-service/src/app/[locale]/home/components/actions/hooks/useToastManager.tsx:1](<../../dozu-ui-service/src/app/[locale]/home/components/actions/hooks/useToastManager.tsx#L1>) | useToastManager, toastManager, id | 1 |
| [dozu-ui-service/src/app/[locale]/home/components/actions/hooks/useUploadConvertFileFormat.tsx:1](<../../dozu-ui-service/src/app/[locale]/home/components/actions/hooks/useUploadConvertFileFormat.tsx#L1>) | appendFields, useUploadConvertFile, upload, formData, response, data, error, reset | 1 |
| [dozu-ui-service/src/app/[locale]/home/components/actions/hooks/useUploadMediaFile.tsx:1](<../../dozu-ui-service/src/app/[locale]/home/components/actions/hooks/useUploadMediaFile.tsx#L1>) | useUploadMediaFile, t, toastManager, validateAudioFile, validated, validateFile, handleProcessingContent, fileName, topic, uploadToastId, fileUploadResult, transcriptSegments, payload, processFiles, file, handleDragOver, handleDragEnter, handleDragLeave, handleFileChange, selectedFiles, handleDrop, droppedFiles | 1 |
| [dozu-ui-service/src/app/[locale]/mindmap/context/MindMapContext.tsx:1](<../../dozu-ui-service/src/app/[locale]/mindmap/context/MindMapContext.tsx#L1>) | MindMapContext, useMindMapContext, context, MindMapProvider, router, params, topicId, initialNodes, initialEdges, urlOfSSEGenerateJob, jobId, extractTextByRange, textRangePages, err, initializeMindmap, mindmapData, nodeStatsData, error, result, id, topicError, saveMindmap, payload, loadPdfDocument, fileContent, response, blob, filename, file, blobUrl, openFileSheet, closeFileSheet, openNodeSheet, closeNodeSheet, addChildNode, newNodeId, parentNod | 84 |
| [dozu-ui-service/src/app/[locale]/mindmap/hooks/useSetCenterOnRoot.ts:1](<../../dozu-ui-service/src/app/[locale]/mindmap/hooks/useSetCenterOnRoot.ts#L1>) | useSetCenterOnRoot, hasCentered, rootNode | 1 |
| [dozu-ui-service/src/app/[locale]/mindmap/hooks/useSetMindmapLayout.ts:1](<../../dozu-ui-service/src/app/[locale]/mindmap/hooks/useSetMindmapLayout.ts#L1>) | useSetMindmapLayout, onLayout, opts | 4 |
| [dozu-ui-service/src/app/[locale]/payment/hooks/usePayment.ts:1](<../../dozu-ui-service/src/app/[locale]/payment/hooks/usePayment.ts#L1>) | usePayment, dispatch, data, error, status, initializePayment, planSource, selectedPlan, paymentRequest, paymentData, err, updateSubscription | 1 |
| [dozu-ui-service/src/app/[locale]/payment/hooks/usePaymentWebhook.ts:1](<../../dozu-ui-service/src/app/[locale]/payment/hooks/usePaymentWebhook.ts#L1>) | usePaymentWebhook, pollingIntervalRef, urlEventSource, startPolling, pollPaymentStatus, response, data, error, stopPolling, startSSE, stopSSE, update | 0 |
| [dozu-ui-service/src/app/[locale]/profile/hooks/useTransactionHistory.ts:1](<../../dozu-ui-service/src/app/[locale]/profile/hooks/useTransactionHistory.ts#L1>) | useTransactionHistory, fetchTransactions, data, err, errorMessage | 2 |
| [dozu-ui-service/src/app/[locale]/schedule/hooks/useScheduleGeneration.ts:1](<../../dozu-ui-service/src/app/[locale]/schedule/hooks/useScheduleGeneration.ts#L1>) | useBatchScheduleGeneration, generateBatch, newLoading, newErrors, promises, response, error, errorMessage, results, newSchedules, getSchedule, getError, isLoading, clearSchedule, clearAll | 0 |
| [dozu-ui-service/src/app/[locale]/teacher/feeds/hooks/useCreateFeed.tsx:1](<../../dozu-ui-service/src/app/[locale]/teacher/feeds/hooks/useCreateFeed.tsx#L1>) | useCreateFeed, tCommon, open, close, onSuccess, submit, value, applyCreate, currentFeeds, result | 84 |
| [dozu-ui-service/src/app/[locale]/teacher/feeds/hooks/useDeleteFeed.tsx:1](<../../dozu-ui-service/src/app/[locale]/teacher/feeds/hooks/useDeleteFeed.tsx#L1>) | useDeleteFeed, open, close, onSuccess, submit, value, applyDelete, currentFeeds, feedsFiltered | 84 |
| [dozu-ui-service/src/app/[locale]/teacher/feeds/hooks/useFeeds.tsx:1](<../../dozu-ui-service/src/app/[locale]/teacher/feeds/hooks/useFeeds.tsx#L1>) | useFeeds, createFeed, updateFeed, deleteFeed, useGroupLabel, tFeed | 84 |
| [dozu-ui-service/src/app/[locale]/teacher/feeds/hooks/useUpdateFeed.tsx:1](<../../dozu-ui-service/src/app/[locale]/teacher/feeds/hooks/useUpdateFeed.tsx#L1>) | useUpdateFeed, tCommon, open, close, onSuccess, submit, value, applyUpdate, currentFeeds, feedsUpdated | 84 |
| [dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/quiz/context/QuizWorkspaceContext.tsx:1](<../../dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/quiz/context/QuizWorkspaceContext.tsx#L1>) | QuizWorkspaceContext, QuizWorkspaceProvider, value, useQuizWorkspace, ctx, useOptionalQuizWorkspace | 84 |
| [dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/quiz/quiz-generate/hooks/useQuizRecommendation.ts:1](<../../dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/quiz/quiz-generate/hooks/useQuizRecommendation.ts#L1>) | useQuizRecommendation | 3 |
| [dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/context/GenerateContext.tsx:1](<../../dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/context/GenerateContext.tsx#L1>) | GenerateContext, GenerateProvider, DEFAULT_LIST_TYPE, DEFAULT_DIFFICULT, DEFAULT_NUMBER_OF_ITEM, updateOption, useGenerateContext, context | 84 |
| [dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/context/TopicWorkspaceContext.tsx:1](<../../dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/context/TopicWorkspaceContext.tsx#L1>) | TopicWorkspaceContext, DEFAULT_TAB, ALLOWED_TABS, TopicWorkspaceProvider, searchParams, activeTab, raw, topicIdRef, contentTextOrigin, selectionContentTimestampRef, setSelectionContentTimestamp, setTopicId, getLearningMaterialContent, getContentReference, reference, timestamp, getCurrentPosition, value, useTopicWorkspace, context | 84 |
| [dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/context/useRequireFlashcardContent.tsx:1](<../../dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/context/useRequireFlashcardContent.tsx#L1>) | useRequireFlashcards, context, useRequireLearningFlashcards, useRequireAnkiSettings | 84 |
| [dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/context/useRequireTopic.tsx:1](<../../dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/context/useRequireTopic.tsx#L1>) | useRequireTopic, context | 84 |
| [dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/hooks/flashcard/useBatchFlashcardsForNode.tsx:1](<../../dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/hooks/flashcard/useBatchFlashcardsForNode.tsx#L1>) | useBatchFlashcardsForNode, dataWithNodeId, onError, onSuccess | 3 |
| [dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/hooks/flashcard/useBatchFlashcardsForTopic.tsx:1](<../../dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/hooks/flashcard/useBatchFlashcardsForTopic.tsx#L1>) | useBatchFlashcardsForTopic, onError, onSuccess | 84 |
| [dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/hooks/media/useMediaPlayer.tsx:1](<../../dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/hooks/media/useMediaPlayer.tsx#L1>) | useMediaPlayer, controllerRef, registerPlayer, seekTo, play | 84 |
| [dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/hooks/tiptap/useCommandOptions.tsx:1](<../../dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/hooks/tiptap/useCommandOptions.tsx#L1>) | useCommandOptions, options, result | 3 |
| [dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/hooks/tiptap/useTiptapOptions.tsx:1](<../../dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/hooks/tiptap/useTiptapOptions.tsx#L1>) | useTiptapOptions, selector, options | 3 |
| [dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/hooks/useAnkiSettings.tsx:1](<../../dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/hooks/useAnkiSettings.tsx#L1>) | useAnkiSettings, currentAnkiSetting | 84 |
| [dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/hooks/useFlashCardWorkSpace.tsx:1](<../../dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/hooks/useFlashCardWorkSpace.tsx#L1>) | useFlashCardWorkSpace, flashcardContentLoading, flashcardContentError, onReviewCard, updatedLearningFlashcards, inserted, i, card, applyCreate, applyUpdate, updatedFlashcard, front, back, imageUrl, nodeId, applyFilter, applyCreateForLearning, result, createdItem, onBatchFlashcardsSuccess, updatedMap, deletedSet, onCreateFlashcardsSuccess | 84 |
| [dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/hooks/useGamesWorkSpace.tsx:1](<../../dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/hooks/useGamesWorkSpace.tsx#L1>) | useGamesWorkSpace, selectGame, resetGame | 84 |
| [dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/hooks/useLearningOptions.tsx:1](<../../dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/hooks/useLearningOptions.tsx#L1>) | useLearningOptions, trackingOptions | 84 |
| [dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/hooks/useMultiNodeFlashcardsGenerate.tsx:1](<../../dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/hooks/useMultiNodeFlashcardsGenerate.tsx#L1>) | useMultiNodeFlashcardsGenerate, validateNodeIds, ok, message, type, data, id, node, validateNodeRanges, start, end, prepareGeneratedDataForPdf, nodesData, nodeFound, startSection, endPageContent, endSection, prepareGeneratedDataForMediaSegments, startSegmentContent, endSegmentContent, prepareGeneratedData, validateNodeIdsResult, nodesForGeneration, validateNodeRangesResult, content, onHandleBeforeGenerate, onError | 3 |
| [dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/hooks/useNote.tsx:1](<../../dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/hooks/useNote.tsx#L1>) | useUpdateNoteAsync, onError, onSuccess | 3 |
| [dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/hooks/useNoteReferences.ts:1](<../../dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/hooks/useNoteReferences.ts#L1>) | useNoteReferences, REFERENCE_STYLE_ID, addedStyle, style, addReferenceClickHandlers, refElements, encodedRef, reference, keyboardEvent, refText, observer | 3 |
| [dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/hooks/useNoteWorkspace.tsx:1](<../../dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/hooks/useNoteWorkspace.tsx#L1>) | useNoteWorkspace | 84 |
| [dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/hooks/usePdfMaterial.tsx:1](<../../dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/hooks/usePdfMaterial.tsx#L1>) | usePdfMaterial, pdfPageTexts, onPageNumberChange | 84 |
| [dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/hooks/useQuizWorkspace.tsx:1](<../../dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/hooks/useQuizWorkspace.tsx#L1>) | useQuizWorkspaceState | 84 |
| [dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/hooks/useSelectMenu.tsx:1](<../../dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/hooks/useSelectMenu.tsx#L1>) | GenerateFlashcards, useSelectMenu, getCleanedContent, onGenerateFlashcardsSuccess, onAddToNoteClick, reference, cleanedContent, escapeHtml, escapedContent, htmlContent, currentContent, newContent, GenerateFlashcardsComponent, GenerateQuizComponent, AddToNoteComponent | 3 |
| [dozu-ui-service/src/app/[locale]/topics/hooks/useCreateTopic.tsx:1](<../../dozu-ui-service/src/app/[locale]/topics/hooks/useCreateTopic.tsx#L1>) | useCreateTopic, validateTopic, tCommon, tTopic, topicLabel, open, close, submit, applyCreate, currentTopics | 10 |
| [dozu-ui-service/src/app/[locale]/topics/hooks/useDeleteTopic.tsx:1](<../../dozu-ui-service/src/app/[locale]/topics/hooks/useDeleteTopic.tsx#L1>) | useDeleteTopic, tCommon, tTopic, topicLabel, open, close, submit, applyDelete, currentTopics, topicsFiltered | 10 |
| [dozu-ui-service/src/app/[locale]/topics/hooks/useSelectPackageForTopic.tsx:1](<../../dozu-ui-service/src/app/[locale]/topics/hooks/useSelectPackageForTopic.tsx#L1>) | useSelectPackageForTopic, open, close | 10 |
| [dozu-ui-service/src/app/[locale]/topics/hooks/useTopicDetails.tsx:1](<../../dozu-ui-service/src/app/[locale]/topics/hooks/useTopicDetails.tsx#L1>) | useTopicDetails, open, selectingTopic, close | 10 |
| [dozu-ui-service/src/app/[locale]/topics/hooks/useTopics.tsx:1](<../../dozu-ui-service/src/app/[locale]/topics/hooks/useTopics.tsx#L1>) | useTopics, fetchFn, createFn, createTopic, updateFn, updateTopic, deleteFn, deleteTopic, showTopicDetails, selectPackage, useValidateTopic, tCommon | 10 |
| [dozu-ui-service/src/app/[locale]/topics/hooks/useUpdateTopic.tsx:1](<../../dozu-ui-service/src/app/[locale]/topics/hooks/useUpdateTopic.tsx#L1>) | useUpdateTopic, validateTopic, tCommon, tTopic, topicLabel, open, close, submit, applyUpdate, currentTopics, topicsUpdated | 10 |
| [dozu-ui-service/src/components/providers/GamificationWrapper.tsx:1](<../../dozu-ui-service/src/components/providers/GamificationWrapper.tsx#L1>) | GamificationWrapper | 0 |
| [dozu-ui-service/src/components/tiptap-node/image-upload-node/image-upload-node.tsx:1](<../../dozu-ui-service/src/components/tiptap-node/image-upload-node/image-upload-node.tsx#L1>) | useFileUpload, uploadFile, error, abortController, fileId, newFileItem, url, uploadFiles, uploadPromises, results, removeFileItem, fileToRemove, clearAllFiles, CloudUploadIcon, FileIcon, FileCornerIcon, ImageUploadDragArea, handleDragEnter, handleDragLeave, handleDragOver, handleDrop, files, ImageUploadPreview, formatFileSize, k, sizes, i, DropZoneContent, ImageUploadNode, inputRef, extension, uploadOptions, handleUpload, urls, pos, imageNodes, f | 3 |
| [dozu-ui-service/src/components/tiptap-ui-primitive/tooltip/tooltip.tsx:1](<../../dozu-ui-service/src/components/tiptap-ui-primitive/tooltip/tooltip.tsx#L1>) | useTooltip, open, setOpen, data, context, hover, focus, dismiss, role, interactions, TooltipContext, useTooltipContext, Tooltip, tooltip, TooltipTrigger, childrenRef, ref, dataAttributes, TooltipContent, content | 3 |
| [dozu-ui-service/src/components/tiptap-ui/image-upload-button/use-image-upload.ts:1](<../../dozu-ui-service/src/components/tiptap-ui/image-upload-button/use-image-upload.ts#L1>) | IMAGE_UPLOAD_SHORTCUT_KEY, canInsertImage, isImageActive, insertImage, shouldShowButton, useImageUpload, isMobile, canInsert, isActive, handleSelectionUpdate, handleImage, success | 3 |
| [dozu-ui-service/src/components/ui/LocaleFontProvider.tsx:1](<../../dozu-ui-service/src/components/ui/LocaleFontProvider.tsx#L1>) | LocaleFontProvider, locale, fontClass, useLocaleFont | 84 |
| [dozu-ui-service/src/components/ui/carousel.tsx:1](<../../dozu-ui-service/src/components/ui/carousel.tsx#L1>) | CarouselContext, useCarousel, context, Carousel, onSelect, scrollPrev, scrollNext, handleKeyDown, CarouselContent, CarouselItem, CarouselPrevious, CarouselNext | 1 |
| [dozu-ui-service/src/components/ui/full-calendar.tsx:1](<../../dozu-ui-service/src/components/ui/full-calendar.tsx#L1>) | monthEventVariants, dayEventVariants, Context, Calendar, changeView, handleGetGenerateScheduleEvent, startDateOfWeek, endDateOfWeek, request, handleResponseGetSchedule, dataEvents, handleChangeWeek, dateNextWeek, useCalendar, CalendarViewTrigger, CalendarNextTrigger, next, CalendarPrevTrigger, prev, CalendarTodayTrigger, jumpToToday, handleClickCallback, CalendarCurrentDate, TimeTable, now, getDaysInMonth, startOfMonthDate, startOfWeekForMonth, c | 4 |
| [dozu-ui-service/src/components/ui/sidebar.tsx:1](<../../dozu-ui-service/src/components/ui/sidebar.tsx#L1>) | SIDEBAR_COOKIE_NAME, SIDEBAR_COOKIE_MAX_AGE, SIDEBAR_WIDTH, SIDEBAR_WIDTH_MOBILE, SIDEBAR_WIDTH_ICON, SIDEBAR_KEYBOARD_SHORTCUT, SidebarContext, useSidebar, context, SidebarProvider, isMobile, open, setOpen, openState, toggleSidebar, handleKeyDown, state, contextValue, Sidebar, SidebarTrigger, SidebarRail, SidebarInset, SidebarInput, SidebarHeader, SidebarFooter, SidebarSeparator, SidebarContent, SidebarGroup, SidebarGroupLabel, Comp, SidebarGrou | 84 |
| [dozu-ui-service/src/components/ui/toast.tsx:1](<../../dozu-ui-service/src/components/ui/toast.tsx#L1>) | ToastProvider, ToastViewport, toastVariants, Toast, ToastAction, ToastClose, ToastTitle, ToastDescription | 84 |
| [dozu-ui-service/src/components/ui/tooltip.tsx:1](<../../dozu-ui-service/src/components/ui/tooltip.tsx#L1>) | TooltipProvider, Tooltip, TooltipTrigger, TooltipContent | 84 |
| [dozu-ui-service/src/contexts/auth/AuthContext.tsx:1](<../../dozu-ui-service/src/contexts/auth/AuthContext.tsx#L1>) | AuthContext, AuthProvider, checkAuthStatus, error, getUserCurrentPlan, subscriptionInfoCache, planWithFeatures, hasRole, hasPermission, contextValue, userType, isNewUser, hasCompletedOnboarding, useAuth, context | 84 |
| [dozu-ui-service/src/contexts/class-based/ClassBasedContext.tsx:1](<../../dozu-ui-service/src/contexts/class-based/ClassBasedContext.tsx#L1>) | ClassBasedContext, ClassBasedProvider, params, idParam, idStr, classId, contextValue, useClassBased, context | 8 |
| [dozu-ui-service/src/contexts/class-based/index.ts:1](<../../dozu-ui-service/src/contexts/class-based/index.ts#L1>) |  | 8 |
| [dozu-ui-service/src/contexts/gamification/GamificationContext.tsx:1](<../../dozu-ui-service/src/contexts/gamification/GamificationContext.tsx#L1>) | GamificationContext, GamificationProvider, lastUpdate, today, refreshStreakData, userString, userObject, userId, data, error, errorMessage, refreshPointsData, updateStreak, lastUpdateKey, result, buyStreakFreeze, success, getStudentGamificationStats, getStudentStreaks, getClassStudentStreaks, statsPromises, response, statsResults, results, stats, buyStreakFreezeForStudent, contextValue, useGamification, context, useStreakTracking, usePointsManage | 1 |
| [dozu-ui-service/src/contexts/tracking/UserTrackingContext.tsx:1](<../../dozu-ui-service/src/contexts/tracking/UserTrackingContext.tsx#L1>) | UserTrackingContext, UserTrackingProvider, activityRef, isTrackingRef, hasDataBeenSent, itemsStudiedRef, correctAnswersRef, sessionStartTimeRef, updateItemsStudied, updateCorrectAnswers, resetLearningSession, newStartTime, newEngagementScore, newClicksPerMinute, newMouseDistance, prev, sendTrackingData, latestActivity, wasTracking, finalEngagementScore, finalClicksPerMinute, data, sendLearningTrackingData, error, handleSaveTrackingProgressLearnin | 84 |
| [dozu-ui-service/src/hooks/generate/normalizeStreamByStructure.ts:1](<../../dozu-ui-service/src/hooks/generate/normalizeStreamByStructure.ts#L1>) | normalizeLLMChunk, values, normalizeAndExtract, extractedItems, i, item, validated, extracted, trimmed, parsed, objects, normalized, createJsonExtractor, createObjectExtractor, obj, field, normalizeFromString, cleaned, items, sanitizeList, splitByLogicalDelimiters, buffer, pushBuffer, char, j, k, looksLikeJsonArray, buildResponse, emptyResponse, extractCompleteObjectsFromStream, depth, objectStart, inString, escapeNext, objectStr | 84 |
| [dozu-ui-service/src/hooks/generate/type.ts:1](<../../dozu-ui-service/src/hooks/generate/type.ts#L1>) |  | 84 |
| [dozu-ui-service/src/hooks/generate/useGenerate.tsx:1](<../../dozu-ui-service/src/hooks/generate/useGenerate.tsx#L1>) | useGenerate, t, executeGenerate, compressedContent, isGenerating, jobId, dataGenerated, dataValidated, validateResult | 1 |
| [dozu-ui-service/src/hooks/generate/useGenerateStream.tsx:1](<../../dozu-ui-service/src/hooks/generate/useGenerateStream.tsx#L1>) | useGenerateStream, t, chunkText, executeGenerate, isGenerating, reset, parsed | 84 |
| [dozu-ui-service/src/hooks/helper.ts:1](<../../dozu-ui-service/src/hooks/helper.ts#L1>) | callApiAsync, isWriteMethod, hasBody, config, response, error | 84 |
| [dozu-ui-service/src/hooks/type.d.ts:1](<../../dozu-ui-service/src/hooks/type.d.ts#L1>) |  | 0 |
| [dozu-ui-service/src/hooks/upload/useUploadAttachmentFiles.tsx:1](<../../dozu-ui-service/src/hooks/upload/useUploadAttachmentFiles.tsx#L1>) | useUploadAttachmentFiles, tCommon, execute, uploadPromises, fileInfo, fileMetadatas, error, message | 5 |
| [dozu-ui-service/src/hooks/use-is-breakpoint.ts:1](<../../dozu-ui-service/src/hooks/use-is-breakpoint.ts#L1>) | useIsBreakpoint, query, mql, onChange | 3 |
| [dozu-ui-service/src/hooks/use-mobile.tsx:1](<../../dozu-ui-service/src/hooks/use-mobile.tsx#L1>) | MOBILE_BREAKPOINT, useIsMobile, mql, onChange | 84 |
| [dozu-ui-service/src/hooks/use-tiptap-editor.ts:1](<../../dozu-ui-service/src/hooks/use-tiptap-editor.ts#L1>) | useTiptapEditor, mainEditor, editorState, selector | 3 |
| [dozu-ui-service/src/hooks/use-toast.ts:1](<../../dozu-ui-service/src/hooks/use-toast.ts#L1>) | TOAST_LIMIT, TOAST_REMOVE_DELAY, actionTypes, count, genId, toastTimeouts, addToRemoveQueue, timeout, reducer, listeners, memoryState, dispatch, toast, id, update, dismiss, useToast, index | 84 |
| [dozu-ui-service/src/hooks/useActivePomodoro.tsx:1](<../../dozu-ui-service/src/hooks/useActivePomodoro.tsx#L1>) | useActivePomodoro, dispatch | 84 |
| [dozu-ui-service/src/hooks/useAuthNavigation.ts:1](<../../dozu-ui-service/src/hooks/useAuthNavigation.ts#L1>) | useAuthNavigation, router, pathname, getCurrentLocale, segments, potentialLocale, error, navigate, hasRole, normalizedRole, isAdmin, isTeacher, handlePostLogin, chain, firstStep, destination, fallbackPath, handlePostRegistration, redirectPath, handleSkipOnboarding, nextDestination, handleOnboardingComplete, handleWelcomeComplete, skipCurrentStep, forceCompleteRedirectChain, navigateToHome, homePath, navigateToLogin, loginPath, navigateToWelcome,  | 5 |
| [dozu-ui-service/src/hooks/useClassInvite.ts:1](<../../dozu-ui-service/src/hooks/useClassInvite.ts#L1>) | useClassInvite, generateInviteLink, inviteLink, error, regenerateInviteLink, sendEmailInvites, results, searchUsers, searchResults, selectUser, removeSelectedUser, clearSelectedUsers, sendSelectedUserInvites, emails, cancelInvite, resendInvite, clearError | 1 |
| [dozu-ui-service/src/hooks/useClickOutSide.ts:1](<../../dozu-ui-service/src/hooks/useClickOutSide.ts#L1>) | useClickOutSide, ref, handleClickOutSide | 84 |
| [dozu-ui-service/src/hooks/useEventSource.ts:1](<../../dozu-ui-service/src/hooks/useEventSource.ts#L1>) | BASE_URL, DEFAULT_TIMEOUT_MS, useEventSource, eventSourceRef, eventSource, timeoutMs, timeoutId, parsedData, error | 84 |
| [dozu-ui-service/src/hooks/useEventSourceStream.ts:1](<../../dozu-ui-service/src/hooks/useEventSourceStream.ts#L1>) | BASE_URL, RetirableError, FatalError, useEventSourceStream, timeoutIdRef, abortControllerRef, handleEventMessage, parsedData, error, execute, onopen, onmessage, onclose, onerror | 84 |
| [dozu-ui-service/src/hooks/useFetch.ts:1](<../../dozu-ui-service/src/hooks/useFetch.ts#L1>) | useFetch, selector, schema, shouldRun, abortControllerRef, fetchData, currentController, rawData, result, finalData, validationError, error | 84 |
| [dozu-ui-service/src/hooks/useGamification.ts:1](<../../dozu-ui-service/src/hooks/useGamification.ts#L1>) | useGamification, fetchAllData, defaultStreak, defaultPoints, stats, streak, points, err, updateStreak, result, buyStreakFreeze, success, awardPoints, fetchRank, leaderboardData, userIndex, useLeaderboard, fetchLeaderboard, data, usePointSystem, POINT_REWARDS, calculatePoints, getActionDescription, descriptions | 2 |
| [dozu-ui-service/src/hooks/useInterval.ts:1](<../../dozu-ui-service/src/hooks/useInterval.ts#L1>) | useInterval, savedCallback, id | 84 |
| [dozu-ui-service/src/hooks/useLanguageSwitcher.ts:1](<../../dozu-ui-service/src/hooks/useLanguageSwitcher.ts#L1>) | LANGS, useLanguageSwitcher, router, pathname, searchParams, code, buildHref, queryString, hashString, changeLocale, segments, hasLocal, basePath, safePath, extendPath, query, hash, href | 84 |
| [dozu-ui-service/src/hooks/useLearningStats.ts:1](<../../dozu-ui-service/src/hooks/useLearningStats.ts#L1>) | useLearningStats, getUserLearningStats, result, err, errorMessage, getClassLearningStats, getTopicLearningStats, getWeeklyLearningActivity | 1 |
| [dozu-ui-service/src/hooks/useLessonCompletion.ts:1](<../../dozu-ui-service/src/hooks/useLessonCompletion.ts#L1>) | useLessonCompletion, fetchLessonStats, stats, err, useClassLessonCompletion, fetchClassStats, useTopicLessonCompletion, fetchTopicStats | 0 |
| [dozu-ui-service/src/hooks/useLocalStorage.ts:1](<../../dozu-ui-service/src/hooks/useLocalStorage.ts#L1>) | useLocalStorage, item, error, setValue, valueToStore, removeValue, handleStorageChange | 84 |
| [dozu-ui-service/src/hooks/useNavigation.ts:1](<../../dozu-ui-service/src/hooks/useNavigation.ts#L1>) | useNavigation, router, navigateToTopicPage | 0 |
| [dozu-ui-service/src/hooks/useOnScreen.ts:1](<../../dozu-ui-service/src/hooks/useOnScreen.ts#L1>) | useOnScreen, element, observer | 0 |
| [dozu-ui-service/src/hooks/usePdfReader.tsx:1](<../../dozu-ui-service/src/hooks/usePdfReader.tsx#L1>) | usePdfReader, loadPdfLibrary, error, extractPdfText, pdfGetDocument, arrayBuffer, pdf, pages, actualStartPage, actualEndPage, fullText, pageTexts, i, pageText, page, textContent, textItems, handleExtractPdfToText, result, err, message, handleExtractPdfToTextByRange | 84 |
| [dozu-ui-service/src/hooks/usePost.ts:1](<../../dozu-ui-service/src/hooks/usePost.ts#L1>) | usePost, reset, validateRequest, validationError, callWithFunctionFormat, validateResponse, validatedData, execute, validatedRequestData, responseData, validatedResponse, error, message | 84 |
| [dozu-ui-service/src/hooks/usePrevious.ts:1](<../../dozu-ui-service/src/hooks/usePrevious.ts#L1>) | usePrevious, currentRef, previousRef | 0 |
| [dozu-ui-service/src/hooks/useProfile.ts:1](<../../dozu-ui-service/src/hooks/useProfile.ts#L1>) | useProfile, fetchProfile, profileData, err, errorMessage, updateProfile, updatedProfile, uploadAvatar, result, removeAvatar, changePassword, deleteAccount | 2 |
| [dozu-ui-service/src/hooks/useProgress.ts:1](<../../dozu-ui-service/src/hooks/useProgress.ts#L1>) | progressKeys, useProgressList, fetchData, result, err, useProgressById, useCreateProgress, createProgress, errorMessage, useUpdateProgress, updateProgress, useDeleteProgress, deleteProgress, useProgressStatistics, useDashboardStatistics, useDailyStudyRecords, useLearningMethodsDistribution, useWeeklyComparison, useCompletedTopics | 1 |
| [dozu-ui-service/src/hooks/useQuery.ts:1](<../../dozu-ui-service/src/hooks/useQuery.ts#L1>) | useQuery, fetchData, response, err | 0 |
| [dozu-ui-service/src/hooks/useQuizActivityWebSocket.ts:1](<../../dozu-ui-service/src/hooks/useQuizActivityWebSocket.ts#L1>) | useQuizActivityWebSocket, socketRef, reconnectAttemptsRef, maxReconnectAttempts, onActivityUpdateRef, onStudentJoinedRef, onStudentLeftRef, apiUrl, userId, socket, emitQuizActivity, currentAttemptId, payload, emitAttemptStarted, emitAnswerSaved, emitAttemptSubmitted, emitActivity, joinRoom, leaveRoom | 2 |
| [dozu-ui-service/src/hooks/useReaderFile.ts:1](<../../dozu-ui-service/src/hooks/useReaderFile.ts#L1>) | readFileAsArrayBuffer, reader, result, readFileAsText, useReaderFile, loadPdfLibrary, error, extractDocxText, arrayBuffer, content, extractTxtText, extractPdfText, pdfGetDocument, pdf, pages, actualStartPage, actualEndPage, fullText, i, page, textContent, textItems, handleExtractDocxToText, activeFile, err, message, handleExtractTxtToText, handleExtractPdfToText, handleFileChange, handleExtractPdfToTextByRange, execute, originalFile, extractedTex | 84 |
| [dozu-ui-service/src/hooks/useRedirectChain.ts:1](<../../dozu-ui-service/src/hooks/useRedirectChain.ts#L1>) | useRedirectChain, pathname, currentChain, getProgress, getChainInfo, isCurrentPageInChain, normalizedPath, validateCurrentStep, advanceToNextStep, nextDestination, updatedChain, skipCurrentStep, handlePageCompletion, clearChain, forceComplete, destination | 0 |
| [dozu-ui-service/src/hooks/useRetry.tsx:1](<../../dozu-ui-service/src/hooks/useRetry.tsx#L1>) | DEFAULT_MAX_RETRIES, DEFAULT_DELAY, useRetry, execute, lastError, attempt, result, error | 1 |
| [dozu-ui-service/src/hooks/useRoleChecker.ts:1](<../../dozu-ui-service/src/hooks/useRoleChecker.ts#L1>) | useRoleChecker | 84 |
| [dozu-ui-service/src/hooks/useSchedule.ts:1](<../../dozu-ui-service/src/hooks/useSchedule.ts#L1>) | TimeSlotSchema, FreeTimeSchema, PreferencesSchema, useGetSchedulePreferences, useUpdateSchedulePreferences | 1 |
| [dozu-ui-service/src/hooks/useSessionStorage.ts:1](<../../dozu-ui-service/src/hooks/useSessionStorage.ts#L1>) | useSessionStorage, item, error, setValue, valueToStore, removeValue, handleStorageChange | 84 |
| [dozu-ui-service/src/hooks/useStreakProgress.ts:1](<../../dozu-ui-service/src/hooks/useStreakProgress.ts#L1>) | useStreakProgress, trackLearningActivity, result, err, errorMessage, trackFlashcardSession, trackQuizCompletion, getUserLearningStreak, useFlashcardStreakTracking, useQuizStreakTracking, useLearningStreak | 3 |
| [dozu-ui-service/src/hooks/useStreakTracking.ts:1](<../../dozu-ui-service/src/hooks/useStreakTracking.ts#L1>) | useStreakTracking | 0 |
| [dozu-ui-service/src/hooks/useTimeOut.ts:1](<../../dozu-ui-service/src/hooks/useTimeOut.ts#L1>) | useTimeOut, callbackRef, timeoutRef, set, clear | 0 |
| [dozu-ui-service/src/hooks/useToggle.ts:1](<../../dozu-ui-service/src/hooks/useToggle.ts#L1>) | useToggle, toggleValue | 84 |
| [dozu-ui-service/src/hooks/useUploadFile.tsx:1](<../../dozu-ui-service/src/hooks/useUploadFile.tsx#L1>) | updateState, useFileUpload, appendFields, upload, formData, response, data, error, reset | 0 |
| [dozu-ui-service/src/hooks/useUserTracking.ts:1](<../../dozu-ui-service/src/hooks/useUserTracking.ts#L1>) | IDLE_THRESHOLD, ACTIVITY_SAMPLE_RATE, useUserTracking, intervalRef, lastMouseSampleRef, visibilityChangeCountRef, activeTimeRef, lastActiveTimeRef, updateActiveTime, now, timeDiff, handleMouseMove, newMovement, handleClick, target, clickEvent, handleScroll, scrollEvent, handleKeyDown, keyEvent, handleVisibilityChange, isVisible, checkIdleState, timeSinceLastActivity, startTracking, stopTracking, clearData, newData, exportData, engagementScore, cl | 84 |
| [dozu-ui-service/src/hooks/useWebSocket.ts:1](<../../dozu-ui-service/src/hooks/useWebSocket.ts#L1>) | useWebSocket, defaultSettings, settings, settingsRef, shouldShowNotification, currentSettings, socketRef, reconnectAttemptsRef, maxReconnectAttempts, currentUserIdRef, onNotificationRef, userId, apiUrl, socket | 0 |
| [dozu-ui-service/src/lib/providers/theme.tsx:1](<../../dozu-ui-service/src/lib/providers/theme.tsx#L1>) | ThemeProvider | 84 |
| [dozu-ui-service/src/services/class-based-learning/comment/comment.hooks.ts:1](<../../dozu-ui-service/src/services/class-based-learning/comment/comment.hooks.ts#L1>) | useGetCommentsByNode, useCreateComment, useGetSingleComment, useGetCommentReplies | 13 |
| [dozu-ui-service/src/services/class-based-learning/comment/publicComment.hooks.ts:1](<../../dozu-ui-service/src/services/class-based-learning/comment/publicComment.hooks.ts#L1>) | useAssignmentComments, query, useCreateAssignmentComment, createComment, result, useLearningMaterialComments, useCreateLearningMaterialComment, useSubmissionComments, useCreateSubmissionComment, useCommentById, useUpdateComment, updateCommentFn, response, err, errorMessage, useDeleteComment, deleteCommentFn | 13 |
| [dozu-ui-service/src/stores/features/subscription/useUpgradeModal.ts:1](<../../dozu-ui-service/src/stores/features/subscription/useUpgradeModal.ts#L1>) | useUpgradeModal, dispatch, openUpgradeModal | 84 |
| [dozu-ui-service/src/stores/features/subscription/useUpgradePlanModal.ts:1](<../../dozu-ui-service/src/stores/features/subscription/useUpgradePlanModal.ts#L1>) | useUpgradePlanModal, dispatch, router, isAlreadyFetchPlan, handleSelectPlan, onClose, openModalHandler, handleSetSelectedPlan, formatFeatureValue, value, calculateSavings, monthlyTotal, savings, formatPrice, symbol, getSelectedPlanName, selected | 84 |
| [dozu-ui-service/src/stores/hooks.tsx:1](<../../dozu-ui-service/src/stores/hooks.tsx#L1>) | useAppDispatch, useAppSelector, useAppStore | 84 |
| [dozu-ui-service/src/types/llm-admin/llmProvider.ts:1](<../../dozu-ui-service/src/types/llm-admin/llmProvider.ts#L1>) |  | 4 |

## Navigation sites

This includes dynamic expressions and event handlers. Route constants and config object values also require review; see configuration references below. Literal targets are evidence candidates, not validation of their destination.

| Source | Site | Literal/template target |
| --- | --- | --- |
| [dozu-ui-service/src/app/[locale]/activities/components/JoinActivityLink.tsx:50](<../../dozu-ui-service/src/app/[locale]/activities/components/JoinActivityLink.tsx#L50>) | url | joinUrl |
| [dozu-ui-service/src/app/[locale]/activities/components/QuestionDetailList.tsx:94](<../../dozu-ui-service/src/app/[locale]/activities/components/QuestionDetailList.tsx#L94>) | acc[question.accuracyLevel].push | (dynamic; see source) |
| [dozu-ui-service/src/app/[locale]/activities/join/[activityId]/page.tsx:50](<../../dozu-ui-service/src/app/[locale]/activities/join/[activityId]/page.tsx#L50>) | router.push | / |
| [dozu-ui-service/src/app/[locale]/activities/join/[activityId]/page.tsx:81](<../../dozu-ui-service/src/app/[locale]/activities/join/[activityId]/page.tsx#L81>) | router.push | `/activities/${params.activityId}/play` |
| [dozu-ui-service/src/app/[locale]/activities/join/[activityId]/page.tsx:221](<../../dozu-ui-service/src/app/[locale]/activities/join/[activityId]/page.tsx#L221>) | activity.quizType.replace | - |
| [dozu-ui-service/src/app/[locale]/admin/features/components/Columns.tsx:22](<../../dozu-ui-service/src/app/[locale]/admin/features/components/Columns.tsx#L22>) | type.replace | _ |
| [dozu-ui-service/src/app/[locale]/admin/feedback/components/feedback-content-cell.tsx:44](<../../dozu-ui-service/src/app/[locale]/admin/feedback/components/feedback-content-cell.tsx#L44>) | a.href | (dynamic; see source) |
| [dozu-ui-service/src/app/[locale]/admin/plans/[planId]/features/components/Columns.tsx:22](<../../dozu-ui-service/src/app/[locale]/admin/plans/[planId]/features/components/Columns.tsx#L22>) | type.replace | _ |
| [dozu-ui-service/src/app/[locale]/admin/plans/[planId]/features/page.tsx:57](<../../dozu-ui-service/src/app/[locale]/admin/plans/[planId]/features/page.tsx#L57>) | Link.href | /admin/plans |
| [dozu-ui-service/src/app/[locale]/admin/plans/components/Columns.tsx:65](<../../dozu-ui-service/src/app/[locale]/admin/plans/components/Columns.tsx#L65>) | Link.href | (dynamic; see source) |
| [dozu-ui-service/src/app/[locale]/admin/revenue/components/RevenueFilter.tsx:132](<../../dozu-ui-service/src/app/[locale]/admin/revenue/components/RevenueFilter.tsx#L132>) | to | weekEnd |
| [dozu-ui-service/src/app/[locale]/admin/revenue/components/RevenueFilter.tsx:319](<../../dozu-ui-service/src/app/[locale]/admin/revenue/components/RevenueFilter.tsx#L319>) | to | date |
| [dozu-ui-service/src/app/[locale]/admin/revenue/components/RevenueFilter.tsx:399](<../../dozu-ui-service/src/app/[locale]/admin/revenue/components/RevenueFilter.tsx#L399>) | to | weekEnd |
| [dozu-ui-service/src/app/[locale]/admin/revenue/components/RevenueFilter.tsx:518](<../../dozu-ui-service/src/app/[locale]/admin/revenue/components/RevenueFilter.tsx#L518>) | to | monthEnd |
| [dozu-ui-service/src/app/[locale]/admin/revenue/components/RevenueFilter.tsx:591](<../../dozu-ui-service/src/app/[locale]/admin/revenue/components/RevenueFilter.tsx#L591>) | to | parseInt(value) |
| [dozu-ui-service/src/app/[locale]/admin/subscriptions/list/components/Columns.tsx:156](<../../dozu-ui-service/src/app/[locale]/admin/subscriptions/list/components/Columns.tsx#L156>) | Link.href | (dynamic; see source) |
| [dozu-ui-service/src/app/[locale]/admin/subscriptions/list/page.tsx:59](<../../dozu-ui-service/src/app/[locale]/admin/subscriptions/list/page.tsx#L59>) | Link.href | /admin/subscriptions |
| [dozu-ui-service/src/app/[locale]/admin/subscriptions/page.tsx:64](<../../dozu-ui-service/src/app/[locale]/admin/subscriptions/page.tsx#L64>) | Link.href | /admin/subscriptions/list |
| [dozu-ui-service/src/app/[locale]/admin/subscriptions/page.tsx:130](<../../dozu-ui-service/src/app/[locale]/admin/subscriptions/page.tsx#L130>) | Link.href | /admin/subscriptions/list?status=active |
| [dozu-ui-service/src/app/[locale]/admin/subscriptions/page.tsx:133](<../../dozu-ui-service/src/app/[locale]/admin/subscriptions/page.tsx#L133>) | Link.href | /admin/subscriptions/list?status=cancelled |
| [dozu-ui-service/src/app/[locale]/admin/subscriptions/page.tsx:136](<../../dozu-ui-service/src/app/[locale]/admin/subscriptions/page.tsx#L136>) | Link.href | /admin/subscriptions/list?status=trialing |
| [dozu-ui-service/src/app/[locale]/admin/subscriptions/page.tsx:139](<../../dozu-ui-service/src/app/[locale]/admin/subscriptions/page.tsx#L139>) | Link.href | /admin/plans |
| [dozu-ui-service/src/app/[locale]/admin/users/components/Columns.tsx:92](<../../dozu-ui-service/src/app/[locale]/admin/users/components/Columns.tsx#L92>) | Link.href | (dynamic; see source) |
| [dozu-ui-service/src/app/[locale]/auth/changePassword/page.tsx:62](<../../dozu-ui-service/src/app/[locale]/auth/changePassword/page.tsx#L62>) | router.push | /home |
| [dozu-ui-service/src/app/[locale]/auth/changePassword/page.tsx:81](<../../dozu-ui-service/src/app/[locale]/auth/changePassword/page.tsx#L81>) | router.replace | /auth/login |
| [dozu-ui-service/src/app/[locale]/auth/changePasswordEmailSent/page.tsx:16](<../../dozu-ui-service/src/app/[locale]/auth/changePasswordEmailSent/page.tsx#L16>) | router.push | /auth/login |
| [dozu-ui-service/src/app/[locale]/auth/forgotPassword/page.tsx:26](<../../dozu-ui-service/src/app/[locale]/auth/forgotPassword/page.tsx#L26>) | router.push | /auth/login |
| [dozu-ui-service/src/app/[locale]/auth/forgotPassword/page.tsx:43](<../../dozu-ui-service/src/app/[locale]/auth/forgotPassword/page.tsx#L43>) | router.push | /auth/changePasswordEmailSent |
| [dozu-ui-service/src/app/[locale]/auth/login/page.tsx:42](<../../dozu-ui-service/src/app/[locale]/auth/login/page.tsx#L42>) | router.push | /auth/forgotPassword |
| [dozu-ui-service/src/app/[locale]/auth/login/page.tsx:181](<../../dozu-ui-service/src/app/[locale]/auth/login/page.tsx#L181>) | Link.href | /auth/register |
| [dozu-ui-service/src/app/[locale]/auth/login/page.tsx:186](<../../dozu-ui-service/src/app/[locale]/auth/login/page.tsx#L186>) | Link.href | /home |
| [dozu-ui-service/src/app/[locale]/auth/register/page.tsx:48](<../../dozu-ui-service/src/app/[locale]/auth/register/page.tsx#L48>) | router.push | (dynamic; see source) |
| [dozu-ui-service/src/app/[locale]/auth/register/page.tsx:135](<../../dozu-ui-service/src/app/[locale]/auth/register/page.tsx#L135>) | Link.href | (dynamic; see source) |
| [dozu-ui-service/src/app/[locale]/auth/verifyEmail/page.tsx:33](<../../dozu-ui-service/src/app/[locale]/auth/verifyEmail/page.tsx#L33>) | router.push | /auth/login |
| [dozu-ui-service/src/app/[locale]/auth/verifyEmail/page.tsx:38](<../../dozu-ui-service/src/app/[locale]/auth/verifyEmail/page.tsx#L38>) | router.push | /home |
| [dozu-ui-service/src/app/[locale]/auth/verifyEmail/page.tsx:45](<../../dozu-ui-service/src/app/[locale]/auth/verifyEmail/page.tsx#L45>) | router.push | /auth/login |
| [dozu-ui-service/src/app/[locale]/class-based/(assignment)/utils/assignment.utils.ts:34](<../../dozu-ui-service/src/app/[locale]/class-based/(assignment)/utils/assignment.utils.ts#L34>) | prevAssignments.push | (dynamic; see source) |
| [dozu-ui-service/src/app/[locale]/class-based/(class-quiz)/components/ClassQuizDraftEditor.tsx:415](<../../dozu-ui-service/src/app/[locale]/class-based/(class-quiz)/components/ClassQuizDraftEditor.tsx#L415>) | e.target.value.replace | (dynamic; see source) |
| [dozu-ui-service/src/app/[locale]/class-based/(class-quiz)/components/ClassQuizItem.tsx:90](<../../dozu-ui-service/src/app/[locale]/class-based/(class-quiz)/components/ClassQuizItem.tsx#L90>) | router.push | (dynamic; see source) |
| [dozu-ui-service/src/app/[locale]/class-based/(class-quiz)/components/ClassQuizItem.tsx:133](<../../dozu-ui-service/src/app/[locale]/class-based/(class-quiz)/components/ClassQuizItem.tsx#L133>) | router.push | (dynamic; see source) |
| [dozu-ui-service/src/app/[locale]/class-based/(class-quiz)/components/ClassQuizItem.tsx:144](<../../dozu-ui-service/src/app/[locale]/class-based/(class-quiz)/components/ClassQuizItem.tsx#L144>) | router.push | `/class-based/${classIdForRoute}/class-quiz/${quiz.classQuizId}/history` |
| [dozu-ui-service/src/app/[locale]/class-based/(class-quiz)/components/ClassQuizItem.tsx:202](<../../dozu-ui-service/src/app/[locale]/class-based/(class-quiz)/components/ClassQuizItem.tsx#L202>) | router.push | (dynamic; see source) |
| [dozu-ui-service/src/app/[locale]/class-based/(class-quiz)/components/QuestionCardClass.tsx:38](<../../dozu-ui-service/src/app/[locale]/class-based/(class-quiz)/components/QuestionCardClass.tsx#L38>) | dups.push | (dynamic; see source) |
| [dozu-ui-service/src/app/[locale]/class-based/(classwork)/components/ClassworkList.tsx:69](<../../dozu-ui-service/src/app/[locale]/class-based/(classwork)/components/ClassworkList.tsx#L69>) | router.push | (dynamic; see source) |
| [dozu-ui-service/src/app/[locale]/class-based/(classwork)/components/ClassworkList.tsx:85](<../../dozu-ui-service/src/app/[locale]/class-based/(classwork)/components/ClassworkList.tsx#L85>) | router.push | (dynamic; see source) |
| [dozu-ui-service/src/app/[locale]/class-based/(classwork)/components/ClassworkList.tsx:89](<../../dozu-ui-service/src/app/[locale]/class-based/(classwork)/components/ClassworkList.tsx#L89>) | router.push | (dynamic; see source) |
| [dozu-ui-service/src/app/[locale]/class-based/(classwork)/components/ClassworkList.tsx:118](<../../dozu-ui-service/src/app/[locale]/class-based/(classwork)/components/ClassworkList.tsx#L118>) | a.href | # |
| [dozu-ui-service/src/app/[locale]/class-based/(classwork)/components/ClassworkList.tsx:190](<../../dozu-ui-service/src/app/[locale]/class-based/(classwork)/components/ClassworkList.tsx#L190>) | router.push | `/teacher/class-based/${learningMaterial.classId}/learning-material/${learningMaterial.learningMaterialId}/edit` |
| [dozu-ui-service/src/app/[locale]/class-based/(classwork)/components/ClassworkList.tsx:209](<../../dozu-ui-service/src/app/[locale]/class-based/(classwork)/components/ClassworkList.tsx#L209>) | router.push | `/class-based/${learningMaterial.classId}/learning-material/${learningMaterial.learningMaterialId}/details` |
| [dozu-ui-service/src/app/[locale]/class-based/(classwork)/components/ClassworkList.tsx:213](<../../dozu-ui-service/src/app/[locale]/class-based/(classwork)/components/ClassworkList.tsx#L213>) | router.push | `/teacher/class-based/${learningMaterial.classId}/learning-material/${learningMaterial.learningMaterialId}/details` |
| [dozu-ui-service/src/app/[locale]/class-based/(classwork)/components/ClassworkList.tsx:229](<../../dozu-ui-service/src/app/[locale]/class-based/(classwork)/components/ClassworkList.tsx#L229>) | a.href | # |
| [dozu-ui-service/src/app/[locale]/class-based/(classwork)/components/ClassworkList.tsx:379](<../../dozu-ui-service/src/app/[locale]/class-based/(classwork)/components/ClassworkList.tsx#L379>) | router.push | (dynamic; see source) |
| [dozu-ui-service/src/app/[locale]/class-based/(classwork)/components/ClassworkList.tsx:404](<../../dozu-ui-service/src/app/[locale]/class-based/(classwork)/components/ClassworkList.tsx#L404>) | router.push | (dynamic; see source) |
| [dozu-ui-service/src/app/[locale]/class-based/(classwork)/components/ClassworkList.tsx:414](<../../dozu-ui-service/src/app/[locale]/class-based/(classwork)/components/ClassworkList.tsx#L414>) | router.push | (dynamic; see source) |
| [dozu-ui-service/src/app/[locale]/class-based/(classwork)/components/common/AttachmentItemWithUrl.tsx:17](<../../dozu-ui-service/src/app/[locale]/class-based/(classwork)/components/common/AttachmentItemWithUrl.tsx#L17>) | a.href | (dynamic; see source) |
| [dozu-ui-service/src/app/[locale]/class-based/(classwork)/components/common/AttachmentItemWithUrl.tsx:25](<../../dozu-ui-service/src/app/[locale]/class-based/(classwork)/components/common/AttachmentItemWithUrl.tsx#L25>) | Link.href | (dynamic; see source) |
| [dozu-ui-service/src/app/[locale]/class-based/(classwork)/components/common/FileItem.tsx:76](<../../dozu-ui-service/src/app/[locale]/class-based/(classwork)/components/common/FileItem.tsx#L76>) | a.href | (dynamic; see source) |
| [dozu-ui-service/src/app/[locale]/class-based/(classwork)/components/common/LearningMaterialItem.tsx:30](<../../dozu-ui-service/src/app/[locale]/class-based/(classwork)/components/common/LearningMaterialItem.tsx#L30>) | router.push | `/teacher/class-based/${material.classId}/learning-material/${material.learningMaterialId}/details` |
| [dozu-ui-service/src/app/[locale]/class-based/(classwork)/components/common/UrlAttachmentItem.tsx:21](<../../dozu-ui-service/src/app/[locale]/class-based/(classwork)/components/common/UrlAttachmentItem.tsx#L21>) | a.href | (dynamic; see source) |
| [dozu-ui-service/src/app/[locale]/class-based/(classwork)/components/old_ver/ClassworkList.tsx:64](<../../dozu-ui-service/src/app/[locale]/class-based/(classwork)/components/old_ver/ClassworkList.tsx#L64>) | router.push | (dynamic; see source) |
| [dozu-ui-service/src/app/[locale]/class-based/(classwork)/components/old_ver/ClassworkList.tsx:80](<../../dozu-ui-service/src/app/[locale]/class-based/(classwork)/components/old_ver/ClassworkList.tsx#L80>) | router.push | (dynamic; see source) |
| [dozu-ui-service/src/app/[locale]/class-based/(classwork)/components/old_ver/ClassworkList.tsx:84](<../../dozu-ui-service/src/app/[locale]/class-based/(classwork)/components/old_ver/ClassworkList.tsx#L84>) | router.push | (dynamic; see source) |
| [dozu-ui-service/src/app/[locale]/class-based/(classwork)/components/old_ver/ClassworkList.tsx:108](<../../dozu-ui-service/src/app/[locale]/class-based/(classwork)/components/old_ver/ClassworkList.tsx#L108>) | a.href | # |
| [dozu-ui-service/src/app/[locale]/class-based/(classwork)/components/old_ver/ClassworkList.tsx:211](<../../dozu-ui-service/src/app/[locale]/class-based/(classwork)/components/old_ver/ClassworkList.tsx#L211>) | a.href | # |
| [dozu-ui-service/src/app/[locale]/class-based/(classwork)/components/old_ver/ClassworkList.tsx:350](<../../dozu-ui-service/src/app/[locale]/class-based/(classwork)/components/old_ver/ClassworkList.tsx#L350>) | router.push | (dynamic; see source) |
| [dozu-ui-service/src/app/[locale]/class-based/(classwork)/components/old_ver/ClassworkList.tsx:357](<../../dozu-ui-service/src/app/[locale]/class-based/(classwork)/components/old_ver/ClassworkList.tsx#L357>) | router.push | (dynamic; see source) |
| [dozu-ui-service/src/app/[locale]/class-based/(classwork)/components/old_ver/ClassworkListCopy.tsx:35](<../../dozu-ui-service/src/app/[locale]/class-based/(classwork)/components/old_ver/ClassworkListCopy.tsx#L35>) | router.push | (dynamic; see source) |
| [dozu-ui-service/src/app/[locale]/class-based/(classwork)/components/old_ver/ClassworkListCopy.tsx:55](<../../dozu-ui-service/src/app/[locale]/class-based/(classwork)/components/old_ver/ClassworkListCopy.tsx#L55>) | a.href | # |
| [dozu-ui-service/src/app/[locale]/class-based/(classwork)/components/old_ver/ClassworkListCopy.tsx:134](<../../dozu-ui-service/src/app/[locale]/class-based/(classwork)/components/old_ver/ClassworkListCopy.tsx#L134>) | router.push | (dynamic; see source) |
| [dozu-ui-service/src/app/[locale]/class-based/(classwork)/components/old_ver/ClassworkListCopy.tsx:141](<../../dozu-ui-service/src/app/[locale]/class-based/(classwork)/components/old_ver/ClassworkListCopy.tsx#L141>) | router.push | (dynamic; see source) |
| [dozu-ui-service/src/app/[locale]/class-based/(classwork)/utils/classwork.utils.ts:51](<../../dozu-ui-service/src/app/[locale]/class-based/(classwork)/utils/classwork.utils.ts#L51>) | prevClasswork.push | (dynamic; see source) |
| [dozu-ui-service/src/app/[locale]/class-based/(learning-material)/utils/learningMaterial.utils.ts:35](<../../dozu-ui-service/src/app/[locale]/class-based/(learning-material)/utils/learningMaterial.utils.ts#L35>) | prevLearningMaterials.push | (dynamic; see source) |
| [dozu-ui-service/src/app/[locale]/class-based/[id]/class-quiz/[classQuizId]/history/page.tsx:84](<../../dozu-ui-service/src/app/[locale]/class-based/[id]/class-quiz/[classQuizId]/history/page.tsx#L84>) | router.push | `/class-based/${classId}/class-quiz/${quizId}/history?attemptId=${at.attemptId}` |
| [dozu-ui-service/src/app/[locale]/class-based/[id]/class-quiz/[classQuizId]/history/page.tsx:172](<../../dozu-ui-service/src/app/[locale]/class-based/[id]/class-quiz/[classQuizId]/history/page.tsx#L172>) | router.push | `/class-based/${classId}/class-quiz/${quizId}/history` |
| [dozu-ui-service/src/app/[locale]/class-based/[id]/class-quiz/[classQuizId]/start/page.tsx:250](<../../dozu-ui-service/src/app/[locale]/class-based/[id]/class-quiz/[classQuizId]/start/page.tsx#L250>) | router.push | `/${locale}${ROUTES.STUDENT.CLASS_BASED_ID_CLASS_QUIZ_SUBMIT(classId, quizId, attempt.attemptId)}` |
| [dozu-ui-service/src/app/[locale]/class-based/[id]/class-quiz/[classQuizId]/submit/page.tsx:84](<../../dozu-ui-service/src/app/[locale]/class-based/[id]/class-quiz/[classQuizId]/submit/page.tsx#L84>) | router.push | (dynamic; see source) |
| [dozu-ui-service/src/app/[locale]/class-based/[id]/dashboard/StudentClassDashboard.tsx:158](<../../dozu-ui-service/src/app/[locale]/class-based/[id]/dashboard/StudentClassDashboard.tsx#L158>) | router.push | (dynamic; see source) |
| [dozu-ui-service/src/app/[locale]/class-based/[id]/mindmap/[topicId]/page.tsx:117](<../../dozu-ui-service/src/app/[locale]/class-based/[id]/mindmap/[topicId]/page.tsx#L117>) | router.push | `/flashcards/edit/${topicId}` |
| [dozu-ui-service/src/app/[locale]/class-based/components/comment/CommentThread.tsx:494](<../../dozu-ui-service/src/app/[locale]/class-based/components/comment/CommentThread.tsx#L494>) | merged.push | (dynamic; see source) |
| [dozu-ui-service/src/app/[locale]/class-based/components/ui/class/StudentClassLibrary.tsx:38](<../../dozu-ui-service/src/app/[locale]/class-based/components/ui/class/StudentClassLibrary.tsx#L38>) | router.push | (dynamic; see source) |
| [dozu-ui-service/src/app/[locale]/class-based/components/ui/class/StudentClassLibrary.tsx:126](<../../dozu-ui-service/src/app/[locale]/class-based/components/ui/class/StudentClassLibrary.tsx#L126>) | router.push | (dynamic; see source) |
| [dozu-ui-service/src/app/[locale]/class-based/components/ui/classFeed/ClassFeedCard.tsx:134](<../../dozu-ui-service/src/app/[locale]/class-based/components/ui/classFeed/ClassFeedCard.tsx#L134>) | Link.href | (dynamic; see source) |
| [dozu-ui-service/src/app/[locale]/flashcards/components/FlashcardEditor.tsx:72](<../../dozu-ui-service/src/app/[locale]/flashcards/components/FlashcardEditor.tsx#L72>) | initialFlashcards.push | (dynamic; see source) |
| [dozu-ui-service/src/app/[locale]/flashcards/components/FlashcardEditor.tsx:195](<../../dozu-ui-service/src/app/[locale]/flashcards/components/FlashcardEditor.tsx#L195>) | initialFlashcards.push | (dynamic; see source) |
| [dozu-ui-service/src/app/[locale]/flashcards/components/FlashcardEditor.tsx:207](<../../dozu-ui-service/src/app/[locale]/flashcards/components/FlashcardEditor.tsx#L207>) | initialFlashcards.push | (dynamic; see source) |
| [dozu-ui-service/src/app/[locale]/flashcards/components/FlashcardEditor.tsx:298](<../../dozu-ui-service/src/app/[locale]/flashcards/components/FlashcardEditor.tsx#L298>) | newFlashcards.push | (dynamic; see source) |
| [dozu-ui-service/src/app/[locale]/flashcards/components/FlashcardEditor.tsx:303](<../../dozu-ui-service/src/app/[locale]/flashcards/components/FlashcardEditor.tsx#L303>) | newFlashcards.push | (dynamic; see source) |
| [dozu-ui-service/src/app/[locale]/flashcards/components/FlashcardEditor.tsx:307](<../../dozu-ui-service/src/app/[locale]/flashcards/components/FlashcardEditor.tsx#L307>) | newFlashcards.push | (dynamic; see source) |
| [dozu-ui-service/src/app/[locale]/flashcards/components/FlashcardEditor.tsx:337](<../../dozu-ui-service/src/app/[locale]/flashcards/components/FlashcardEditor.tsx#L337>) | newFlashcards.push | (dynamic; see source) |
| [dozu-ui-service/src/app/[locale]/flashcards/components/FlashcardEditor.tsx:407](<../../dozu-ui-service/src/app/[locale]/flashcards/components/FlashcardEditor.tsx#L407>) | newFlashcards.push | (dynamic; see source) |
| [dozu-ui-service/src/app/[locale]/flashcards/components/FlashcardEditor.tsx:422](<../../dozu-ui-service/src/app/[locale]/flashcards/components/FlashcardEditor.tsx#L422>) | newFlashcards.push | (dynamic; see source) |
| [dozu-ui-service/src/app/[locale]/flashcards/components/FlashcardEditor.tsx:441](<../../dozu-ui-service/src/app/[locale]/flashcards/components/FlashcardEditor.tsx#L441>) | newFlashcards.push | (dynamic; see source) |
| [dozu-ui-service/src/app/[locale]/flashcards/components/FlashcardEditor.tsx:445](<../../dozu-ui-service/src/app/[locale]/flashcards/components/FlashcardEditor.tsx#L445>) | newFlashcards.push | (dynamic; see source) |
| [dozu-ui-service/src/app/[locale]/flashcards/components/FlashcardEditor.tsx:486](<../../dozu-ui-service/src/app/[locale]/flashcards/components/FlashcardEditor.tsx#L486>) | url | image.url.small |
| [dozu-ui-service/src/app/[locale]/flashcards/learning/hooks/useQuizMilestones.ts:476](<../../dozu-ui-service/src/app/[locale]/flashcards/learning/hooks/useQuizMilestones.ts#L476>) | router.push | `/quiz/local?topicId=${topicId}&chunk=${chunk}` |
| [dozu-ui-service/src/app/[locale]/games/brain-chase/components/Setting.tsx:46](<../../dozu-ui-service/src/app/[locale]/games/brain-chase/components/Setting.tsx#L46>) | options.push | (dynamic; see source) |
| [dozu-ui-service/src/app/[locale]/games/brain-chase/components/Setting.tsx:47](<../../dozu-ui-service/src/app/[locale]/games/brain-chase/components/Setting.tsx#L47>) | options.push | (dynamic; see source) |
| [dozu-ui-service/src/app/[locale]/games/brain-chase/components/Setting.tsx:48](<../../dozu-ui-service/src/app/[locale]/games/brain-chase/components/Setting.tsx#L48>) | options.push | (dynamic; see source) |
| [dozu-ui-service/src/app/[locale]/games/brain-chase/components/Setting.tsx:52](<../../dozu-ui-service/src/app/[locale]/games/brain-chase/components/Setting.tsx#L52>) | options.push | (dynamic; see source) |
| [dozu-ui-service/src/app/[locale]/games/brain-chase/components/Setting.tsx:60](<../../dozu-ui-service/src/app/[locale]/games/brain-chase/components/Setting.tsx#L60>) | options.push | (dynamic; see source) |
| [dozu-ui-service/src/app/[locale]/games/brain-chase/context/brainChaseContext.tsx:197](<../../dozu-ui-service/src/app/[locale]/games/brain-chase/context/brainChaseContext.tsx#L197>) | wrongAnswers.push | (dynamic; see source) |
| [dozu-ui-service/src/app/[locale]/games/brain-chase/context/brainChaseContext.tsx:199](<../../dozu-ui-service/src/app/[locale]/games/brain-chase/context/brainChaseContext.tsx#L199>) | wrongAnswers.push | `Option ${wrongAnswers.length + 1}` |
| [dozu-ui-service/src/app/[locale]/games/memory-match/utils/BatchManager.ts:124](<../../dozu-ui-service/src/app/[locale]/games/memory-match/utils/BatchManager.ts#L124>) | selectedCards.push | (dynamic; see source) |
| [dozu-ui-service/src/app/[locale]/games/memory-match/utils/BatchManager.ts:130](<../../dozu-ui-service/src/app/[locale]/games/memory-match/utils/BatchManager.ts#L130>) | selectedCards.push | (dynamic; see source) |
| [dozu-ui-service/src/app/[locale]/games/memory-match/utils/BatchManager.ts:139](<../../dozu-ui-service/src/app/[locale]/games/memory-match/utils/BatchManager.ts#L139>) | selectedCards.push | (dynamic; see source) |
| [dozu-ui-service/src/app/[locale]/games/memory-match/utils/BatchManager.ts:197](<../../dozu-ui-service/src/app/[locale]/games/memory-match/utils/BatchManager.ts#L197>) | balanced.push | (dynamic; see source) |
| [dozu-ui-service/src/app/[locale]/games/memory-match/utils/BatchManager.ts:198](<../../dozu-ui-service/src/app/[locale]/games/memory-match/utils/BatchManager.ts#L198>) | balanced.push | (dynamic; see source) |
| [dozu-ui-service/src/app/[locale]/games/memory-match/utils/BatchManager.ts:214](<../../dozu-ui-service/src/app/[locale]/games/memory-match/utils/BatchManager.ts#L214>) | cards.push | (dynamic; see source) |
| [dozu-ui-service/src/app/[locale]/games/memory-match/utils/BatchManager.ts:226](<../../dozu-ui-service/src/app/[locale]/games/memory-match/utils/BatchManager.ts#L226>) | cards.push | (dynamic; see source) |
| [dozu-ui-service/src/app/[locale]/games/memory-match/utils/BatchManager.ts:300](<../../dozu-ui-service/src/app/[locale]/games/memory-match/utils/BatchManager.ts#L300>) | updatedProgress.completedBatches.push | (dynamic; see source) |
| [dozu-ui-service/src/app/[locale]/games/memory-match/utils/BatchManager.ts:329](<../../dozu-ui-service/src/app/[locale]/games/memory-match/utils/BatchManager.ts#L329>) | recommendations.push | Take your time to improve accuracy - focus on reading cards carefully |
| [dozu-ui-service/src/app/[locale]/games/memory-match/utils/BatchManager.ts:333](<../../dozu-ui-service/src/app/[locale]/games/memory-match/utils/BatchManager.ts#L333>) | recommendations.push | `You have ${stats.cardsNeedingReview} cards that need review` |
| [dozu-ui-service/src/app/[locale]/games/memory-match/utils/BatchManager.ts:337](<../../dozu-ui-service/src/app/[locale]/games/memory-match/utils/BatchManager.ts#L337>) | recommendations.push | Great progress! You're mastering cards quickly |
| [dozu-ui-service/src/app/[locale]/games/memory-match/utils/BatchManager.ts:341](<../../dozu-ui-service/src/app/[locale]/games/memory-match/utils/BatchManager.ts#L341>) | recommendations.push | Keep up the great work! Continue learning at your own pace |
| [dozu-ui-service/src/app/[locale]/generate/components/ImportPanel.tsx:82](<../../dozu-ui-service/src/app/[locale]/generate/components/ImportPanel.tsx#L82>) | validFiles.push | (dynamic; see source) |
| [dozu-ui-service/src/app/[locale]/generate/components/detail-extract/WebsiteView.tsx:39](<../../dozu-ui-service/src/app/[locale]/generate/components/detail-extract/WebsiteView.tsx#L39>) | a.href | (dynamic; see source) |
| [dozu-ui-service/src/app/[locale]/generate/components/detail-extract/WebsiteView.tsx:88](<../../dozu-ui-service/src/app/[locale]/generate/components/detail-extract/WebsiteView.tsx#L88>) | a.href | (dynamic; see source) |
| [dozu-ui-service/src/app/[locale]/generate/components/import/components/FileTab.tsx:33](<../../dozu-ui-service/src/app/[locale]/generate/components/import/components/FileTab.tsx#L33>) | url | /convert/file |
| [dozu-ui-service/src/app/[locale]/generate/detail-extract/components/WebsiteView.tsx:39](<../../dozu-ui-service/src/app/[locale]/generate/detail-extract/components/WebsiteView.tsx#L39>) | a.href | (dynamic; see source) |
| [dozu-ui-service/src/app/[locale]/generate/detail-extract/components/WebsiteView.tsx:88](<../../dozu-ui-service/src/app/[locale]/generate/detail-extract/components/WebsiteView.tsx#L88>) | a.href | (dynamic; see source) |
| [dozu-ui-service/src/app/[locale]/generate/helper/reduceTokenInput.ts:123](<../../dozu-ui-service/src/app/[locale]/generate/helper/reduceTokenInput.ts#L123>) | result.replace | (dynamic; see source) |
| [dozu-ui-service/src/app/[locale]/generate/helper/reduceTokenInput.ts:128](<../../dozu-ui-service/src/app/[locale]/generate/helper/reduceTokenInput.ts#L128>) | result.replace | (dynamic; see source) |
| [dozu-ui-service/src/app/[locale]/generate/helper/reduceTokenInput.ts:130](<../../dozu-ui-service/src/app/[locale]/generate/helper/reduceTokenInput.ts#L130>) | result.replace | (dynamic; see source) |
| [dozu-ui-service/src/app/[locale]/generate/helper/reduceTokenInput.ts:135](<../../dozu-ui-service/src/app/[locale]/generate/helper/reduceTokenInput.ts#L135>) | result.replace | (dynamic; see source) |
| [dozu-ui-service/src/app/[locale]/generate/helper/reduceTokenInput.ts:137](<../../dozu-ui-service/src/app/[locale]/generate/helper/reduceTokenInput.ts#L137>) | result.replace | (dynamic; see source) |
| [dozu-ui-service/src/app/[locale]/generate/helper/reduceTokenInput.ts:141](<../../dozu-ui-service/src/app/[locale]/generate/helper/reduceTokenInput.ts#L141>) | result.replace | (dynamic; see source) |
| [dozu-ui-service/src/app/[locale]/generate/helper/reduceTokenInput.ts:151](<../../dozu-ui-service/src/app/[locale]/generate/helper/reduceTokenInput.ts#L151>) | result.replace | (dynamic; see source) |
| [dozu-ui-service/src/app/[locale]/generate/hooks/useContentGeneration.ts:108](<../../dozu-ui-service/src/app/[locale]/generate/hooks/useContentGeneration.ts#L108>) | router.push | (dynamic; see source) |
| [dozu-ui-service/src/app/[locale]/generate/hooks/useContentGeneration.ts:121](<../../dozu-ui-service/src/app/[locale]/generate/hooks/useContentGeneration.ts#L121>) | router.push | (dynamic; see source) |
| [dozu-ui-service/src/app/[locale]/generate/hooks/useContentGeneration.ts:155](<../../dozu-ui-service/src/app/[locale]/generate/hooks/useContentGeneration.ts#L155>) | router.replace | (dynamic; see source) |
| [dozu-ui-service/src/app/[locale]/generate/hooks/useContentGeneration.ts:159](<../../dozu-ui-service/src/app/[locale]/generate/hooks/useContentGeneration.ts#L159>) | router.push | (dynamic; see source) |
| [dozu-ui-service/src/app/[locale]/generate/hooks/useContentGeneration.ts:225](<../../dozu-ui-service/src/app/[locale]/generate/hooks/useContentGeneration.ts#L225>) | url | inputUrl |
| [dozu-ui-service/src/app/[locale]/generate/hooks/useContentGeneration.ts:240](<../../dozu-ui-service/src/app/[locale]/generate/hooks/useContentGeneration.ts#L240>) | url | inputUrl |
| [dozu-ui-service/src/app/[locale]/generate/stores/features/contentExtractionSlice.ts:116](<../../dozu-ui-service/src/app/[locale]/generate/stores/features/contentExtractionSlice.ts#L116>) | url | validUrl |
| [dozu-ui-service/src/app/[locale]/home/components/CoreActionCards.tsx:26](<../../dozu-ui-service/src/app/[locale]/home/components/CoreActionCards.tsx#L26>) | router.push | (dynamic; see source) |
| [dozu-ui-service/src/app/[locale]/home/components/CoreActionCards.tsx:30](<../../dozu-ui-service/src/app/[locale]/home/components/CoreActionCards.tsx#L30>) | router.push | (dynamic; see source) |
| [dozu-ui-service/src/app/[locale]/home/components/CoreActionCards.tsx:34](<../../dozu-ui-service/src/app/[locale]/home/components/CoreActionCards.tsx#L34>) | router.push | (dynamic; see source) |
| [dozu-ui-service/src/app/[locale]/home/components/CurrentProcessLearning.tsx:100](<../../dozu-ui-service/src/app/[locale]/home/components/CurrentProcessLearning.tsx#L100>) | router.push | (dynamic; see source) |
| [dozu-ui-service/src/app/[locale]/home/components/GuestLibraryPlaceholder.tsx:33](<../../dozu-ui-service/src/app/[locale]/home/components/GuestLibraryPlaceholder.tsx#L33>) | router.push | (dynamic; see source) |
| [dozu-ui-service/src/app/[locale]/home/components/GuestLibraryPlaceholder.tsx:41](<../../dozu-ui-service/src/app/[locale]/home/components/GuestLibraryPlaceholder.tsx#L41>) | router.push | (dynamic; see source) |
| [dozu-ui-service/src/app/[locale]/home/components/HeroSection.tsx:29](<../../dozu-ui-service/src/app/[locale]/home/components/HeroSection.tsx#L29>) | router.push | (dynamic; see source) |
| [dozu-ui-service/src/app/[locale]/home/components/HeroSection.tsx:36](<../../dozu-ui-service/src/app/[locale]/home/components/HeroSection.tsx#L36>) | router.push | (dynamic; see source) |
| [dozu-ui-service/src/app/[locale]/home/components/actions/UploadModal.tsx:46](<../../dozu-ui-service/src/app/[locale]/home/components/actions/UploadModal.tsx#L46>) | url | /convert/file |
| [dozu-ui-service/src/app/[locale]/home/components/actions/context/ActionContext.tsx:43](<../../dozu-ui-service/src/app/[locale]/home/components/actions/context/ActionContext.tsx#L43>) | router.push | (dynamic; see source) |
| [dozu-ui-service/src/app/[locale]/home/components/actions/hooks/useToastManager.tsx:12](<../../dozu-ui-service/src/app/[locale]/home/components/actions/hooks/useToastManager.tsx#L12>) | toastManager.ids.push | (dynamic; see source) |
| [dozu-ui-service/src/app/[locale]/home/components/actions/services/contentCreation.service.ts:26](<../../dozu-ui-service/src/app/[locale]/home/components/actions/services/contentCreation.service.ts#L26>) | url | pastedUrl |
| [dozu-ui-service/src/app/[locale]/home/components/actions/services/contentCreation.service.ts:47](<../../dozu-ui-service/src/app/[locale]/home/components/actions/services/contentCreation.service.ts#L47>) | url | pastedUrl |
| [dozu-ui-service/src/app/[locale]/home/components/package/TreeView.tsx:197](<../../dozu-ui-service/src/app/[locale]/home/components/package/TreeView.tsx#L197>) | router.push | (dynamic; see source) |
| [dozu-ui-service/src/app/[locale]/home/page.tsx:47](<../../dozu-ui-service/src/app/[locale]/home/page.tsx#L47>) | router.replace | (dynamic; see source) |
| [dozu-ui-service/src/app/[locale]/home/page.tsx:54](<../../dozu-ui-service/src/app/[locale]/home/page.tsx#L54>) | router.push | (dynamic; see source) |
| [dozu-ui-service/src/app/[locale]/mindmap/[topicId]/page.tsx:187](<../../dozu-ui-service/src/app/[locale]/mindmap/[topicId]/page.tsx#L187>) | router.push | `/flashcards/edit/${topicId}` |
| [dozu-ui-service/src/app/[locale]/mindmap/add-flashcard/page.tsx:74](<../../dozu-ui-service/src/app/[locale]/mindmap/add-flashcard/page.tsx#L74>) | router.push | `/flashcards/edit/${topicId}` |
| [dozu-ui-service/src/app/[locale]/mindmap/components/FileSheet.tsx:70](<../../dozu-ui-service/src/app/[locale]/mindmap/components/FileSheet.tsx#L70>) | Link.href | (dynamic; see source) |
| [dozu-ui-service/src/app/[locale]/mindmap/components/GenerateMindmapCard.tsx:78](<../../dozu-ui-service/src/app/[locale]/mindmap/components/GenerateMindmapCard.tsx#L78>) | router.push | /home |
| [dozu-ui-service/src/app/[locale]/mindmap/components/NodeSheetViewOnly.tsx:66](<../../dozu-ui-service/src/app/[locale]/mindmap/components/NodeSheetViewOnly.tsx#L66>) | router.push | `/mindmap/nodes/${selectedNodeData.nodeId}/flashcard` |
| [dozu-ui-service/src/app/[locale]/mindmap/components/buttons/ExportToCSVButton.tsx:40](<../../dozu-ui-service/src/app/[locale]/mindmap/components/buttons/ExportToCSVButton.tsx#L40>) | outerLeafs.push | (dynamic; see source) |
| [dozu-ui-service/src/app/[locale]/mindmap/components/buttons/ExportToCSVButton.tsx:52](<../../dozu-ui-service/src/app/[locale]/mindmap/components/buttons/ExportToCSVButton.tsx#L52>) | pathArray.push | (dynamic; see source) |
| [dozu-ui-service/src/app/[locale]/mindmap/components/buttons/ExportToCSVButton.tsx:55](<../../dozu-ui-service/src/app/[locale]/mindmap/components/buttons/ExportToCSVButton.tsx#L55>) | pathArray.push | (dynamic; see source) |
| [dozu-ui-service/src/app/[locale]/mindmap/components/buttons/ExportToCSVButton.tsx:60](<../../dozu-ui-service/src/app/[locale]/mindmap/components/buttons/ExportToCSVButton.tsx#L60>) | pathArrays.push | (dynamic; see source) |
| [dozu-ui-service/src/app/[locale]/mindmap/components/buttons/ExportToCSVButton.tsx:73](<../../dozu-ui-service/src/app/[locale]/mindmap/components/buttons/ExportToCSVButton.tsx#L73>) | padded.push | (dynamic; see source) |
| [dozu-ui-service/src/app/[locale]/mindmap/components/buttons/ImportButton.tsx:104](<../../dozu-ui-service/src/app/[locale]/mindmap/components/buttons/ImportButton.tsx#L104>) | nodes.push | (dynamic; see source) |
| [dozu-ui-service/src/app/[locale]/mindmap/components/buttons/ImportButton.tsx:121](<../../dozu-ui-service/src/app/[locale]/mindmap/components/buttons/ImportButton.tsx#L121>) | edges.push | (dynamic; see source) |
| [dozu-ui-service/src/app/[locale]/mindmap/components/buttons/RoadmapButton.tsx:34](<../../dozu-ui-service/src/app/[locale]/mindmap/components/buttons/RoadmapButton.tsx#L34>) | children.push | (dynamic; see source) |
| [dozu-ui-service/src/app/[locale]/mindmap/view/[topicId]/page.tsx:182](<../../dozu-ui-service/src/app/[locale]/mindmap/view/[topicId]/page.tsx#L182>) | router.push | `/flashcards/edit/${topicId}` |
| [dozu-ui-service/src/app/[locale]/onboarding/components/OnboardingCompleteCard.tsx:18](<../../dozu-ui-service/src/app/[locale]/onboarding/components/OnboardingCompleteCard.tsx#L18>) | Link.href | / |
| [dozu-ui-service/src/app/[locale]/page.tsx:24](<../../dozu-ui-service/src/app/[locale]/page.tsx#L24>) | router.push | (dynamic; see source) |
| [dozu-ui-service/src/app/[locale]/page.tsx:29](<../../dozu-ui-service/src/app/[locale]/page.tsx#L29>) | router.push | (dynamic; see source) |
| [dozu-ui-service/src/app/[locale]/page.tsx:35](<../../dozu-ui-service/src/app/[locale]/page.tsx#L35>) | router.push | (dynamic; see source) |
| [dozu-ui-service/src/app/[locale]/page.tsx:41](<../../dozu-ui-service/src/app/[locale]/page.tsx#L41>) | router.push | (dynamic; see source) |
| [dozu-ui-service/src/app/[locale]/payment/page.tsx:86](<../../dozu-ui-service/src/app/[locale]/payment/page.tsx#L86>) | router.push | (dynamic; see source) |
| [dozu-ui-service/src/app/[locale]/payment/page.tsx:184](<../../dozu-ui-service/src/app/[locale]/payment/page.tsx#L184>) | router.push | (dynamic; see source) |
| [dozu-ui-service/src/app/[locale]/payment/page.tsx:408](<../../dozu-ui-service/src/app/[locale]/payment/page.tsx#L408>) | redirectTo | ROUTES.LANDING |
| [dozu-ui-service/src/app/[locale]/profile/components/ProfilePage.tsx:349](<../../dozu-ui-service/src/app/[locale]/profile/components/ProfilePage.tsx#L349>) | key.replace(/([A-Z])/g, ' $1').replace | (dynamic; see source) |
| [dozu-ui-service/src/app/[locale]/profile/components/ProfilePage.tsx:349](<../../dozu-ui-service/src/app/[locale]/profile/components/ProfilePage.tsx#L349>) | key.replace | (dynamic; see source) |
| [dozu-ui-service/src/app/[locale]/profile/components/ProfilePage.tsx:369](<../../dozu-ui-service/src/app/[locale]/profile/components/ProfilePage.tsx#L369>) | key.replace(/([A-Z])/g, ' $1').replace | (dynamic; see source) |
| [dozu-ui-service/src/app/[locale]/profile/components/ProfilePage.tsx:369](<../../dozu-ui-service/src/app/[locale]/profile/components/ProfilePage.tsx#L369>) | key.replace | (dynamic; see source) |
| [dozu-ui-service/src/app/[locale]/progress/components/ProgressDashboard.tsx:460](<../../dozu-ui-service/src/app/[locale]/progress/components/ProgressDashboard.tsx#L460>) | url | window.location.href |
| [dozu-ui-service/src/app/[locale]/progress/components/ProgressManager.tsx:193](<../../dozu-ui-service/src/app/[locale]/progress/components/ProgressManager.tsx#L193>) | status.replace | _ |
| [dozu-ui-service/src/app/[locale]/progress/components/ProgressManager.tsx:193](<../../dozu-ui-service/src/app/[locale]/progress/components/ProgressManager.tsx#L193>) | status.replace | _ |
| [dozu-ui-service/src/app/[locale]/progress/components/ProgressManager.tsx:277](<../../dozu-ui-service/src/app/[locale]/progress/components/ProgressManager.tsx#L277>) | progress.status.replace | _ |
| [dozu-ui-service/src/app/[locale]/question/components/QuestionCard.tsx:53](<../../dozu-ui-service/src/app/[locale]/question/components/QuestionCard.tsx#L53>) | dups.push | (dynamic; see source) |
| [dozu-ui-service/src/app/[locale]/question/components/QuestionEditor.tsx:254](<../../dozu-ui-service/src/app/[locale]/question/components/QuestionEditor.tsx#L254>) | router.push | (dynamic; see source) |
| [dozu-ui-service/src/app/[locale]/question/components/QuestionEditor.tsx:305](<../../dozu-ui-service/src/app/[locale]/question/components/QuestionEditor.tsx#L305>) | normalizedOptions.push | (dynamic; see source) |
| [dozu-ui-service/src/app/[locale]/question/utils/handleConvertToQuestionsEdited.ts:57](<../../dozu-ui-service/src/app/[locale]/question/utils/handleConvertToQuestionsEdited.ts#L57>) | initialQuestions.push | (dynamic; see source) |
| [dozu-ui-service/src/app/[locale]/question/utils/handleConvertToQuestionsEdited.ts:72](<../../dozu-ui-service/src/app/[locale]/question/utils/handleConvertToQuestionsEdited.ts#L72>) | initialQuestions.push | (dynamic; see source) |
| [dozu-ui-service/src/app/[locale]/quiz/[topicId]/doing/page.tsx:173](<../../dozu-ui-service/src/app/[locale]/quiz/[topicId]/doing/page.tsx#L173>) | router.push | `/quiz/${topicId}/result/${quizResultId}` |
| [dozu-ui-service/src/app/[locale]/quiz/[topicId]/history/page.tsx:96](<../../dozu-ui-service/src/app/[locale]/quiz/[topicId]/history/page.tsx#L96>) | router.push | `/quiz/${params.topicId}/history/${quiz.quizResultId}` |
| [dozu-ui-service/src/app/[locale]/quiz/layout.tsx:26](<../../dozu-ui-service/src/app/[locale]/quiz/layout.tsx#L26>) | router.push | `/quiz/${topicId}/quiz-type` |
| [dozu-ui-service/src/app/[locale]/quiz/local/page.tsx:29](<../../dozu-ui-service/src/app/[locale]/quiz/local/page.tsx#L29>) | router.replace | `/flashcards/learning/${topicId}` |
| [dozu-ui-service/src/app/[locale]/quiz/local/page.tsx:88](<../../dozu-ui-service/src/app/[locale]/quiz/local/page.tsx#L88>) | router.replace | `/flashcards/learning/${topicId}` |
| [dozu-ui-service/src/app/[locale]/request-teacher/components/RequestStatus.tsx:51](<../../dozu-ui-service/src/app/[locale]/request-teacher/components/RequestStatus.tsx#L51>) | router.push | /request-teacher/reapply |
| [dozu-ui-service/src/app/[locale]/request-teacher/reapply/page.tsx:31](<../../dozu-ui-service/src/app/[locale]/request-teacher/reapply/page.tsx#L31>) | router.push | /request-teacher |
| [dozu-ui-service/src/app/[locale]/schedule/services/schedule.service.ts:169](<../../dozu-ui-service/src/app/[locale]/schedule/services/schedule.service.ts#L169>) | errors.push | fromDate is required |
| [dozu-ui-service/src/app/[locale]/schedule/services/schedule.service.ts:173](<../../dozu-ui-service/src/app/[locale]/schedule/services/schedule.service.ts#L173>) | errors.push | toDate is required |
| [dozu-ui-service/src/app/[locale]/schedule/services/schedule.service.ts:181](<../../dozu-ui-service/src/app/[locale]/schedule/services/schedule.service.ts#L181>) | errors.push | fromDate must be a valid ISO 8601 date string |
| [dozu-ui-service/src/app/[locale]/schedule/services/schedule.service.ts:185](<../../dozu-ui-service/src/app/[locale]/schedule/services/schedule.service.ts#L185>) | errors.push | toDate must be a valid ISO 8601 date string |
| [dozu-ui-service/src/app/[locale]/schedule/services/schedule.service.ts:189](<../../dozu-ui-service/src/app/[locale]/schedule/services/schedule.service.ts#L189>) | errors.push | fromDate must be earlier than toDate |
| [dozu-ui-service/src/app/[locale]/schedule/services/schedule.service.ts:195](<../../dozu-ui-service/src/app/[locale]/schedule/services/schedule.service.ts#L195>) | errors.push | Date range cannot exceed 365 days |
| [dozu-ui-service/src/app/[locale]/setting/components/SettingSidebar.tsx:12](<../../dozu-ui-service/src/app/[locale]/setting/components/SettingSidebar.tsx#L12>) | path | ROUTES.PROFILE |
| [dozu-ui-service/src/app/[locale]/setting/components/SettingSidebar.tsx:13](<../../dozu-ui-service/src/app/[locale]/setting/components/SettingSidebar.tsx#L13>) | path | ROUTES.SETTING_SCHEDULE_SETUP |
| [dozu-ui-service/src/app/[locale]/setting/components/SettingSidebar.tsx:17](<../../dozu-ui-service/src/app/[locale]/setting/components/SettingSidebar.tsx#L17>) | router.push | (dynamic; see source) |
| [dozu-ui-service/src/app/[locale]/setting/profile/page.tsx:14](<../../dozu-ui-service/src/app/[locale]/setting/profile/page.tsx#L14>) | router.push | /request-teacher |
| [dozu-ui-service/src/app/[locale]/teacher/class-based/[id]/assignments/[assignmentId]/details/components/CommentInput.tsx:131](<../../dozu-ui-service/src/app/[locale]/teacher/class-based/[id]/assignments/[assignmentId]/details/components/CommentInput.tsx#L131>) | currentLine.replace | (dynamic; see source) |
| [dozu-ui-service/src/app/[locale]/teacher/class-based/[id]/assignments/[assignmentId]/details/components/CommentInput.tsx:148](<../../dozu-ui-service/src/app/[locale]/teacher/class-based/[id]/assignments/[assignmentId]/details/components/CommentInput.tsx#L148>) | selectedText .replace(/\*\*([^*]+)\*\*/g, '$1') // Bold .replace(/\*([^*]+)\*/g, '$1') // Italic .replace(/__([^_]+)__/g, '$1') // Underline .replace | (dynamic; see source) |
| [dozu-ui-service/src/app/[locale]/teacher/class-based/[id]/assignments/[assignmentId]/details/components/CommentInput.tsx:148](<../../dozu-ui-service/src/app/[locale]/teacher/class-based/[id]/assignments/[assignmentId]/details/components/CommentInput.tsx#L148>) | selectedText .replace(/\*\*([^*]+)\*\*/g, '$1') // Bold .replace(/\*([^*]+)\*/g, '$1') // Italic .replace | (dynamic; see source) |
| [dozu-ui-service/src/app/[locale]/teacher/class-based/[id]/assignments/[assignmentId]/details/components/CommentInput.tsx:148](<../../dozu-ui-service/src/app/[locale]/teacher/class-based/[id]/assignments/[assignmentId]/details/components/CommentInput.tsx#L148>) | selectedText .replace(/\*\*([^*]+)\*\*/g, '$1') // Bold .replace | (dynamic; see source) |
| [dozu-ui-service/src/app/[locale]/teacher/class-based/[id]/assignments/[assignmentId]/details/components/CommentInput.tsx:148](<../../dozu-ui-service/src/app/[locale]/teacher/class-based/[id]/assignments/[assignmentId]/details/components/CommentInput.tsx#L148>) | selectedText .replace | (dynamic; see source) |
| [dozu-ui-service/src/app/[locale]/teacher/class-based/[id]/assignments/[assignmentId]/details/components/CommentInput.tsx:157](<../../dozu-ui-service/src/app/[locale]/teacher/class-based/[id]/assignments/[assignmentId]/details/components/CommentInput.tsx#L157>) | content .replace(/\*\*([^*]+)\*\*/g, '$1') .replace(/\*([^*]+)\*/g, '$1') .replace(/__([^_]+)__/g, '$1') .replace | (dynamic; see source) |
| [dozu-ui-service/src/app/[locale]/teacher/class-based/[id]/assignments/[assignmentId]/details/components/CommentInput.tsx:157](<../../dozu-ui-service/src/app/[locale]/teacher/class-based/[id]/assignments/[assignmentId]/details/components/CommentInput.tsx#L157>) | content .replace(/\*\*([^*]+)\*\*/g, '$1') .replace(/\*([^*]+)\*/g, '$1') .replace | (dynamic; see source) |
| [dozu-ui-service/src/app/[locale]/teacher/class-based/[id]/assignments/[assignmentId]/details/components/CommentInput.tsx:157](<../../dozu-ui-service/src/app/[locale]/teacher/class-based/[id]/assignments/[assignmentId]/details/components/CommentInput.tsx#L157>) | content .replace(/\*\*([^*]+)\*\*/g, '$1') .replace | (dynamic; see source) |
| [dozu-ui-service/src/app/[locale]/teacher/class-based/[id]/assignments/[assignmentId]/details/components/CommentInput.tsx:157](<../../dozu-ui-service/src/app/[locale]/teacher/class-based/[id]/assignments/[assignmentId]/details/components/CommentInput.tsx#L157>) | content .replace | (dynamic; see source) |
| [dozu-ui-service/src/app/[locale]/teacher/class-based/[id]/assignments/[assignmentId]/details/page.tsx:157](<../../dozu-ui-service/src/app/[locale]/teacher/class-based/[id]/assignments/[assignmentId]/details/page.tsx#L157>) | router.push | (dynamic; see source) |
| [dozu-ui-service/src/app/[locale]/teacher/class-based/[id]/assignments/[assignmentId]/details/page.tsx:162](<../../dozu-ui-service/src/app/[locale]/teacher/class-based/[id]/assignments/[assignmentId]/details/page.tsx#L162>) | router.push | (dynamic; see source) |
| [dozu-ui-service/src/app/[locale]/teacher/class-based/[id]/assignments/[assignmentId]/edit/page.tsx:81](<../../dozu-ui-service/src/app/[locale]/teacher/class-based/[id]/assignments/[assignmentId]/edit/page.tsx#L81>) | router.push | (dynamic; see source) |
| [dozu-ui-service/src/app/[locale]/teacher/class-based/[id]/assignments/page.tsx:67](<../../dozu-ui-service/src/app/[locale]/teacher/class-based/[id]/assignments/page.tsx#L67>) | router.push | (dynamic; see source) |
| [dozu-ui-service/src/app/[locale]/teacher/class-based/[id]/class-quiz/[classQuizId]/edit/page.tsx:68](<../../dozu-ui-service/src/app/[locale]/teacher/class-based/[id]/class-quiz/[classQuizId]/edit/page.tsx#L68>) | router.push | (dynamic; see source) |
| [dozu-ui-service/src/app/[locale]/teacher/class-based/[id]/dashboard/TeacherClassDashboard.tsx:281](<../../dozu-ui-service/src/app/[locale]/teacher/class-based/[id]/dashboard/TeacherClassDashboard.tsx#L281>) | router.push | (dynamic; see source) |
| [dozu-ui-service/src/app/[locale]/teacher/class-based/[id]/dashboard/TeacherClassDashboard.tsx:285](<../../dozu-ui-service/src/app/[locale]/teacher/class-based/[id]/dashboard/TeacherClassDashboard.tsx#L285>) | router.push | (dynamic; see source) |
| [dozu-ui-service/src/app/[locale]/teacher/class-based/[id]/dashboard/TeacherClassDashboard.tsx:289](<../../dozu-ui-service/src/app/[locale]/teacher/class-based/[id]/dashboard/TeacherClassDashboard.tsx#L289>) | router.push | (dynamic; see source) |
| [dozu-ui-service/src/app/[locale]/teacher/class-based/[id]/learning-material/[learningMaterialId]/details/page.tsx:136](<../../dozu-ui-service/src/app/[locale]/teacher/class-based/[id]/learning-material/[learningMaterialId]/details/page.tsx#L136>) | router.push | (dynamic; see source) |
| [dozu-ui-service/src/app/[locale]/teacher/class-based/[id]/learning-material/[learningMaterialId]/details/page.tsx:142](<../../dozu-ui-service/src/app/[locale]/teacher/class-based/[id]/learning-material/[learningMaterialId]/details/page.tsx#L142>) | router.push | `/teacher/class-based/${classId}/learning-material/${learningMaterialId}/edit` |
| [dozu-ui-service/src/app/[locale]/teacher/class-based/[id]/learning-material/[learningMaterialId]/edit/page.tsx:89](<../../dozu-ui-service/src/app/[locale]/teacher/class-based/[id]/learning-material/[learningMaterialId]/edit/page.tsx#L89>) | router.push | (dynamic; see source) |
| [dozu-ui-service/src/app/[locale]/teacher/class-based/[id]/learning-material/[learningMaterialId]/page.tsx:76](<../../dozu-ui-service/src/app/[locale]/teacher/class-based/[id]/learning-material/[learningMaterialId]/page.tsx#L76>) | a.href | # |
| [dozu-ui-service/src/app/[locale]/teacher/class-based/[id]/learning-material/components/CreateLearningMaterial.tsx:114](<../../dozu-ui-service/src/app/[locale]/teacher/class-based/[id]/learning-material/components/CreateLearningMaterial.tsx#L114>) | router.push | (dynamic; see source) |
| [dozu-ui-service/src/app/[locale]/teacher/class-based/[id]/mindmap/[topicId]/page.tsx:184](<../../dozu-ui-service/src/app/[locale]/teacher/class-based/[id]/mindmap/[topicId]/page.tsx#L184>) | router.push | `/flashcards/edit/${topicId}` |
| [dozu-ui-service/src/app/[locale]/teacher/home/components/ui/TeacherClassLibrary.tsx:41](<../../dozu-ui-service/src/app/[locale]/teacher/home/components/ui/TeacherClassLibrary.tsx#L41>) | router.push | (dynamic; see source) |
| [dozu-ui-service/src/app/[locale]/teacher/home/components/ui/TeacherClassLibrary.tsx:142](<../../dozu-ui-service/src/app/[locale]/teacher/home/components/ui/TeacherClassLibrary.tsx#L142>) | router.push | (dynamic; see source) |
| [dozu-ui-service/src/app/[locale]/teacher/home/components/ui/TeacherClassLibrary.tsx:146](<../../dozu-ui-service/src/app/[locale]/teacher/home/components/ui/TeacherClassLibrary.tsx#L146>) | router.push | (dynamic; see source) |
| [dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/flashcard/edit/FlashcardsEdit.tsx:163](<../../dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/flashcard/edit/FlashcardsEdit.tsx#L163>) | result.push | (dynamic; see source) |
| [dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/flashcard/edit/FlashcardsEdit.tsx:205](<../../dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/flashcard/edit/FlashcardsEdit.tsx#L205>) | newFlashcards.push | (dynamic; see source) |
| [dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/flashcard/edit/FlashcardsEdit.tsx:229](<../../dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/flashcard/edit/FlashcardsEdit.tsx#L229>) | url | image.url.small |
| [dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/flashcard/flashcard-image/SearchTab.tsx:26](<../../dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/flashcard/flashcard-image/SearchTab.tsx#L26>) | title.toLowerCase().replace | (dynamic; see source) |
| [dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/flashcard/import/FlashcardImportCsv.tsx:38](<../../dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/flashcard/import/FlashcardImportCsv.tsx#L38>) | flashcardsImported.push | (dynamic; see source) |
| [dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/flashcard/node/MultiNodeFlashcardsPreview.tsx:60](<../../dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/flashcard/node/MultiNodeFlashcardsPreview.tsx#L60>) | result.push | (dynamic; see source) |
| [dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/flashcard/node/MultiNodeFlashcardsPreview.tsx:91](<../../dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/flashcard/node/MultiNodeFlashcardsPreview.tsx#L91>) | flashcardsInput.push | (dynamic; see source) |
| [dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/material/LearningMaterial.tsx:72](<../../dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/material/LearningMaterial.tsx#L72>) | router.push | (dynamic; see source) |
| [dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/material/pdf/CustomPDFViewer.tsx:108](<../../dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/material/pdf/CustomPDFViewer.tsx#L108>) | a.href | (dynamic; see source) |
| [dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/mindmap/components/Roadmap.tsx:31](<../../dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/mindmap/components/Roadmap.tsx#L31>) | children.push | (dynamic; see source) |
| [dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/mindmap/node/NodeDetails.tsx:233](<../../dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/mindmap/node/NodeDetails.tsx#L233>) | router.push | `/mindmap/add-flashcard?topicId=${selectedNodeData.topicId}&nodeId=${selectedNodeData.nodeId}` |
| [dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/mindmap/node/NodeDetails.tsx:241](<../../dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/mindmap/node/NodeDetails.tsx#L241>) | router.push | `/mindmap/nodes/${selectedNodeData.nodeId}/flashcard` |
| [dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/note/NoteSegmentRenderer.tsx:33](<../../dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/note/NoteSegmentRenderer.tsx#L33>) | segments.push | (dynamic; see source) |
| [dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/quiz/import/QuestionImportText.tsx:34](<../../dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/quiz/import/QuestionImportText.tsx#L34>) | parsed.push | (dynamic; see source) |
| [dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/quiz/quiz-generate/QuizGenerateTab.tsx:278](<../../dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/components/quiz/quiz-generate/QuizGenerateTab.tsx#L278>) | normalizedOptions.push | (dynamic; see source) |
| [dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/hooks/useFlashCardWorkSpace.tsx:116](<../../dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/hooks/useFlashCardWorkSpace.tsx#L116>) | updatedLearningFlashcards.push | (dynamic; see source) |
| [dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/hooks/useFlashCardWorkSpace.tsx:181](<../../dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/hooks/useFlashCardWorkSpace.tsx#L181>) | result.push | (dynamic; see source) |
| [dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/hooks/useMultiNodeFlashcardsGenerate.tsx:47](<../../dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/hooks/useMultiNodeFlashcardsGenerate.tsx#L47>) | data.push | (dynamic; see source) |
| [dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/hooks/useMultiNodeFlashcardsGenerate.tsx:118](<../../dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/hooks/useMultiNodeFlashcardsGenerate.tsx#L118>) | nodesData.push | (dynamic; see source) |
| [dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/hooks/useMultiNodeFlashcardsGenerate.tsx:150](<../../dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/hooks/useMultiNodeFlashcardsGenerate.tsx#L150>) | nodesData.push | (dynamic; see source) |
| [dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/hooks/useSelectMenu.tsx:52](<../../dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/hooks/useSelectMenu.tsx#L52>) | selectingContentText.replace | (dynamic; see source) |
| [dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/hooks/useSelectMenu.tsx:72](<../../dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/hooks/useSelectMenu.tsx#L72>) | text .replace(/&/g, '&amp;') .replace(/</g, '&lt;') .replace(/>/g, '&gt;') .replace(/"/g, '&quot;') .replace | (dynamic; see source) |
| [dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/hooks/useSelectMenu.tsx:72](<../../dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/hooks/useSelectMenu.tsx#L72>) | text .replace(/&/g, '&amp;') .replace(/</g, '&lt;') .replace(/>/g, '&gt;') .replace | (dynamic; see source) |
| [dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/hooks/useSelectMenu.tsx:72](<../../dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/hooks/useSelectMenu.tsx#L72>) | text .replace(/&/g, '&amp;') .replace(/</g, '&lt;') .replace | (dynamic; see source) |
| [dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/hooks/useSelectMenu.tsx:72](<../../dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/hooks/useSelectMenu.tsx#L72>) | text .replace(/&/g, '&amp;') .replace | (dynamic; see source) |
| [dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/hooks/useSelectMenu.tsx:72](<../../dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/hooks/useSelectMenu.tsx#L72>) | text .replace | (dynamic; see source) |
| [dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/utils/flashcard.utils.ts:28](<../../dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/utils/flashcard.utils.ts#L28>) | result.push | (dynamic; see source) |
| [dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/utils/flashcard.utils.ts:38](<../../dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/utils/flashcard.utils.ts#L38>) | flashcardsRandom.push | (dynamic; see source) |
| [dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/utils/flashcard.utils.ts:91](<../../dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/utils/flashcard.utils.ts#L91>) | initialFlashcards.push | (dynamic; see source) |
| [dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/utils/note-reference.utils.ts:47](<../../dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/utils/note-reference.utils.ts#L47>) | parts.push | `⏱ ${minutes}:${seconds.toString().padStart(2, '0')}` |
| [dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/utils/note-reference.utils.ts:53](<../../dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/utils/note-reference.utils.ts#L53>) | parts.push | `Page ${reference.page}` |
| [dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/utils/note-reference.utils.ts:58](<../../dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/utils/note-reference.utils.ts#L58>) | parts.push | YouTube |
| [dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/utils/note-reference.utils.ts:60](<../../dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/utils/note-reference.utils.ts#L60>) | parts.push | Media |
| [dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/utils/note-reference.utils.ts:62](<../../dozu-ui-service/src/app/[locale]/topics/[topicId]/(topic)/utils/note-reference.utils.ts#L62>) | parts.push | PDF |
| [dozu-ui-service/src/app/[locale]/topics/[topicId]/settings/anki/utils/ankiSetting.util.ts:10](<../../dozu-ui-service/src/app/[locale]/topics/[topicId]/settings/anki/utils/ankiSetting.util.ts#L10>) | strings.push | (dynamic; see source) |
| [dozu-ui-service/src/app/[locale]/topics/[topicId]/settings/anki/utils/ankiSetting.util.ts:12](<../../dozu-ui-service/src/app/[locale]/topics/[topicId]/settings/anki/utils/ankiSetting.util.ts#L12>) | strings.push | (dynamic; see source) |
| [dozu-ui-service/src/app/[locale]/topics/[topicId]/settings/anki/utils/ankiSetting.util.ts:14](<../../dozu-ui-service/src/app/[locale]/topics/[topicId]/settings/anki/utils/ankiSetting.util.ts#L14>) | strings.push | (dynamic; see source) |
| [dozu-ui-service/src/app/[locale]/topics/[topicId]/settings/anki/utils/ankiSetting.util.ts:32](<../../dozu-ui-service/src/app/[locale]/topics/[topicId]/settings/anki/utils/ankiSetting.util.ts#L32>) | values.push | (dynamic; see source) |
| [dozu-ui-service/src/app/[locale]/topics/[topicId]/settings/anki/utils/ankiSetting.util.ts:33](<../../dozu-ui-service/src/app/[locale]/topics/[topicId]/settings/anki/utils/ankiSetting.util.ts#L33>) | strings.push | (dynamic; see source) |
| [dozu-ui-service/src/app/[locale]/topics/[topicId]/settings/anki/utils/ankiSetting.util.ts:36](<../../dozu-ui-service/src/app/[locale]/topics/[topicId]/settings/anki/utils/ankiSetting.util.ts#L36>) | values.push | (dynamic; see source) |
| [dozu-ui-service/src/app/[locale]/topics/[topicId]/settings/anki/utils/ankiSetting.util.ts:37](<../../dozu-ui-service/src/app/[locale]/topics/[topicId]/settings/anki/utils/ankiSetting.util.ts#L37>) | strings.push | (dynamic; see source) |
| [dozu-ui-service/src/app/[locale]/topics/[topicId]/settings/anki/utils/ankiSetting.util.ts:40](<../../dozu-ui-service/src/app/[locale]/topics/[topicId]/settings/anki/utils/ankiSetting.util.ts#L40>) | values.push | (dynamic; see source) |
| [dozu-ui-service/src/app/[locale]/topics/[topicId]/settings/anki/utils/ankiSetting.util.ts:41](<../../dozu-ui-service/src/app/[locale]/topics/[topicId]/settings/anki/utils/ankiSetting.util.ts#L41>) | strings.push | (dynamic; see source) |
| [dozu-ui-service/src/app/[locale]/topics/components/modals/StudentProfileModal.tsx:173](<../../dozu-ui-service/src/app/[locale]/topics/components/modals/StudentProfileModal.tsx#L173>) | errorMessages.push | Failed to load gamification data |
| [dozu-ui-service/src/app/[locale]/topics/components/modals/StudentProfileModal.tsx:174](<../../dozu-ui-service/src/app/[locale]/topics/components/modals/StudentProfileModal.tsx#L174>) | errorMessages.push | Failed to load streak data |
| [dozu-ui-service/src/app/[locale]/topics/components/modals/StudentProfileModal.tsx:175](<../../dozu-ui-service/src/app/[locale]/topics/components/modals/StudentProfileModal.tsx#L175>) | errorMessages.push | Failed to load learning statistics |
| [dozu-ui-service/src/app/[locale]/topics/components/modals/TopicDetailsModal.tsx:65](<../../dozu-ui-service/src/app/[locale]/topics/components/modals/TopicDetailsModal.tsx#L65>) | Link.href | / |
| [dozu-ui-service/src/app/[locale]/topics/components/ui/ActivityTab.tsx:108](<../../dozu-ui-service/src/app/[locale]/topics/components/ui/ActivityTab.tsx#L108>) | router.push | `/activities/${activityId}` |
| [dozu-ui-service/src/app/[locale]/topics/components/ui/PersonalTopicLibrary.tsx:140](<../../dozu-ui-service/src/app/[locale]/topics/components/ui/PersonalTopicLibrary.tsx#L140>) | router.push | (dynamic; see source) |
| [dozu-ui-service/src/app/[locale]/welcome/page.tsx:470](<../../dozu-ui-service/src/app/[locale]/welcome/page.tsx#L470>) | a.href | # |
| [dozu-ui-service/src/app/[locale]/welcome/page.tsx:477](<../../dozu-ui-service/src/app/[locale]/welcome/page.tsx#L477>) | a.href | # |
| [dozu-ui-service/src/app/[locale]/welcome/page.tsx:484](<../../dozu-ui-service/src/app/[locale]/welcome/page.tsx#L484>) | a.href | # |
| [dozu-ui-service/src/app/[locale]/welcome/page.tsx:491](<../../dozu-ui-service/src/app/[locale]/welcome/page.tsx#L491>) | a.href | mailto:support@dozu.com |
| [dozu-ui-service/src/app/[locale]/welcome/page.tsx:506](<../../dozu-ui-service/src/app/[locale]/welcome/page.tsx#L506>) | a.href | # |
| [dozu-ui-service/src/app/[locale]/welcome/page.tsx:514](<../../dozu-ui-service/src/app/[locale]/welcome/page.tsx#L514>) | a.href | # |
| [dozu-ui-service/src/app/[locale]/welcome/page.tsx:522](<../../dozu-ui-service/src/app/[locale]/welcome/page.tsx#L522>) | a.href | # |
| [dozu-ui-service/src/app/[locale]/welcome/page.tsx:530](<../../dozu-ui-service/src/app/[locale]/welcome/page.tsx#L530>) | a.href | # |
| [dozu-ui-service/src/app/[locale]/welcome/page.tsx:545](<../../dozu-ui-service/src/app/[locale]/welcome/page.tsx#L545>) | a.href | # |
| [dozu-ui-service/src/app/[locale]/welcome/page.tsx:553](<../../dozu-ui-service/src/app/[locale]/welcome/page.tsx#L553>) | a.href | # |
| [dozu-ui-service/src/app/[locale]/welcome/page.tsx:561](<../../dozu-ui-service/src/app/[locale]/welcome/page.tsx#L561>) | a.href | # |
| [dozu-ui-service/src/app/[locale]/welcome/page.tsx:569](<../../dozu-ui-service/src/app/[locale]/welcome/page.tsx#L569>) | a.href | # |
| [dozu-ui-service/src/app/[locale]/welcome/page.tsx:584](<../../dozu-ui-service/src/app/[locale]/welcome/page.tsx#L584>) | a.href | # |
| [dozu-ui-service/src/app/[locale]/welcome/page.tsx:592](<../../dozu-ui-service/src/app/[locale]/welcome/page.tsx#L592>) | a.href | # |
| [dozu-ui-service/src/app/[locale]/welcome/page.tsx:600](<../../dozu-ui-service/src/app/[locale]/welcome/page.tsx#L600>) | a.href | # |
| [dozu-ui-service/src/app/[locale]/welcome/page.tsx:608](<../../dozu-ui-service/src/app/[locale]/welcome/page.tsx#L608>) | a.href | # |
| [dozu-ui-service/src/app/layout.tsx:23](<../../dozu-ui-service/src/app/layout.tsx#L23>) | path | ../fonts/static/Geist-Thin.ttf |
| [dozu-ui-service/src/app/layout.tsx:28](<../../dozu-ui-service/src/app/layout.tsx#L28>) | path | ../fonts/static/Geist-ExtraLight.ttf |
| [dozu-ui-service/src/app/layout.tsx:33](<../../dozu-ui-service/src/app/layout.tsx#L33>) | path | ../fonts/static/Geist-Light.ttf |
| [dozu-ui-service/src/app/layout.tsx:38](<../../dozu-ui-service/src/app/layout.tsx#L38>) | path | ../fonts/static/Geist-Regular.ttf |
| [dozu-ui-service/src/app/layout.tsx:43](<../../dozu-ui-service/src/app/layout.tsx#L43>) | path | ../fonts/static/Geist-Medium.ttf |
| [dozu-ui-service/src/app/layout.tsx:48](<../../dozu-ui-service/src/app/layout.tsx#L48>) | path | ../fonts/static/Geist-SemiBold.ttf |
| [dozu-ui-service/src/app/layout.tsx:53](<../../dozu-ui-service/src/app/layout.tsx#L53>) | path | ../fonts/static/Geist-Bold.ttf |
| [dozu-ui-service/src/app/layout.tsx:58](<../../dozu-ui-service/src/app/layout.tsx#L58>) | path | ../fonts/static/Geist-ExtraBold.ttf |
| [dozu-ui-service/src/app/layout.tsx:63](<../../dozu-ui-service/src/app/layout.tsx#L63>) | path | ../fonts/static/Geist-Black.ttf |
| [dozu-ui-service/src/components/admin/Sidebar.tsx:19](<../../dozu-ui-service/src/components/admin/Sidebar.tsx#L19>) | href | /admin |
| [dozu-ui-service/src/components/admin/Sidebar.tsx:24](<../../dozu-ui-service/src/components/admin/Sidebar.tsx#L24>) | href | /admin/users |
| [dozu-ui-service/src/components/admin/Sidebar.tsx:29](<../../dozu-ui-service/src/components/admin/Sidebar.tsx#L29>) | href | /admin/subscriptions |
| [dozu-ui-service/src/components/admin/Sidebar.tsx:34](<../../dozu-ui-service/src/components/admin/Sidebar.tsx#L34>) | href | /admin/revenue |
| [dozu-ui-service/src/components/admin/Sidebar.tsx:39](<../../dozu-ui-service/src/components/admin/Sidebar.tsx#L39>) | href | /admin/payments |
| [dozu-ui-service/src/components/admin/Sidebar.tsx:45](<../../dozu-ui-service/src/components/admin/Sidebar.tsx#L45>) | href | /admin/feedback |
| [dozu-ui-service/src/components/admin/Sidebar.tsx:51](<../../dozu-ui-service/src/components/admin/Sidebar.tsx#L51>) | href | /admin/stats |
| [dozu-ui-service/src/components/admin/Sidebar.tsx:99](<../../dozu-ui-service/src/components/admin/Sidebar.tsx#L99>) | Link.href | (dynamic; see source) |
| [dozu-ui-service/src/components/class/InviteStudentsModal.tsx:241](<../../dozu-ui-service/src/components/class/InviteStudentsModal.tsx#L241>) | extractedEmails.push | (dynamic; see source) |
| [dozu-ui-service/src/components/comments/CommentList.tsx:73](<../../dozu-ui-service/src/components/comments/CommentList.tsx#L73>) | acc.push | (dynamic; see source) |
| [dozu-ui-service/src/components/comments/CommentList.tsx:75](<../../dozu-ui-service/src/components/comments/CommentList.tsx#L75>) | acc.push | (dynamic; see source) |
| [dozu-ui-service/src/components/comments/utils/markdown.ts:18](<../../dozu-ui-service/src/components/comments/utils/markdown.ts#L18>) | processedLines.push | (dynamic; see source) |
| [dozu-ui-service/src/components/comments/utils/markdown.ts:31](<../../dozu-ui-service/src/components/comments/utils/markdown.ts#L31>) | processedLines.push | `<pre class="bg-muted p-4 rounded-lg overflow-x-auto my-4"><code>${escapeHtml(codeBlockContent.join('\n'))}</code></pre>` |
| [dozu-ui-service/src/components/comments/utils/markdown.ts:38](<../../dozu-ui-service/src/components/comments/utils/markdown.ts#L38>) | processedLines.push | (dynamic; see source) |
| [dozu-ui-service/src/components/comments/utils/markdown.ts:48](<../../dozu-ui-service/src/components/comments/utils/markdown.ts#L48>) | codeBlockContent.push | (dynamic; see source) |
| [dozu-ui-service/src/components/comments/utils/markdown.ts:56](<../../dozu-ui-service/src/components/comments/utils/markdown.ts#L56>) | processedLines.push | (dynamic; see source) |
| [dozu-ui-service/src/components/comments/utils/markdown.ts:60](<../../dozu-ui-service/src/components/comments/utils/markdown.ts#L60>) | processedLines.push | <hr class="my-4 border-t border-border" /> |
| [dozu-ui-service/src/components/comments/utils/markdown.ts:72](<../../dozu-ui-service/src/components/comments/utils/markdown.ts#L72>) | tableRows.push | (dynamic; see source) |
| [dozu-ui-service/src/components/comments/utils/markdown.ts:76](<../../dozu-ui-service/src/components/comments/utils/markdown.ts#L76>) | processedLines.push | (dynamic; see source) |
| [dozu-ui-service/src/components/comments/utils/markdown.ts:92](<../../dozu-ui-service/src/components/comments/utils/markdown.ts#L92>) | processedLines.push | `<h${level} class="${headingClass}">${processInlineMarkdown(content)}</h${level}>` |
| [dozu-ui-service/src/components/comments/utils/markdown.ts:102](<../../dozu-ui-service/src/components/comments/utils/markdown.ts#L102>) | processedLines.push | <ul class="list-disc ml-6 space-y-1 my-2"> |
| [dozu-ui-service/src/components/comments/utils/markdown.ts:105](<../../dozu-ui-service/src/components/comments/utils/markdown.ts#L105>) | processedLines.push | `<li class="ml-2">${processInlineMarkdown(listMatch[1])}</li>` |
| [dozu-ui-service/src/components/comments/utils/markdown.ts:115](<../../dozu-ui-service/src/components/comments/utils/markdown.ts#L115>) | processedLines.push | <ol class="list-decimal ml-6 space-y-1 my-2"> |
| [dozu-ui-service/src/components/comments/utils/markdown.ts:118](<../../dozu-ui-service/src/components/comments/utils/markdown.ts#L118>) | processedLines.push | `<li class="ml-2">${processInlineMarkdown(numberedListMatch[1])}</li>` |
| [dozu-ui-service/src/components/comments/utils/markdown.ts:130](<../../dozu-ui-service/src/components/comments/utils/markdown.ts#L130>) | processedLines.push | <br /> |
| [dozu-ui-service/src/components/comments/utils/markdown.ts:136](<../../dozu-ui-service/src/components/comments/utils/markdown.ts#L136>) | processedLines.push | `<p class="my-2">${processInlineMarkdown(trimmedLine)}</p>` |
| [dozu-ui-service/src/components/comments/utils/markdown.ts:142](<../../dozu-ui-service/src/components/comments/utils/markdown.ts#L142>) | processedLines.push | (dynamic; see source) |
| [dozu-ui-service/src/components/comments/utils/markdown.ts:145](<../../dozu-ui-service/src/components/comments/utils/markdown.ts#L145>) | processedLines.push | `<pre class="bg-muted p-4 rounded-lg overflow-x-auto my-4"><code>${escapeHtml(codeBlockContent.join('\n'))}</code></pre>` |
| [dozu-ui-service/src/components/comments/utils/markdown.ts:160](<../../dozu-ui-service/src/components/comments/utils/markdown.ts#L160>) | html.replace | (dynamic; see source) |
| [dozu-ui-service/src/components/comments/utils/markdown.ts:164](<../../dozu-ui-service/src/components/comments/utils/markdown.ts#L164>) | html.replace | (dynamic; see source) |
| [dozu-ui-service/src/components/comments/utils/markdown.ts:168](<../../dozu-ui-service/src/components/comments/utils/markdown.ts#L168>) | html.replace | (dynamic; see source) |
| [dozu-ui-service/src/components/comments/utils/markdown.ts:183](<../../dozu-ui-service/src/components/comments/utils/markdown.ts#L183>) | html.replace | (dynamic; see source) |
| [dozu-ui-service/src/components/comments/utils/markdown.ts:192](<../../dozu-ui-service/src/components/comments/utils/markdown.ts#L192>) | text .replace(/&/g, '&amp;') .replace(/</g, '&lt;') .replace | (dynamic; see source) |
| [dozu-ui-service/src/components/comments/utils/markdown.ts:192](<../../dozu-ui-service/src/components/comments/utils/markdown.ts#L192>) | text .replace(/&/g, '&amp;') .replace | (dynamic; see source) |
| [dozu-ui-service/src/components/comments/utils/markdown.ts:192](<../../dozu-ui-service/src/components/comments/utils/markdown.ts#L192>) | text .replace | (dynamic; see source) |
| [dozu-ui-service/src/components/comments/utils/markdown.ts:219](<../../dozu-ui-service/src/components/comments/utils/markdown.ts#L219>) | processedRows.push | `<tr>${cellElements.join('')}</tr>` |
| [dozu-ui-service/src/components/errors/DataStatus.tsx:111](<../../dozu-ui-service/src/components/errors/DataStatus.tsx#L111>) | Link.href | (dynamic; see source) |
| [dozu-ui-service/src/components/errors/ErrorPageFallback.tsx:39](<../../dozu-ui-service/src/components/errors/ErrorPageFallback.tsx#L39>) | a.href | / |
| [dozu-ui-service/src/components/errors/NotFoundView.tsx:11](<../../dozu-ui-service/src/components/errors/NotFoundView.tsx#L11>) | Link.href | / |
| [dozu-ui-service/src/components/feedback/FeedbackDialog.tsx:179](<../../dozu-ui-service/src/components/feedback/FeedbackDialog.tsx#L179>) | a.href | https://discord.gg/dozu |
| [dozu-ui-service/src/components/feynman/FeynmanEditor.tsx:63](<../../dozu-ui-service/src/components/feynman/FeynmanEditor.tsx#L63>) | arr.push | (dynamic; see source) |
| [dozu-ui-service/src/components/feynman/FeynmanEditor.tsx:130](<../../dozu-ui-service/src/components/feynman/FeynmanEditor.tsx#L130>) | w.replace | (dynamic; see source) |
| [dozu-ui-service/src/components/feynman/FeynmanEditor.tsx:135](<../../dozu-ui-service/src/components/feynman/FeynmanEditor.tsx#L135>) | decos.push | (dynamic; see source) |
| [dozu-ui-service/src/components/mindmap/TeacherNodeSheet.tsx:113](<../../dozu-ui-service/src/components/mindmap/TeacherNodeSheet.tsx#L113>) | router.push | `/mindmap/add-flashcard?topicId=${selectedNodeData.topicId}&nodeId=${selectedNodeData.nodeId}` |
| [dozu-ui-service/src/components/mindmap/TeacherNodeSheet.tsx:136](<../../dozu-ui-service/src/components/mindmap/TeacherNodeSheet.tsx#L136>) | router.push | `/mindmap/nodes/${selectedNodeData.nodeId}/flashcard` |
| [dozu-ui-service/src/components/permission/AuthGuard.tsx:47](<../../dozu-ui-service/src/components/permission/AuthGuard.tsx#L47>) | router.push | (dynamic; see source) |
| [dozu-ui-service/src/components/pomodoro/Pomodoro.tsx:156](<../../dozu-ui-service/src/components/pomodoro/Pomodoro.tsx#L156>) | merged.push | (dynamic; see source) |
| [dozu-ui-service/src/components/pomodoro/Pomodoro.tsx:456](<../../dozu-ui-service/src/components/pomodoro/Pomodoro.tsx#L456>) | src.replace | indexeddb: |
| [dozu-ui-service/src/components/pomodoro/Pomodoro.tsx:567](<../../dozu-ui-service/src/components/pomodoro/Pomodoro.tsx#L567>) | file.name.replace | (dynamic; see source) |
| [dozu-ui-service/src/components/pomodoro/Pomodoro.tsx:584](<../../dozu-ui-service/src/components/pomodoro/Pomodoro.tsx#L584>) | customBlobUrlsRef.current.push | (dynamic; see source) |
| [dozu-ui-service/src/components/react-bits/Particles.tsx:25](<../../dozu-ui-service/src/components/react-bits/Particles.tsx#L25>) | hex.replace | (dynamic; see source) |
| [dozu-ui-service/src/components/schedule/CalendarWeekView.tsx:56](<../../dozu-ui-service/src/components/schedule/CalendarWeekView.tsx#L56>) | weekDates.push | (dynamic; see source) |
| [dozu-ui-service/src/components/schedule/CalendarWeekView.tsx:66](<../../dozu-ui-service/src/components/schedule/CalendarWeekView.tsx#L66>) | daysOfWeek.push | (dynamic; see source) |
| [dozu-ui-service/src/components/schedule/CalendarWeekView.tsx:139](<../../dozu-ui-service/src/components/schedule/CalendarWeekView.tsx#L139>) | schedulesByDate[dateKey].push | (dynamic; see source) |
| [dozu-ui-service/src/components/schedule/EventCard.tsx:50](<../../dozu-ui-service/src/components/schedule/EventCard.tsx#L50>) | router.push | (dynamic; see source) |
| [dozu-ui-service/src/components/schedule/EventCard.tsx:52](<../../dozu-ui-service/src/components/schedule/EventCard.tsx#L52>) | router.push | (dynamic; see source) |
| [dozu-ui-service/src/components/schedule/FreeTimeSelector.tsx:54](<../../dozu-ui-service/src/components/schedule/FreeTimeSelector.tsx#L54>) | timeSlots.push | (dynamic; see source) |
| [dozu-ui-service/src/components/schedule/FreeTimeSelector.tsx:64](<../../dozu-ui-service/src/components/schedule/FreeTimeSelector.tsx#L64>) | timeSlots.push | (dynamic; see source) |
| [dozu-ui-service/src/components/side-bar/SideBar.tsx:40](<../../dozu-ui-service/src/components/side-bar/SideBar.tsx#L40>) | url | ROUTES.HOME |
| [dozu-ui-service/src/components/side-bar/SideBar.tsx:45](<../../dozu-ui-service/src/components/side-bar/SideBar.tsx#L45>) | url | ROUTES.HOME |
| [dozu-ui-service/src/components/side-bar/SideBar.tsx:50](<../../dozu-ui-service/src/components/side-bar/SideBar.tsx#L50>) | url | ROUTES.PROGRESS |
| [dozu-ui-service/src/components/side-bar/SideBar.tsx:58](<../../dozu-ui-service/src/components/side-bar/SideBar.tsx#L58>) | url | ROUTES.SCHEDULE |
| [dozu-ui-service/src/components/side-bar/SideBar.tsx:63](<../../dozu-ui-service/src/components/side-bar/SideBar.tsx#L63>) | url | ROUTES.SETTING_SCHEDULE_SETUP |
| [dozu-ui-service/src/components/side-bar/SideBar.tsx:68](<../../dozu-ui-service/src/components/side-bar/SideBar.tsx#L68>) | url | # |
| [dozu-ui-service/src/components/side-bar/SideBar.tsx:122](<../../dozu-ui-service/src/components/side-bar/SideBar.tsx#L122>) | Link.href | (dynamic; see source) |
| [dozu-ui-service/src/components/side-bar/SideBar.tsx:157](<../../dozu-ui-service/src/components/side-bar/SideBar.tsx#L157>) | Link.href | (dynamic; see source) |
| [dozu-ui-service/src/components/side-bar/SideBar.tsx:180](<../../dozu-ui-service/src/components/side-bar/SideBar.tsx#L180>) | Link.href | (dynamic; see source) |
| [dozu-ui-service/src/components/tiptap-node/image-upload-node/image-upload-node.tsx:462](<../../dozu-ui-service/src/components/tiptap-node/image-upload-node/image-upload-node.tsx#L462>) | files[index]?.name.replace | (dynamic; see source) |
| [dozu-ui-service/src/components/tiptap-node/image-upload-node/image-upload-node.tsx:477](<../../dozu-ui-service/src/components/tiptap-node/image-upload-node/image-upload-node.tsx#L477>) | to | pos + props.node.nodeSize |
| [dozu-ui-service/src/components/toolbar/AuthButton.tsx:46](<../../dozu-ui-service/src/components/toolbar/AuthButton.tsx#L46>) | router.replace | (dynamic; see source) |
| [dozu-ui-service/src/components/toolbar/AuthButton.tsx:64](<../../dozu-ui-service/src/components/toolbar/AuthButton.tsx#L64>) | Link.href | (dynamic; see source) |
| [dozu-ui-service/src/components/toolbar/LearningModeSelect.tsx:40](<../../dozu-ui-service/src/components/toolbar/LearningModeSelect.tsx#L40>) | router.push | (dynamic; see source) |
| [dozu-ui-service/src/components/toolbar/LearningModeSelect.tsx:42](<../../dozu-ui-service/src/components/toolbar/LearningModeSelect.tsx#L42>) | router.push | (dynamic; see source) |
| [dozu-ui-service/src/components/toolbar/Navbar.tsx:29](<../../dozu-ui-service/src/components/toolbar/Navbar.tsx#L29>) | Link.href | / |
| [dozu-ui-service/src/components/toolbar/UserMenu.tsx:56](<../../dozu-ui-service/src/components/toolbar/UserMenu.tsx#L56>) | router.replace | (dynamic; see source) |
| [dozu-ui-service/src/components/toolbar/UserMenu.tsx:123](<../../dozu-ui-service/src/components/toolbar/UserMenu.tsx#L123>) | router.push | (dynamic; see source) |
| [dozu-ui-service/src/components/ui/full-calendar.tsx:535](<../../dozu-ui-service/src/components/ui/full-calendar.tsx#L535>) | calendar.push | (dynamic; see source) |
| [dozu-ui-service/src/components/ui/full-calendar.tsx:546](<../../dozu-ui-service/src/components/ui/full-calendar.tsx#L546>) | daysOfWeek.push | (dynamic; see source) |
| [dozu-ui-service/src/components/upload/DialogImportFile.tsx:164](<../../dozu-ui-service/src/components/upload/DialogImportFile.tsx#L164>) | newFiles.push | (dynamic; see source) |
| [dozu-ui-service/src/components/upload/DialogImportFile.tsx:351](<../../dozu-ui-service/src/components/upload/DialogImportFile.tsx#L351>) | uploadResults.push | (dynamic; see source) |
| [dozu-ui-service/src/configs/layout/layoutConfig.ts:19](<../../dozu-ui-service/src/configs/layout/layoutConfig.ts#L19>) | pattern.replace | (dynamic; see source) |
| [dozu-ui-service/src/configs/layout/layoutConfig.ts:21](<../../dozu-ui-service/src/configs/layout/layoutConfig.ts#L21>) | p.replace | (dynamic; see source) |
| [dozu-ui-service/src/configs/layout/layoutConfig.ts:23](<../../dozu-ui-service/src/configs/layout/layoutConfig.ts#L23>) | p.replace | (dynamic; see source) |
| [dozu-ui-service/src/configs/layout/layoutConfig.ts:25](<../../dozu-ui-service/src/configs/layout/layoutConfig.ts#L25>) | p.replace | (dynamic; see source) |
| [dozu-ui-service/src/configs/layout/layoutConfig.ts:27](<../../dozu-ui-service/src/configs/layout/layoutConfig.ts#L27>) | l.replace | (dynamic; see source) |
| [dozu-ui-service/src/configs/layout/layoutConfig.ts:29](<../../dozu-ui-service/src/configs/layout/layoutConfig.ts#L29>) | p.replace | (dynamic; see source) |
| [dozu-ui-service/src/configs/layout/list.config.ts:6](<../../dozu-ui-service/src/configs/layout/list.config.ts#L6>) | route/layout constant | /${locale}/welcome |
| [dozu-ui-service/src/configs/layout/list.config.ts:12](<../../dozu-ui-service/src/configs/layout/list.config.ts#L12>) | route/layout constant | /${locale}/auth/* |
| [dozu-ui-service/src/configs/layout/list.config.ts:18](<../../dozu-ui-service/src/configs/layout/list.config.ts#L18>) | route/layout constant | /${locale}/onboarding |
| [dozu-ui-service/src/configs/layout/list.config.ts:24](<../../dozu-ui-service/src/configs/layout/list.config.ts#L24>) | route/layout constant | /${locale} |
| [dozu-ui-service/src/configs/layout/list.config.ts:30](<../../dozu-ui-service/src/configs/layout/list.config.ts#L30>) | route/layout constant | /${locale}/admin |
| [dozu-ui-service/src/configs/layout/list.config.ts:36](<../../dozu-ui-service/src/configs/layout/list.config.ts#L36>) | route/layout constant | /${locale}/admin/* |
| [dozu-ui-service/src/configs/layout/list.config.ts:42](<../../dozu-ui-service/src/configs/layout/list.config.ts#L42>) | route/layout constant | /${locale}/topics/* |
| [dozu-ui-service/src/configs/layout/list.config.ts:48](<../../dozu-ui-service/src/configs/layout/list.config.ts#L48>) | route/layout constant | /${locale}/class-based/*/topics/* |
| [dozu-ui-service/src/configs/layout/list.config.ts:54](<../../dozu-ui-service/src/configs/layout/list.config.ts#L54>) | route/layout constant | /${locale}/teacher/class-based/*/topics/* |
| [dozu-ui-service/src/configs/layout/list.config.ts:63](<../../dozu-ui-service/src/configs/layout/list.config.ts#L63>) | route/layout constant | /${locale}/*/teacher/* |
| [dozu-ui-service/src/configs/layout/list.config.ts:67](<../../dozu-ui-service/src/configs/layout/list.config.ts#L67>) | route/layout constant | /${locale}/*/class-based/* |
| [dozu-ui-service/src/contexts/tracking/UserTrackingContext.tsx:241](<../../dozu-ui-service/src/contexts/tracking/UserTrackingContext.tsx#L241>) | url | window.location.href |
| [dozu-ui-service/src/fonts/geist-config.ts:6](<../../dozu-ui-service/src/fonts/geist-config.ts#L6>) | path | ../fonts/static/Geist-Thin.ttf |
| [dozu-ui-service/src/fonts/geist-config.ts:11](<../../dozu-ui-service/src/fonts/geist-config.ts#L11>) | path | ../fonts/static/Geist-ExtraLight.ttf |
| [dozu-ui-service/src/fonts/geist-config.ts:16](<../../dozu-ui-service/src/fonts/geist-config.ts#L16>) | path | ../fonts/static/Geist-Light.ttf |
| [dozu-ui-service/src/fonts/geist-config.ts:21](<../../dozu-ui-service/src/fonts/geist-config.ts#L21>) | path | ../fonts/static/Geist-Regular.ttf |
| [dozu-ui-service/src/fonts/geist-config.ts:26](<../../dozu-ui-service/src/fonts/geist-config.ts#L26>) | path | ../fonts/static/Geist-Medium.ttf |
| [dozu-ui-service/src/fonts/geist-config.ts:31](<../../dozu-ui-service/src/fonts/geist-config.ts#L31>) | path | ../fonts/static/Geist-SemiBold.ttf |
| [dozu-ui-service/src/fonts/geist-config.ts:36](<../../dozu-ui-service/src/fonts/geist-config.ts#L36>) | path | ../fonts/static/Geist-Bold.ttf |
| [dozu-ui-service/src/fonts/geist-config.ts:41](<../../dozu-ui-service/src/fonts/geist-config.ts#L41>) | path | ../fonts/static/Geist-ExtraBold.ttf |
| [dozu-ui-service/src/fonts/geist-config.ts:46](<../../dozu-ui-service/src/fonts/geist-config.ts#L46>) | path | ../fonts/static/Geist-Black.ttf |
| [dozu-ui-service/src/hoc/withAuth.tsx:45](<../../dozu-ui-service/src/hoc/withAuth.tsx#L45>) | router.push | `${redirectTo}?redirect=${redirectBackPath}` |
| [dozu-ui-service/src/hoc/withAuth.tsx:54](<../../dozu-ui-service/src/hoc/withAuth.tsx#L54>) | router.push | (dynamic; see source) |
| [dozu-ui-service/src/hoc/withAuth.tsx:64](<../../dozu-ui-service/src/hoc/withAuth.tsx#L64>) | router.push | (dynamic; see source) |
| [dozu-ui-service/src/hooks/generate/normalizeStreamByStructure.ts:77](<../../dozu-ui-service/src/hooks/generate/normalizeStreamByStructure.ts#L77>) | extractedItems.push | (dynamic; see source) |
| [dozu-ui-service/src/hooks/generate/normalizeStreamByStructure.ts:82](<../../dozu-ui-service/src/hooks/generate/normalizeStreamByStructure.ts#L82>) | extractedItems.push | (dynamic; see source) |
| [dozu-ui-service/src/hooks/generate/normalizeStreamByStructure.ts:113](<../../dozu-ui-service/src/hooks/generate/normalizeStreamByStructure.ts#L113>) | extractedItems.push | (dynamic; see source) |
| [dozu-ui-service/src/hooks/generate/normalizeStreamByStructure.ts:140](<../../dozu-ui-service/src/hooks/generate/normalizeStreamByStructure.ts#L140>) | extractedItems.push | (dynamic; see source) |
| [dozu-ui-service/src/hooks/generate/normalizeStreamByStructure.ts:231](<../../dozu-ui-service/src/hooks/generate/normalizeStreamByStructure.ts#L231>) | items.push | (dynamic; see source) |
| [dozu-ui-service/src/hooks/generate/normalizeStreamByStructure.ts:362](<../../dozu-ui-service/src/hooks/generate/normalizeStreamByStructure.ts#L362>) | objects.push | (dynamic; see source) |
| [dozu-ui-service/src/hooks/helper.ts:24](<../../dozu-ui-service/src/hooks/helper.ts#L24>) | url | url.startsWith('/') ? url : `/${url}` |
| [dozu-ui-service/src/hooks/use-toast.ts:173](<../../dozu-ui-service/src/hooks/use-toast.ts#L173>) | listeners.push | (dynamic; see source) |
| [dozu-ui-service/src/hooks/useAuthNavigation.ts:55](<../../dozu-ui-service/src/hooks/useAuthNavigation.ts#L55>) | router.push | (dynamic; see source) |
| [dozu-ui-service/src/hooks/useLanguageSwitcher.ts:41](<../../dozu-ui-service/src/hooks/useLanguageSwitcher.ts#L41>) | safePath.replace | (dynamic; see source) |
| [dozu-ui-service/src/hooks/useLanguageSwitcher.ts:52](<../../dozu-ui-service/src/hooks/useLanguageSwitcher.ts#L52>) | router.push | (dynamic; see source) |
| [dozu-ui-service/src/hooks/useNavigation.ts:16](<../../dozu-ui-service/src/hooks/useNavigation.ts#L16>) | router.push | (dynamic; see source) |
| [dozu-ui-service/src/hooks/useNavigation.ts:19](<../../dozu-ui-service/src/hooks/useNavigation.ts#L19>) | router.push | (dynamic; see source) |
| [dozu-ui-service/src/hooks/usePdfReader.tsx:87](<../../dozu-ui-service/src/hooks/usePdfReader.tsx#L87>) | pageTexts.push | (dynamic; see source) |
| [dozu-ui-service/src/hooks/useRedirectChain.ts:42](<../../dozu-ui-service/src/hooks/useRedirectChain.ts#L42>) | pathname?.replace | (dynamic; see source) |
| [dozu-ui-service/src/hooks/useRedirectChain.ts:51](<../../dozu-ui-service/src/hooks/useRedirectChain.ts#L51>) | pathname?.replace | (dynamic; see source) |
| [dozu-ui-service/src/hooks/useRedirectChain.ts:87](<../../dozu-ui-service/src/hooks/useRedirectChain.ts#L87>) | pathname?.replace | (dynamic; see source) |
| [dozu-ui-service/src/lib/tiptap-utils.ts:431](<../../dozu-ui-service/src/lib/tiptap-utils.ts#L431>) | allowedProtocols.push | (dynamic; see source) |
| [dozu-ui-service/src/lib/tiptap-utils.ts:438](<../../dozu-ui-service/src/lib/tiptap-utils.ts#L438>) | uri.replace | (dynamic; see source) |
| [dozu-ui-service/src/services/flashcard/flashcard.service.ts:186](<../../dozu-ui-service/src/services/flashcard/flashcard.service.ts#L186>) | result.push | (dynamic; see source) |
| [dozu-ui-service/src/services/progress/learningStats.service.ts:196](<../../dozu-ui-service/src/services/progress/learningStats.service.ts#L196>) | week.push | (dynamic; see source) |
| [dozu-ui-service/src/services/upload/upload.service.ts:479](<../../dozu-ui-service/src/services/upload/upload.service.ts#L479>) | results.push | (dynamic; see source) |
| [dozu-ui-service/src/services/upload/upload.service.ts:481](<../../dozu-ui-service/src/services/upload/upload.service.ts#L481>) | results.push | (dynamic; see source) |
| [dozu-ui-service/src/stores/features/mindmap/selectedNodeSlice.ts:67](<../../dozu-ui-service/src/stores/features/mindmap/selectedNodeSlice.ts#L67>) | state.hiddenNodeIds.push | (dynamic; see source) |
| [dozu-ui-service/src/stores/features/package/packageSlice.ts:86](<../../dozu-ui-service/src/stores/features/package/packageSlice.ts#L86>) | state.packages.push | (dynamic; see source) |
| [dozu-ui-service/src/stores/features/package/packageSlice.ts:172](<../../dozu-ui-service/src/stores/features/package/packageSlice.ts#L172>) | next.push | (dynamic; see source) |
| [dozu-ui-service/src/stores/features/subscription/useUpgradePlanModal.ts:40](<../../dozu-ui-service/src/stores/features/subscription/useUpgradePlanModal.ts#L40>) | router.push | (dynamic; see source) |
| [dozu-ui-service/src/utils/auth/subscription.ts:11](<../../dozu-ui-service/src/utils/auth/subscription.ts#L11>) | url.replace | (dynamic; see source) |
| [dozu-ui-service/src/utils/constants/routes.ts:5](<../../dozu-ui-service/src/utils/constants/routes.ts#L5>) | route/layout constant | / |
| [dozu-ui-service/src/utils/constants/routes.ts:6](<../../dozu-ui-service/src/utils/constants/routes.ts#L6>) | route/layout constant | /home |
| [dozu-ui-service/src/utils/constants/routes.ts:7](<../../dozu-ui-service/src/utils/constants/routes.ts#L7>) | route/layout constant | /auth/login |
| [dozu-ui-service/src/utils/constants/routes.ts:8](<../../dozu-ui-service/src/utils/constants/routes.ts#L8>) | route/layout constant | /auth/register |
| [dozu-ui-service/src/utils/constants/routes.ts:9](<../../dozu-ui-service/src/utils/constants/routes.ts#L9>) | route/layout constant | /welcome |
| [dozu-ui-service/src/utils/constants/routes.ts:10](<../../dozu-ui-service/src/utils/constants/routes.ts#L10>) | route/layout constant | /onboarding |
| [dozu-ui-service/src/utils/constants/routes.ts:11](<../../dozu-ui-service/src/utils/constants/routes.ts#L11>) | route/layout constant | /generate |
| [dozu-ui-service/src/utils/constants/routes.ts:12](<../../dozu-ui-service/src/utils/constants/routes.ts#L12>) | route/layout constant | /flashcard |
| [dozu-ui-service/src/utils/constants/routes.ts:13](<../../dozu-ui-service/src/utils/constants/routes.ts#L13>) | route/layout constant | /flashcard/create |
| [dozu-ui-service/src/utils/constants/routes.ts:14](<../../dozu-ui-service/src/utils/constants/routes.ts#L14>) | route/layout constant | `/flashcards/edit/${topicId}` |
| [dozu-ui-service/src/utils/constants/routes.ts:15](<../../dozu-ui-service/src/utils/constants/routes.ts#L15>) | route/layout constant | `/flashcards/browse/${topicId}` |
| [dozu-ui-service/src/utils/constants/routes.ts:16](<../../dozu-ui-service/src/utils/constants/routes.ts#L16>) | route/layout constant | `/flashcards/learning/${topicId}` |
| [dozu-ui-service/src/utils/constants/routes.ts:17](<../../dozu-ui-service/src/utils/constants/routes.ts#L17>) | route/layout constant | `/quiz/${topicId}/quiz-type` |
| [dozu-ui-service/src/utils/constants/routes.ts:18](<../../dozu-ui-service/src/utils/constants/routes.ts#L18>) | route/layout constant | /setting/schedule-setup |
| [dozu-ui-service/src/utils/constants/routes.ts:19](<../../dozu-ui-service/src/utils/constants/routes.ts#L19>) | route/layout constant | /unauthorized |
| [dozu-ui-service/src/utils/constants/routes.ts:20](<../../dozu-ui-service/src/utils/constants/routes.ts#L20>) | route/layout constant | /schedule |
| [dozu-ui-service/src/utils/constants/routes.ts:21](<../../dozu-ui-service/src/utils/constants/routes.ts#L21>) | route/layout constant | /library |
| [dozu-ui-service/src/utils/constants/routes.ts:22](<../../dozu-ui-service/src/utils/constants/routes.ts#L22>) | route/layout constant | /progress |
| [dozu-ui-service/src/utils/constants/routes.ts:23](<../../dozu-ui-service/src/utils/constants/routes.ts#L23>) | route/layout constant | /setting/profile |
| [dozu-ui-service/src/utils/constants/routes.ts:24](<../../dozu-ui-service/src/utils/constants/routes.ts#L24>) | route/layout constant | /setting/profile/edit |
| [dozu-ui-service/src/utils/constants/routes.ts:25](<../../dozu-ui-service/src/utils/constants/routes.ts#L25>) | route/layout constant | /setting/profile/avatar |
| [dozu-ui-service/src/utils/constants/routes.ts:26](<../../dozu-ui-service/src/utils/constants/routes.ts#L26>) | route/layout constant | /setting/profile/password |
| [dozu-ui-service/src/utils/constants/routes.ts:27](<../../dozu-ui-service/src/utils/constants/routes.ts#L27>) | route/layout constant | /setting/profile/notifications |
| [dozu-ui-service/src/utils/constants/routes.ts:28](<../../dozu-ui-service/src/utils/constants/routes.ts#L28>) | route/layout constant | /setting/profile/privacy |
| [dozu-ui-service/src/utils/constants/routes.ts:29](<../../dozu-ui-service/src/utils/constants/routes.ts#L29>) | route/layout constant | /setting/profile/settings |
| [dozu-ui-service/src/utils/constants/routes.ts:30](<../../dozu-ui-service/src/utils/constants/routes.ts#L30>) | route/layout constant | `/payment?planId=${planId}` |
| [dozu-ui-service/src/utils/constants/routes.ts:31](<../../dozu-ui-service/src/utils/constants/routes.ts#L31>) | route/layout constant | `/feynman/${topicId}?method=${method}` |
| [dozu-ui-service/src/utils/constants/routes.ts:32](<../../dozu-ui-service/src/utils/constants/routes.ts#L32>) | route/layout constant | `/topics/${topicId}/settings/anki` |
| [dozu-ui-service/src/utils/constants/routes.ts:34](<../../dozu-ui-service/src/utils/constants/routes.ts#L34>) | route/layout constant | `/topics/${topicId}?tab=${tab}` |
| [dozu-ui-service/src/utils/constants/routes.ts:34](<../../dozu-ui-service/src/utils/constants/routes.ts#L34>) | route/layout constant | `/topics/${topicId}` |
| [dozu-ui-service/src/utils/constants/routes.ts:38](<../../dozu-ui-service/src/utils/constants/routes.ts#L38>) | route/layout constant | /admin |
| [dozu-ui-service/src/utils/constants/routes.ts:39](<../../dozu-ui-service/src/utils/constants/routes.ts#L39>) | route/layout constant | /admin/stats |
| [dozu-ui-service/src/utils/constants/routes.ts:42](<../../dozu-ui-service/src/utils/constants/routes.ts#L42>) | route/layout constant | /admin/llm-models |
| [dozu-ui-service/src/utils/constants/routes.ts:43](<../../dozu-ui-service/src/utils/constants/routes.ts#L43>) | route/layout constant | `/admin/llm-models?${query}` |
| [dozu-ui-service/src/utils/constants/routes.ts:43](<../../dozu-ui-service/src/utils/constants/routes.ts#L43>) | route/layout constant | /admin/llm-models |
| [dozu-ui-service/src/utils/constants/routes.ts:44](<../../dozu-ui-service/src/utils/constants/routes.ts#L44>) | route/layout constant | /admin/llm-models |
| [dozu-ui-service/src/utils/constants/routes.ts:45](<../../dozu-ui-service/src/utils/constants/routes.ts#L45>) | route/layout constant | `/admin/llm-models/${id}` |
| [dozu-ui-service/src/utils/constants/routes.ts:46](<../../dozu-ui-service/src/utils/constants/routes.ts#L46>) | route/layout constant | `/admin/llm-models/${id}` |
| [dozu-ui-service/src/utils/constants/routes.ts:47](<../../dozu-ui-service/src/utils/constants/routes.ts#L47>) | route/layout constant | `/admin/llm-models/${id}/toggle-availability` |
| [dozu-ui-service/src/utils/constants/routes.ts:50](<../../dozu-ui-service/src/utils/constants/routes.ts#L50>) | route/layout constant | /admin/llm-providers |
| [dozu-ui-service/src/utils/constants/routes.ts:51](<../../dozu-ui-service/src/utils/constants/routes.ts#L51>) | route/layout constant | `/admin/llm-providers?${query}` |
| [dozu-ui-service/src/utils/constants/routes.ts:51](<../../dozu-ui-service/src/utils/constants/routes.ts#L51>) | route/layout constant | /admin/llm-providers |
| [dozu-ui-service/src/utils/constants/routes.ts:52](<../../dozu-ui-service/src/utils/constants/routes.ts#L52>) | route/layout constant | /admin/llm-providers?limit=100 |
| [dozu-ui-service/src/utils/constants/routes.ts:53](<../../dozu-ui-service/src/utils/constants/routes.ts#L53>) | route/layout constant | /admin/llm-providers |
| [dozu-ui-service/src/utils/constants/routes.ts:54](<../../dozu-ui-service/src/utils/constants/routes.ts#L54>) | route/layout constant | `/admin/llm-providers/${id}` |
| [dozu-ui-service/src/utils/constants/routes.ts:55](<../../dozu-ui-service/src/utils/constants/routes.ts#L55>) | route/layout constant | `/admin/llm-providers/${id}` |
| [dozu-ui-service/src/utils/constants/routes.ts:56](<../../dozu-ui-service/src/utils/constants/routes.ts#L56>) | route/layout constant | `/admin/llm-providers/${id}/toggle-availability` |
| [dozu-ui-service/src/utils/constants/routes.ts:59](<../../dozu-ui-service/src/utils/constants/routes.ts#L59>) | route/layout constant | /admin/llm-api-keys |
| [dozu-ui-service/src/utils/constants/routes.ts:60](<../../dozu-ui-service/src/utils/constants/routes.ts#L60>) | route/layout constant | `/admin/llm-api-keys?${query}` |
| [dozu-ui-service/src/utils/constants/routes.ts:60](<../../dozu-ui-service/src/utils/constants/routes.ts#L60>) | route/layout constant | /admin/llm-api-keys |
| [dozu-ui-service/src/utils/constants/routes.ts:61](<../../dozu-ui-service/src/utils/constants/routes.ts#L61>) | route/layout constant | /admin/llm-api-keys |
| [dozu-ui-service/src/utils/constants/routes.ts:62](<../../dozu-ui-service/src/utils/constants/routes.ts#L62>) | route/layout constant | `/admin/llm-api-keys/${id}` |
| [dozu-ui-service/src/utils/constants/routes.ts:63](<../../dozu-ui-service/src/utils/constants/routes.ts#L63>) | route/layout constant | `/admin/llm-api-keys/${id}` |
| [dozu-ui-service/src/utils/constants/routes.ts:64](<../../dozu-ui-service/src/utils/constants/routes.ts#L64>) | route/layout constant | `/admin/llm-api-keys/${id}/toggle-status` |
| [dozu-ui-service/src/utils/constants/routes.ts:67](<../../dozu-ui-service/src/utils/constants/routes.ts#L67>) | route/layout constant | /admin/llm-api-key-models |
| [dozu-ui-service/src/utils/constants/routes.ts:69](<../../dozu-ui-service/src/utils/constants/routes.ts#L69>) | route/layout constant | `/admin/llm-api-key-models?${query}` |
| [dozu-ui-service/src/utils/constants/routes.ts:69](<../../dozu-ui-service/src/utils/constants/routes.ts#L69>) | route/layout constant | /admin/llm-api-key-models |
| [dozu-ui-service/src/utils/constants/routes.ts:70](<../../dozu-ui-service/src/utils/constants/routes.ts#L70>) | route/layout constant | /admin/llm-api-key-models |
| [dozu-ui-service/src/utils/constants/routes.ts:71](<../../dozu-ui-service/src/utils/constants/routes.ts#L71>) | route/layout constant | `/admin/llm-api-key-models/${id}` |
| [dozu-ui-service/src/utils/constants/routes.ts:72](<../../dozu-ui-service/src/utils/constants/routes.ts#L72>) | route/layout constant | `/admin/llm-api-key-models/${id}` |
| [dozu-ui-service/src/utils/constants/routes.ts:75](<../../dozu-ui-service/src/utils/constants/routes.ts#L75>) | route/layout constant | /admin/feedback |
| [dozu-ui-service/src/utils/constants/routes.ts:76](<../../dozu-ui-service/src/utils/constants/routes.ts#L76>) | route/layout constant | `/admin/feedback?${query}` |
| [dozu-ui-service/src/utils/constants/routes.ts:76](<../../dozu-ui-service/src/utils/constants/routes.ts#L76>) | route/layout constant | /admin/feedback |
| [dozu-ui-service/src/utils/constants/routes.ts:77](<../../dozu-ui-service/src/utils/constants/routes.ts#L77>) | route/layout constant | `/admin/feedback/${id}` |
| [dozu-ui-service/src/utils/constants/routes.ts:78](<../../dozu-ui-service/src/utils/constants/routes.ts#L78>) | route/layout constant | /admin/feedback/ops/auto-ignore |
| [dozu-ui-service/src/utils/constants/routes.ts:81](<../../dozu-ui-service/src/utils/constants/routes.ts#L81>) | route/layout constant | /class-based |
| [dozu-ui-service/src/utils/constants/routes.ts:82](<../../dozu-ui-service/src/utils/constants/routes.ts#L82>) | route/layout constant | `/class-based/${classId}` |
| [dozu-ui-service/src/utils/constants/routes.ts:83](<../../dozu-ui-service/src/utils/constants/routes.ts#L83>) | route/layout constant | `/class-based/${classId}/generate` |
| [dozu-ui-service/src/utils/constants/routes.ts:84](<../../dozu-ui-service/src/utils/constants/routes.ts#L84>) | route/layout constant | `/class-based/${classId}/students` |
| [dozu-ui-service/src/utils/constants/routes.ts:86](<../../dozu-ui-service/src/utils/constants/routes.ts#L86>) | route/layout constant | `/class-based/${classId}/assignments/${assignmentId}/details` |
| [dozu-ui-service/src/utils/constants/routes.ts:95](<../../dozu-ui-service/src/utils/constants/routes.ts#L95>) | route/layout constant | `/class-based/${classId}/topics/${topicId}?tab=${tab}` |
| [dozu-ui-service/src/utils/constants/routes.ts:95](<../../dozu-ui-service/src/utils/constants/routes.ts#L95>) | route/layout constant | `/class-based/${classId}/topics/${topicId}` |
| [dozu-ui-service/src/utils/constants/routes.ts:97](<../../dozu-ui-service/src/utils/constants/routes.ts#L97>) | route/layout constant | `/mindmap/${topicId}` |
| [dozu-ui-service/src/utils/constants/routes.ts:98](<../../dozu-ui-service/src/utils/constants/routes.ts#L98>) | route/layout constant | `/mindmap/view/${topicId}` |
| [dozu-ui-service/src/utils/constants/routes.ts:100](<../../dozu-ui-service/src/utils/constants/routes.ts#L100>) | route/layout constant | `/class-based/${classId}/mindmap/${topicId}` |
| [dozu-ui-service/src/utils/constants/routes.ts:102](<../../dozu-ui-service/src/utils/constants/routes.ts#L102>) | route/layout constant | `/quiz/${topicId}/quiz-type` |
| [dozu-ui-service/src/utils/constants/routes.ts:103](<../../dozu-ui-service/src/utils/constants/routes.ts#L103>) | route/layout constant | `/question/edit/${topicId}` |
| [dozu-ui-service/src/utils/constants/routes.ts:106](<../../dozu-ui-service/src/utils/constants/routes.ts#L106>) | route/layout constant | `/games/brain-chase?topicId=${topicId}` |
| [dozu-ui-service/src/utils/constants/routes.ts:107](<../../dozu-ui-service/src/utils/constants/routes.ts#L107>) | route/layout constant | `/games/memory-match?topicId=${topicId}` |
| [dozu-ui-service/src/utils/constants/routes.ts:112](<../../dozu-ui-service/src/utils/constants/routes.ts#L112>) | route/layout constant | /teacher/home |
| [dozu-ui-service/src/utils/constants/routes.ts:113](<../../dozu-ui-service/src/utils/constants/routes.ts#L113>) | route/layout constant | /teacher/class-based |
| [dozu-ui-service/src/utils/constants/routes.ts:115](<../../dozu-ui-service/src/utils/constants/routes.ts#L115>) | route/layout constant | `/teacher/class-based/${classId}${defaultTab ? `?defaultTab=${defaultTab}` : ''}` |
| [dozu-ui-service/src/utils/constants/routes.ts:116](<../../dozu-ui-service/src/utils/constants/routes.ts#L116>) | route/layout constant | `/teacher/class-based/${classId}/generate` |
| [dozu-ui-service/src/utils/constants/routes.ts:117](<../../dozu-ui-service/src/utils/constants/routes.ts#L117>) | route/layout constant | `/teacher/class-based/${classId}/students` |
| [dozu-ui-service/src/utils/constants/routes.ts:119](<../../dozu-ui-service/src/utils/constants/routes.ts#L119>) | route/layout constant | `/teacher/class-based/${classId}/mindmap/${topicId}` |
| [dozu-ui-service/src/utils/constants/routes.ts:120](<../../dozu-ui-service/src/utils/constants/routes.ts#L120>) | route/layout constant | `/teacher/class-based/${classId}/assignments` |
| [dozu-ui-service/src/utils/constants/routes.ts:122](<../../dozu-ui-service/src/utils/constants/routes.ts#L122>) | route/layout constant | `/teacher/class-based/${classId}/assignments/${assignmentId}/edit` |
| [dozu-ui-service/src/utils/constants/routes.ts:124](<../../dozu-ui-service/src/utils/constants/routes.ts#L124>) | route/layout constant | `/teacher/class-based/${classId}/assignments/${assignmentId}/details` |
| [dozu-ui-service/src/utils/constants/routes.ts:126](<../../dozu-ui-service/src/utils/constants/routes.ts#L126>) | route/layout constant | `/teacher/class-based/${classId}/learning-material` |
| [dozu-ui-service/src/utils/constants/routes.ts:129](<../../dozu-ui-service/src/utils/constants/routes.ts#L129>) | route/layout constant | `/teacher/class-based/${classId}/topics/${topicId}` |
| [dozu-ui-service/src/utils/constants/routes.ts:130](<../../dozu-ui-service/src/utils/constants/routes.ts#L130>) | route/layout constant | `/teacher/class-based/${classId}` |
| [dozu-ui-service/src/utils/constants/routes.ts:132](<../../dozu-ui-service/src/utils/constants/routes.ts#L132>) | route/layout constant | `/teacher/class-based/${classId}/class-quiz/${classQuizId}/edit` |
| [dozu-ui-service/src/utils/constants/routes.ts:134](<../../dozu-ui-service/src/utils/constants/routes.ts#L134>) | route/layout constant | `/teacher/class-based/${classId}/activities/${classQuizId}` |
| [dozu-ui-service/src/utils/constants/routes.ts:140](<../../dozu-ui-service/src/utils/constants/routes.ts#L140>) | route/layout constant | `/class-based/${classId}/class-quiz/${classQuizId}/start` |
| [dozu-ui-service/src/utils/constants/routes.ts:142](<../../dozu-ui-service/src/utils/constants/routes.ts#L142>) | route/layout constant | `/class-based/${classId}/class-quiz/${classQuizId}/submit?attemptId=${attemptId}` |
| [dozu-ui-service/src/utils/date/date.util.ts:70](<../../dozu-ui-service/src/utils/date/date.util.ts#L70>) | pattern.replace(/YYYY/g, 'yyyy').replace | (dynamic; see source) |
| [dozu-ui-service/src/utils/date/date.util.ts:70](<../../dozu-ui-service/src/utils/date/date.util.ts#L70>) | pattern.replace | (dynamic; see source) |
| [dozu-ui-service/src/utils/feeds/feed.helper.ts:64](<../../dozu-ui-service/src/utils/feeds/feed.helper.ts#L64>) | currentFeeds.push | (dynamic; see source) |
| [dozu-ui-service/src/utils/formatters.ts:92](<../../dozu-ui-service/src/utils/formatters.ts#L92>) | formattedNumber.replace | (dynamic; see source) |
| [dozu-ui-service/src/utils/helper.ts:13](<../../dozu-ui-service/src/utils/helper.ts#L13>) | value.trim().replace | (dynamic; see source) |
| [dozu-ui-service/src/utils/helper.ts:15](<../../dozu-ui-service/src/utils/helper.ts#L15>) | s.replace | (dynamic; see source) |
| [dozu-ui-service/src/utils/helper.ts:21](<../../dozu-ui-service/src/utils/helper.ts#L21>) | s.replace | (dynamic; see source) |
| [dozu-ui-service/src/utils/helper.ts:23](<../../dozu-ui-service/src/utils/helper.ts#L23>) | s.replace | (dynamic; see source) |
| [dozu-ui-service/src/utils/helper.ts:186](<../../dozu-ui-service/src/utils/helper.ts#L186>) | text .toLocaleLowerCase() .replace | (dynamic; see source) |
| [dozu-ui-service/src/utils/mindmap/colorThemeUtils.ts:15](<../../dozu-ui-service/src/utils/mindmap/colorThemeUtils.ts#L15>) | sameDepthNodes.push | (dynamic; see source) |
| [dozu-ui-service/src/utils/mindmap/colorThemeUtils.ts:77](<../../dozu-ui-service/src/utils/mindmap/colorThemeUtils.ts#L77>) | adjacentVertices.push | (dynamic; see source) |
| [dozu-ui-service/src/utils/mindmap/colorThemeUtils.ts:99](<../../dozu-ui-service/src/utils/mindmap/colorThemeUtils.ts#L99>) | colorsFound.push | (dynamic; see source) |
| [dozu-ui-service/src/utils/mindmap/initialElements.ts:78](<../../dozu-ui-service/src/utils/mindmap/initialElements.ts#L78>) | nodes.push | (dynamic; see source) |
| [dozu-ui-service/src/utils/mindmap/initialElements.ts:86](<../../dozu-ui-service/src/utils/mindmap/initialElements.ts#L86>) | nodes.push | (dynamic; see source) |
| [dozu-ui-service/src/utils/mindmap/initialElements.ts:88](<../../dozu-ui-service/src/utils/mindmap/initialElements.ts#L88>) | edges.push | (dynamic; see source) |

Navigation configuration: [dozu-ui-service/src/utils/constants/routes.ts:1](<../../dozu-ui-service/src/utils/constants/routes.ts#L1>), [dozu-ui-service/src/utils/auth/redirectService.ts:1](<../../dozu-ui-service/src/utils/auth/redirectService.ts#L1>), [dozu-ui-service/src/configs/layout/list.config.ts:1](<../../dozu-ui-service/src/configs/layout/list.config.ts#L1>), [dozu-ui-service/src/components/side-bar/SideBar.tsx:1](<../../dozu-ui-service/src/components/side-bar/SideBar.tsx#L1>), [dozu-ui-service/src/components/admin/Sidebar.tsx:1](<../../dozu-ui-service/src/components/admin/Sidebar.tsx#L1>), [dozu-ui-service/src/layouts/DefaultLayout.tsx:1](<../../dozu-ui-service/src/layouts/DefaultLayout.tsx#L1>)
