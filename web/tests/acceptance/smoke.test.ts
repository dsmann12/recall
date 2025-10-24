import { test, expect } from '@playwright/test';


test('has title', async ({ page }) => {
  await page.goto('/');

  await expect(page).toHaveTitle(/recall/i);
});

test('has construction placeholder', async ({ page }) => {
  await page.goto('/');

  await expect(page.getByText(/recall is currently under construction/i)).toBeVisible();
});
