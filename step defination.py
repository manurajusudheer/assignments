import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import cucumber.api.java.After;
import cucumber.api.java.Before;
import cucumber.api.java.en.*;

public class RegistrationSteps {
    private WebDriver driver:

    @Before
    public void setUp() {
        // Set up WebDriver instance (Assuming ChromeDriver is used)
        System.setProperty("webdriver.chrome.driver", "path/to/chromedriver");
        driver = new ChromeDriver();
    }

    @Given("^the user is on the registration page$")
    public void the_user_is_on_the_registration_page() {
        driver.get("URL_OF_REGISTRATION_PAGE");
    }

    @When("^they enter \"([^\"])\" and \"([^\"])\"$")
    public void they_enter_username_and_email(String username, String email) {
        driver.findElement(By.id("username")).sendKeys(username);
        driver.findElement(By.id("email")).sendKeys(email);
    }

    @And("^they set the password to \"([^\"]*)\"$")
    public void they_set_the_password(String password) {
        driver.findElement(By.id("password")).sendKeys(password);
    }

    @And("^they confirm the password$")
    public void they_confirm_the_password() {
        driver.findElement(By.id("confirmPassword")).sendKeys(driver.findElement(By.id("password")).getAttribute("value"));
    }

    @Then("^the registration should be successful$")
    public void the_registration_should_be_successful() {
        // Add assertion or verification logic for successful registration
    }

    @After
    public void tearDown() {
        // Close the WebDriver instance after each scenario
        if (driver != null) {
            driver.quit();
        }
    }
}