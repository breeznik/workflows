# Workflow: Deployment

> **Trigger**: Merge to main or Manual Release.

## 🚀 Pipeline

1.  **Build**: `npm run build`
2.  **Migrate**: `npx prisma migrate deploy`
3.  **Deploy**: `vercel --prod`

## 🛡️ Safety Checks

- [ ] Schema validation passed?
- [ ] No P0 issues in `context/active/status.json`?
- [ ] User approval received?
