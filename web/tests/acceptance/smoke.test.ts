import { test, expect } from '@playwright/test';

const RECALL_CLIENT_TEST_URL = 'http://localhost:5173';

test('has title', async ({ page }) => {
  await page.goto(RECALL_CLIENT_TEST_URL);

  await expect(page).toHaveTitle(/recall/i);
});

test('has construction placeholder', async ({ page }) => {
  await page.goto(RECALL_CLIENT_TEST_URL);

  await expect(page.getByText(/recall is currently under construction/i)).toBeVisible();
});
