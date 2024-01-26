package starter.interactions;

import net.serenitybdd.screenplay.Actor;
import net.serenitybdd.screenplay.Interaction;
import net.thucydides.core.webdriver.ThucydidesWebDriverSupport;
import org.openqa.selenium.Alert;
import org.openqa.selenium.WebDriver;

public class HandleAlert implements Interaction {

    @Override
    public <T extends Actor> void performAs(T actor) {
        WebDriver driver = ThucydidesWebDriverSupport.getDriver();
        try {
            Alert alert = driver.switchTo().alert();

            // Read the alert text and handle the alert
            String alertText = alert.getText();
            System.out.println("Alert text is: " + alertText);
            alert.accept(); // or alert.dismiss() based on your requirement
        } catch (Exception e) {
            // Handle the case where there is no alert
            System.out.println("No alert present: " + e.getMessage());
        }
    }

    public static HandleAlert handleIt() {
        return new HandleAlert();
    }
}
