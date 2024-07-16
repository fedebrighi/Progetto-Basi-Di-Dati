package progetto;
import java.util.List;

import progetto.model.Model;

public class Controller {
    private Model model;

    public Controller(Model model) {
        this.model = model;
    }

    public void aggiungiSquadra(String nome, String annoFondazione, String cittaRiferimento, int trofeiVinti,
            int quotaIscrizione, int punteggio, int posClassifica) {
        model.aggiungiSquadra(nome, annoFondazione, cittaRiferimento, trofeiVinti, quotaIscrizione, punteggio,
                posClassifica);
    }
    

    public List<String> getSquadre() {
        return model.getSquadre();
    }

    // Aggiungi ulteriori metodi per altre operazioni
}
