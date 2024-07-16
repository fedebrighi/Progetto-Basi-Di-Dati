-- *********************************************
-- * SQL MySQL generation                      
-- *--------------------------------------------
-- * DB-MAIN version: 11.0.2              
-- * Generator date: Sep 14 2021              
-- * Generation date: Mon Jul 15 21:55:53 2024 
-- * LUN file: C:\Users\ddunl\OneDrive\Desktop\Progetto-Basi-Di-Dati\ER BASI DATI.lun 
-- * Schema: CHAMPION HUB/Logico-1 
-- ********************************************* 


-- Database Section
-- ________________ 

create database CHAMPION_HUB;
use CHAMPION_HUB;


-- Tables Section
-- _____________ 

create table ALLENATORE (
     CodiceFiscale char(1) not null,
     Sce_CodiceFiscale char(1) not null,
     All_Nome char(1) not null,
     Nome char(1) not null,
     Cognome char(1) not null,
     DataNascita char(1) not null,
     Nazionalita char(1) not null,
     Stipendio char(1) not null,
     constraint ID_ALLENATORE_ID primary key (CodiceFiscale),
     constraint SID_ALLEN_DIRET_ID unique (Sce_CodiceFiscale),
     constraint SID_ALLEN_SQUAD_ID unique (All_Nome));

create table CONTRIBUZIONE (
     IBAN char(1) not null,
     NomeSponsor char(1) not null,
     constraint ID_CONTRIBUZIONE_ID primary key (IBAN, NomeSponsor));

create table DATA (
     Giorno char(1) not null,
     Mese char(1) not null,
     Anno char(1) not null,
     CodTorneo char(1) not null,
     constraint ID_DATA_ID primary key (Giorno, Mese, Anno));

create table DIRETTORE_SPORTIVO (
     CodiceFiscale char(1) not null,
     Nome char(1) not null,
     Cognome char(1) not null,
     DataNascita char(1) not null,
     Nazionalita char(1) not null,
     Stipendio char(1) not null,
     constraint ID_DIRETTORE_SPORTIVO_ID primary key (CodiceFiscale));

create table FONDI (
     IBAN char(1) not null,
     Totale char(1) not null,
     CodicePresidente char(1) not null,
     CodiceDir char(1) not null,
     constraint ID_FONDI_ID primary key (IBAN));

create table GIOCATORE (
     CodiceFiscale char(1) not null,
     Nome char(1) not null,
     Cognome char(1) not null,
     DataNascita char(1) not null,
     Nazionalita char(1) not null,
     Stipendio char(1) not null,
     Infortunio char(1),
     Espulsione char(1),
     NomeSquadra char(1) not null,
     constraint ID_GIOCATORE_ID primary key (CodiceFiscale));

create table INFO_TORNEO (
     CodTorneo char(1) not null,
     Spese char(1) not null,
     TotaleFondi char(1) not null,
     Vincitrice char(1),
     PuntiPersi char(1) not null,
     PuntiGuadagnati char(1) not null,
     PunteggioMinimo char(1) not null,
     PunteggioVittoria char(1) not null,
     constraint ID_INFO_TORNEO_ID primary key (CodTorneo));

create table Infortuni (
     CodiceTabellino char(1) not null,
     Infortuni char(1) not null,
     constraint ID_Infortuni_ID primary key (CodiceTabellino, Infortuni));

create table Marcatori (
     CodiceTabellino char(1) not null,
     Marcatori char(1) not null,
     constraint ID_Marcatori_ID primary key (CodiceTabellino, Marcatori));

create table MERCATO_GIOCATORI (
     CodiceGiocatore char(1) not null,
     Durata char(1) not null,
     Costo char(1) not null,
     constraint ID_MERCATO_GIOCATORI_ID primary key (CodiceGiocatore, Durata));

create table NUMERO (
     NomeSquadra char(1) not null,
     Numero char(1) not null,
     CodiceFiscale char(1) not null,
     Ruolo char(1) not null,
     constraint ID_NUMERO_ID primary key (NomeSquadra, Numero),
     constraint SID_NUMER_GIOCA_ID unique (CodiceFiscale));

create table PARTITA (
     CodicePartita char(1) not null,
     CodiceTabellino char(1) not null,
     Risultato char(1),
     Vincitrice char(1),
     Biglietti char(1) not null,
     PrezzoBiglietto char(1) not null,
     NomeOspite char(1) not null,
     NomeCasa char(1) not null,
     CodiceStadio char(1) not null,
     Giorno char(1) not null,
     Mese char(1) not null,
     Anno char(1) not null,
     constraint ID_PARTITA_ID primary key (CodicePartita),
     constraint SID_PARTI_TABEL_ID unique (CodiceTabellino));

