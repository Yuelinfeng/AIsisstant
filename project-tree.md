```
AIsisstant
├─ .dockerignore
├─ .typos.toml
├─ CODE_OF_CONDUCT.md
├─ CONTRIBUTING.md
├─ LICENSE
├─ README.md
├─ README_CN.md
├─ SECURITY.md
├─ USE-CASES.md
├─ apps
│  ├─ __init__.py
│  ├─ application
│  │  ├─ __init__.py
│  │  ├─ admin.py
│  │  ├─ apps.py
│  │  ├─ chat_pipeline
│  │  │  ├─ I_base_chat_pipeline.py
│  │  │  ├─ __init__.py
│  │  │  ├─ pipeline_manage.py
│  │  │  └─ step
│  │  │     ├─ __init__.py
│  │  │     ├─ chat_step
│  │  │     │  ├─ __init__.py
│  │  │     │  ├─ i_chat_step.py
│  │  │     │  └─ impl
│  │  │     │     └─ base_chat_step.py
│  │  │     ├─ generate_human_message_step
│  │  │     │  ├─ __init__.py
│  │  │     │  ├─ i_generate_human_message_step.py
│  │  │     │  └─ impl
│  │  │     │     └─ base_generate_human_message_step.py
│  │  │     └─ reset_problem_step
│  │  │        ├─ __init__.py
│  │  │        ├─ i_reset_problem_step.py
│  │  │        └─ impl
│  │  │           └─ base_reset_problem_step.py
│  │  ├─ flow
│  │  │  ├─ __init__.py
│  │  │  ├─ common.py
│  │  │  ├─ default_workflow.json
│  │  │  ├─ default_workflow_en.json
│  │  │  ├─ default_workflow_zh.json
│  │  │  ├─ default_workflow_zh_Hant.json
│  │  │  ├─ i_step_node.py
│  │  │  ├─ step_node
│  │  │  │  ├─ __init__.py
│  │  │  │  ├─ ai_chat_step_node
│  │  │  │  │  ├─ __init__.py
│  │  │  │  │  ├─ i_chat_node.py
│  │  │  │  │  └─ impl
│  │  │  │  │     ├─ __init__.py
│  │  │  │  │     └─ base_chat_node.py
│  │  │  │  ├─ application_node
│  │  │  │  │  ├─ __init__.py
│  │  │  │  │  ├─ i_application_node.py
│  │  │  │  │  └─ impl
│  │  │  │  │     ├─ __init__.py
│  │  │  │  │     └─ base_application_node.py
│  │  │  │  ├─ condition_node
│  │  │  │  │  ├─ __init__.py
│  │  │  │  │  ├─ compare
│  │  │  │  │  │  ├─ __init__.py
│  │  │  │  │  │  ├─ compare.py
│  │  │  │  │  │  ├─ contain_compare.py
│  │  │  │  │  │  ├─ equal_compare.py
│  │  │  │  │  │  ├─ ge_compare.py
│  │  │  │  │  │  ├─ gt_compare.py
│  │  │  │  │  │  ├─ is_not_null_compare.py
│  │  │  │  │  │  ├─ is_not_true.py
│  │  │  │  │  │  ├─ is_null_compare.py
│  │  │  │  │  │  ├─ is_true.py
│  │  │  │  │  │  ├─ le_compare.py
│  │  │  │  │  │  ├─ len_equal_compare.py
│  │  │  │  │  │  ├─ len_ge_compare.py
│  │  │  │  │  │  ├─ len_gt_compare.py
│  │  │  │  │  │  ├─ len_le_compare.py
│  │  │  │  │  │  ├─ len_lt_compare.py
│  │  │  │  │  │  ├─ lt_compare.py
│  │  │  │  │  │  └─ not_contain_compare.py
│  │  │  │  │  ├─ i_condition_node.py
│  │  │  │  │  └─ impl
│  │  │  │  │     ├─ __init__.py
│  │  │  │  │     └─ base_condition_node.py
│  │  │  │  ├─ direct_reply_node
│  │  │  │  │  ├─ __init__.py
│  │  │  │  │  ├─ i_reply_node.py
│  │  │  │  │  └─ impl
│  │  │  │  │     ├─ __init__.py
│  │  │  │  │     └─ base_reply_node.py
│  │  │  │  ├─ document_extract_node
│  │  │  │  │  ├─ __init__.py
│  │  │  │  │  ├─ i_document_extract_node.py
│  │  │  │  │  └─ impl
│  │  │  │  │     ├─ __init__.py
│  │  │  │  │     └─ base_document_extract_node.py
│  │  │  │  ├─ form_node
│  │  │  │  │  ├─ __init__.py
│  │  │  │  │  ├─ i_form_node.py
│  │  │  │  │  └─ impl
│  │  │  │  │     ├─ __init__.py
│  │  │  │  │     └─ base_form_node.py
│  │  │  │  ├─ function_lib_node
│  │  │  │  │  ├─ __init__.py
│  │  │  │  │  ├─ i_function_lib_node.py
│  │  │  │  │  └─ impl
│  │  │  │  │     ├─ __init__.py
│  │  │  │  │     └─ base_function_lib_node.py
│  │  │  │  ├─ function_node
│  │  │  │  │  ├─ __init__.py
│  │  │  │  │  ├─ i_function_node.py
│  │  │  │  │  └─ impl
│  │  │  │  │     ├─ __init__.py
│  │  │  │  │     └─ base_function_node.py
│  │  │  │  ├─ image_generate_step_node
│  │  │  │  │  ├─ __init__.py
│  │  │  │  │  ├─ i_image_generate_node.py
│  │  │  │  │  └─ impl
│  │  │  │  │     ├─ __init__.py
│  │  │  │  │     └─ base_image_generate_node.py
│  │  │  │  ├─ image_understand_step_node
│  │  │  │  │  ├─ __init__.py
│  │  │  │  │  ├─ i_image_understand_node.py
│  │  │  │  │  └─ impl
│  │  │  │  │     ├─ __init__.py
│  │  │  │  │     └─ base_image_understand_node.py
│  │  │  │  ├─ mcp_node
│  │  │  │  │  ├─ __init__.py
│  │  │  │  │  ├─ i_mcp_node.py
│  │  │  │  │  └─ impl
│  │  │  │  │     ├─ __init__.py
│  │  │  │  │     └─ base_mcp_node.py
│  │  │  │  ├─ question_node
│  │  │  │  │  ├─ __init__.py
│  │  │  │  │  ├─ i_question_node.py
│  │  │  │  │  └─ impl
│  │  │  │  │     ├─ __init__.py
│  │  │  │  │     └─ base_question_node.py
│  │  │  │  ├─ reranker_node
│  │  │  │  │  ├─ __init__.py
│  │  │  │  │  ├─ i_reranker_node.py
│  │  │  │  │  └─ impl
│  │  │  │  │     ├─ __init__.py
│  │  │  │  │     └─ base_reranker_node.py
│  │  │  │  ├─ speech_to_text_step_node
│  │  │  │  │  ├─ __init__.py
│  │  │  │  │  ├─ i_speech_to_text_node.py
│  │  │  │  │  └─ impl
│  │  │  │  │     ├─ __init__.py
│  │  │  │  │     └─ base_speech_to_text_node.py
│  │  │  │  ├─ start_node
│  │  │  │  │  ├─ __init__.py
│  │  │  │  │  ├─ i_start_node.py
│  │  │  │  │  └─ impl
│  │  │  │  │     ├─ __init__.py
│  │  │  │  │     └─ base_start_node.py
│  │  │  │  ├─ text_to_speech_step_node
│  │  │  │  │  ├─ __init__.py
│  │  │  │  │  ├─ i_text_to_speech_node.py
│  │  │  │  │  └─ impl
│  │  │  │  │     ├─ __init__.py
│  │  │  │  │     └─ base_text_to_speech_node.py
│  │  │  │  └─ variable_assign_node
│  │  │  │     ├─ __init__.py
│  │  │  │     ├─ i_variable_assign_node.py
│  │  │  │     └─ impl
│  │  │  │        ├─ __init__.py
│  │  │  │        └─ base_variable_assign_node.py
│  │  │  ├─ tools.py
│  │  │  └─ workflow_manage.py
│  │  ├─ migrations
│  │  │  ├─ 0001_initial.py
│  │  │  ├─ 0002_chat_client_id.py
│  │  │  ├─ 0003_application_icon.py
│  │  │  ├─ 0004_applicationaccesstoken_show_source.py
│  │  │  ├─ 0005_alter_chat_abstract_alter_chatrecord_answer_text.py
│  │  │  ├─ 0006_applicationapikey_allow_cross_domain_and_more.py
│  │  │  ├─ 0007_alter_application_prologue.py
│  │  │  ├─ 0008_chat_is_deleted.py
│  │  │  ├─ 0009_application_type_application_work_flow_and_more.py
│  │  │  ├─ 0010_alter_chatrecord_details.py
│  │  │  ├─ 0011_application_model_params_setting.py
│  │  │  ├─ 0012_application_stt_model_application_stt_model_enable_and_more.py
│  │  │  ├─ 0013_application_tts_type.py
│  │  │  ├─ 0014_application_problem_optimization_prompt.py
│  │  │  ├─ 0016_alter_chatrecord_problem_text.py
│  │  │  ├─ 0017_application_tts_model_params_setting.py
│  │  │  ├─ 0018_workflowversion_name.py
│  │  │  ├─ 0019_application_file_upload_enable_and_more.py
│  │  │  ├─ 0020_application_record_update_time.py
│  │  │  ├─ 0021_applicationpublicaccessclient_client_id_and_more.py
│  │  │  ├─ 0022_application_tts_autoplay.py
│  │  │  ├─ 0023_application_stt_autosend.py
│  │  │  ├─ 0024_applicationaccesstoken_language.py
│  │  │  ├─ 0025_alter_application_prologue.py
│  │  │  ├─ 0026_chat_asker.py
│  │  │  └─ __init__.py
│  │  ├─ serializers
│  │  │  ├─ application_serializers.py
│  │  │  ├─ application_statistics_serializers.py
│  │  │  ├─ application_version_serializers.py
│  │  │  ├─ chat_message_serializers.py
│  │  │  └─ chat_serializers.py
│  │  ├─ sql
│  │  │  ├─ chat_record_count.sql
│  │  │  ├─ chat_record_count_trend.sql
│  │  │  ├─ customer_count.sql
│  │  │  ├─ customer_count_trend.sql
│  │  │  ├─ export_application_chat.sql
│  │  │  ├─ list_application.sql
│  │  │  └─ list_application_chat.sql
│  │  ├─ swagger_api
│  │  │  ├─ application_api.py
│  │  │  ├─ application_statistics_api.py
│  │  │  ├─ application_version_api.py
│  │  │  └─ chat_api.py
│  │  ├─ task
│  │  │  └─ __init__.py
│  │  ├─ template
│  │  │  └─ embed.js
│  │  ├─ tests.py
│  │  ├─ urls.py
│  │  └─ views
│  │     ├─ __init__.py
│  │     ├─ application_version_views.py
│  │     ├─ application_views.py
│  │     ├─ chat_views.py
│  │     └─ common.py
│  ├─ common
│  │  ├─ __init__.py
│  │  ├─ auth
│  │  │  ├─ __init__.py
│  │  │  ├─ authenticate.py
│  │  │  ├─ authentication.py
│  │  │  └─ handle
│  │  │     ├─ auth_base_handle.py
│  │  │     └─ impl
│  │  │        ├─ application_key.py
│  │  │        ├─ public_access_token.py
│  │  │        └─ user_token.py
│  │  ├─ cache
│  │  │  ├─ file_cache.py
│  │  │  └─ mem_cache.py
│  │  ├─ chunk
│  │  │  ├─ __init__.py
│  │  │  ├─ i_chunk_handle.py
│  │  │  └─ impl
│  │  │     └─ mark_chunk_handle.py
│  │  ├─ config
│  │  │  ├─ embedding_config.py
│  │  │  ├─ swagger_conf.py
│  │  │  └─ tokenizer_manage_config.py
│  │  ├─ constants
│  │  │  ├─ authentication_type.py
│  │  │  ├─ cache_code_constants.py
│  │  │  ├─ exception_code_constants.py
│  │  │  └─ permission_constants.py
│  │  ├─ db
│  │  │  ├─ compiler.py
│  │  │  ├─ search.py
│  │  │  └─ sql_execute.py
│  │  ├─ encoder
│  │  │  └─ encoder.py
│  │  ├─ event
│  │  │  ├─ __init__.py
│  │  │  ├─ common.py
│  │  │  └─ listener_manage.py
│  │  ├─ exception
│  │  │  └─ app_exception.py
│  │  ├─ field
│  │  │  ├─ __init__.py
│  │  │  ├─ common.py
│  │  │  └─ vector_field.py
│  │  ├─ forms
│  │  │  ├─ __init__.py
│  │  │  ├─ array_object_card.py
│  │  │  ├─ base_field.py
│  │  │  ├─ base_form.py
│  │  │  ├─ label
│  │  │  │  ├─ __init__.py
│  │  │  │  ├─ base_label.py
│  │  │  │  └─ tooltip_label.py
│  │  │  ├─ multi_select.py
│  │  │  ├─ object_card.py
│  │  │  ├─ password_input.py
│  │  │  ├─ radio_button_field.py
│  │  │  ├─ radio_card_field.py
│  │  │  ├─ radio_field.py
│  │  │  ├─ single_select_field.py
│  │  │  ├─ slider_field.py
│  │  │  ├─ switch_field.py
│  │  │  ├─ tab_card.py
│  │  │  ├─ table_checkbox.py
│  │  │  ├─ table_radio.py
│  │  │  └─ text_input_field.py
│  │  ├─ handle
│  │  │  ├─ __init__.py
│  │  │  ├─ base_parse_qa_handle.py
│  │  │  ├─ base_parse_table_handle.py
│  │  │  ├─ base_split_handle.py
│  │  │  ├─ base_to_response.py
│  │  │  ├─ handle_exception.py
│  │  │  └─ impl
│  │  │     ├─ csv_split_handle.py
│  │  │     ├─ doc_split_handle.py
│  │  │     ├─ html_split_handle.py
│  │  │     ├─ pdf_split_handle.py
│  │  │     ├─ qa
│  │  │     │  ├─ csv_parse_qa_handle.py
│  │  │     │  ├─ xls_parse_qa_handle.py
│  │  │     │  ├─ xlsx_parse_qa_handle.py
│  │  │     │  └─ zip_parse_qa_handle.py
│  │  │     ├─ response
│  │  │     │  ├─ openai_to_response.py
│  │  │     │  └─ system_to_response.py
│  │  │     ├─ table
│  │  │     │  ├─ csv_parse_table_handle.py
│  │  │     │  ├─ xls_parse_table_handle.py
│  │  │     │  └─ xlsx_parse_table_handle.py
│  │  │     ├─ text_split_handle.py
│  │  │     ├─ tools.py
│  │  │     ├─ xls_split_handle.py
│  │  │     ├─ xlsx_split_handle.py
│  │  │     └─ zip_split_handle.py
│  │  ├─ init
│  │  │  └─ init_doc.py
│  │  ├─ job
│  │  │  ├─ __init__.py
│  │  │  ├─ clean_chat_job.py
│  │  │  ├─ clean_debug_file_job.py
│  │  │  └─ client_access_num_job.py
│  │  ├─ lock
│  │  │  ├─ base_lock.py
│  │  │  └─ impl
│  │  │     └─ file_lock.py
│  │  ├─ log
│  │  │  └─ log.py
│  │  ├─ management
│  │  │  ├─ __init__.py
│  │  │  └─ commands
│  │  │     ├─ __init__.py
│  │  │     ├─ celery.py
│  │  │     ├─ restart.py
│  │  │     ├─ services
│  │  │     │  ├─ __init__.py
│  │  │     │  ├─ command.py
│  │  │     │  ├─ hands.py
│  │  │     │  ├─ services
│  │  │     │  │  ├─ __init__.py
│  │  │     │  │  ├─ base.py
│  │  │     │  │  ├─ celery_base.py
│  │  │     │  │  ├─ celery_default.py
│  │  │     │  │  ├─ gunicorn.py
│  │  │     │  │  └─ local_model.py
│  │  │     │  └─ utils.py
│  │  │     ├─ start.py
│  │  │     ├─ status.py
│  │  │     └─ stop.py
│  │  ├─ middleware
│  │  │  ├─ cross_domain_middleware.py
│  │  │  ├─ doc_headers_middleware.py
│  │  │  ├─ gzip.py
│  │  │  └─ static_headers_middleware.py
│  │  ├─ mixins
│  │  │  ├─ api_mixin.py
│  │  │  └─ app_model_mixin.py
│  │  ├─ response
│  │  │  └─ result.py
│  │  ├─ sql
│  │  │  └─ list_embedding_text.sql
│  │  ├─ swagger_api
│  │  │  └─ common_api.py
│  │  ├─ task
│  │  │  └─ __init__.py
│  │  ├─ template
│  │  │  ├─ email_template_en.html
│  │  │  ├─ email_template_zh.html
│  │  │  └─ email_template_zh_Hant.html
│  │  └─ util
│  │     ├─ cache_util.py
│  │     ├─ common.py
│  │     ├─ field_message.py
│  │     ├─ file_util.py
│  │     ├─ fork.py
│  │     ├─ function_code.py
│  │     ├─ lock.py
│  │     ├─ page_utils.py
│  │     ├─ rsa_util.py
│  │     ├─ split_model.py
│  │     ├─ test.py
│  │     └─ ts_vecto_util.py
│  ├─ embedding
│  │  ├─ __init__.py
│  │  ├─ admin.py
│  │  ├─ apps.py
│  │  ├─ migrations
│  │  │  ├─ 0001_initial.py
│  │  │  ├─ 0002_embedding_search_vector.py
│  │  │  ├─ 0003_alter_embedding_unique_together.py
│  │  │  └─ __init__.py
│  │  ├─ sql
│  │  │  ├─ blend_search.sql
│  │  │  ├─ embedding_search.sql
│  │  │  ├─ hit_test.sql
│  │  │  └─ keywords_search.sql
│  │  ├─ task
│  │  │  ├─ __init__.py
│  │  │  └─ embedding.py
│  │  ├─ tests.py
│  │  ├─ vector
│  │  │  ├─ base_vector.py
│  │  │  └─ pg_vector.py
│  │  └─ views.py
│  ├─ locales
│  │  ├─ en_US
│  │  │  └─ LC_MESSAGES
│  │  │     └─ django.po
│  │  ├─ zh_CN
│  │  │  └─ LC_MESSAGES
│  │  │     └─ django.po
│  │  └─ zh_Hant
│  │     └─ LC_MESSAGES
│  │        └─ django.po
│  ├─ manage.py
│  ├─ ops
│  │  ├─ __init__.py
│  │  └─ celery
│  │     ├─ __init__.py
│  │     ├─ const.py
│  │     ├─ decorator.py
│  │     ├─ heartbeat.py
│  │     ├─ logger.py
│  │     ├─ signal_handler.py
│  │     └─ utils.py
│  ├─ setting
│  │  ├─ __init__.py
│  │  ├─ admin.py
│  │  ├─ apps.py
│  │  ├─ migrations
│  │  │  ├─ 0001_initial.py
│  │  │  ├─ 0002_systemsetting.py
│  │  │  ├─ 0003_model_meta_model_status.py
│  │  │  ├─ 0004_alter_model_credential.py
│  │  │  ├─ 0005_model_permission_type.py
│  │  │  ├─ 0006_alter_model_status.py
│  │  │  ├─ 0007_model_model_params_form.py
│  │  │  ├─ 0008_modelparam.py
│  │  │  ├─ 0009_set_default_model_params_form.py
│  │  │  ├─ 0010_log.py
│  │  │  └─ __init__.py
│  │  ├─ models_provider
│  │  │  ├─ __init__.py
│  │  │  ├─ base_model_provider.py
│  │  │  ├─ constants
│  │  │  │  └─ model_provider_constants.py
│  │  │  ├─ impl
│  │  │  │  ├─ aliyun_bai_lian_model_provider
│  │  │  │  │  ├─ __init__.py
│  │  │  │  │  ├─ aliyun_bai_lian_model_provider.py
│  │  │  │  │  ├─ credential
│  │  │  │  │  │  ├─ embedding.py
│  │  │  │  │  │  ├─ image.py
│  │  │  │  │  │  ├─ llm.py
│  │  │  │  │  │  ├─ reranker.py
│  │  │  │  │  │  ├─ stt.py
│  │  │  │  │  │  ├─ tti.py
│  │  │  │  │  │  └─ tts.py
│  │  │  │  │  ├─ icon
│  │  │  │  │  │  └─ aliyun_bai_lian_icon_svg
│  │  │  │  │  └─ model
│  │  │  │  │     ├─ embedding.py
│  │  │  │  │     ├─ iat_mp3_16k.mp3
│  │  │  │  │     ├─ image.py
│  │  │  │  │     ├─ llm.py
│  │  │  │  │     ├─ reranker.py
│  │  │  │  │     ├─ stt.py
│  │  │  │  │     ├─ tti.py
│  │  │  │  │     └─ tts.py
│  │  │  │  ├─ anthropic_model_provider
│  │  │  │  │  ├─ __init__.py
│  │  │  │  │  ├─ anthropic_model_provider.py
│  │  │  │  │  ├─ credential
│  │  │  │  │  │  ├─ image.py
│  │  │  │  │  │  └─ llm.py
│  │  │  │  │  ├─ icon
│  │  │  │  │  │  └─ anthropic_icon_svg
│  │  │  │  │  └─ model
│  │  │  │  │     ├─ image.py
│  │  │  │  │     └─ llm.py
│  │  │  │  ├─ aws_bedrock_model_provider
│  │  │  │  │  ├─ __init__.py
│  │  │  │  │  ├─ aws_bedrock_model_provider.py
│  │  │  │  │  ├─ credential
│  │  │  │  │  │  ├─ embedding.py
│  │  │  │  │  │  └─ llm.py
│  │  │  │  │  ├─ icon
│  │  │  │  │  │  └─ bedrock_icon_svg
│  │  │  │  │  └─ model
│  │  │  │  │     ├─ embedding.py
│  │  │  │  │     └─ llm.py
│  │  │  │  ├─ azure_model_provider
│  │  │  │  │  ├─ __init__.py
│  │  │  │  │  ├─ azure_model_provider.py
│  │  │  │  │  ├─ credential
│  │  │  │  │  │  ├─ embedding.py
│  │  │  │  │  │  ├─ image.py
│  │  │  │  │  │  ├─ llm.py
│  │  │  │  │  │  ├─ stt.py
│  │  │  │  │  │  ├─ tti.py
│  │  │  │  │  │  └─ tts.py
│  │  │  │  │  ├─ icon
│  │  │  │  │  │  └─ azure_icon_svg
│  │  │  │  │  └─ model
│  │  │  │  │     ├─ azure_chat_model.py
│  │  │  │  │     ├─ embedding.py
│  │  │  │  │     ├─ image.py
│  │  │  │  │     ├─ stt.py
│  │  │  │  │     ├─ tti.py
│  │  │  │  │     └─ tts.py
│  │  │  │  ├─ base_chat_open_ai.py
│  │  │  │  ├─ base_stt.py
│  │  │  │  ├─ base_tti.py
│  │  │  │  ├─ base_tts.py
│  │  │  │  ├─ deepseek_model_provider
│  │  │  │  │  ├─ __init__.py
│  │  │  │  │  ├─ credential
│  │  │  │  │  │  └─ llm.py
│  │  │  │  │  ├─ deepseek_model_provider.py
│  │  │  │  │  ├─ icon
│  │  │  │  │  │  └─ deepseek_icon_svg
│  │  │  │  │  └─ model
│  │  │  │  │     └─ llm.py
│  │  │  │  ├─ gemini_model_provider
│  │  │  │  │  ├─ __init__.py
│  │  │  │  │  ├─ credential
│  │  │  │  │  │  ├─ embedding.py
│  │  │  │  │  │  ├─ image.py
│  │  │  │  │  │  ├─ llm.py
│  │  │  │  │  │  └─ stt.py
│  │  │  │  │  ├─ gemini_model_provider.py
│  │  │  │  │  ├─ icon
│  │  │  │  │  │  └─ gemini_icon_svg
│  │  │  │  │  └─ model
│  │  │  │  │     ├─ embedding.py
│  │  │  │  │     ├─ image.py
│  │  │  │  │     ├─ llm.py
│  │  │  │  │     └─ stt.py
│  │  │  │  ├─ kimi_model_provider
│  │  │  │  │  ├─ __init__.py
│  │  │  │  │  ├─ credential
│  │  │  │  │  │  └─ llm.py
│  │  │  │  │  ├─ icon
│  │  │  │  │  │  └─ kimi_icon_svg
│  │  │  │  │  ├─ kimi_model_provider.py
│  │  │  │  │  └─ model
│  │  │  │  │     └─ llm.py
│  │  │  │  ├─ local_model_provider
│  │  │  │  │  ├─ __init__.py
│  │  │  │  │  ├─ credential
│  │  │  │  │  │  ├─ embedding.py
│  │  │  │  │  │  └─ reranker.py
│  │  │  │  │  ├─ icon
│  │  │  │  │  │  └─ local_icon_svg
│  │  │  │  │  ├─ local_model_provider.py
│  │  │  │  │  └─ model
│  │  │  │  │     ├─ embedding.py
│  │  │  │  │     └─ reranker.py
│  │  │  │  ├─ ollama_model_provider
│  │  │  │  │  ├─ __init__.py
│  │  │  │  │  ├─ credential
│  │  │  │  │  │  ├─ embedding.py
│  │  │  │  │  │  ├─ image.py
│  │  │  │  │  │  ├─ llm.py
│  │  │  │  │  │  └─ reranker.py
│  │  │  │  │  ├─ icon
│  │  │  │  │  │  └─ ollama_icon_svg
│  │  │  │  │  ├─ model
│  │  │  │  │  │  ├─ embedding.py
│  │  │  │  │  │  ├─ image.py
│  │  │  │  │  │  ├─ llm.py
│  │  │  │  │  │  └─ reranker.py
│  │  │  │  │  └─ ollama_model_provider.py
│  │  │  │  ├─ openai_model_provider
│  │  │  │  │  ├─ __init__.py
│  │  │  │  │  ├─ credential
│  │  │  │  │  │  ├─ embedding.py
│  │  │  │  │  │  ├─ image.py
│  │  │  │  │  │  ├─ llm.py
│  │  │  │  │  │  ├─ stt.py
│  │  │  │  │  │  ├─ tti.py
│  │  │  │  │  │  └─ tts.py
│  │  │  │  │  ├─ icon
│  │  │  │  │  │  └─ openai_icon_svg
│  │  │  │  │  ├─ model
│  │  │  │  │  │  ├─ embedding.py
│  │  │  │  │  │  ├─ image.py
│  │  │  │  │  │  ├─ llm.py
│  │  │  │  │  │  ├─ stt.py
│  │  │  │  │  │  ├─ tti.py
│  │  │  │  │  │  └─ tts.py
│  │  │  │  │  └─ openai_model_provider.py
│  │  │  │  ├─ qwen_model_provider
│  │  │  │  │  ├─ __init__.py
│  │  │  │  │  ├─ credential
│  │  │  │  │  │  ├─ image.py
│  │  │  │  │  │  ├─ llm.py
│  │  │  │  │  │  └─ tti.py
│  │  │  │  │  ├─ icon
│  │  │  │  │  │  └─ qwen_icon_svg
│  │  │  │  │  ├─ model
│  │  │  │  │  │  ├─ image.py
│  │  │  │  │  │  ├─ llm.py
│  │  │  │  │  │  └─ tti.py
│  │  │  │  │  └─ qwen_model_provider.py
│  │  │  │  ├─ regolo_model_provider
│  │  │  │  │  ├─ __init__.py
│  │  │  │  │  ├─ credential
│  │  │  │  │  │  ├─ embedding.py
│  │  │  │  │  │  ├─ image.py
│  │  │  │  │  │  ├─ llm.py
│  │  │  │  │  │  └─ tti.py
│  │  │  │  │  ├─ icon
│  │  │  │  │  │  └─ regolo_icon_svg
│  │  │  │  │  ├─ model
│  │  │  │  │  │  ├─ embedding.py
│  │  │  │  │  │  ├─ image.py
│  │  │  │  │  │  ├─ llm.py
│  │  │  │  │  │  └─ tti.py
│  │  │  │  │  └─ regolo_model_provider.py
│  │  │  │  ├─ siliconCloud_model_provider
│  │  │  │  │  ├─ __init__.py
│  │  │  │  │  ├─ credential
│  │  │  │  │  │  ├─ embedding.py
│  │  │  │  │  │  ├─ image.py
│  │  │  │  │  │  ├─ llm.py
│  │  │  │  │  │  ├─ reranker.py
│  │  │  │  │  │  ├─ stt.py
│  │  │  │  │  │  ├─ tti.py
│  │  │  │  │  │  └─ tts.py
│  │  │  │  │  ├─ icon
│  │  │  │  │  │  └─ siliconCloud_icon_svg
│  │  │  │  │  ├─ model
│  │  │  │  │  │  ├─ embedding.py
│  │  │  │  │  │  ├─ image.py
│  │  │  │  │  │  ├─ llm.py
│  │  │  │  │  │  ├─ reranker.py
│  │  │  │  │  │  ├─ stt.py
│  │  │  │  │  │  ├─ tti.py
│  │  │  │  │  │  └─ tts.py
│  │  │  │  │  └─ siliconCloud_model_provider.py
│  │  │  │  ├─ tencent_cloud_model_provider
│  │  │  │  │  ├─ __init__.py
│  │  │  │  │  ├─ credential
│  │  │  │  │  │  └─ llm.py
│  │  │  │  │  ├─ icon
│  │  │  │  │  │  └─ tencent_cloud_icon_svg
│  │  │  │  │  ├─ model
│  │  │  │  │  │  └─ llm.py
│  │  │  │  │  └─ tencent_cloud_model_provider.py
│  │  │  │  ├─ tencent_model_provider
│  │  │  │  │  ├─ __init__.py
│  │  │  │  │  ├─ credential
│  │  │  │  │  │  ├─ embedding.py
│  │  │  │  │  │  ├─ image.py
│  │  │  │  │  │  ├─ llm.py
│  │  │  │  │  │  └─ tti.py
│  │  │  │  │  ├─ icon
│  │  │  │  │  │  └─ tencent_icon_svg
│  │  │  │  │  ├─ model
│  │  │  │  │  │  ├─ embedding.py
│  │  │  │  │  │  ├─ hunyuan.py
│  │  │  │  │  │  ├─ image.py
│  │  │  │  │  │  ├─ llm.py
│  │  │  │  │  │  └─ tti.py
│  │  │  │  │  └─ tencent_model_provider.py
│  │  │  │  ├─ vllm_model_provider
│  │  │  │  │  ├─ __init__.py
│  │  │  │  │  ├─ credential
│  │  │  │  │  │  ├─ embedding.py
│  │  │  │  │  │  ├─ image.py
│  │  │  │  │  │  └─ llm.py
│  │  │  │  │  ├─ icon
│  │  │  │  │  │  └─ vllm_icon_svg
│  │  │  │  │  ├─ model
│  │  │  │  │  │  ├─ embedding.py
│  │  │  │  │  │  ├─ image.py
│  │  │  │  │  │  └─ llm.py
│  │  │  │  │  └─ vllm_model_provider.py
│  │  │  │  ├─ volcanic_engine_model_provider
│  │  │  │  │  ├─ __init__.py
│  │  │  │  │  ├─ credential
│  │  │  │  │  │  ├─ embedding.py
│  │  │  │  │  │  ├─ image.py
│  │  │  │  │  │  ├─ llm.py
│  │  │  │  │  │  ├─ stt.py
│  │  │  │  │  │  ├─ tti.py
│  │  │  │  │  │  └─ tts.py
│  │  │  │  │  ├─ icon
│  │  │  │  │  │  └─ volcanic_engine_icon_svg
│  │  │  │  │  ├─ model
│  │  │  │  │  │  ├─ embedding.py
│  │  │  │  │  │  ├─ iat_mp3_16k.mp3
│  │  │  │  │  │  ├─ image.py
│  │  │  │  │  │  ├─ llm.py
│  │  │  │  │  │  ├─ stt.py
│  │  │  │  │  │  ├─ tti.py
│  │  │  │  │  │  └─ tts.py
│  │  │  │  │  └─ volcanic_engine_model_provider.py
│  │  │  │  ├─ wenxin_model_provider
│  │  │  │  │  ├─ __init__.py
│  │  │  │  │  ├─ credential
│  │  │  │  │  │  ├─ embedding.py
│  │  │  │  │  │  └─ llm.py
│  │  │  │  │  ├─ icon
│  │  │  │  │  │  └─ azure_icon_svg
│  │  │  │  │  ├─ model
│  │  │  │  │  │  ├─ embedding.py
│  │  │  │  │  │  └─ llm.py
│  │  │  │  │  └─ wenxin_model_provider.py
│  │  │  │  ├─ xf_model_provider
│  │  │  │  │  ├─ __init__.py
│  │  │  │  │  ├─ credential
│  │  │  │  │  │  ├─ embedding.py
│  │  │  │  │  │  ├─ image.py
│  │  │  │  │  │  ├─ img_1.png
│  │  │  │  │  │  ├─ llm.py
│  │  │  │  │  │  ├─ stt.py
│  │  │  │  │  │  └─ tts.py
│  │  │  │  │  ├─ icon
│  │  │  │  │  │  └─ xf_icon_svg
│  │  │  │  │  ├─ model
│  │  │  │  │  │  ├─ embedding.py
│  │  │  │  │  │  ├─ iat_mp3_16k.mp3
│  │  │  │  │  │  ├─ image.py
│  │  │  │  │  │  ├─ img_1.png
│  │  │  │  │  │  ├─ llm.py
│  │  │  │  │  │  ├─ stt.py
│  │  │  │  │  │  └─ tts.py
│  │  │  │  │  └─ xf_model_provider.py
│  │  │  │  ├─ xinference_model_provider
│  │  │  │  │  ├─ __init__.py
│  │  │  │  │  ├─ credential
│  │  │  │  │  │  ├─ embedding.py
│  │  │  │  │  │  ├─ image.py
│  │  │  │  │  │  ├─ llm.py
│  │  │  │  │  │  ├─ reranker.py
│  │  │  │  │  │  ├─ stt.py
│  │  │  │  │  │  ├─ tti.py
│  │  │  │  │  │  └─ tts.py
│  │  │  │  │  ├─ icon
│  │  │  │  │  │  └─ xinference_icon_svg
│  │  │  │  │  ├─ model
│  │  │  │  │  │  ├─ embedding.py
│  │  │  │  │  │  ├─ image.py
│  │  │  │  │  │  ├─ llm.py
│  │  │  │  │  │  ├─ reranker.py
│  │  │  │  │  │  ├─ stt.py
│  │  │  │  │  │  ├─ tti.py
│  │  │  │  │  │  └─ tts.py
│  │  │  │  │  └─ xinference_model_provider.py
│  │  │  │  └─ zhipu_model_provider
│  │  │  │     ├─ __init__.py
│  │  │  │     ├─ credential
│  │  │  │     │  ├─ image.py
│  │  │  │     │  ├─ llm.py
│  │  │  │     │  └─ tti.py
│  │  │  │     ├─ icon
│  │  │  │     │  └─ zhipuai_icon_svg
│  │  │  │     ├─ model
│  │  │  │     │  ├─ image.py
│  │  │  │     │  ├─ llm.py
│  │  │  │     │  └─ tti.py
│  │  │  │     └─ zhipu_model_provider.py
│  │  │  └─ tools.py
│  │  ├─ serializers
│  │  │  ├─ model_apply_serializers.py
│  │  │  ├─ provider_serializers.py
│  │  │  ├─ system_setting.py
│  │  │  ├─ team_serializers.py
│  │  │  └─ valid_serializers.py
│  │  ├─ sql
│  │  │  ├─ check_member_permission_target_exists.sql
│  │  │  ├─ get_member_permission.sql
│  │  │  └─ get_user_permission.sql
│  │  ├─ swagger_api
│  │  │  ├─ provide_api.py
│  │  │  ├─ system_setting.py
│  │  │  └─ valid_api.py
│  │  ├─ tests.py
│  │  ├─ urls.py
│  │  └─ views
│  │     ├─ Team.py
│  │     ├─ __init__.py
│  │     ├─ common.py
│  │     ├─ model.py
│  │     ├─ model_apply.py
│  │     ├─ system_setting.py
│  │     └─ valid.py
│  ├─ smartdoc
│  │  ├─ __init__.py
│  │  ├─ asgi.py
│  │  ├─ conf.py
│  │  ├─ const.py
│  │  ├─ settings
│  │  │  ├─ __init__.py
│  │  │  ├─ auth.py
│  │  │  ├─ base.py
│  │  │  ├─ lib.py
│  │  │  └─ logging.py
│  │  ├─ urls.py
│  │  └─ wsgi.py
│  ├─ static
│  │  ├─ drf-yasg
│  │  │  ├─ README
│  │  │  ├─ immutable.js
│  │  │  ├─ immutable.min.js
│  │  │  ├─ insQ.js
│  │  │  ├─ insQ.min.js
│  │  │  ├─ redoc
│  │  │  │  ├─ LICENSE
│  │  │  │  ├─ redoc-logo.png
│  │  │  │  ├─ redoc.min.js
│  │  │  │  └─ redoc.standalone.js.map
│  │  │  ├─ redoc-init.js
│  │  │  ├─ redoc-old
│  │  │  │  ├─ LICENSE
│  │  │  │  ├─ redoc.min.js
│  │  │  │  └─ redoc.min.js.map
│  │  │  ├─ style.css
│  │  │  └─ swagger-ui-init.js
│  │  └─ rest_framework
│  │     ├─ css
│  │     │  ├─ bootstrap-theme.min.css
│  │     │  ├─ bootstrap-theme.min.css.map
│  │     │  ├─ bootstrap-tweaks.css
│  │     │  ├─ bootstrap.min.css
│  │     │  ├─ bootstrap.min.css.map
│  │     │  ├─ default.css
│  │     │  ├─ font-awesome-4.0.3.css
│  │     │  └─ prettify.css
│  │     ├─ docs
│  │     │  ├─ css
│  │     │  │  ├─ base.css
│  │     │  │  ├─ highlight.css
│  │     │  │  └─ jquery.json-view.min.css
│  │     │  ├─ img
│  │     │  │  ├─ favicon.ico
│  │     │  │  └─ grid.png
│  │     │  └─ js
│  │     │     ├─ api.js
│  │     │     ├─ highlight.pack.js
│  │     │     └─ jquery.json-view.min.js
│  │     ├─ fonts
│  │     │  ├─ fontawesome-webfont.eot
│  │     │  ├─ fontawesome-webfont.svg
│  │     │  ├─ fontawesome-webfont.ttf
│  │     │  ├─ fontawesome-webfont.woff
│  │     │  ├─ glyphicons-halflings-regular.eot
│  │     │  ├─ glyphicons-halflings-regular.svg
│  │     │  ├─ glyphicons-halflings-regular.ttf
│  │     │  ├─ glyphicons-halflings-regular.woff
│  │     │  └─ glyphicons-halflings-regular.woff2
│  │     ├─ img
│  │     │  ├─ glyphicons-halflings-white.png
│  │     │  ├─ glyphicons-halflings.png
│  │     │  └─ grid.png
│  │     └─ js
│  │        ├─ ajax-form.js
│  │        ├─ bootstrap.min.js
│  │        ├─ coreapi-0.1.1.js
│  │        ├─ csrf.js
│  │        ├─ default.js
│  │        ├─ jquery-3.7.1.min.js
│  │        ├─ load-ajax-form.js
│  │        └─ prettify-min.js
│  └─ users
│     ├─ __init__.py
│     ├─ apps.py
│     ├─ migrations
│     │  ├─ 0001_initial.py
│     │  ├─ 0002_user_create_time_user_update_time.py
│     │  ├─ 0003_user_source.py
│     │  ├─ 0004_alter_user_email.py
│     │  ├─ 0005_user_language.py
│     │  └─ __init__.py
│     ├─ serializers
│     │  └─ user_serializers.py
│     ├─ task
│     │  └─ __init__.py
│     ├─ urls.py
│     └─ views
│        ├─ __init__.py
│        ├─ common.py
│        └─ user.py
├─ config_example.yml
├─ installer
│  ├─ Dockerfile
│  ├─ Dockerfile-python-pg
│  ├─ Dockerfile-vector-model
│  ├─ config.yaml
│  ├─ init.sql
│  ├─ install_model.py
│  ├─ run-maxkb.sh
│  └─ start-maxkb.sh
├─ logs
│  └─ celery
│     ├─ 0
│     │  ├─ 1
│     │  ├─ 2
│     │  ├─ 4
│     │  ├─ 5
│     │  ├─ 8
│     │  ├─ 9
│     │  ├─ a
│     │  ├─ b
│     │  └─ c
│     ├─ 1
│     │  ├─ 1
│     │  ├─ 2
│     │  ├─ 5
│     │  ├─ 6
│     │  ├─ a
│     │  ├─ b
│     │  ├─ d
│     │  └─ e
│     ├─ 2
│     │  ├─ 0
│     │  ├─ 2
│     │  ├─ 3
│     │  ├─ 5
│     │  ├─ 6
│     │  ├─ 7
│     │  ├─ b
│     │  ├─ d
│     │  ├─ e
│     │  └─ f
│     ├─ 3
│     │  ├─ 1
│     │  ├─ 3
│     │  ├─ 4
│     │  ├─ 5
│     │  ├─ 7
│     │  ├─ 9
│     │  ├─ a
│     │  ├─ b
│     │  ├─ d
│     │  └─ e
│     ├─ 4
│     │  ├─ 0
│     │  ├─ 1
│     │  ├─ 3
│     │  ├─ 4
│     │  ├─ 5
│     │  ├─ 6
│     │  ├─ a
│     │  ├─ c
│     │  ├─ d
│     │  └─ e
│     ├─ 5
│     │  ├─ 3
│     │  ├─ 4
│     │  ├─ 6
│     │  ├─ 7
│     │  ├─ 8
│     │  ├─ a
│     │  ├─ e
│     │  └─ f
│     ├─ 6
│     │  ├─ 1
│     │  ├─ 2
│     │  ├─ 4
│     │  ├─ 5
│     │  ├─ 6
│     │  ├─ 7
│     │  ├─ 8
│     │  ├─ 9
│     │  ├─ a
│     │  ├─ b
│     │  ├─ c
│     │  └─ e
│     ├─ 7
│     │  ├─ 0
│     │  ├─ 2
│     │  ├─ 4
│     │  ├─ 5
│     │  ├─ 6
│     │  ├─ 7
│     │  ├─ 8
│     │  ├─ 9
│     │  ├─ a
│     │  ├─ b
│     │  ├─ c
│     │  ├─ d
│     │  ├─ e
│     │  └─ f
│     ├─ 8
│     │  ├─ 3
│     │  ├─ 5
│     │  ├─ 8
│     │  ├─ d
│     │  ├─ e
│     │  └─ f
│     ├─ 9
│     │  ├─ 1
│     │  ├─ 4
│     │  ├─ 6
│     │  ├─ 7
│     │  ├─ a
│     │  └─ c
│     ├─ a
│     │  ├─ 1
│     │  ├─ 2
│     │  ├─ 3
│     │  ├─ 5
│     │  ├─ 6
│     │  ├─ 7
│     │  ├─ 8
│     │  ├─ a
│     │  ├─ b
│     │  ├─ c
│     │  ├─ d
│     │  ├─ e
│     │  └─ f
│     ├─ b
│     │  ├─ 1
│     │  ├─ 3
│     │  ├─ 4
│     │  ├─ 5
│     │  ├─ 6
│     │  ├─ 7
│     │  ├─ 8
│     │  ├─ 9
│     │  └─ f
│     ├─ c
│     │  ├─ 1
│     │  ├─ 4
│     │  ├─ 6
│     │  ├─ 7
│     │  ├─ 8
│     │  ├─ 9
│     │  ├─ b
│     │  ├─ c
│     │  └─ d
│     ├─ d
│     │  ├─ 1
│     │  ├─ 3
│     │  ├─ 5
│     │  ├─ 7
│     │  ├─ 9
│     │  ├─ a
│     │  ├─ b
│     │  ├─ c
│     │  ├─ d
│     │  └─ e
│     ├─ e
│     │  ├─ 0
│     │  ├─ 2
│     │  ├─ 4
│     │  ├─ 6
│     │  ├─ 7
│     │  ├─ 9
│     │  ├─ d
│     │  ├─ e
│     │  └─ f
│     └─ f
│        ├─ 0
│        ├─ 2
│        ├─ 3
│        ├─ 5
│        ├─ 6
│        ├─ 7
│        ├─ 9
│        ├─ a
│        ├─ b
│        ├─ d
│        └─ f
├─ main.py
├─ package-lock.json
├─ pyproject.toml
└─ ui
   ├─ .eslintrc.cjs
   ├─ .prettierrc.json
   ├─ README.md
   ├─ env.d.ts
   ├─ index.html
   ├─ package-lock.json
   ├─ package.json
   ├─ public
   │  ├─ MaxKB.gif
   │  ├─ favicon.ico
   │  └─ fx
   │     ├─ bochaai
   │     │  ├─ detail.md
   │     │  └─ icon.png
   │     ├─ google_search
   │     │  ├─ detail.md
   │     │  └─ icon.png
   │     ├─ img
   │     │  ├─ MySQL_app_used.jpg
   │     │  ├─ MySQL_setting.jpg
   │     │  ├─ PostgreSQL_app_used.jpg
   │     │  ├─ PostgreSQL_setting.jpg
   │     │  ├─ bocha_APIKey.jpg
   │     │  ├─ bocha_app_used.jpg
   │     │  ├─ bocha_setting.jpg
   │     │  ├─ google_APIKey.jpg
   │     │  ├─ google_AddSearchEngine.jpg
   │     │  ├─ google_app_used.jpg
   │     │  ├─ google_cx.jpg
   │     │  ├─ google_setting.jpg
   │     │  ├─ langsearch_APIKey.jpg
   │     │  ├─ langsearch_app_used.jpg
   │     │  └─ langsearch_setting.jpg
   │     ├─ langsearch
   │     │  ├─ detail.md
   │     │  └─ icon.png
   │     ├─ mysql
   │     │  ├─ detail.md
   │     │  └─ icon.png
   │     └─ postgresql
   │        ├─ detail.md
   │        └─ icon.png
   ├─ src
   │  ├─ App.vue
   │  ├─ api
   │  │  ├─ application-overview.ts
   │  │  ├─ application-xpack.ts
   │  │  ├─ application.ts
   │  │  ├─ auth-setting.ts
   │  │  ├─ document.ts
   │  │  ├─ email-setting.ts
   │  │  ├─ function-lib.ts
   │  │  ├─ image.ts
   │  │  ├─ license.ts
   │  │  ├─ log.ts
   │  │  ├─ model.ts
   │  │  ├─ operate-log.ts
   │  │  ├─ paragraph.ts
   │  │  ├─ platform-source.ts
   │  │  ├─ problem.ts
   │  │  ├─ provider.ts
   │  │  ├─ system-api-key.ts
   │  │  ├─ team.ts
   │  │  ├─ theme.ts
   │  │  ├─ type
   │  │  │  ├─ application.ts
   │  │  │  ├─ common.ts
   │  │  │  ├─ function-lib.ts
   │  │  │  ├─ model.ts
   │  │  │  ├─ team.ts
   │  │  │  └─ user.ts
   │  │  ├─ user-manage.ts
   │  │  └─ user.ts
   │  ├─ assets
   │  │  ├─ 404.png
   │  │  ├─ acoustic-color.svg
   │  │  ├─ acoustic.svg
   │  │  ├─ display-bg1.png
   │  │  ├─ display-bg2.png
   │  │  ├─ display-bg3.png
   │  │  ├─ fileType
   │  │  │  ├─ csv-icon.svg
   │  │  │  ├─ doc-icon.svg
   │  │  │  ├─ docx-icon.svg
   │  │  │  ├─ file-icon.svg
   │  │  │  ├─ html-icon.svg
   │  │  │  ├─ md-icon.svg
   │  │  │  ├─ pdf-icon.svg
   │  │  │  ├─ txt-icon.svg
   │  │  │  ├─ unknown-icon.svg
   │  │  │  ├─ xls-icon.svg
   │  │  │  ├─ xlsx-icon.svg
   │  │  │  └─ zip-icon.svg
   │  │  ├─ hit-test-empty.png
   │  │  ├─ icon_and.svg
   │  │  ├─ icon_assigner.svg
   │  │  ├─ icon_condition.svg
   │  │  ├─ icon_docs.svg
   │  │  ├─ icon_document.svg
   │  │  ├─ icon_file-audio.svg
   │  │  ├─ icon_file-doc.svg
   │  │  ├─ icon_file-folder_colorful.svg
   │  │  ├─ icon_file-image.svg
   │  │  ├─ icon_form.svg
   │  │  ├─ icon_function_outlined.svg
   │  │  ├─ icon_globe_color.svg
   │  │  ├─ icon_hi.svg
   │  │  ├─ icon_image.svg
   │  │  ├─ icon_mcp.svg
   │  │  ├─ icon_or.svg
   │  │  ├─ icon_qr_outlined.svg
   │  │  ├─ icon_reply.svg
   │  │  ├─ icon_reranker.svg
   │  │  ├─ icon_robot.svg
   │  │  ├─ icon_send.svg
   │  │  ├─ icon_send_colorful.svg
   │  │  ├─ icon_setting.svg
   │  │  ├─ icon_speech_to_text.svg
   │  │  ├─ icon_start.svg
   │  │  ├─ icon_text-image.svg
   │  │  ├─ icon_text_to_speech.svg
   │  │  ├─ icon_web.svg
   │  │  ├─ load_error.png
   │  │  ├─ logo
   │  │  │  ├─ MaxKB-logo-currentColor.svg
   │  │  │  ├─ MaxKB-logo.svg
   │  │  │  ├─ logo-currentColor.svg
   │  │  │  └─ logo.svg
   │  │  ├─ logo_dingtalk.svg
   │  │  ├─ logo_lark.svg
   │  │  ├─ logo_slack.svg
   │  │  ├─ logo_wechat-work.svg
   │  │  ├─ logo_wechat.svg
   │  │  ├─ sort.svg
   │  │  ├─ theme
   │  │  │  ├─ default.jpg
   │  │  │  ├─ default_back.jpg
   │  │  │  ├─ green.jpg
   │  │  │  ├─ orange.jpg
   │  │  │  ├─ purple.jpg
   │  │  │  └─ red.jpg
   │  │  ├─ tipIMG.jpg
   │  │  ├─ upload-icon.svg
   │  │  ├─ user-icon.svg
   │  │  ├─ window1.png
   │  │  ├─ window2.png
   │  │  └─ window3.png
   │  ├─ bus
   │  │  └─ index.ts
   │  ├─ components
   │  │  ├─ ai-chat
   │  │  │  ├─ ExecutionDetailDialog.vue
   │  │  │  ├─ KnowledgeSource.vue
   │  │  │  ├─ ParagraphSourceDialog.vue
   │  │  │  ├─ component
   │  │  │  │  ├─ ParagraphCard.vue
   │  │  │  │  ├─ answer-content
   │  │  │  │  │  └─ index.vue
   │  │  │  │  ├─ chat-input-operate
   │  │  │  │  │  ├─ TouchChat.vue
   │  │  │  │  │  └─ index.vue
   │  │  │  │  ├─ control
   │  │  │  │  │  └─ index.vue
   │  │  │  │  ├─ operation-button
   │  │  │  │  │  ├─ ChatOperationButton.vue
   │  │  │  │  │  ├─ LogOperationButton.vue
   │  │  │  │  │  └─ index.vue
   │  │  │  │  ├─ prologue-content
   │  │  │  │  │  └─ index.vue
   │  │  │  │  ├─ question-content
   │  │  │  │  │  └─ index.vue
   │  │  │  │  ├─ transition-content
   │  │  │  │  │  └─ index.vue
   │  │  │  │  └─ user-form
   │  │  │  │     └─ index.vue
   │  │  │  ├─ index.scss
   │  │  │  └─ index.vue
   │  │  ├─ app-avatar
   │  │  │  └─ index.vue
   │  │  ├─ app-charts
   │  │  │  ├─ components
   │  │  │  │  └─ LineCharts.vue
   │  │  │  └─ index.vue
   │  │  ├─ app-table
   │  │  │  └─ index.vue
   │  │  ├─ auto-tooltip
   │  │  │  └─ index.vue
   │  │  ├─ back-button
   │  │  │  └─ index.vue
   │  │  ├─ card-add
   │  │  │  └─ index.vue
   │  │  ├─ card-box
   │  │  │  └─ index.vue
   │  │  ├─ card-checkbox
   │  │  │  └─ index.vue
   │  │  ├─ codemirror-editor
   │  │  │  └─ index.vue
   │  │  ├─ common-list
   │  │  │  └─ index.vue
   │  │  ├─ dynamics-form
   │  │  │  ├─ Demo.vue
   │  │  │  ├─ DemoConstructor.vue
   │  │  │  ├─ FormItem.vue
   │  │  │  ├─ FormItemLabel.vue
   │  │  │  ├─ constructor
   │  │  │  │  ├─ index.vue
   │  │  │  │  └─ items
   │  │  │  │     ├─ DatePickerConstructor.vue
   │  │  │  │     ├─ JsonInputConstructor.vue
   │  │  │  │     ├─ MultiSelectConstructor.vue
   │  │  │  │     ├─ PasswordInputConstructor.vue
   │  │  │  │     ├─ RadioCardConstructor.vue
   │  │  │  │     ├─ RadioRowConstructor.vue
   │  │  │  │     ├─ SingleSelectConstructor.vue
   │  │  │  │     ├─ SliderConstructor.vue
   │  │  │  │     ├─ SwitchInputConstructor.vue
   │  │  │  │     └─ TextInputConstructor.vue
   │  │  │  ├─ index.ts
   │  │  │  ├─ index.vue
   │  │  │  ├─ items
   │  │  │  │  ├─ DatePicker.vue
   │  │  │  │  ├─ JsonInput.vue
   │  │  │  │  ├─ PasswordInput.vue
   │  │  │  │  ├─ TextInput.vue
   │  │  │  │  ├─ complex
   │  │  │  │  │  ├─ ArrayObjectCard.vue
   │  │  │  │  │  ├─ ObjectCard.vue
   │  │  │  │  │  └─ TabCard.vue
   │  │  │  │  ├─ label
   │  │  │  │  │  └─ TooltipLabel.vue
   │  │  │  │  ├─ radio
   │  │  │  │  │  ├─ Radio.vue
   │  │  │  │  │  ├─ RadioButton.vue
   │  │  │  │  │  ├─ RadioCard.vue
   │  │  │  │  │  └─ RadioRow.vue
   │  │  │  │  ├─ select
   │  │  │  │  │  ├─ MultiSelect.vue
   │  │  │  │  │  └─ SingleSelect.vue
   │  │  │  │  ├─ slider
   │  │  │  │  │  └─ Slider.vue
   │  │  │  │  ├─ switch
   │  │  │  │  │  └─ SwitchInput.vue
   │  │  │  │  └─ table
   │  │  │  │     ├─ ProgressTableItem.vue
   │  │  │  │     ├─ TableCheckbox.vue
   │  │  │  │     ├─ TableColumn.vue
   │  │  │  │     └─ TableRadio.vue
   │  │  │  └─ type.ts
   │  │  ├─ generate-related-dialog
   │  │  │  └─ index.vue
   │  │  ├─ icons
   │  │  │  ├─ AppIcon.vue
   │  │  │  └─ index.ts
   │  │  ├─ index.ts
   │  │  ├─ infinite-scroll
   │  │  │  └─ index.vue
   │  │  ├─ layout-container
   │  │  │  └─ index.vue
   │  │  ├─ loading
   │  │  │  └─ DownloadLoading.vue
   │  │  ├─ login-container
   │  │  │  └─ index.vue
   │  │  ├─ login-layout
   │  │  │  └─ index.vue
   │  │  ├─ logo
   │  │  │  ├─ LogoFull.vue
   │  │  │  ├─ LogoIcon.vue
   │  │  │  └─ SendIcon.vue
   │  │  ├─ markdown
   │  │  │  ├─ EchartsRander.vue
   │  │  │  ├─ FormRander.vue
   │  │  │  ├─ HtmlRander.vue
   │  │  │  ├─ MdEditor.vue
   │  │  │  ├─ MdEditorMagnify.vue
   │  │  │  ├─ MdPreview.vue
   │  │  │  ├─ MdRenderer.vue
   │  │  │  ├─ ReasoningRander.vue
   │  │  │  └─ assets
   │  │  │     └─ markdown-iconfont.js
   │  │  ├─ model-select
   │  │  │  └─ index.vue
   │  │  ├─ read-write
   │  │  │  └─ index.vue
   │  │  ├─ tag-ellipsis
   │  │  │  └─ index.vue
   │  │  └─ tags-input
   │  │     └─ index.vue
   │  ├─ directives
   │  │  ├─ clickoutside.ts
   │  │  ├─ hasPermission.ts
   │  │  ├─ index.ts
   │  │  ├─ infiniteScrollUp.ts
   │  │  └─ resize.ts
   │  ├─ enums
   │  │  ├─ application.ts
   │  │  ├─ common.ts
   │  │  ├─ document.ts
   │  │  ├─ model.ts
   │  │  ├─ team.ts
   │  │  └─ workflow.ts
   │  ├─ layout
   │  │  ├─ components
   │  │  │  ├─ app-header
   │  │  │  │  └─ index.vue
   │  │  │  ├─ app-main
   │  │  │  │  └─ index.vue
   │  │  │  ├─ breadcrumb
   │  │  │  │  └─ index.vue
   │  │  │  ├─ index.ts
   │  │  │  ├─ sidebar
   │  │  │  │  ├─ SidebarItem.vue
   │  │  │  │  └─ index.vue
   │  │  │  └─ top-bar
   │  │  │     ├─ avatar
   │  │  │     │  ├─ APIKeyDialog.vue
   │  │  │     │  ├─ AboutDialog.vue
   │  │  │     │  ├─ ResetPassword.vue
   │  │  │     │  └─ index.vue
   │  │  │     ├─ index.vue
   │  │  │     └─ top-menu
   │  │  │        ├─ MenuItem.vue
   │  │  │        └─ index.vue
   │  │  ├─ hooks
   │  │  │  └─ useResize.ts
   │  │  └─ layout-template
   │  │     ├─ AppLayout.vue
   │  │     ├─ DetailLayout.vue
   │  │     ├─ SystemLayout.vue
   │  │     └─ index.scss
   │  ├─ locales
   │  │  ├─ index.ts
   │  │  ├─ lang
   │  │  │  ├─ en-US
   │  │  │  │  ├─ ai-chat.ts
   │  │  │  │  ├─ common.ts
   │  │  │  │  ├─ components.ts
   │  │  │  │  ├─ dynamics-form.ts
   │  │  │  │  ├─ index.ts
   │  │  │  │  ├─ layout.ts
   │  │  │  │  └─ views
   │  │  │  │     ├─ 404.ts
   │  │  │  │     ├─ application-overview.ts
   │  │  │  │     ├─ application-workflow.ts
   │  │  │  │     ├─ application.ts
   │  │  │  │     ├─ document.ts
   │  │  │  │     ├─ function-lib.ts
   │  │  │  │     ├─ index.ts
   │  │  │  │     ├─ log.ts
   │  │  │  │     ├─ login.ts
   │  │  │  │     ├─ operate-log.ts
   │  │  │  │     ├─ paragraph.ts
   │  │  │  │     ├─ problem.ts
   │  │  │  │     ├─ system.ts
   │  │  │  │     ├─ team.ts
   │  │  │  │     ├─ template.ts
   │  │  │  │     └─ user.ts
   │  │  │  ├─ zh-CN
   │  │  │  │  ├─ ai-chat.ts
   │  │  │  │  ├─ common.ts
   │  │  │  │  ├─ components.ts
   │  │  │  │  ├─ dynamics-form.ts
   │  │  │  │  ├─ index.ts
   │  │  │  │  ├─ layout.ts
   │  │  │  │  └─ views
   │  │  │  │     ├─ 404.ts
   │  │  │  │     ├─ application-overview.ts
   │  │  │  │     ├─ application-workflow.ts
   │  │  │  │     ├─ application.ts
   │  │  │  │     ├─ document.ts
   │  │  │  │     ├─ function-lib.ts
   │  │  │  │     ├─ index.ts
   │  │  │  │     ├─ log.ts
   │  │  │  │     ├─ login.ts
   │  │  │  │     ├─ operate-log.ts
   │  │  │  │     ├─ paragraph.ts
   │  │  │  │     ├─ problem.ts
   │  │  │  │     ├─ system.ts
   │  │  │  │     ├─ team.ts
   │  │  │  │     ├─ template.ts
   │  │  │  │     └─ user.ts
   │  │  │  └─ zh-Hant
   │  │  │     ├─ ai-chat.ts
   │  │  │     ├─ common.ts
   │  │  │     ├─ components.ts
   │  │  │     ├─ dynamics-form.ts
   │  │  │     ├─ index.ts
   │  │  │     ├─ layout.ts
   │  │  │     └─ views
   │  │  │        ├─ 404.ts
   │  │  │        ├─ application-overview.ts
   │  │  │        ├─ application-workflow.ts
   │  │  │        ├─ application.ts
   │  │  │        ├─ document.ts
   │  │  │        ├─ function-lib.ts
   │  │  │        ├─ index.ts
   │  │  │        ├─ log.ts
   │  │  │        ├─ login.ts
   │  │  │        ├─ operate-log.ts
   │  │  │        ├─ paragraph.ts
   │  │  │        ├─ problem.ts
   │  │  │        ├─ system.ts
   │  │  │        ├─ team.ts
   │  │  │        ├─ template.ts
   │  │  │        └─ user.ts
   │  │  └─ useLocale.ts
   │  ├─ main.ts
   │  ├─ request
   │  │  ├─ Result.ts
   │  │  └─ index.ts
   │  ├─ router
   │  │  ├─ index.ts
   │  │  ├─ modules
   │  │  │  ├─ application.ts
   │  │  │  ├─ function-lib.ts
   │  │  │  └─ setting.ts
   │  │  └─ routes.ts
   │  ├─ stores
   │  │  ├─ index.ts
   │  │  └─ modules
   │  │     ├─ application.ts
   │  │     ├─ common.ts
   │  │     ├─ document.ts
   │  │     ├─ log.ts
   │  │     ├─ model.ts
   │  │     ├─ paragraph.ts
   │  │     ├─ problem.ts
   │  │     ├─ prompt.ts
   │  │     └─ user.ts
   │  ├─ styles
   │  │  ├─ app.scss
   │  │  ├─ element-plus.scss
   │  │  ├─ font
   │  │  │  ├─ AlibabaPuHuiTi-3-55-Regular.eot
   │  │  │  ├─ AlibabaPuHuiTi-3-55-Regular.otf
   │  │  │  ├─ AlibabaPuHuiTi-3-55-Regular.ttf
   │  │  │  ├─ AlibabaPuHuiTi-3-55-Regular.woff
   │  │  │  └─ AlibabaPuHuiTi-3-55-Regular.woff2
   │  │  ├─ index.scss
   │  │  ├─ md-editor.scss
   │  │  └─ variables.scss
   │  ├─ utils
   │  │  ├─ application.ts
   │  │  ├─ clipboard.ts
   │  │  ├─ common.ts
   │  │  ├─ decimalFormat.ts
   │  │  ├─ message.ts
   │  │  ├─ permission
   │  │  │  ├─ index.ts
   │  │  │  └─ type.ts
   │  │  ├─ status.ts
   │  │  ├─ theme.ts
   │  │  ├─ time.ts
   │  │  └─ utils.ts
   │  ├─ views
   │  │  ├─ 404
   │  │  │  └─ index.vue
   │  │  ├─ application
   │  │  │  ├─ ApplicationAccess.vue
   │  │  │  ├─ ApplicationSetting.vue
   │  │  │  ├─ component
   │  │  │  │  ├─ AIModeParamSettingDialog.vue
   │  │  │  │  ├─ AccessSettingDrawer.vue
   │  │  │  │  ├─ AddDatasetDialog.vue
   │  │  │  │  ├─ CopyApplicationDialog.vue
   │  │  │  │  ├─ CreateApplicationDialog.vue
   │  │  │  │  ├─ McpServersDialog.vue
   │  │  │  │  ├─ ParamSettingDialog.vue
   │  │  │  │  ├─ ReasoningParamSettingDialog.vue
   │  │  │  │  └─ TTSModeParamSettingDialog.vue
   │  │  │  └─ index.vue
   │  │  ├─ application-overview
   │  │  │  ├─ component
   │  │  │  │  ├─ APIKeyDialog.vue
   │  │  │  │  ├─ DisplaySettingDialog.vue
   │  │  │  │  ├─ EditAvatarDialog.vue
   │  │  │  │  ├─ EmbedDialog.vue
   │  │  │  │  ├─ LimitDialog.vue
   │  │  │  │  ├─ SettingAPIKeyDialog.vue
   │  │  │  │  ├─ StatisticsCharts.vue
   │  │  │  │  └─ XPackDisplaySettingDialog.vue
   │  │  │  └─ index.vue
   │  │  ├─ application-workflow
   │  │  │  ├─ component
   │  │  │  │  ├─ DropdownMenu.vue
   │  │  │  │  └─ PublishHistory.vue
   │  │  │  └─ index.vue
   │  │  ├─ authentication
   │  │  │  ├─ component
   │  │  │  │  ├─ CAS.vue
   │  │  │  │  ├─ EditModal.vue
   │  │  │  │  ├─ LDAP.vue
   │  │  │  │  ├─ OAuth2.vue
   │  │  │  │  ├─ OIDC.vue
   │  │  │  │  └─ SCAN.vue
   │  │  │  └─ index.vue
   │  │  ├─ chat
   │  │  │  ├─ auth
   │  │  │  │  ├─ component
   │  │  │  │  │  └─ password.vue
   │  │  │  │  └─ index.vue
   │  │  │  ├─ base
   │  │  │  │  └─ index.vue
   │  │  │  ├─ embed
   │  │  │  │  └─ index.vue
   │  │  │  ├─ index.vue
   │  │  │  ├─ mobile
   │  │  │  │  └─ index.vue
   │  │  │  └─ pc
   │  │  │     ├─ EditTitleDialog.vue
   │  │  │     └─ index.vue
   │  │  ├─ document
   │  │  │  ├─ component
   │  │  │  │  ├─ EmbeddingContentDialog.vue
   │  │  │  │  ├─ ImportDocumentDialog.vue
   │  │  │  │  ├─ SelectDatasetDialog.vue
   │  │  │  │  ├─ Status.vue
   │  │  │  │  └─ StatusTable.vue
   │  │  │  └─ index.vue
   │  │  ├─ email
   │  │  │  └─ index.vue
   │  │  ├─ first
   │  │  │  └─ index.vue
   │  │  ├─ hit-test
   │  │  │  └─ index.vue
   │  │  ├─ log
   │  │  │  ├─ component
   │  │  │  │  ├─ ChatRecordDrawer.vue
   │  │  │  │  ├─ EditContentDialog.vue
   │  │  │  │  └─ EditMarkDialog.vue
   │  │  │  └─ index.vue
   │  │  ├─ login
   │  │  │  ├─ components
   │  │  │  │  ├─ QrCodeTab.vue
   │  │  │  │  ├─ dingtalkQrCode.vue
   │  │  │  │  ├─ larkQrCode.vue
   │  │  │  │  └─ wecomQrCode.vue
   │  │  │  ├─ forgot-password
   │  │  │  │  └─ index.vue
   │  │  │  ├─ index.vue
   │  │  │  ├─ register
   │  │  │  │  └─ index.vue
   │  │  │  └─ reset-password
   │  │  │     └─ index.vue
   │  │  ├─ operate-log
   │  │  │  ├─ component
   │  │  │  │  └─ DetailDialog.vue
   │  │  │  └─ index.vue
   │  │  ├─ paragraph
   │  │  │  ├─ component
   │  │  │  │  ├─ ParagraphDialog.vue
   │  │  │  │  ├─ ParagraphForm.vue
   │  │  │  │  ├─ ProblemComponent.vue
   │  │  │  │  └─ SelectDocumentDialog.vue
   │  │  │  └─ index.vue
   │  │  ├─ problem
   │  │  │  ├─ component
   │  │  │  │  ├─ CreateProblemDialog.vue
   │  │  │  │  ├─ DetailProblemDrawer.vue
   │  │  │  │  └─ RelateProblemDialog.vue
   │  │  │  └─ index.vue
   │  │  ├─ team
   │  │  │  ├─ component
   │  │  │  │  ├─ CreateMemberDialog.vue
   │  │  │  │  └─ PermissionSetting.vue
   │  │  │  └─ index.vue
   │  │  ├─ template
   │  │  │  ├─ component
   │  │  │  │  ├─ AddParamDrawer.vue
   │  │  │  │  ├─ CreateModelDialog.vue
   │  │  │  │  ├─ EditModel.vue
   │  │  │  │  ├─ ModelCard.vue
   │  │  │  │  ├─ ParamSettingDialog.vue
   │  │  │  │  └─ SelectProviderDialog.vue
   │  │  │  └─ index.vue
   │  │  ├─ theme
   │  │  │  ├─ LoginPreview.vue
   │  │  │  └─ index.vue
   │  │  └─ user-manage
   │  │     ├─ component
   │  │     │  ├─ UserDialog.vue
   │  │     │  └─ UserPwdDialog.vue
   │  │     └─ index.vue
   │  └─ workflow
   │     ├─ common
   │     │  ├─ AddFormCollect.vue
   │     │  ├─ CustomLine.vue
   │     │  ├─ EditFormCollect.vue
   │     │  ├─ NodeCascader.vue
   │     │  ├─ NodeContainer.vue
   │     │  ├─ NodeControl.vue
   │     │  ├─ app-node.ts
   │     │  ├─ edge.ts
   │     │  ├─ shortcut.ts
   │     │  ├─ teleport.ts
   │     │  └─ validate.ts
   │     ├─ icons
   │     │  ├─ ai-chat-node-icon.vue
   │     │  ├─ application-node-icon.vue
   │     │  ├─ base-node-icon.vue
   │     │  ├─ condition-node-icon.vue
   │     │  ├─ document-extract-node-icon.vue
   │     │  ├─ form-node-icon.vue
   │     │  ├─ function-lib-node-icon.vue
   │     │  ├─ function-node-icon.vue
   │     │  ├─ global-icon.vue
   │     │  ├─ image-generate-node-icon.vue
   │     │  ├─ image-understand-node-icon.vue
   │     │  ├─ mcp-node-icon.vue
   │     │  ├─ question-node-icon.vue
   │     │  ├─ reply-node-icon.vue
   │     │  ├─ reranker-node-icon.vue
   │     │  ├─ speech-to-text-node-icon.vue
   │     │  ├─ start-node-icon.vue
   │     │  ├─ text-to-speech-node-icon.vue
   │     │  ├─ utils.ts
   │     │  └─ variable-assign-node-icon.vue
   │     ├─ index.vue
   │     ├─ nodes
   │     │  ├─ ai-chat-node
   │     │  │  ├─ index.ts
   │     │  │  └─ index.vue
   │     │  ├─ application-node
   │     │  │  ├─ index.ts
   │     │  │  └─ index.vue
   │     │  ├─ base-node
   │     │  │  ├─ component
   │     │  │  │  ├─ ApiFieldFormDialog.vue
   │     │  │  │  ├─ ApiInputFieldTable.vue
   │     │  │  │  ├─ FileUploadSettingDialog.vue
   │     │  │  │  ├─ UserFieldFormDialog.vue
   │     │  │  │  ├─ UserInputFieldTable.vue
   │     │  │  │  └─ UserInputTitleDialog.vue
   │     │  │  ├─ index.ts
   │     │  │  └─ index.vue
   │     │  ├─ condition-node
   │     │  │  ├─ index.ts
   │     │  │  └─ index.vue
   │     │  ├─ document-extract-node
   │     │  │  ├─ index.ts
   │     │  │  └─ index.vue
   │     │  ├─ form-node
   │     │  │  ├─ index.ts
   │     │  │  └─ index.vue
   │     │  ├─ function-lib-node
   │     │  │  ├─ index.ts
   │     │  │  └─ index.vue
   │     │  ├─ function-node
   │     │  │  ├─ index.ts
   │     │  │  └─ index.vue
   │     │  ├─ image-generate
   │     │  │  ├─ index.ts
   │     │  │  └─ index.vue
   │     │  ├─ image-understand
   │     │  │  ├─ index.ts
   │     │  │  └─ index.vue
   │     │  ├─ mcp-node
   │     │  │  ├─ index.ts
   │     │  │  └─ index.vue
   │     │  ├─ question-node
   │     │  │  ├─ index.ts
   │     │  │  └─ index.vue
   │     │  ├─ reply-node
   │     │  │  ├─ index.ts
   │     │  │  └─ index.vue
   │     │  ├─ reranker-node
   │     │  │  ├─ ParamSettingDialog.vue
   │     │  │  ├─ index.ts
   │     │  │  └─ index.vue
   │     │  ├─ speech-to-text-node
   │     │  │  ├─ index.ts
   │     │  │  └─ index.vue
   │     │  ├─ start-node
   │     │  │  ├─ index.ts
   │     │  │  └─ index.vue
   │     │  ├─ text-to-speech-node
   │     │  │  ├─ index.ts
   │     │  │  └─ index.vue
   │     │  └─ variable-assign-node
   │     │     ├─ index.ts
   │     │     └─ index.vue
   │     └─ plugins
   │        └─ dagre.ts
   ├─ tsconfig.app.json
   ├─ tsconfig.json
   ├─ tsconfig.node.json
   ├─ tsconfig.vitest.json
   ├─ vite.config.ts
   └─ vitest.config.ts

```