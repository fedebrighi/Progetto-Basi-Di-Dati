
package progetto;

import progetto.data.DAOUtils;
import progetto.model.Model;

public class App {
    public static void main(String[] args) {
        
        DAOUtils.testConnection();

        Model model = new Model();
        Controller controller = new Controller(model);
        View view = new View(controller);

        // Esempio di inserimento di squadre
        controller.aggiungiSquadra("Juve", "1989", "Torino", 50, 100, 20, 1);
        controller.aggiungiSquadra("Inter", "1985", "Milano", 30, 100, 15, 2);
        controller.aggiungiSquadra("Milan", "1990", "Milano", 20, 100, 10, 3);

        // Aggiungi ulteriori chiamate ai metodi del controller per altre operazioni
    }
}
