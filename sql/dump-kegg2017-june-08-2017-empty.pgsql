--
-- PostgreSQL database dump
--

SET statement_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;

--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET search_path = public, pg_catalog;

--
-- Name: accessions_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE accessions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.accessions_id_seq OWNER TO postgres;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: accessions; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE accessions (
    id integer DEFAULT nextval('accessions_id_seq'::regclass) NOT NULL,
    accession character varying(200) DEFAULT NULL::character varying,
    created_at timestamp with time zone,
    updated_at timestamp without time zone DEFAULT now() NOT NULL
);


ALTER TABLE public.accessions OWNER TO postgres;

--
-- Name: clustering_methods_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE clustering_methods_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.clustering_methods_id_seq OWNER TO postgres;

--
-- Name: clusters_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE clusters_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.clusters_id_seq OWNER TO postgres;

--
-- Name: domains_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE domains_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.domains_id_seq OWNER TO postgres;

--
-- Name: ec_intragenomic_analogy_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE ec_intragenomic_analogy_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.ec_intragenomic_analogy_id_seq OWNER TO postgres;

--
-- Name: ec_maps_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE ec_maps_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.ec_maps_id_seq OWNER TO postgres;

--
-- Name: ec_maps; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE ec_maps (
    id integer DEFAULT nextval('ec_maps_id_seq'::regclass) NOT NULL,
    ec_id integer,
    map_id integer,
    created_at timestamp with time zone,
    updated_at timestamp without time zone DEFAULT now() NOT NULL
);


ALTER TABLE public.ec_maps OWNER TO postgres;

--
-- Name: ec_reaction_classes_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE ec_reaction_classes_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.ec_reaction_classes_id_seq OWNER TO postgres;

--
-- Name: ec_reaction_classes; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE ec_reaction_classes (
    id integer DEFAULT nextval('ec_reaction_classes_id_seq'::regclass) NOT NULL,
    reaction character varying(200),
    reaction_prefix integer
);


ALTER TABLE public.ec_reaction_classes OWNER TO postgres;

--
-- Name: ec_rectangles_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE ec_rectangles_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.ec_rectangles_id_seq OWNER TO postgres;

--
-- Name: ecs_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE ecs_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.ecs_id_seq OWNER TO postgres;

--
-- Name: ecs; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE ecs (
    id integer DEFAULT nextval('ecs_id_seq'::regclass) NOT NULL,
    ec character varying(100) DEFAULT NULL::character varying(100),
    created_at timestamp with time zone,
    updated_at timestamp without time zone DEFAULT now() NOT NULL,
    ec_reaction_class_id integer
);


ALTER TABLE public.ecs OWNER TO postgres;

--
-- Name: genome_comparison_clusters_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE genome_comparison_clusters_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.genome_comparison_clusters_id_seq OWNER TO postgres;

--
-- Name: genome_comparisons_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE genome_comparisons_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.genome_comparisons_id_seq OWNER TO postgres;

--
-- Name: kingdoms_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE kingdoms_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.kingdoms_id_seq OWNER TO postgres;

--
-- Name: map_arrow_coordinates_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE map_arrow_coordinates_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.map_arrow_coordinates_id_seq OWNER TO postgres;

--
-- Name: map_arrows_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE map_arrows_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.map_arrows_id_seq OWNER TO postgres;

--
-- Name: map_line_coordinates_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE map_line_coordinates_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.map_line_coordinates_id_seq OWNER TO postgres;

--
-- Name: map_lines_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE map_lines_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.map_lines_id_seq OWNER TO postgres;

--
-- Name: map_polygon_coordinates_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE map_polygon_coordinates_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.map_polygon_coordinates_id_seq OWNER TO postgres;

--
-- Name: map_polygons_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE map_polygons_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.map_polygons_id_seq OWNER TO postgres;

--
-- Name: map_rectangle_coordinates_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE map_rectangle_coordinates_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.map_rectangle_coordinates_id_seq OWNER TO postgres;

--
-- Name: map_rectangles_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE map_rectangles_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.map_rectangles_id_seq OWNER TO postgres;

--
-- Name: metabolic_pathways_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE metabolic_pathways_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.metabolic_pathways_id_seq OWNER TO postgres;

