const puppeteer = require('puppeteer');

(async () => {
  try {
    // Launch the browser
    const browser = await puppeteer.launch();

    // Open a new page
    const page = await browser.newPage();

    // Navigate to the website
    await page.goto('https://www.1mg.com/drugs/calpol-500mg-tablet-69656');

    // Click on the button using CSS selector
    const buttonSelector = '#eta-content > div > div.style__deliveryBox___g_mGG.style__padded___2vNu9.style__marginTop-12___36A_e > div.style__marginLeft-4___fp1Ae.style__delivery-cta___1C7Gt > span.style__deliveryText___1f5Qp';
    await page.waitForSelector(buttonSelector);
    await page.click(buttonSelector);
    await new Promise((resolve) => setTimeout(resolve, 5000));
    // Wait for the input field to load
    const inputSelector = '#container > div > div > div.style__wrapper___1S4gB.style__vertical-aligner___3W6ut > div > div > div > div > div > div.styles__padding-20___Wy_Nw.styles__content___3072V > div.styles__sticky-input-wrapper___P-Kfd > div.styles__flex___11AYu.styles__spaceBetween___1Fvac.styles__input-wrapper___34GKg > div.styles__input-box___LiENa > div > div.InputField__flex___3-uuk.InputField__inputContainer___2UaoX > input';
    await page.waitForSelector(inputSelector);
    const inputElement = await page.$(inputSelector);
    await new Promise((resolve) => setTimeout(resolve, 5000));
    // Insert data into the input field
    await inputElement.type('226001');
    await new Promise((resolve) => setTimeout(resolve, 5000));
    // Press Enter
    await inputElement.press('Enter');
    await new Promise((resolve) => setTimeout(resolve, 5000));
    // Wait for the element you want to extract to appear
    const elementSelector = '#eta-content > div > div.style__padded___2vNu9.style__headerText___3sw_C > span:nth-child(2)';
    await page.waitForSelector(elementSelector);
    const elementValue = await page.$eval(elementSelector, (element) => element.textContent);

    console.log('Element value:', elementValue);
    
    // Close the browser
    await browser.close();
  } catch (error) {
    console.error('An error occurred:', error);
  }
})();
