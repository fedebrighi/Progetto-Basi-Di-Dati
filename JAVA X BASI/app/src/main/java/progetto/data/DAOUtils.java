package progetto.data;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

public class DAOUtils {
    private static final String URL = "jdbc:mysql://127.0.0.1:3306/PROGETTO"; // URL del database
    private static final String USER = "root"; // Nome utente del database
    private static final String PASSWORD = "your_password_here"; // Password del database

    static {
        try {
            Class.forName("com.mysql.cj.jdbc.Driver");
        } catch (ClassNotFoundException e) {
            e.printStackTrace();
            System.out.println("Errore nel caricamento del driver JDBC: " + e.getMessage());
        }
    }

    public static Connection getConnection() throws SQLException {
        return DriverManager.getConnection(URL, USER, PASSWORD);
    }

    public static void testConnection() {
        try (Connection conn = getConnection()) {
            System.out.println("Connessione al database riuscita!");
        } catch (SQLException e) {
            e.printStackTrace();
            System.out.println("Errore nella connessione al database: " + e.getMessage());
        }
    }
}