--
-- Name: metabolic_pathways_maps_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE metabolic_pathways_maps_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.metabolic_pathways_maps_id_seq OWNER TO postgres;

--
-- Name: organism_ecs_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE organism_ecs_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.organism_ecs_id_seq OWNER TO postgres;

--
-- Name: organism_ecs; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE organism_ecs (
    id integer DEFAULT nextval('organism_ecs_id_seq'::regclass) NOT NULL,
    organism_id integer,
    ec_id integer
);


ALTER TABLE public.organism_ecs OWNER TO postgres;

--
-- Name: organism_maps_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE organism_maps_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.organism_maps_id_seq OWNER TO postgres;

--
-- Name: organism_maps; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE organism_maps (
    id integer DEFAULT nextval('organism_maps_id_seq'::regclass) NOT NULL,
    organism_id integer,
    map_id integer,
    created_at timestamp with time zone,
    updated_at timestamp without time zone DEFAULT now() NOT NULL
);


ALTER TABLE public.organism_maps OWNER TO postgres;

--
-- Name: organism_rectangle_coordinates_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE organism_rectangle_coordinates_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.organism_rectangle_coordinates_id_seq OWNER TO postgres;

--
-- Name: organism_taxonomies_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE organism_taxonomies_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.organism_taxonomies_id_seq OWNER TO postgres;

--
-- Name: organism_taxonomies; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE organism_taxonomies (
    id integer DEFAULT nextval('organism_taxonomies_id_seq'::regclass) NOT NULL,
    organism_id integer,
    taxonomy_id integer,
    created_at timestamp with time zone,
    updated_at timestamp without time zone DEFAULT now() NOT NULL
);


ALTER TABLE public.organism_taxonomies OWNER TO postgres;

--
-- Name: organisms_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE organisms_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.organisms_id_seq OWNER TO postgres;

--
-- Name: organisms; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE organisms (
    id integer DEFAULT nextval('organisms_id_seq'::regclass) NOT NULL,
    code character varying(200) DEFAULT NULL::character varying(200),
    name character varying(200) DEFAULT NULL::character varying(200),
    created_at timestamp with time zone,
    updated_at timestamp without time zone DEFAULT now() NOT NULL,
    taxonomy_id integer,
    internal_id character varying(40)
)
WITH (autovacuum_vacuum_scale_factor='0.0', autovacuum_vacuum_threshold='5000', autovacuum_analyze_scale_factor='0.0', autovacuum_analyze_threshold='5000');


ALTER TABLE public.organisms OWNER TO postgres;

--
-- Name: pathway_subsystems_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE pathway_subsystems_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.pathway_subsystems_id_seq OWNER TO postgres;

--
-- Name: pathway_classes; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE pathway_classes (
    id integer DEFAULT nextval('pathway_subsystems_id_seq'::regclass) NOT NULL,
    super_class_id integer,
    created_at timestamp with time zone,
    updated_at timestamp without time zone DEFAULT now() NOT NULL,
    name character varying(200)
);


ALTER TABLE public.pathway_classes OWNER TO postgres;

--
-- Name: pathway_maps; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE pathway_maps (
    id integer DEFAULT nextval('metabolic_pathways_maps_id_seq'::regclass) NOT NULL,
    identification character varying(100) DEFAULT NULL::character varying(100),
    class_id integer,
    created_at timestamp with time zone,
    updated_at timestamp without time zone DEFAULT now() NOT NULL,
    name character varying(255)
);


ALTER TABLE public.pathway_maps OWNER TO postgres;

--
-- Name: pathway_systems_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE pathway_systems_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.pathway_systems_id_seq OWNER TO postgres;

--
-- Name: pathway_super_classes; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE pathway_super_classes (
    id integer DEFAULT nextval('pathway_systems_id_seq'::regclass) NOT NULL,
    created_at timestamp with time zone,
    updated_at timestamp without time zone DEFAULT now() NOT NULL,
    name character varying(200)
);


ALTER TABLE public.pathway_super_classes OWNER TO postgres;

--
-- Name: protein_accessions_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE protein_accessions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.protein_accessions_id_seq OWNER TO postgres;