create table PRESIDENTE (
     CodiceFiscale char(1) not null,
     Nome char(1) not null,
     Cognome char(1) not null,
     DataNascita char(1) not null,
     Nazionalita char(1) not null,
     constraint ID_PRESIDENTE_ID primary key (CodiceFiscale));

create table SPONSOR (
     Nome char(1) not null,
     Quota char(1) not null,
     DescContratto char(1) not null,
     constraint ID_SPONSOR_ID primary key (Nome));

create table SPONSOR_TORNEO (
     Nome char(1) not null,
     Contributo char(1) not null,
     CodTorneo char(1) not null,
     constraint ID_SPONSOR_TORNEO_ID primary key (Nome));

create table SQUADRA (
     Nome char(1) not null,
     AnnoFondazione char(1) not null,
     CittaRiferimento char(1) not null,
     TrofeiVinti char(1) not null,
     Quota_Iscrizione char(1) not null,
     Punteggio char(1) not null,
     PosClassifica char(1) not null,
     constraint ID_SQUADRA_ID primary key (Nome));

create table STADIO (
     CodiceStadio char(1) not null,
     Nome char(1) not null,
     Citta char(1) not null,
     Capienza char(1) not null,
     Affitto char(1) not null,
     constraint ID_STADIO_ID primary key (CodiceStadio));

create table STAFF (
     CodiceFiscale char(1) not null,
     Nome char(1) not null,
     Cognome char(1) not null,
     DataNascita char(1) not null,
     Nazionalita char(1) not null,
     Ruolo char(1) not null,
     Stipendio char(1) not null,
     CodiceAll char(1) not null,
     constraint ID_STAFF_ID primary key (CodiceFiscale));

create table STAFF_PARTITA (
     CodiceFiscale char(1) not null,
     Nome char(1) not null,
     Cognome char(1) not null,
     DataNascita char(1) not null,
     Nazionalita char(1) not null,
     Ruolo char(1) not null,
     Stipendio char(1) not null,
     constraint ID_STAFF_PARTITA_ID primary key (CodiceFiscale));

create table SUPERVISIONE (
     CodiceStaff char(1) not null,
     CodicePartita char(1) not null,
     constraint ID_SUPERVISIONE_ID primary key (CodicePartita, CodiceStaff));

create table TABELLINO_STATISTICHE (
     CodiceTabellino char(1) not null,
     Data char(1) not null,
     GoalOspite char(1) not null,
     GoalCasa char(1) not null,
     Pali char(1) not null,
     Cartellini char(1) not null,
     CodiceStaff char(1) not null,
     constraint ID_TABELLINO_STATISTICHE_ID primary key (CodiceTabellino));

create table TELEVISIONE (
     Nome char(1) not null,
     Contributo char(1) not null,
     constraint ID_TELEVISIONE_ID primary key (Nome));

create table TRAMITE (
     CodiceDir char(1) not null,
     CodiceGiocatore char(1) not null,
     Durata char(1) not null,
     constraint ID_TRAMI_DIRET_ID primary key (CodiceDir));

create table TRASMISSIONE (
     NomeTV char(1) not null,
     CodTorneo char(1) not null,
     constraint ID_TRASMISSIONE_ID primary key (CodTorneo, NomeTV));


-- Constraints Section
-- ___________________ 

alter table ALLENATORE add constraint SID_ALLEN_DIRET_FK
     foreign key (Sce_CodiceFiscale)
     references DIRETTORE_SPORTIVO (CodiceFiscale);

alter table ALLENATORE add constraint SID_ALLEN_SQUAD_FK
     foreign key (All_Nome)
     references SQUADRA (Nome);

alter table CONTRIBUZIONE add constraint REF_CONTR_SPONS_FK
     foreign key (NomeSponsor)
     references SPONSOR (Nome);

alter table CONTRIBUZIONE add constraint REF_CONTR_FONDI
     foreign key (IBAN)
     references FONDI (IBAN);

alter table DATA add constraint REF_DATA_INFO__FK
     foreign key (CodTorneo)
     references INFO_TORNEO (CodTorneo);

-- Not implemented
-- alter table DIRETTORE_SPORTIVO add constraint ID_DIRETTORE_SPORTIVO_CHK
--     check(exists(select * from ALLENATORE
--                  where ALLENATORE.Sce_CodiceFiscale = CodiceFiscale)); 

