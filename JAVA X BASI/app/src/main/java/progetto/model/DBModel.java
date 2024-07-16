package progetto.model;

import progetto.data.DAOUtils;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.List;

public class DBModel {
    public void inserisciSquadra(String nome, String annoFondazione, String cittaRiferimento, int trofeiVinti,
            int quotaIscrizione, int punteggio, int posClassifica) throws SQLException {
        String query = "INSERT INTO squadra (Nome, AnnoFondazione, CittaRiferimento, TrofeiVinti, Quota_Iscrizione, Punteggio, PosClassifica) VALUES (?, ?, ?, ?, ?, ?, ?)";
        try (Connection conn = DAOUtils.getConnection();
                PreparedStatement pstmt = conn.prepareStatement(query)) {
            pstmt.setString(1, nome);
            pstmt.setString(2, annoFondazione);
            pstmt.setString(3, cittaRiferimento);
            pstmt.setInt(4, trofeiVinti);
            pstmt.setInt(5, quotaIscrizione);
            pstmt.setInt(6, punteggio);
            pstmt.setInt(7, posClassifica);
            pstmt.executeUpdate();
        }
    }

    public List<String> getAllSquadre() throws SQLException {
        String query = "SELECT * FROM squadra";
        List<String> squadre = new ArrayList<>();
        try (Connection conn = DAOUtils.getConnection();
                PreparedStatement pstmt = conn.prepareStatement(query);
                ResultSet rs = pstmt.executeQuery()) {
            while (rs.next()) {
                String squadra = String.format("Nome: %s, Anno: %s, Città: %s, Trofei: %d, Quota: %d, Punteggio: %d, Posizione: %d",
                        rs.getString("Nome"), rs.getString("AnnoFondazione"), rs.getString("CittaRiferimento"),
                        rs.getInt("TrofeiVinti"), rs.getInt("Quota_Iscrizione"), rs.getInt("Punteggio"), rs.getInt("PosClassifica"));
                squadre.add(squadra);
            }
        }
        return squadre;
    }

    // Aggiungi ulteriori metodi per altre tabelle e operazioni
}