--
-- Name: protein_accessions; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE protein_accessions (
    id integer DEFAULT nextval('protein_accessions_id_seq'::regclass) NOT NULL,
    protein_id integer,
    accession_id integer,
    created_at timestamp with time zone,
    updated_at timestamp without time zone DEFAULT now() NOT NULL
);


ALTER TABLE public.protein_accessions OWNER TO postgres;

--
-- Name: protein_ecs_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE protein_ecs_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.protein_ecs_id_seq OWNER TO postgres;

--
-- Name: protein_ecs; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE protein_ecs (
    id integer DEFAULT nextval('protein_ecs_id_seq'::regclass) NOT NULL,
    protein_id integer,
    ec_id integer,
    created_at timestamp with time zone,
    updated_at timestamp without time zone DEFAULT now() NOT NULL
);


ALTER TABLE public.protein_ecs OWNER TO postgres;

--
-- Name: protein_maps_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE protein_maps_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.protein_maps_id_seq OWNER TO postgres;

--
-- Name: protein_maps; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE protein_maps (
    id integer DEFAULT nextval('protein_maps_id_seq'::regclass) NOT NULL,
    protein_id integer,
    map_id integer,
    created_at timestamp with time zone,
    updated_at timestamp without time zone DEFAULT now() NOT NULL
);


ALTER TABLE public.protein_maps OWNER TO postgres;

--
-- Name: protein_pdb_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE protein_pdb_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.protein_pdb_id_seq OWNER TO postgres;

--
-- Name: protein_pdbs; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE protein_pdbs (
    id integer DEFAULT nextval('protein_pdb_id_seq'::regclass) NOT NULL,
    protein_id integer,
    pdb_id character varying(255) DEFAULT NULL::character varying
);


ALTER TABLE public.protein_pdbs OWNER TO postgres;

--
-- Name: proteins_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE proteins_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.proteins_id_seq OWNER TO postgres;

--
-- Name: proteins; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE proteins (
    id integer DEFAULT nextval('proteins_id_seq'::regclass) NOT NULL,
    sequence text,
    identification character varying(255) DEFAULT NULL::character varying(255),
    organism_id integer,
    created_at timestamp with time zone,
    updated_at timestamp without time zone DEFAULT now() NOT NULL,
    description character varying(3000) DEFAULT NULL::character varying(3000),
    full_fasta_header text
);


ALTER TABLE public.proteins OWNER TO postgres;

--
-- Name: similarities_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE similarities_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.similarities_id_seq OWNER TO postgres;

--
-- Name: similarity_methods_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE similarity_methods_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.similarity_methods_id_seq OWNER TO postgres;

--
-- Name: source_databases_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE source_databases_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.source_databases_id_seq OWNER TO postgres;

--
-- Name: source_databases; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE source_databases (
    id integer DEFAULT nextval('source_databases_id_seq'::regclass) NOT NULL,
    name character varying(200) DEFAULT NULL::character varying(200),
    date timestamp with time zone,
    site character varying(255) DEFAULT NULL::character varying(200),
    version character varying(20) DEFAULT NULL::character varying(200),
    size bigint,
    "installedDirectory" character varying(200) DEFAULT NULL::character varying(200),
    created_at timestamp with time zone,
    updated_at timestamp without time zone DEFAULT now() NOT NULL
);


ALTER TABLE public.source_databases OWNER TO postgres;

--
-- Name: taxonomic_groups_level3_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE taxonomic_groups_level3_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.taxonomic_groups_level3_id_seq OWNER TO postgres;

--
-- Name: taxonomic_groups_level4_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE taxonomic_groups_level4_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.taxonomic_groups_level4_id_seq OWNER TO postgres;

--
-- Name: taxonomies_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE taxonomies_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.taxonomies_id_seq OWNER TO postgres;

--
-- Name: taxonomies; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE taxonomies (
    id integer DEFAULT nextval('taxonomies_id_seq'::regclass) NOT NULL,
    taxonomy character varying(200) DEFAULT NULL::character varying,
    created_at timestamp with time zone,
    updated_at timestamp without time zone DEFAULT now() NOT NULL,
    tax_id integer,
    tax_type character varying(100)
);


ALTER TABLE public.taxonomies OWNER TO postgres;

--
-- Data for Name: accessions; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY accessions (id, accession, created_at, updated_at) FROM stdin;
\.


