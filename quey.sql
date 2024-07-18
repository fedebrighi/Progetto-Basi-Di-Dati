INSERT INTO direttore_sportivo (CodiceFiscale, Nome, Cognome, DataNascita, Nazionalita, Stipendio) VALUES
('SCE123XYZ456DEF0', 'Pietro', 'Neri', '1970-03-15', 'Italiana', '80000'),
('SCE456XYZ123ABC1', 'Marco', 'Gialli', '1978-12-10', 'Italiana', '85000'),
('SCE789XYZ456JKL2', 'Antonio', 'Blu', '1985-07-25', 'Italiana', '90000');

INSERT INTO presidente (CodiceFiscale, Nome, Cognome, DataNascita, Nazionalita) VALUES 
('PRES123456', 'Giuseppe', 'Verdi', '1960-04-15', 'Italiana'),
('PRES654321', 'Alessandro', 'Rossi', '1972-08-22', 'Italiana'),
('PRES789012', 'Federico', 'Bianchi', '1985-12-05', 'Italiana');

INSERT INTO fondi (IBAN, Totale, CodicePresidente, CodiceDir) VALUES 
('IT60X0542811101000000123456', '100000', 'PRES123456', 'SCE123XYZ456DEF0'),
('IT40S0542811101000000123457', '150000', 'PRES654321', 'SCE456XYZ123ABC1'),
('IT90R0542811101000000123458', '200000', 'PRES789012', 'SCE789XYZ456JKL2');

INSERT INTO sponsor(Nome,Quota,DescContratto)VALUES
('Nike','10000','Contratto x 2 anni'),
('Adidas','17000','Contratto x 3 anni'),
('Puma','8000','Contratto x 4 anni');

INSERT INTO contribuzione(IBAN,NomeSponsor) VALUES
('IT60X0542811101000000123456','Nike'),
('IT40S0542811101000000123457','Adidas'),
('IT90R0542811101000000123458','Puma');

INSERT INTO televisione (Nome, Contributo) VALUES 
('TeleSport', '1000000'),
('SportTV', '1500000'),
('SportNetwork', '2000000');

INSERT INTO info_torneo (CodTorneo, Spese, TotaleFondi, Vincitrice, PuntiPersi, PuntiGuadagnati, PunteggioMinimo, PunteggioVittoria) VALUES 
('TORN123456', '5000', '100000', 'SquadraA', '10', '20', '5', '25'),
('TORN654321', '7500', '150000', 'SquadraB', '15', '25', '7', '30'),
('TORN789012', '10000', '200000', 'SquadraC', '8', '18', '6', '28');

INSERT INTO trasmissione (NomeTV, CodTorneo) VALUES 
('TeleSport', 'TORN123456'),
('SportTV', 'TORN654321'),
('SportNetwork', 'TORN789012');

INSERT INTO sponsor_torneo (Nome, Contributo, CodTorneo) VALUES
('Spotify', '100000', 'TORN123456'),
('Armani', '150000', 'TORN654321'),
('Netflix', '200000', 'TORN789012');

INSERT INTO data (Giorno, Mese, Anno, CodTorneo) VALUES 
('15', '04', '2024', 'TORN123456'),
('22', '05', '2024', 'TORN123456'),
('30', '06', '2024', 'TORN123456');

INSERT INTO stadio (CodiceStadio, Nome, Citta, Capienza, Affitto) VALUES 
('STAD001', 'Stadio Olimpico', 'Roma', '70000', '50000'),
('STAD002', 'San Siro', 'Milano', '80000', '60000'),
('STAD003', 'Stadio Artemio Franchi', 'Firenze', '43000', '30000');

INSERT INTO squadra (Nome,AnnoFondazione,CittaRiferimento,TrofeiVinti,Quota_Iscrizione,Punteggio,PosClassifica) VALUES
('Juventus', '1989', 'Torino',50, 100,20,1),
('Inter', '1985', 'Milano',30, 100,15,2),
('Milan', '1990', 'Milano',20, 100,10,3);

INSERT INTO staff_partita (CodiceFiscale, Nome, Cognome, DataNascita, Nazionalita, Ruolo, Stipendio) VALUES 
('STAFF001', 'Luca', 'Bianchi', '1980-01-15', 'Italiana', 'Allenatore', '45000'),
('STAFF002', 'Marco', 'Rossi', '1985-05-22', 'Italiana', 'Preparatore Atletico', '40000'),
('STAFF003', 'Anna', 'Verdi', '1990-10-30', 'Italiana', 'Fisioterapista', '42000');

