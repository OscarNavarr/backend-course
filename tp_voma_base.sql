--
-- PostgreSQL database dump
--

-- Dumped from database version 17.4
-- Dumped by pg_dump version 17.4

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: consultations; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.consultations (
    id integer NOT NULL,
    utilisateur_id integer,
    date_consultation timestamp with time zone,
    semaine date
);


ALTER TABLE public.consultations OWNER TO postgres;

--
-- Name: consultations_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.consultations_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.consultations_id_seq OWNER TO postgres;

--
-- Name: consultations_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.consultations_id_seq OWNED BY public.consultations.id;


--
-- Name: cours; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.cours (
    enseignant_id character varying,
    promotion_id integer,
    salle_id integer,
    debut timestamp with time zone,
    type_cours character varying,
    annule boolean,
    duree integer,
    id integer NOT NULL,
    titre character varying(255),
    fin time with time zone
);


ALTER TABLE public.cours OWNER TO postgres;

--
-- Name: cours_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.cours_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.cours_id_seq OWNER TO postgres;

--
-- Name: cours_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.cours_id_seq OWNED BY public.cours.id;


--
-- Name: enseignants; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.enseignants (
    nom character varying,
    email character varying,
    telephone character varying,
    id integer NOT NULL
);


ALTER TABLE public.enseignants OWNER TO postgres;

--
-- Name: enseignants_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.enseignants_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.enseignants_id_seq OWNER TO postgres;

--
-- Name: enseignants_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.enseignants_id_seq OWNED BY public.enseignants.id;


--
-- Name: promotions; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.promotions (
    nom character varying,
    annee integer,
    id integer NOT NULL
);


ALTER TABLE public.promotions OWNER TO postgres;

--
-- Name: promotions_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.promotions_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.promotions_id_seq OWNER TO postgres;

--
-- Name: promotions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.promotions_id_seq OWNED BY public.promotions.id;


--
-- Name: salles; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.salles (
    id integer NOT NULL,
    capacite integer,
    nom character varying(255)
);


ALTER TABLE public.salles OWNER TO postgres;

--
-- Name: salles_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.salles_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.salles_id_seq OWNER TO postgres;

--
-- Name: salles_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.salles_id_seq OWNED BY public.salles.id;


--
-- Name: utilisateurs; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.utilisateurs (
    id integer,
    nom character varying,
    email character varying,
    mot_de_passe character varying,
    admin boolean
);


ALTER TABLE public.utilisateurs OWNER TO postgres;

--
-- Name: consultations id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.consultations ALTER COLUMN id SET DEFAULT nextval('public.consultations_id_seq'::regclass);


--
-- Name: cours id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.cours ALTER COLUMN id SET DEFAULT nextval('public.cours_id_seq'::regclass);


--
-- Name: enseignants id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.enseignants ALTER COLUMN id SET DEFAULT nextval('public.enseignants_id_seq'::regclass);


--
-- Name: promotions id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.promotions ALTER COLUMN id SET DEFAULT nextval('public.promotions_id_seq'::regclass);


--
-- Name: salles id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.salles ALTER COLUMN id SET DEFAULT nextval('public.salles_id_seq'::regclass);


--
-- Data for Name: consultations; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.consultations (id, utilisateur_id, date_consultation, semaine) FROM stdin;
1	1	\N	2025-09-01
2	2	\N	2025-09-01
3	3	\N	2025-09-02
\.


--
-- Data for Name: cours; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.cours (enseignant_id, promotion_id, salle_id, debut, type_cours, annule, duree, id, titre, fin) FROM stdin;
1	1	1	2025-09-01 08:15:00+02	dirigé	f	120	1	Algorithmique	10:15:00+02
2	1	2	2025-09-01 10:30:00+02	dirigé	f	120	2	Programmation	12:30:00+02
3	2	3	2025-09-02 08:15:00+02	autonomie	f	120	3	Marketing Digital	10:15:00+02
4	3	4	2025-09-02 14:00:00+02	dirigé	f	120	4	Big Data	16:00:00+02
5	4	5	2025-09-03 08:15:00+02	autonomie	f	120	5	Gestion de Projet	10:15:00+02
\.


--
-- Data for Name: enseignants; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.enseignants (nom, email, telephone, id) FROM stdin;
M. Dupont	dupont@example.com	0102030405	1
Mme Martin	martin@example.com	0102030607	2
M. Bernard	bernard@example.com	0102030809	3
Mme Lefevre	lefevre@example.com	0102031011	4
M. Robert	robert@example.com	0102031213	5
\.


--
-- Data for Name: promotions; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.promotions (nom, annee, id) FROM stdin;
BTS Informatique	2025	1
BTS Commerce	2025	2
Master Data Science	2025	3
Master Marketing	2025	4
\.


--
-- Data for Name: salles; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.salles (id, capacite, nom) FROM stdin;
1	35	A1
2	50	Open Space
3	35	A2
\.


--
-- Data for Name: utilisateurs; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.utilisateurs (id, nom, email, mot_de_passe, admin) FROM stdin;
\N	Alice Dupont	alice.dupont@example.com	motdepassecrypté1	f
\N	Bob Martin	bob.martin@example.com	motdepassecrypté2	f
\N	Charlie Bernard	charlie.bernard@example.com	motdepassecrypté3	t
\N	Alice Dupont	alice.dupont@example.com	motdepassecrypté1	f
\N	Bob Martin	bob.martin@example.com	motdepassecrypté2	f
\N	Charlie Bernard	charlie.bernard@example.com	motdepassecrypté3	t
\.


--
-- Name: consultations_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.consultations_id_seq', 3, true);


--
-- Name: cours_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.cours_id_seq', 5, true);


--
-- Name: enseignants_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.enseignants_id_seq', 5, true);


--
-- Name: promotions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.promotions_id_seq', 4, true);


--
-- Name: salles_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.salles_id_seq', 1, true);


--
-- Name: salles salles_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.salles
    ADD CONSTRAINT salles_pkey PRIMARY KEY (id);


--
-- PostgreSQL database dump complete
--