--
-- Name: accessions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('accessions_id_seq', 1, false);


--
-- Name: clustering_methods_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('clustering_methods_id_seq', 1, false);


--
-- Name: clusters_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('clusters_id_seq', 1, false);


--
-- Name: domains_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('domains_id_seq', 1, false);


--
-- Name: ec_intragenomic_analogy_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('ec_intragenomic_analogy_id_seq', 1, false);


--
-- Data for Name: ec_maps; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY ec_maps (id, ec_id, map_id, created_at, updated_at) FROM stdin;
\.


--
-- Name: ec_maps_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('ec_maps_id_seq', 1, false);


--
-- Data for Name: ec_reaction_classes; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY ec_reaction_classes (id, reaction, reaction_prefix) FROM stdin;
\.


--
-- Name: ec_reaction_classes_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('ec_reaction_classes_id_seq', 1, false);


--
-- Name: ec_rectangles_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('ec_rectangles_id_seq', 1, false);


--
-- Data for Name: ecs; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY ecs (id, ec, created_at, updated_at, ec_reaction_class_id) FROM stdin;
\.


--
-- Name: ecs_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('ecs_id_seq', 1, false);


--
-- Name: genome_comparison_clusters_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('genome_comparison_clusters_id_seq', 1, false);


--
-- Name: genome_comparisons_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('genome_comparisons_id_seq', 1, false);


--
-- Name: kingdoms_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('kingdoms_id_seq', 1, false);


--
-- Name: map_arrow_coordinates_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('map_arrow_coordinates_id_seq', 1, false);


--
-- Name: map_arrows_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('map_arrows_id_seq', 1, false);


--
-- Name: map_line_coordinates_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('map_line_coordinates_id_seq', 1, false);


--
-- Name: map_lines_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('map_lines_id_seq', 1, false);


--
-- Name: map_polygon_coordinates_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('map_polygon_coordinates_id_seq', 1, false);


--
-- Name: map_polygons_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('map_polygons_id_seq', 1, false);


--
-- Name: map_rectangle_coordinates_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('map_rectangle_coordinates_id_seq', 1, false);


--
-- Name: map_rectangles_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('map_rectangles_id_seq', 1, false);


--
-- Name: metabolic_pathways_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('metabolic_pathways_id_seq', 1, false);


--
-- Name: metabolic_pathways_maps_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('metabolic_pathways_maps_id_seq', 1, false);


--
-- Data for Name: organism_ecs; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY organism_ecs (id, organism_id, ec_id) FROM stdin;
\.


--
-- Name: organism_ecs_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('organism_ecs_id_seq', 1, false);


--
-- Data for Name: organism_maps; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY organism_maps (id, organism_id, map_id, created_at, updated_at) FROM stdin;
\.


--
-- Name: organism_maps_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('organism_maps_id_seq', 1, false);


--
-- Name: organism_rectangle_coordinates_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('organism_rectangle_coordinates_id_seq', 1, false);


--
-- Data for Name: organism_taxonomies; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY organism_taxonomies (id, organism_id, taxonomy_id, created_at, updated_at) FROM stdin;
\.


--
-- Name: organism_taxonomies_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('organism_taxonomies_id_seq', 1, false);


--
-- Data for Name: organisms; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY organisms (id, code, name, created_at, updated_at, taxonomy_id, internal_id) FROM stdin;
\.


--
-- Name: organisms_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('organisms_id_seq', 1, false);


--
-- Data for Name: pathway_classes; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY pathway_classes (id, super_class_id, created_at, updated_at, name) FROM stdin;
\.


--
-- Data for Name: pathway_maps; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY pathway_maps (id, identification, class_id, created_at, updated_at, name) FROM stdin;
\.


--
-- Name: pathway_subsystems_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('pathway_subsystems_id_seq', 1, false);


--
-- Data for Name: pathway_super_classes; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY pathway_super_classes (id, created_at, updated_at, name) FROM stdin;
\.


--
-- Name: pathway_systems_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('pathway_systems_id_seq', 1, false);


--
-- Data for Name: protein_accessions; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY protein_accessions (id, protein_id, accession_id, created_at, updated_at) FROM stdin;
\.


--
-- Name: protein_accessions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('protein_accessions_id_seq', 1, false);