-- Not implemented
-- alter table DIRETTORE_SPORTIVO add constraint ID_DIRETTORE_SPORTIVO_CHK
--     check(exists(select * from TRAMITE
--                  where TRAMITE.CodiceDir = CodiceFiscale)); 

alter table FONDI add constraint REF_FONDI_PRESI_FK
     foreign key (CodicePresidente)
     references PRESIDENTE (CodiceFiscale);

alter table FONDI add constraint REF_FONDI_DIRET_FK
     foreign key (CodiceDir)
     references DIRETTORE_SPORTIVO (CodiceFiscale);

-- Not implemented
-- alter table GIOCATORE add constraint ID_GIOCATORE_CHK
--     check(exists(select * from NUMERO
--                  where NUMERO.CodiceFiscale = CodiceFiscale)); 

alter table GIOCATORE add constraint REF_GIOCA_SQUAD_FK
     foreign key (NomeSquadra)
     references SQUADRA (Nome);

alter table Infortuni add constraint REF_Infor_TABEL
     foreign key (CodiceTabellino)
     references TABELLINO_STATISTICHE (CodiceTabellino);

alter table Marcatori add constraint REF_Marca_TABEL
     foreign key (CodiceTabellino)
     references TABELLINO_STATISTICHE (CodiceTabellino);

alter table MERCATO_GIOCATORI add constraint REF_MERCA_GIOCA
     foreign key (CodiceGiocatore)
     references GIOCATORE (CodiceFiscale);

alter table NUMERO add constraint REF_NUMER_SQUAD
     foreign key (NomeSquadra)
     references SQUADRA (Nome);

alter table NUMERO add constraint SID_NUMER_GIOCA_FK
     foreign key (CodiceFiscale)
     references GIOCATORE (CodiceFiscale);

alter table PARTITA add constraint REF_PARTI_SQUAD_1_FK
     foreign key (NomeOspite)
     references SQUADRA (Nome);

alter table PARTITA add constraint REF_PARTI_SQUAD_FK
     foreign key (NomeCasa)
     references SQUADRA (Nome);

alter table PARTITA add constraint REF_PARTI_STADI_FK
     foreign key (CodiceStadio)
     references STADIO (CodiceStadio);

alter table PARTITA add constraint REF_PARTI_DATA_FK
     foreign key (Giorno, Mese, Anno)
     references DATA (Giorno, Mese, Anno);

alter table PARTITA add constraint SID_PARTI_TABEL_FK
     foreign key (CodiceTabellino)
     references TABELLINO_STATISTICHE (CodiceTabellino);

alter table SPONSOR_TORNEO add constraint REF_SPONS_INFO__FK
     foreign key (CodTorneo)
     references INFO_TORNEO (CodTorneo);

-- Not implemented
-- alter table SQUADRA add constraint ID_SQUADRA_CHK
--     check(exists(select * from ALLENATORE
--                  where ALLENATORE.All_Nome = Nome)); 

alter table STAFF add constraint REF_STAFF_ALLEN_FK
     foreign key (CodiceAll)
     references ALLENATORE (CodiceFiscale);

alter table SUPERVISIONE add constraint REF_SUPER_PARTI
     foreign key (CodicePartita)
     references PARTITA (CodicePartita);

alter table SUPERVISIONE add constraint REF_SUPER_STAFF_FK
     foreign key (CodiceStaff)
     references STAFF_PARTITA (CodiceFiscale);

-- Not implemented
-- alter table TABELLINO_STATISTICHE add constraint ID_TABELLINO_STATISTICHE_CHK
--     check(exists(select * from PARTITA
--                  where PARTITA.CodiceTabellino = CodiceTabellino)); 

alter table TABELLINO_STATISTICHE add constraint REF_TABEL_STAFF_FK
     foreign key (CodiceStaff)
     references STAFF_PARTITA (CodiceFiscale);

alter table TRAMITE add constraint ID_TRAMI_DIRET_FK
     foreign key (CodiceDir)
     references DIRETTORE_SPORTIVO (CodiceFiscale);

alter table TRAMITE add constraint REF_TRAMI_MERCA_FK
     foreign key (CodiceGiocatore, Durata)
     references MERCATO_GIOCATORI (CodiceGiocatore, Durata);

alter table TRASMISSIONE add constraint REF_TRASM_INFO_
     foreign key (CodTorneo)
     references INFO_TORNEO (CodTorneo);