INSERT INTO tabellino_statistiche (CodiceTabellino, DataTab, GoalOspite, GoalCasa, Pali, Cartellini, CodiceStaff) VALUES
('TAB123456', '2024-04-15', '2', '3', '1', '2', 'STAFF001'),
('TAB654321', '2024-05-22', '1', '1', '0', '3', 'STAFF002'),
('TAB789012', '2024-06-30', '0', '2', '2', '1', 'STAFF003');

INSERT INTO partita (CodicePartita, CodiceTabellino, Risultato, Vincitrice, Biglietti, PrezzoBiglietto, NomeOspite, NomeCasa, CodiceStadio, Giorno, Mese, Anno) VALUES
('PART001', 'TAB123456', '3-2', 'Juventus', '20000', '50', 'Juventus', 'Inter', 'STAD001', '15', '04', '2024'),
('PART002', 'TAB654321', '1-1', 'Nessuna', '18000', '45', 'Inter', 'Milan', 'STAD002', '22', '05', '2024'),
('PART003', 'TAB789012', '0-2', 'Milan', '22000', '55', 'Juventus', 'Milan', 'STAD003', '30', '06', '2024');

INSERT INTO supervisione (CodiceStaff, CodicePartita) VALUES 
('STAFF001', 'PART001'),
('STAFF002', 'PART002'),
('STAFF003', 'PART003');

INSERT INTO infortuni(Codicetabellino,Infortuni) VALUES 
('TAB123456','Infortunato'),
('TAB654321','Non Infortunato'),
('TAB789012','Non Infortunato');

INSERT INTO marcatori (CodiceTabellino, Marcatori) VALUES 
('TAB123456', 'Giovanni Rossi'),
('TAB654321', 'Marco Bianchi'),
('TAB789012', 'Luca Verdi');

INSERT INTO allenatore (CodiceFiscale, Sce_CodiceFiscale, All_Nome, Nome, Cognome, DataNascita, Nazionalita, Stipendio) VALUES
('ABC123XYZ456DEF0', 'SCE123XYZ456DEF0', 'Juventus', 'Mario', 'Rossi', '1975-05-15', 'Italiana', '50000'),
('DEF456XYZ123ABC1', 'SCE456XYZ123ABC1', 'Inter', 'Luigi', 'Bianchi', '1980-11-22', 'Italiana', '60000'),
('GHI789XYZ456JKL2', 'SCE789XYZ456JKL2', 'Milan', 'Giovanni', 'Verdi', '1985-07-30', 'Italiana', '70000');

INSERT INTO staff (CodiceFiscale, Nome, Cognome, DataNascita, Nazionalita, Ruolo, Stipendio, CodiceAll) VALUES 
('STAFF001', 'Luca', 'Bianchi', '1980-01-15', 'Italiana', 'Preparatore Atletico', '40000', 'ABC123XYZ456DEF0'),
('STAFF002', 'Marco', 'Rossi', '1985-05-22', 'Italiana', 'Fisioterapista', '42000', 'DEF456XYZ123ABC1'),
('STAFF003', 'Anna', 'Verdi', '1990-10-30', 'Italiana', 'Allenatore in seconda', '45000', 'GHI789XYZ456JKL2');

INSERT INTO giocatore (Codicefiscale, Nome, Cognome, DataNascita, Nazionalita, Stipendio,Infortunio,Espulsione,Nomesquadra) VALUES
('CF1234567890', 'Mario', 'Rossi', '1990-01-01', 'Italiana', 50000,'Disponibile', 'Disponibile' ,'Juventus'),
('CF0987654321', 'Luigi', 'Verdi', '1988-05-10', 'Italiana', 45000,'Infortunato','Disponibile' ,'Inter'),
('CF1122334455', 'Paolo', 'Bianchi', '1992-07-20', 'Italiana', 60000,'Disponibile','Disponibile' ,'Milan');

INSERT INTO mercato_giocatori (CodiceGiocatore, Durata, Costo) VALUES 
('CF0987654321', '2024-2026', '5000000'),
('CF1122334455', '2023-2025', '7500000'),
('CF1234567890', '2025-2028', '10000000');

INSERT INTO tramite (CodiceDir, CodiceGiocatore, Durata) VALUES 
('SCE123XYZ456DEF0', 'CF0987654321', '2024-2026'),
('SCE456XYZ123ABC1', 'CF1122334455', '2023-2025'),
('SCE789XYZ456JKL2', 'CF1234567890', '2025-2028');

INSERT INTO numero (NomeSquadra, Numero, CodiceFiscale, Ruolo) VALUES
('Juventus', '10', 'CF1234567890', 'Attaccante'),
('Inter', '5', 'CF0987654321', 'Difensore'),
('Milan', '7', 'CF1122334455', 'Centrocampista');