--
-- Data for Name: protein_ecs; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY protein_ecs (id, protein_id, ec_id, created_at, updated_at) FROM stdin;
\.


--
-- Name: protein_ecs_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('protein_ecs_id_seq', 1, false);


--
-- Data for Name: protein_maps; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY protein_maps (id, protein_id, map_id, created_at, updated_at) FROM stdin;
\.


--
-- Name: protein_maps_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('protein_maps_id_seq', 1, false);


--
-- Name: protein_pdb_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('protein_pdb_id_seq', 1, false);


--
-- Data for Name: protein_pdbs; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY protein_pdbs (id, protein_id, pdb_id) FROM stdin;
\.


--
-- Data for Name: proteins; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY proteins (id, sequence, identification, organism_id, created_at, updated_at, description, full_fasta_header) FROM stdin;
\.


--
-- Name: proteins_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('proteins_id_seq', 1, false);


--
-- Name: similarities_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('similarities_id_seq', 1, false);


--
-- Name: similarity_methods_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('similarity_methods_id_seq', 1, false);


--
-- Data for Name: source_databases; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY source_databases (id, name, date, site, version, size, "installedDirectory", created_at, updated_at) FROM stdin;
\.


--
-- Name: source_databases_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('source_databases_id_seq', 1, false);


--
-- Name: taxonomic_groups_level3_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('taxonomic_groups_level3_id_seq', 1, false);


--
-- Name: taxonomic_groups_level4_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('taxonomic_groups_level4_id_seq', 1, false);


--
-- Data for Name: taxonomies; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY taxonomies (id, taxonomy, created_at, updated_at, tax_id, tax_type) FROM stdin;
\.


--
-- Name: taxonomies_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('taxonomies_id_seq', 1, false);


--
-- Name: ec_maps_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY ec_maps
    ADD CONSTRAINT ec_maps_pkey PRIMARY KEY (id);


--
-- Name: ecs_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY ecs
    ADD CONSTRAINT ecs_pkey PRIMARY KEY (id);


--
-- Name: metabolic_pathways_maps_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY pathway_maps
    ADD CONSTRAINT metabolic_pathways_maps_pkey PRIMARY KEY (id);


--
-- Name: organism_ecs_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY organism_ecs
    ADD CONSTRAINT organism_ecs_pkey PRIMARY KEY (id);


--
-- Name: organism_maps_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY organism_maps
    ADD CONSTRAINT organism_maps_pkey PRIMARY KEY (id);


--
-- Name: organisms_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY organisms
    ADD CONSTRAINT organisms_pkey PRIMARY KEY (id);


--
-- Name: pathway_subsystems_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY pathway_classes
    ADD CONSTRAINT pathway_subsystems_pkey PRIMARY KEY (id);


--
-- Name: pathway_systems_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY pathway_super_classes
    ADD CONSTRAINT pathway_systems_pkey PRIMARY KEY (id);


--
-- Name: pk_protein_pdbs; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY protein_pdbs
    ADD CONSTRAINT pk_protein_pdbs PRIMARY KEY (id);


--
-- Name: protein_ecs_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY protein_ecs
    ADD CONSTRAINT protein_ecs_pkey PRIMARY KEY (id);


--
-- Name: protein_maps_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY protein_maps
    ADD CONSTRAINT protein_maps_pkey PRIMARY KEY (id);


--
-- Name: proteins_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY proteins
    ADD CONSTRAINT proteins_pkey PRIMARY KEY (id);


--
-- Name: source_databases_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY source_databases
    ADD CONSTRAINT source_databases_pkey PRIMARY KEY (id);


--
-- Name: uniq_tax_id; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY taxonomies
    ADD CONSTRAINT uniq_tax_id UNIQUE (id);


--
-- Name: unique_id; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY accessions
    ADD CONSTRAINT unique_id UNIQUE (id);


--
-- Name: unique_id_ot; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY organism_taxonomies
    ADD CONSTRAINT unique_id_ot UNIQUE (id);


--
-- Name: unique_reaction_class_id; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY ec_reaction_classes
    ADD CONSTRAINT unique_reaction_class_id UNIQUE (id);


