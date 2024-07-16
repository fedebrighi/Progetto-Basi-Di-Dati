package progetto;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import progetto.model.Model;

import static org.junit.jupiter.api.Assertions.assertDoesNotThrow;

public class AppTest {
    private Controller controller;

    @BeforeEach
    public void setUp() {
        Model model = new Model();
        controller = new Controller(model);
    }

    @Test
    public void testAggiungiSquadra() {
        assertDoesNotThrow(() -> {
            controller.aggiungiSquadra("Juve", "1989", "Torino", 50, 100, 20, 1);
            controller.aggiungiSquadra("Inter", "1985", "Milano", 30, 100, 15, 2);
            controller.aggiungiSquadra("Milan", "1990", "Milano", 20, 100, 10, 3);
        });
    }

    // Aggiungi ulteriori test per altre operazioni
}
