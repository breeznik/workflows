# Workflow: Testing

> **Trigger**: Before every commit or verification phase.

## 🧪 Test Suite

| Type | Command | Description |
|------|---------|-------------|
| **Unit** | `npm run test` | Fast, isolated logic tests. |
| **Integration** | `npm run test:int` | DB and API interaction tests. |
| **E2E** | `npm run test:e2e` | Full browser automation. |

## 🛠️ Troubleshooting

- If tests fail, check `logs/test-error.log`.
- Ensure `.env.test` is configured.
