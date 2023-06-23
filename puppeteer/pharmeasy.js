const puppeteer = require('puppeteer');

(async () => {
  try {
    // Launch the browser
    const browser = await puppeteer.launch();

    // Open a new page
    const page = await browser.newPage();

    // Navigate to the website
    await page.goto('https://pharmeasy.in/online-medicine-order/calpol-500mg-strip-of-15-tablets-38810');

    // Click on the button using CSS selector
    const buttonSelector = '#__next > header > div.Header_firstRow__jmzPI > div > div.Header_firstRowContentLhs__P1yGK > div.PincodeTrigger_wrapper___dldv > div.ClickableElement_clickable__ItKj2.PincodeTrigger_pincodeDrawerTrigger__B2Jiq > div > span';
    await page.waitForSelector(buttonSelector);
    await page.click(buttonSelector);
    await new Promise((resolve) => setTimeout(resolve, 5000));
    // Wait for the input field to load
    const inputSelector = '#drawers-portal > div > div.Drawer_content__pyx8d.Drawer_right__WsHZS.Drawer_fullHeightDrawer__WVc3p > div.PincodeDrawer_pincodeDrawerWrapper__KYnyZ > div:nth-child(1) > div.PincodeDrawer_inputErrorWrapper__kZvzn > div > div > input';
    await page.waitForSelector(inputSelector);
    const inputElement = await page.$(inputSelector);
    await new Promise((resolve) => setTimeout(resolve, 5000));
    // Insert data into the input field
    await inputElement.type('226001');
    await new Promise((resolve) => setTimeout(resolve, 5000));
    // Press Enter
    await inputElement.press('Enter');
    await new Promise((resolve) => setTimeout(resolve, 5000));;
    // Wait for the element you want to extract to appear
    const elementSelector = '#__next > main > div > div.Content_container__oOxF6 > div.LHS_container__mrQkM > div.PDPDesktop_infoContainer__LCH8b > div.MedicineOverviewSection_medicineUnitContainer__F6ZV_ > div > div > div > div.MedicineOverviewSection_productWarningAndCta__LLTZI.MedicineOverviewSection_displayBlock__S4sRp > div.Edd_eddDetails__8kgLR > div > span';
    await page.waitForSelector(elementSelector);
    const elementValue = await page.$eval(elementSelector, (element) => element.textContent);

    console.log('Element value:', elementValue);
    
    // Close the browser
    await browser.close();
  } catch (error) {
    console.error('An error occurred:', error);
  }
})();
