
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time

var page = require('webpage').create();
page.settings.userAgent = 'Mozilla/4.0 (compatible; MSIE 6.1; Windows XP)';
page.open('http://www.httpuseragent.org', function (status) {
    if (status == 'success') {
        var agent = page.evaluate(function () {
            return document.getElementById('myagent').innerText;
        });
        console.log(agent);
    } else {
    	console.log('cannot open page');
    }
    phantom.exit();
});
