package progetto;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.List;

public class View {
    private JFrame frame;
    private JTextField nomeField;
    private JTextField annoField;
    private JTextField cittaField;
    private JTextField trofeiField;
    private JTextField quotaField;
    private JTextField punteggioField;
    private JTextField posizioneField;
    private Controller controller;
    private JTextArea squadreArea;

    public View(Controller controller) {
        this.controller = controller;
        initialize();
    }

    private void initialize() {
        frame = new JFrame("Gestione Squadre");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(400, 400);
        frame.setLayout(new GridLayout(10, 2));

        // Campi di input
        frame.add(new JLabel("Nome:"));
        nomeField = new JTextField();
        frame.add(nomeField);

        frame.add(new JLabel("Anno di Fondazione:"));
        annoField = new JTextField();
        frame.add(annoField);

        frame.add(new JLabel("Città di Riferimento:"));
        cittaField = new JTextField();
        frame.add(cittaField);

        frame.add(new JLabel("Trofei Vinti:"));
        trofeiField = new JTextField();
        frame.add(trofeiField);

        frame.add(new JLabel("Quota Iscrizione:"));
        quotaField = new JTextField();
        frame.add(quotaField);

        frame.add(new JLabel("Punteggio:"));
        punteggioField = new JTextField();
        frame.add(punteggioField);

        frame.add(new JLabel("Posizione in Classifica:"));
        posizioneField = new JTextField();
        frame.add(posizioneField);

        // Bottone di submit
        JButton submitButton = new JButton("Aggiungi Squadra");
        frame.add(submitButton);

        // Bottone per visualizzare le squadre
        JButton showButton = new JButton("Visualizza Squadre");
        frame.add(showButton);

        // Area di testo per visualizzare le squadre
        squadreArea = new JTextArea();
        frame.add(squadreArea);

        // Etichetta di stato
        JLabel statusLabel = new JLabel();
        frame.add(statusLabel);

        // Listener per il bottone di submit
        submitButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                try {
                    String nome = nomeField.getText();
                    String anno = annoField.getText();
                    String citta = cittaField.getText();
                    int trofei = Integer.parseInt(trofeiField.getText());
                    int quota = Integer.parseInt(quotaField.getText());
                    int punteggio = Integer.parseInt(punteggioField.getText());
                    int posizione = Integer.parseInt(posizioneField.getText());

                    // Validazione dei campi
                    if (nome.isEmpty() || anno.isEmpty() || citta.isEmpty() || 
                        trofei < 0 || quota < 0 || punteggio < 0 || posizione < 0) {
                        statusLabel.setText("Errore: tutti i campi devono essere riempiti correttamente.");
                        return;
                    }

                    controller.aggiungiSquadra(nome, anno, citta, trofei, quota, punteggio, posizione);
                    statusLabel.setText("Squadra aggiunta con successo!");
                } catch (NumberFormatException nfe) {
                    statusLabel.setText("Errore: inserire numeri validi per i campi Trofei, Quota, Punteggio, Posizione.");
                } catch (Exception ex) {
                    statusLabel.setText("Errore: " + ex.getMessage());
                }
            }
        });

        // Listener per il bottone di visualizzazione delle squadre
        showButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                List<String> squadre = controller.getSquadre();
                squadreArea.setText("");
                for (String squadra : squadre) {
                    squadreArea.append(squadra + "\n");
                }
            }
        });

        frame.setVisible(true);
    }
}
