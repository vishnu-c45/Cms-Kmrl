-- MySQL dump 10.13  Distrib 8.0.31, for Linux (x86_64)
--
-- Host: 127.0.0.1    Database: kmr
-- ------------------------------------------------------
-- Server version	8.0.31-0ubuntu0.22.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add member',7,'add_member'),(26,'Can change member',7,'change_member'),(27,'Can delete member',7,'delete_member'),(28,'Can view member',7,'view_member'),(29,'Can add login_table',8,'add_login_table'),(30,'Can change login_table',8,'change_login_table'),(31,'Can delete login_table',8,'delete_login_table'),(32,'Can view login_table',8,'view_login_table'),(33,'Can add metrostaion',9,'add_metrostaion'),(34,'Can change metrostaion',9,'change_metrostaion'),(35,'Can delete metrostaion',9,'delete_metrostaion'),(36,'Can view metrostaion',9,'view_metrostaion'),(37,'Can add metro staion contact',10,'add_metrostaioncontact'),(38,'Can change metro staion contact',10,'change_metrostaioncontact'),(39,'Can delete metro staion contact',10,'delete_metrostaioncontact'),(40,'Can view metro staion contact',10,'view_metrostaioncontact'),(41,'Can add metrostation',9,'add_metrostation'),(42,'Can change metrostation',9,'change_metrostation'),(43,'Can delete metrostation',9,'delete_metrostation'),(44,'Can view metrostation',9,'view_metrostation'),(45,'Can add metro station contact',10,'add_metrostationcontact'),(46,'Can change metro station contact',10,'change_metrostationcontact'),(47,'Can delete metro station contact',10,'delete_metrostationcontact'),(48,'Can view metro station contact',10,'view_metrostationcontact'),(49,'Can add space',11,'add_space'),(50,'Can change space',11,'change_space'),(51,'Can delete space',11,'delete_space'),(52,'Can view space',11,'view_space'),(53,'Can add customer',12,'add_customer'),(54,'Can change customer',12,'change_customer'),(55,'Can delete customer',12,'delete_customer'),(56,'Can view customer',12,'view_customer'),(57,'Can add customer_contact',13,'add_customer_contact'),(58,'Can change customer_contact',13,'change_customer_contact'),(59,'Can delete customer_contact',13,'delete_customer_contact'),(60,'Can view customer_contact',13,'view_customer_contact'),(61,'Can add contract',14,'add_contract'),(62,'Can change contract',14,'change_contract'),(63,'Can delete contract',14,'delete_contract'),(64,'Can view contract',14,'view_contract'),(65,'Can add company_details',15,'add_company_details'),(66,'Can change company_details',15,'change_company_details'),(67,'Can delete company_details',15,'delete_company_details'),(68,'Can view company_details',15,'view_company_details'),(69,'Can add invoices',16,'add_invoices'),(70,'Can change invoices',16,'change_invoices'),(71,'Can delete invoices',16,'delete_invoices'),(72,'Can view invoices',16,'view_invoices'),(73,'Can add bank',17,'add_bank'),(74,'Can change bank',17,'change_bank'),(75,'Can delete bank',17,'delete_bank'),(76,'Can view bank',17,'view_bank'),(77,'Can add payments',18,'add_payments'),(78,'Can change payments',18,'change_payments'),(79,'Can delete payments',18,'delete_payments'),(80,'Can view payments',18,'view_payments'),(81,'Can add payments_ data',18,'add_payments_data'),(82,'Can change payments_ data',18,'change_payments_data'),(83,'Can delete payments_ data',18,'delete_payments_data'),(84,'Can view payments_ data',18,'view_payments_data'),(85,'Can add customer_grievance',19,'add_customer_grievance'),(86,'Can change customer_grievance',19,'change_customer_grievance'),(87,'Can delete customer_grievance',19,'delete_customer_grievance'),(88,'Can view customer_grievance',19,'view_customer_grievance'),(89,'Can add notification',20,'add_notification'),(90,'Can change notification',20,'change_notification'),(91,'Can delete notification',20,'delete_notification'),(92,'Can view notification',20,'view_notification'),(93,'Can add credit note',21,'add_creditnote'),(94,'Can change credit note',21,'change_creditnote'),(95,'Can delete credit note',21,'delete_creditnote'),(96,'Can view credit note',21,'view_creditnote'),(97,'Can add general_parameter',22,'add_general_parameter'),(98,'Can change general_parameter',22,'change_general_parameter'),(99,'Can delete general_parameter',22,'delete_general_parameter'),(100,'Can view general_parameter',22,'view_general_parameter');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$600000$maAB7VAnqjZgEZR0TFeuX8$vWrDosViRFGsu+SAZG4xTQhEDo4GDYOOut+LQxc0THs=','2023-04-11 11:31:25.702312',1,'vishnu','','','vishnu@gamil.com',1,1,'2023-04-11 11:30:16.083244');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(17,'firstapp','bank'),(15,'firstapp','company_details'),(14,'firstapp','contract'),(21,'firstapp','creditnote'),(12,'firstapp','customer'),(13,'firstapp','customer_contact'),(19,'firstapp','customer_grievance'),(22,'firstapp','general_parameter'),(16,'firstapp','invoices'),(8,'firstapp','login_table'),(7,'firstapp','member'),(9,'firstapp','metrostation'),(10,'firstapp','metrostationcontact'),(20,'firstapp','notification'),(18,'firstapp','payments_data'),(11,'firstapp','space'),(6,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2023-04-10 05:00:01.173711'),(2,'auth','0001_initial','2023-04-10 05:00:05.398625'),(3,'admin','0001_initial','2023-04-10 05:00:06.209550'),(4,'admin','0002_logentry_remove_auto_add','2023-04-10 05:00:06.260640'),(5,'admin','0003_logentry_add_action_flag_choices','2023-04-10 05:00:06.315558'),(6,'contenttypes','0002_remove_content_type_name','2023-04-10 05:00:06.696227'),(7,'auth','0002_alter_permission_name_max_length','2023-04-10 05:00:07.015187'),(8,'auth','0003_alter_user_email_max_length','2023-04-10 05:00:07.109327'),(9,'auth','0004_alter_user_username_opts','2023-04-10 05:00:07.143614'),(10,'auth','0005_alter_user_last_login_null','2023-04-10 05:00:07.410526'),(11,'auth','0006_require_contenttypes_0002','2023-04-10 05:00:07.431081'),(12,'auth','0007_alter_validators_add_error_messages','2023-04-10 05:00:07.466169'),(13,'auth','0008_alter_user_username_max_length','2023-04-10 05:00:07.823121'),(14,'auth','0009_alter_user_last_name_max_length','2023-04-10 05:00:08.186211'),(15,'auth','0010_alter_group_name_max_length','2023-04-10 05:00:08.296813'),(16,'auth','0011_update_proxy_permissions','2023-04-10 05:00:08.346514'),(17,'auth','0012_alter_user_first_name_max_length','2023-04-10 05:00:08.725208'),(18,'firstapp','0001_initial','2023-04-10 05:00:08.883419'),(19,'firstapp','0002_member_joined_date_member_phone','2023-04-10 05:00:09.118122'),(20,'firstapp','0003_alter_member_phone','2023-04-10 05:00:09.418937'),(21,'firstapp','0004_login','2023-04-10 05:00:09.606432'),(22,'firstapp','0005_login_table_delete_login','2023-04-10 05:00:09.847275'),(23,'firstapp','0006_alter_login_table_created_on','2023-04-10 05:00:10.095464'),(24,'sessions','0001_initial','2023-04-10 05:00:10.349614'),(25,'firstapp','0007_metrostaion','2023-04-12 05:25:41.953339'),(26,'firstapp','0008_metrostaioncontact','2023-04-12 05:48:40.242615'),(27,'firstapp','0009_rename_metrostaion_metrostation_and_more','2023-04-28 05:01:06.854609'),(28,'firstapp','0010_rename_metrostaioncontact_metrostationcontact','2023-04-28 05:02:57.317073'),(29,'firstapp','0011_alter_metrostation_created_on_and_more','2023-04-28 07:48:09.374607'),(30,'firstapp','0012_spaces','2023-05-05 10:44:40.766764'),(31,'firstapp','0013_rename_spaces_space','2023-05-05 10:44:40.990509'),(32,'firstapp','0014_space_master_space','2023-05-05 10:44:41.222825'),(33,'firstapp','0015_alter_space_master_space','2023-05-05 10:44:42.354255'),(34,'firstapp','0016_alter_space_area','2023-05-06 04:27:59.818932'),(35,'firstapp','0017_alter_space_metrostation','2023-05-08 04:05:28.820271'),(36,'firstapp','0016_space_vacancy_status','2023-05-08 04:50:21.831754'),(37,'firstapp','0018_merge_20230508_1020','2023-05-08 04:50:21.883682'),(38,'firstapp','0019_customer_alter_space_area_customer_contact_contract','2023-05-12 07:01:57.131828'),(39,'firstapp','0019_alter_space_area','2023-05-13 05:17:12.020231'),(40,'firstapp','0020_merge_20230513_1047','2023-05-13 05:17:12.041862'),(41,'firstapp','0021_alter_contract_customer_and_more','2023-05-15 09:32:34.697560'),(42,'firstapp','0022_rename_customer_contract_customer_contact','2023-05-15 09:53:09.515605'),(43,'firstapp','0023_remove_contract_final_allotment_ref_number_and_more','2023-05-15 11:00:58.880971'),(44,'firstapp','0020_merge_20230515_0952','2023-05-17 05:03:53.454591'),(45,'firstapp','0024_merge_20230515_1650','2023-05-17 05:03:53.476561'),(46,'firstapp','0025_alter_contract_job_card_issue_and_more','2023-05-17 05:03:55.101232'),(47,'firstapp','0026_contract_status','2023-05-17 05:03:55.225341'),(48,'firstapp','0027_company_details_contract_sq_ft_rate_and_more','2023-05-18 08:29:48.718937'),(49,'firstapp','0028_customer_contact_state','2023-05-18 08:29:48.901094'),(50,'firstapp','0029_remove_contract_job_card_issue','2023-05-18 08:29:49.036718'),(51,'firstapp','0030_invoices_company','2023-05-18 08:29:49.466327'),(52,'firstapp','0031_company_details_created_by_and_more','2023-05-18 08:29:50.948735'),(53,'firstapp','0032_alter_company_details_fax_and_more','2023-05-18 08:29:52.004606'),(54,'firstapp','0033_remove_invoices_customer_contact_and_more','2023-05-20 04:09:01.207045'),(55,'firstapp','0034_invoices_customer_contact','2023-05-20 04:09:01.849953'),(56,'firstapp','0035_invoices_master_space','2023-05-20 04:09:02.340219'),(57,'firstapp','0036_invoices_status','2023-05-20 04:09:02.507907'),(58,'firstapp','0037_bank_alter_invoices_taxable_amount_and_more','2023-05-20 04:09:03.653398'),(59,'firstapp','0038_invoices_maintanence','2023-05-20 04:09:03.798497'),(60,'firstapp','0039_invoices_cgst_invoices_scgst','2023-05-20 04:09:04.072831'),(61,'firstapp','0040_rename_scgst_invoices_sgst','2023-05-20 04:09:04.202376'),(62,'firstapp','0041_alter_company_details_fax_and_more','2023-05-23 10:48:05.808286'),(63,'firstapp','0042_invoices_tax_amount_sum','2023-05-23 10:48:06.026566'),(64,'firstapp','0043_bank_acc_no_bank_branch_name_bank_ifsc_code_and_more','2023-05-23 10:48:06.616469'),(65,'firstapp','0044_bank_created_by_bank_created_on_bank_status_and_more','2023-05-23 10:48:07.375655'),(66,'firstapp','0045_invoices_bank','2023-05-23 10:48:07.879046'),(67,'firstapp','0046_company_details_signature','2023-05-23 10:48:08.039870'),(68,'firstapp','0047_alter_company_details_signature','2023-05-23 10:48:08.139553'),(69,'firstapp','0048_alter_company_details_signature','2023-05-23 10:48:08.483050'),(70,'firstapp','0049_alter_company_details_signature','2023-05-23 10:48:08.585866'),(71,'firstapp','0050_alter_company_details_signature','2023-05-23 10:48:08.918266'),(72,'firstapp','0051_alter_company_details_signature','2023-05-23 10:48:08.961127'),(73,'firstapp','0052_alter_company_details_signature','2023-05-23 10:48:09.011562'),(74,'firstapp','0053_payments','2023-05-24 05:37:51.327702'),(75,'firstapp','0054_rename_payments_payments_data','2023-05-24 06:28:19.627932'),(76,'firstapp','0055_rename_customer_id_payments_data_customer','2023-05-24 07:04:48.942826'),(77,'firstapp','0053_customer_grievance','2023-05-25 12:25:12.886590'),(78,'firstapp','0054_rename_signature_customer_grievance_complaint_pic','2023-05-25 12:25:13.053117'),(79,'firstapp','0055_alter_customer_grievance_complaint_pic','2023-05-25 12:25:13.098657'),(80,'firstapp','0056_alter_customer_grievance_complaint_pic','2023-05-25 12:25:13.138362'),(81,'firstapp','0057_alter_customer_grievance_complaint_pic','2023-05-25 12:25:13.188617'),(82,'firstapp','0058_customer_grievance_reply','2023-05-25 12:25:13.323041'),(83,'firstapp','0059_metrostation_s_name','2023-05-25 12:25:13.451456'),(84,'firstapp','0060_merge_20230525_1754','2023-05-25 12:25:13.478766'),(85,'firstapp','0060_merge_20230525_1746','2023-05-29 05:51:32.378153'),(86,'firstapp','0061_merge_20230527_0941','2023-05-29 05:51:32.399594'),(87,'firstapp','0062_login_table_email_login_table_phno','2023-05-31 12:14:45.328637'),(88,'firstapp','0063_login_table_profile_pic','2023-05-31 12:14:45.554152'),(89,'firstapp','0064_notification_alter_login_table_phno_and_more','2023-06-01 05:51:22.045400'),(90,'firstapp','0065_notification_status','2023-06-01 06:41:09.763214'),(91,'firstapp','0066_notification_type','2023-06-01 09:08:32.479011'),(92,'firstapp','0067_alter_invoices_customer_contact_and_more','2023-06-03 05:12:15.643754'),(93,'firstapp','0068_alter_invoices_customer_contact_and_more','2023-06-03 05:12:15.714966'),(94,'firstapp','0069_remove_payments_data_payment_status','2023-06-06 04:19:21.953410'),(95,'firstapp','0070_payments_data_master_space_creditnote','2023-06-07 04:35:33.365935'),(96,'firstapp','0071_login_table_customer_id','2023-06-08 04:27:04.090609'),(97,'firstapp','0072_customer_contact_password_customer_contact_username','2023-06-16 04:07:57.183959'),(98,'firstapp','0073_rename_payment_history_payments_data_payment_order_id_and_more','2023-06-16 04:07:57.449272'),(99,'firstapp','0074_notification_invoice_no_notification_name_and_more','2023-06-16 04:07:58.064222'),(100,'firstapp','0075_general_parameter','2023-06-17 06:37:30.304700'),(101,'firstapp','0076_alter_login_table_profile_pic','2023-06-21 11:46:30.411575'),(102,'firstapp','0077_alter_login_table_profile_pic','2023-06-21 11:46:30.457112'),(103,'firstapp','0078_alter_login_table_profile_pic','2023-06-21 11:46:30.509452'),(104,'firstapp','0079_alter_login_table_profile_pic','2023-06-21 11:46:30.552854'),(105,'firstapp','0080_alter_login_table_profile_pic','2023-06-21 11:46:30.597888'),(106,'firstapp','0081_remove_metrostationcontact_address','2023-06-21 12:15:12.224472');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('080b494p8zsz8w0x1rn7hcpsphzc3b4b','eyJzdXBpZCI6MX0:1q6Pli:aOxx295CSbpRe13RhCEJzQLx6cI1QqfhkSvprIap__Q','2023-06-20 06:02:10.041281'),('0smkgd3bvzs37b7l8usf53xqerrvfofo','eyJzdXBpZCI6MX0:1qBwrJ:Bp64ehRP46AwaEFQVCvjNC59BOx9RTAM8coPnTSQeQo','2023-07-05 12:22:49.705504');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `firstapp_bank`
--

LOCK TABLES `firstapp_bank` WRITE;
/*!40000 ALTER TABLE `firstapp_bank` DISABLE KEYS */;
INSERT INTO `firstapp_bank` VALUES (1,'SBI',12234675543,'SBIKAKKNAD','3444435','334545TTTF',1,'2023-06-03 05:46:16.000000',2,NULL,NULL),(2,'SBI',21111111535,'SBIKAKKNAD','3444435','334545TTTF',1,'2023-06-07 05:25:12.000000',1,NULL,NULL);
/*!40000 ALTER TABLE `firstapp_bank` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `firstapp_company_details`
--

LOCK TABLES `firstapp_company_details` WRITE;
/*!40000 ALTER TABLE `firstapp_company_details` DISABLE KEYS */;
INSERT INTO `firstapp_company_details` VALUES (1,'KMRL','Aluva','Ernakulam','kerala',6787822,'Jln metro','GBH2321','SBH324F','aluva','8899829892','8888888323','1','kmrl@123@gmail.com','www.company.org',32,1,'2023-05-20 05:16:15.000000',1,'2023-06-03 04:53:59.000000','/media/2023-06-03_10%3A23%3A59.jpg'),(2,'KMRL','JLN','Ernakulam','kerala',7889,'Jln metro','GBH2321','SBH324F','c56554645','65578788987','74678787','756798','vishnu.c@technovia.co.in','www.company.org',32,1,'2023-06-07 05:21:26.000000',NULL,NULL,'/media/sign.jpg');
/*!40000 ALTER TABLE `firstapp_company_details` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `firstapp_contract`
--

LOCK TABLES `firstapp_contract` WRITE;
/*!40000 ALTER TABLE `firstapp_contract` DISABLE KEYS */;
INSERT INTO `firstapp_contract` VALUES (4,'1004','1899','2023-05-14','545','2023-05-14','455454','2023-05-07','4555','2023-05-14','4545','455','2023-05-18','555','2023-05-10','545','2023-05-09','2023-05-18','2023-05-17','2023-05-11',5,14,12,'2023-05-17',24,334,344,43444,10,'jijo','tm','2023-05-20 05:27:33.000000','2023-06-06 05:08:11.000000',1,1,4,4,'2023-05-06',2,324),(5,'1009','1899','2023-06-15','545','2023-06-15','455454','2023-06-15','4555','2023-06-15','4545','455','2023-06-15','555','2023-06-15','545','2023-06-15','2023-06-15','2023-06-15','2030-04-14',5,15,30,'2023-06-15',45000,500,456,1500,10,'jijo','manager','2023-06-16 05:08:23.000000','2023-06-16 05:16:24.000000',1,1,12,5,'2023-06-15',1,2500);
/*!40000 ALTER TABLE `firstapp_contract` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `firstapp_creditnote`
--

LOCK TABLES `firstapp_creditnote` WRITE;
/*!40000 ALTER TABLE `firstapp_creditnote` DISABLE KEYS */;
/*!40000 ALTER TABLE `firstapp_creditnote` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `firstapp_customer`
--

LOCK TABLES `firstapp_customer` WRITE;
/*!40000 ALTER TABLE `firstapp_customer` DISABLE KEYS */;
INSERT INTO `firstapp_customer` VALUES (6,NULL,'David','Partnership','shop',2,'2023-05-20 04:55:47.000000',NULL,NULL,1),(7,NULL,'James','Limited Liability Company (LLC)','Tms Solution',2,'2023-05-20 04:57:57.000000',NULL,NULL,1),(8,NULL,'Arjun','Software Company','shop',2,'2023-06-01 06:05:23.000000',NULL,NULL,1),(9,NULL,'Arjun','Software Company','shop',2,'2023-06-01 06:05:44.000000',NULL,NULL,1),(10,NULL,'Mahi','Software Company','shop',2,'2023-06-01 06:08:12.000000',NULL,NULL,1),(11,NULL,'James','Limited Liability Company (LLC)','Tms Solution',2,'2023-06-01 06:43:32.000000',NULL,NULL,1),(12,NULL,'David','Software Company','shop',2,'2023-06-01 08:31:01.000000',NULL,NULL,1),(13,NULL,'Arjun','Software Company','shop',2,'2023-06-01 08:31:49.000000',NULL,NULL,1),(14,NULL,'','','',2,'2023-06-07 04:36:07.000000',NULL,NULL,1),(15,NULL,'Ash','','',2,'2023-06-07 04:43:53.000000',NULL,NULL,1),(16,NULL,'vishnu','electronics store','phone4',2,'2023-06-16 04:12:50.000000',NULL,NULL,NULL),(17,NULL,'vishnu',NULL,NULL,2,'2023-06-16 04:23:33.000000',NULL,NULL,NULL);
/*!40000 ALTER TABLE `firstapp_customer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `firstapp_customer_contact`
--

LOCK TABLES `firstapp_customer_contact` WRITE;
/*!40000 ALTER TABLE `firstapp_customer_contact` DISABLE KEYS */;
INSERT INTO `firstapp_customer_contact` VALUES (4,'David@uk.co.in',9002928222,'Aluva','Ernakulam',67644,'aluva metro','34ABC34',1,'2023-05-20 04:55:47.000000',NULL,NULL,1,6,'GH45111',32,'kerala',NULL,NULL),(5,'jaes1234@gmail.com',90029282,'cusat','Ernakulam',445454,'Cusat metro','3445ABC34',1,'2023-05-20 04:57:57.000000',NULL,NULL,1,7,'SBH324F',32,'kerala32',NULL,NULL),(6,'arjun@technovia.co.in',9002928222,'kochi','Ernakulam',679233,'aluva metro','3445ABC34',4,'2023-06-01 06:05:44.000000',NULL,NULL,1,9,'',32,'kerala',NULL,NULL),(7,'mahi@technovia.co.in',9002928222,'kochi','Ernakulam',679233,'aluva metro','3445ABC34',1,'2023-06-01 06:08:12.000000',NULL,NULL,1,10,'',32,'kerala',NULL,NULL),(8,'aluvametro@technovia.co.in',9002928223,'High court','Ernakullam',323,'3323','3445ABC34',2,'2023-06-01 06:43:32.000000',NULL,NULL,1,11,'SBH324F',23,'k',NULL,NULL),(9,'aluvametro@technovia.co.in',90029282223444,'253','Ernakulam',4554,'323','3445ABC34',5,'2023-06-01 08:31:01.000000',NULL,NULL,1,12,'35',52,'235',NULL,NULL),(10,'cusat123@gmail.com',90029282223444,'JLN','Ernakullam',67,'Jln metro','3445ABC34',4,'2023-06-01 08:31:49.000000',NULL,NULL,1,13,'',32,'',NULL,NULL),(11,'',12,'','',12,'','',4,'2023-06-07 04:43:53.000000',NULL,NULL,1,15,'',12,'',NULL,NULL),(12,'vishnu.c@technovia.co.in',9020487598,'kochi','Ernakulam',4456432,'Jln metro','GBH2321',1,'2023-06-16 04:12:50.000000',NULL,NULL,NULL,16,'SBH324F',32,'Kerala','pbkdf2_sha256$600000$4zxLfQTyIfsuMhFEZRb9hm$aKbnfVSd5RJqMSIMqBcPNfP5rmNaTVHcwEKvuGLWehc=','vishnu'),(13,'vishnu.c@technovia.co.in',9020487598,NULL,NULL,NULL,NULL,NULL,4,'2023-06-16 04:23:33.000000',NULL,NULL,NULL,17,NULL,NULL,NULL,'pbkdf2_sha256$600000$tdVaQAMVptkm47HylVyf4Y$76d5+V8BNNnKRJC6lw7RfX8kgwXNH2aWn70SAI2cT4w=','vishnu');
/*!40000 ALTER TABLE `firstapp_customer_contact` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `firstapp_customer_grievance`
--

LOCK TABLES `firstapp_customer_grievance` WRITE;
/*!40000 ALTER TABLE `firstapp_customer_grievance` DISABLE KEYS */;
INSERT INTO `firstapp_customer_grievance` VALUES (1,'/static/media/2023-06-01%2014%3A52%3A46.jpg','Kore reason ind','pryula',1,'2023-06-01 09:22:46.000000',NULL,NULL,1,NULL,3,NULL),(2,'','Kore reason ind','eeeeeeeeeeeee',1,'2023-06-02 09:17:13.000000',NULL,NULL,1,NULL,3,NULL),(3,'/media/greivence.jpg','Kore reason ind','wwwwwwwwwww',1,'2023-06-02 09:22:16.000000',NULL,NULL,1,NULL,5,NULL),(4,'/media/2023-06-02%2016%3A32%3A56.jpg','Kore reason ind','vjh\r\n',2,'2023-06-02 09:23:17.000000','2023-06-02 11:03:27.000000',1,1,NULL,3,'ok'),(5,'','Electricity Failure','property damage',1,'2023-06-16 06:32:27.000000',NULL,NULL,15,12,5,NULL);
/*!40000 ALTER TABLE `firstapp_customer_grievance` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `firstapp_general_parameter`
--

LOCK TABLES `firstapp_general_parameter` WRITE;
/*!40000 ALTER TABLE `firstapp_general_parameter` DISABLE KEYS */;
INSERT INTO `firstapp_general_parameter` VALUES (13,'space_type','office',1),(14,'area_level','STRT',1),(15,'space_type','Kiosk',1),(16,'area_level','CONC',1),(17,'area_level','PLTF',1),(18,'area_type','Paid',1),(19,'area_type','Unpaid',1),(20,'area_side','LHS',1),(21,'area_side','RHS',1),(22,'area_level','PD',1);
/*!40000 ALTER TABLE `firstapp_general_parameter` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `firstapp_invoices`
--

LOCK TABLES `firstapp_invoices` WRITE;
/*!40000 ALTER TABLE `firstapp_invoices` DISABLE KEYS */;
INSERT INTO `firstapp_invoices` VALUES (1,1001,'2023-05-19','2023-06-23','566',5666,'2023-05-09','2023-05-25','2023-05-19',34444,38434.00,9,46768.12,4,1,1,'2023-05-20 06:05:10.000000',1,'2023-06-07 05:16:36.000000',4,4,2,1200.00,3567.06,3567.06,38434.00,1),(2,1,'2023-06-06','2023-06-06','01',1,'2023-06-06','2023-06-06','2023-06-06',223,2000.00,10,32400.00,4,2,1,'2023-06-07 05:29:26.000000',NULL,NULL,4,4,4,25000.00,2700.00,2700.00,27000.00,2),(3,1002,'2023-06-16','2023-06-16','7c2903chwc9329e399ff3278fcc88678c9e999d87889sfv9990v954s67vs792defc1',5667,'2023-06-16','2023-06-01','2023-06-30',997212,45000.00,9,53100.00,5,2,1,'2023-06-15 18:30:00.000000',NULL,NULL,12,5,3,0.00,4050.00,4050.00,45000.00,2);
/*!40000 ALTER TABLE `firstapp_invoices` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `firstapp_login_table`
--

LOCK TABLES `firstapp_login_table` WRITE;
/*!40000 ALTER TABLE `firstapp_login_table` DISABLE KEYS */;
INSERT INTO `firstapp_login_table` VALUES (1,' KMRL','admin','pbkdf2_sha256$600000$giL4sdOh1bDcLoZRyBTIku$4bIWOv64y9HredOGOSjot3KfXAMEzgKxqmKdPAbYXsc=',1,NULL,1,'2023-06-01 10:10:47.000000',1,'2023-06-16 10:41:00.000000',1,'KMRL@technovia.co.in','900292822','/media/profilepicture_8ztMSHa.jpg',NULL),(7,'ashwin','ashwin','pbkdf2_sha256$600000$6kPEmU3TjYY6FUEsoQeYTX$RtXTjgXq3DmdWoUibPwtLYrsLMs7MlMZr/xSxmmdGJo=',1,NULL,2,NULL,NULL,NULL,NULL,NULL,NULL,'',NULL),(13,'Arjun123','admin2323','pbkdf2_sha256$600000$40cQNxtQjJVXPJokSVWDui$GnKrZmgEEO8Bhyb4kroAK+o+8LcNlz0BjHSrEATRZ/c=',4,NULL,2,NULL,NULL,NULL,NULL,NULL,NULL,'',NULL),(14,'customer','customer','pbkdf2_sha256$600000$tsvpf2jo60894wBpu4zdIi$ClXS8k/NVG0bBLlRadnQF3wK2UVZMf8cp8O0CpZJNRo=',2,NULL,1,NULL,NULL,NULL,NULL,NULL,NULL,NULL,1),(15,'vishnu','vishnu','pbkdf2_sha256$600000$4zxLfQTyIfsuMhFEZRb9hm$aKbnfVSd5RJqMSIMqBcPNfP5rmNaTVHcwEKvuGLWehc=',2,NULL,1,'2023-06-16 04:25:11.000000',1,'2023-06-20 05:44:38.000000',15,'vishnu.c@technovia.co.in','9020487598','/media/profilepicture_fRXxY1m.jpg',12),(16,'admin','admin2','pbkdf2_sha256$600000$gQMZp9nIVdX5fMslotU5yK$ool5yLMWvB+KnDm5trOWw6DPEheocrww4eOMgexlumY=',1,NULL,1,NULL,NULL,'2023-06-21 04:54:43.000000',16,'vishnu.c@technovia.co.in','None','',NULL);
/*!40000 ALTER TABLE `firstapp_login_table` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `firstapp_login_table_notifications`
--

LOCK TABLES `firstapp_login_table_notifications` WRITE;
/*!40000 ALTER TABLE `firstapp_login_table_notifications` DISABLE KEYS */;
INSERT INTO `firstapp_login_table_notifications` VALUES (1,1,1),(2,1,2),(4,1,4),(6,1,6),(8,1,8),(10,1,10),(12,1,12),(14,1,14),(16,1,16),(18,1,18),(20,1,20),(21,1,21),(22,1,22),(24,1,24),(26,1,26),(3,7,3),(5,7,5),(7,7,7),(9,7,9),(11,7,11),(13,7,13),(15,7,15),(17,7,17),(19,7,19),(23,7,23),(25,7,25),(27,7,27);
/*!40000 ALTER TABLE `firstapp_login_table_notifications` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `firstapp_member`
--

LOCK TABLES `firstapp_member` WRITE;
/*!40000 ALTER TABLE `firstapp_member` DISABLE KEYS */;
/*!40000 ALTER TABLE `firstapp_member` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `firstapp_metrostation`
--

LOCK TABLES `firstapp_metrostation` WRITE;
/*!40000 ALTER TABLE `firstapp_metrostation` DISABLE KEYS */;
INSERT INTO `firstapp_metrostation` VALUES (19,'Aluva','10:00:00.000000','22:00:00.000000',1,'2023-05-20 04:31:24.000000',1,NULL,NULL,NULL),(20,'Cusat','10:00:00.000000','22:00:00.000000',1,'2023-05-20 04:32:37.000000',1,NULL,NULL,'CST');
/*!40000 ALTER TABLE `firstapp_metrostation` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `firstapp_metrostationcontact`
--

LOCK TABLES `firstapp_metrostationcontact` WRITE;
/*!40000 ALTER TABLE `firstapp_metrostationcontact` DISABLE KEYS */;
INSERT INTO `firstapp_metrostationcontact` VALUES (1,'Aluva','Ernakulam',679233,'aluvametro@technovia.co.in',9002928223,1,'2023-05-20 04:31:24.000000',1,NULL,NULL,19),(2,'cusat','Ernakulam',653332,'cusat123@gmail.com',9002928222,1,'2023-05-20 04:32:37.000000',1,'2023-06-05 04:59:54.609470',1,20);
/*!40000 ALTER TABLE `firstapp_metrostationcontact` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `firstapp_notification`
--

LOCK TABLES `firstapp_notification` WRITE;
/*!40000 ALTER TABLE `firstapp_notification` DISABLE KEYS */;
INSERT INTO `firstapp_notification` VALUES (1,'New customer registered: Arjun','2023-06-01 06:05:44.706622',2,1,NULL,NULL,NULL),(2,'New customer registered: Mahi','2023-06-01 06:08:12.252445',2,1,NULL,NULL,NULL),(3,'New customer registered: Mahi','2023-06-01 06:08:12.299457',1,1,NULL,NULL,NULL),(4,'New customer registered: James','2023-06-01 06:43:32.191786',2,1,NULL,NULL,NULL),(5,'New customer registered: James','2023-06-01 06:43:32.243674',1,1,NULL,NULL,NULL),(6,'New customer registered: David','2023-06-01 08:31:01.238349',2,1,NULL,NULL,NULL),(7,'New customer registered: David','2023-06-01 08:31:01.303498',1,1,NULL,NULL,NULL),(8,'New customer registered: Arjun','2023-06-01 08:31:49.167553',2,1,NULL,NULL,NULL),(9,'New customer registered: Arjun','2023-06-01 08:31:49.209260',1,1,NULL,NULL,NULL),(10,'You have received a new message','2023-06-01 09:22:46.045644',2,2,NULL,NULL,NULL),(11,'You have received a new message','2023-06-01 09:22:46.098076',1,2,NULL,NULL,NULL),(12,'You have received a new message','2023-06-02 09:17:13.336784',2,2,NULL,NULL,NULL),(13,'You have received a new message','2023-06-02 09:17:13.377982',1,2,NULL,NULL,NULL),(14,'You have received a new message','2023-06-02 09:22:16.906019',2,2,NULL,NULL,NULL),(15,'You have received a new message','2023-06-02 09:22:16.960199',1,2,NULL,NULL,NULL),(16,'You have received a new message','2023-06-02 09:23:17.990997',2,2,NULL,NULL,NULL),(17,'You have received a new message','2023-06-02 09:23:18.033523',1,2,NULL,NULL,NULL),(18,'New customer registered: Ash','2023-06-07 04:43:53.866934',2,1,NULL,NULL,NULL),(19,'New customer registered: Ash','2023-06-07 04:43:53.917626',1,1,NULL,NULL,NULL),(20,'New customer registered: vishnu','2023-06-16 04:12:50.945726',2,1,NULL,NULL,NULL),(21,'New customer registered: vishnu','2023-06-16 04:23:34.022692',2,1,NULL,NULL,NULL),(22,'','2023-06-16 05:19:09.896022',2,3,' #1002','vishnu ','/media/profilepicture_fRXxY1m.jpg '),(23,'','2023-06-16 05:19:09.947401',1,3,' #1002','vishnu ','/media/profilepicture_fRXxY1m.jpg '),(24,'','2023-06-16 05:29:46.116340',2,3,' #1002','vishnu ','/media/profilepicture_fRXxY1m.jpg '),(25,'','2023-06-16 05:29:46.175170',1,3,' #1002','vishnu ','/media/profilepicture_fRXxY1m.jpg '),(26,'You have received a new message','2023-06-16 06:32:27.161227',2,2,NULL,NULL,NULL),(27,'You have received a new message','2023-06-16 06:32:27.218445',1,2,NULL,NULL,NULL);
/*!40000 ALTER TABLE `firstapp_notification` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `firstapp_payments_data`
--

LOCK TABLES `firstapp_payments_data` WRITE;
/*!40000 ALTER TABLE `firstapp_payments_data` DISABLE KEYS */;
INSERT INTO `firstapp_payments_data` VALUES (1,'25689825',35000.00,'Card',NULL,NULL,NULL,NULL,2,'2023-05-20 04:55:47.000000',1,4,1,NULL,NULL),(5,'343333',23444.00,'Card',NULL,NULL,NULL,NULL,1,'2023-05-20 04:55:47.000000',1,5,1,NULL,NULL),(6,'356655',23444.00,'Card',NULL,NULL,NULL,NULL,3,'2023-05-20 04:55:47.000000',1,5,1,NULL,NULL),(8,'pay_M2UD6mqfsTjW8e',53100.00,NULL,'order_M2UCnxeJ1VZ3K2',NULL,NULL,NULL,1,'2023-06-16 05:29:46.000000',15,12,3,5,'04aacd6435b289417668b9c7c853e81aea446526cb41ec9bd49f9360d917f9bf');
/*!40000 ALTER TABLE `firstapp_payments_data` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `firstapp_space`
--

LOCK TABLES `firstapp_space` WRITE;
/*!40000 ALTER TABLE `firstapp_space` DISABLE KEYS */;
INSERT INTO `firstapp_space` VALUES (3,'LHS HIGH CONC 08','Office','Paid','LHS','CONC',400,1,'2023-05-20 04:33:11.000000','2023-06-07 06:29:49.000000',1,1,1,3,1),(4,'RHS HIGH STR 08','Kiosk','Unpaid','RHS','STRT',450,1,'2023-05-20 04:33:55.000000',NULL,NULL,1,2,4,1),(5,'RHS ALUV STR 08','Office','Unpaid','RHS','STRT',535,1,'2023-05-25 11:34:17.000000',NULL,NULL,1,1,5,2),(6,'LHS CST STR 08','Kiosk','Unpaid','RHS','PLTF',400,1,'2023-06-19 10:54:46.000000','2023-06-21 06:36:58.000000',1,1,2,5,1);
/*!40000 ALTER TABLE `firstapp_space` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-06-21 18:09:57