--
-- Name: protein_pdbs_id_idx; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX protein_pdbs_id_idx ON protein_pdbs USING btree (id);


--
-- Name: protein_pdbs_pdb_id_idx; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX protein_pdbs_pdb_id_idx ON protein_pdbs USING btree (pdb_id);


--
-- Name: protein_pdbs_protein_id_idx; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX protein_pdbs_protein_id_idx ON protein_pdbs USING btree (protein_id);


--
-- Name: fk_accession_protein; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY protein_accessions
    ADD CONSTRAINT fk_accession_protein FOREIGN KEY (accession_id) REFERENCES accessions(id);


--
-- Name: fk_ec; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY protein_ecs
    ADD CONSTRAINT fk_ec FOREIGN KEY (ec_id) REFERENCES ecs(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: fk_ec_map; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY ec_maps
    ADD CONSTRAINT fk_ec_map FOREIGN KEY (ec_id) REFERENCES ecs(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: fk_map_organism; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY organism_maps
    ADD CONSTRAINT fk_map_organism FOREIGN KEY (map_id) REFERENCES pathway_maps(id);


--
-- Name: fk_map_protein; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY protein_maps
    ADD CONSTRAINT fk_map_protein FOREIGN KEY (map_id) REFERENCES pathway_maps(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: fk_maps; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY ec_maps
    ADD CONSTRAINT fk_maps FOREIGN KEY (map_id) REFERENCES pathway_maps(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: fk_organism; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY proteins
    ADD CONSTRAINT fk_organism FOREIGN KEY (organism_id) REFERENCES organisms(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: fk_organism_ec_ec; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY organism_ecs
    ADD CONSTRAINT fk_organism_ec_ec FOREIGN KEY (ec_id) REFERENCES ecs(id);


--
-- Name: fk_organism_ec_organism; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY organism_ecs
    ADD CONSTRAINT fk_organism_ec_organism FOREIGN KEY (organism_id) REFERENCES organisms(id);


--
-- Name: fk_organism_map; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY organism_maps
    ADD CONSTRAINT fk_organism_map FOREIGN KEY (organism_id) REFERENCES organisms(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: fk_organism_taxonomy; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY organism_taxonomies
    ADD CONSTRAINT fk_organism_taxonomy FOREIGN KEY (organism_id) REFERENCES organisms(id);


--
-- Name: fk_pathway_class; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY pathway_maps
    ADD CONSTRAINT fk_pathway_class FOREIGN KEY (class_id) REFERENCES pathway_classes(id) MATCH FULL;


--
-- Name: fk_pathway_superclass; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY pathway_classes
    ADD CONSTRAINT fk_pathway_superclass FOREIGN KEY (super_class_id) REFERENCES pathway_super_classes(id);


--
-- Name: fk_protein; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY protein_ecs
    ADD CONSTRAINT fk_protein FOREIGN KEY (protein_id) REFERENCES proteins(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: fk_protein_accession; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY protein_accessions
    ADD CONSTRAINT fk_protein_accession FOREIGN KEY (protein_id) REFERENCES proteins(id);


--
-- Name: fk_protein_map; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY protein_maps
    ADD CONSTRAINT fk_protein_map FOREIGN KEY (protein_id) REFERENCES proteins(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: fk_protein_pdb; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY protein_pdbs
    ADD CONSTRAINT fk_protein_pdb FOREIGN KEY (protein_id) REFERENCES proteins(id);


--
-- Name: fk_reaction_class; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY ecs
    ADD CONSTRAINT fk_reaction_class FOREIGN KEY (ec_reaction_class_id) REFERENCES ec_reaction_classes(id);


--
-- Name: fk_taxonomy_organism; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY organism_taxonomies
    ADD CONSTRAINT fk_taxonomy_organism FOREIGN KEY (taxonomy_id) REFERENCES taxonomies(id);


--
-- Name: public; Type: ACL; Schema: -; Owner: postgres
--

REVOKE ALL ON SCHEMA public FROM PUBLIC;
REVOKE ALL ON SCHEMA public FROM postgres;
GRANT ALL ON SCHEMA public TO postgres;
GRANT ALL ON SCHEMA public TO anendb;


--
-- PostgreSQL database dump complete
--