alter table TRASMISSIONE add constraint REF_TRASM_TELEV_FK
     foreign key (NomeTV)
     references TELEVISIONE (Nome);


-- Index Section
-- _____________ 

create unique index ID_ALLENATORE_IND
     on ALLENATORE (CodiceFiscale);

create unique index SID_ALLEN_DIRET_IND
     on ALLENATORE (Sce_CodiceFiscale);

create unique index SID_ALLEN_SQUAD_IND
     on ALLENATORE (All_Nome);

create unique index ID_CONTRIBUZIONE_IND
     on CONTRIBUZIONE (IBAN, NomeSponsor);

create index REF_CONTR_SPONS_IND
     on CONTRIBUZIONE (NomeSponsor);

create unique index ID_DATA_IND
     on DATA (Giorno, Mese, Anno);

create index REF_DATA_INFO__IND
     on DATA (CodTorneo);

create unique index ID_DIRETTORE_SPORTIVO_IND
     on DIRETTORE_SPORTIVO (CodiceFiscale);

create unique index ID_FONDI_IND
     on FONDI (IBAN);

create index REF_FONDI_PRESI_IND
     on FONDI (CodicePresidente);

create index REF_FONDI_DIRET_IND
     on FONDI (CodiceDir);

create unique index ID_GIOCATORE_IND
     on GIOCATORE (CodiceFiscale);

create index REF_GIOCA_SQUAD_IND
     on GIOCATORE (NomeSquadra);

create unique index ID_INFO_TORNEO_IND
     on INFO_TORNEO (CodTorneo);

create unique index ID_Infortuni_IND
     on Infortuni (CodiceTabellino, Infortuni);

create unique index ID_Marcatori_IND
     on Marcatori (CodiceTabellino, Marcatori);

create unique index ID_MERCATO_GIOCATORI_IND
     on MERCATO_GIOCATORI (CodiceGiocatore, Durata);

create unique index ID_NUMERO_IND
     on NUMERO (NomeSquadra, Numero);

create unique index SID_NUMER_GIOCA_IND
     on NUMERO (CodiceFiscale);

create unique index ID_PARTITA_IND
     on PARTITA (CodicePartita);

create index REF_PARTI_SQUAD_1_IND
     on PARTITA (NomeOspite);

create index REF_PARTI_SQUAD_IND
     on PARTITA (NomeCasa);

create index REF_PARTI_STADI_IND
     on PARTITA (CodiceStadio);

create index REF_PARTI_DATA_IND
     on PARTITA (Giorno, Mese, Anno);

create unique index SID_PARTI_TABEL_IND
     on PARTITA (CodiceTabellino);

create unique index ID_PRESIDENTE_IND
     on PRESIDENTE (CodiceFiscale);

create unique index ID_SPONSOR_IND
     on SPONSOR (Nome);

create unique index ID_SPONSOR_TORNEO_IND
     on SPONSOR_TORNEO (Nome);

create index REF_SPONS_INFO__IND
     on SPONSOR_TORNEO (CodTorneo);

create unique index ID_SQUADRA_IND
     on SQUADRA (Nome);

create unique index ID_STADIO_IND
     on STADIO (CodiceStadio);

create unique index ID_STAFF_IND
     on STAFF (CodiceFiscale);

create index REF_STAFF_ALLEN_IND
     on STAFF (CodiceAll);

create unique index ID_STAFF_PARTITA_IND
     on STAFF_PARTITA (CodiceFiscale);

create unique index ID_SUPERVISIONE_IND
     on SUPERVISIONE (CodicePartita, CodiceStaff);

create index REF_SUPER_STAFF_IND
     on SUPERVISIONE (CodiceStaff);

create unique index ID_TABELLINO_STATISTICHE_IND
     on TABELLINO_STATISTICHE (CodiceTabellino);

create index REF_TABEL_STAFF_IND
     on TABELLINO_STATISTICHE (CodiceStaff);

create unique index ID_TELEVISIONE_IND
     on TELEVISIONE (Nome);

create unique index ID_TRAMI_DIRET_IND
     on TRAMITE (CodiceDir);

create index REF_TRAMI_MERCA_IND
     on TRAMITE (CodiceGiocatore, Durata);

create unique index ID_TRASMISSIONE_IND
     on TRASMISSIONE (CodTorneo, NomeTV);

create index REF_TRASM_TELEV_IND
     on TRASMISSIONE (NomeTV);

