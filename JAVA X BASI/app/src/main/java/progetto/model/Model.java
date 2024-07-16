package progetto.model;
import java.sql.SQLException;
import java.util.List;

public class Model {
    private DBModel dbModel;

    public Model() {
        this.dbModel = new DBModel();
    }

    public void aggiungiSquadra(String nome, String annoFondazione, String cittaRiferimento, int trofeiVinti, int quotaIscrizione, int punteggio, int posClassifica) {
        try {
            dbModel.inserisciSquadra(nome, annoFondazione, cittaRiferimento, trofeiVinti, quotaIscrizione, punteggio, posClassifica);
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

     public List<String> getSquadre() {
        try {
            return dbModel.getAllSquadre();
        } catch (SQLException e) {
            e.printStackTrace();
            return null;
        }

    }

    // Aggiungi ulteriori metodi per altre operazioni
}
