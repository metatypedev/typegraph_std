from typegraph.importers.base.importer import Import
from typegraph.utils.sanitizers import inject_params
from typegraph import t
from box import Box
from typegraph.runtimes.http import HTTPRuntime


def import_ghes(params=None):
    target_url = inject_params("{protocol}://{hostname}/api/v3", params)
    ghes = HTTPRuntime(target_url)

    renames = {
        "global_hook": "_ghes_1_global_hook",
        "global_hook_2": "_ghes_2_global_hook_2",
        "public_key_full": "_ghes_3_public_key_full",
        "ldap_mapping_team": "_ghes_4_ldap_mapping_team",
        "ldap_mapping_user": "_ghes_5_ldap_mapping_user",
        "organization_simple": "_ghes_6_organization_simple",
        "pre_receive_environment": "_ghes_7_pre_receive_environment",
        "pre_receive_environment_download_status": "_ghes_8_pre_receive_environment_download_status",
        "pre_receive_hook": "_ghes_9_pre_receive_hook",
        "nullable_simple_user": "_ghes_10_nullable_simple_user",
        "app_permissions": "_ghes_11_app_permissions",
        "simple_user": "_ghes_12_simple_user",
        "nullable_scoped_installation": "_ghes_13_nullable_scoped_installation",
        "authorization": "_ghes_14_authorization",
        "integration": "_ghes_15_integration",
        "basic_error": "_ghes_16_basic_error",
        "validation_error_simple": "_ghes_17_validation_error_simple",
        "webhook_config_url": "_ghes_18_webhook_config_url",
        "webhook_config_content_type": "_ghes_19_webhook_config_content_type",
        "webhook_config_secret": "_ghes_20_webhook_config_secret",
        "webhook_config_insecure_ssl": "_ghes_21_webhook_config_insecure_ssl",
        "webhook_config": "_ghes_22_webhook_config",
        "enterprise": "_ghes_23_enterprise",
        "installation": "_ghes_24_installation",
        "nullable_license_simple": "_ghes_25_nullable_license_simple",
        "repository": "_ghes_26_repository",
        "installation_token": "_ghes_27_installation_token",
        "validation_error": "_ghes_28_validation_error",
        "application_grant": "_ghes_29_application_grant",
        "nullable_authorization": "_ghes_30_nullable_authorization",
        "code_of_conduct": "_ghes_31_code_of_conduct",
        "announcement_message": "_ghes_32_announcement_message",
        "announcement_expiration": "_ghes_33_announcement_expiration",
        "announcement": "_ghes_34_announcement",
        "license_info": "_ghes_35_license_info",
        "enterprise_repository_overview": "_ghes_36_enterprise_repository_overview",
        "enterprise_hook_overview": "_ghes_37_enterprise_hook_overview",
        "enterprise_page_overview": "_ghes_38_enterprise_page_overview",
        "enterprise_organization_overview": "_ghes_39_enterprise_organization_overview",
        "enterprise_user_overview": "_ghes_40_enterprise_user_overview",
        "enterprise_pull_request_overview": "_ghes_41_enterprise_pull_request_overview",
        "enterprise_issue_overview": "_ghes_42_enterprise_issue_overview",
        "enterprise_milestone_overview": "_ghes_43_enterprise_milestone_overview",
        "enterprise_gist_overview": "_ghes_44_enterprise_gist_overview",
        "enterprise_comment_overview": "_ghes_45_enterprise_comment_overview",
        "enterprise_overview": "_ghes_46_enterprise_overview",
        "enabled_organizations": "_ghes_47_enabled_organizations",
        "allowed_actions": "_ghes_48_allowed_actions",
        "selected_actions_url": "_ghes_49_selected_actions_url",
        "actions_enterprise_permissions": "_ghes_50_actions_enterprise_permissions",
        "selected_actions": "_ghes_51_selected_actions",
        "runner_groups_enterprise": "_ghes_52_runner_groups_enterprise",
        "runner_label": "_ghes_53_runner_label",
        "runner": "_ghes_54_runner",
        "runner_application": "_ghes_55_runner_application",
        "authentication_token": "_ghes_56_authentication_token",
        "actor": "_ghes_57_actor",
        "nullable_milestone": "_ghes_58_nullable_milestone",
        "nullable_integration": "_ghes_59_nullable_integration",
        "author_association": "_ghes_60_author_association",
        "reaction_rollup": "_ghes_61_reaction_rollup",
        "issue": "_ghes_62_issue",
        "issue_comment": "_ghes_63_issue_comment",
        "event": "_ghes_64_event",
        "link_with_type": "_ghes_65_link_with_type",
        "feed": "_ghes_66_feed",
        "base_gist": "_ghes_67_base_gist",
        "public_user": "_ghes_68_public_user",
        "gist_history": "_ghes_69_gist_history",
        "gist_simple": "_ghes_70_gist_simple",
        "gist_comment": "_ghes_71_gist_comment",
        "gist_commit": "_ghes_72_gist_commit",
        "gitignore_template": "_ghes_73_gitignore_template",
        "license_simple": "_ghes_74_license_simple",
        "license": "_ghes_75_license",
        "api_overview": "_ghes_76_api_overview",
        "nullable_repository": "_ghes_77_nullable_repository",
        "minimal_repository": "_ghes_78_minimal_repository",
        "thread": "_ghes_79_thread",
        "thread_subscription": "_ghes_80_thread_subscription",
        "organization_full": "_ghes_81_organization_full",
        "enabled_repositories": "_ghes_82_enabled_repositories",
        "actions_organization_permissions": "_ghes_83_actions_organization_permissions",
        "runner_groups_org": "_ghes_84_runner_groups_org",
        "organization_actions_secret": "_ghes_85_organization_actions_secret",
        "actions_public_key": "_ghes_86_actions_public_key",
        "empty_object": "_ghes_87_empty_object",
        "org_hook": "_ghes_88_org_hook",
        "org_membership": "_ghes_89_org_membership",
        "org_pre_receive_hook": "_ghes_90_org_pre_receive_hook",
        "project": "_ghes_91_project",
        "nullable_team_simple": "_ghes_92_nullable_team_simple",
        "team": "_ghes_93_team",
        "team_full": "_ghes_94_team_full",
        "team_discussion": "_ghes_95_team_discussion",
        "team_discussion_comment": "_ghes_96_team_discussion_comment",
        "reaction": "_ghes_97_reaction",
        "team_membership": "_ghes_98_team_membership",
        "team_project": "_ghes_99_team_project",
        "team_repository": "_ghes_100_team_repository",
        "project_card": "_ghes_101_project_card",
        "project_column": "_ghes_102_project_column",
        "project_collaborator_permission": "_ghes_103_project_collaborator_permission",
        "rate_limit": "_ghes_104_rate_limit",
        "rate_limit_overview": "_ghes_105_rate_limit_overview",
        "code_of_conduct_simple": "_ghes_106_code_of_conduct_simple",
        "full_repository": "_ghes_107_full_repository",
        "artifact": "_ghes_108_artifact",
        "job": "_ghes_109_job",
        "actions_enabled": "_ghes_110_actions_enabled",
        "actions_repository_permissions": "_ghes_111_actions_repository_permissions",
        "pull_request_minimal": "_ghes_112_pull_request_minimal",
        "nullable_simple_commit": "_ghes_113_nullable_simple_commit",
        "workflow_run": "_ghes_114_workflow_run",
        "actions_secret": "_ghes_115_actions_secret",
        "workflow": "_ghes_116_workflow",
        "protected_branch_required_status_check": "_ghes_117_protected_branch_required_status_check",
        "protected_branch_admin_enforced": "_ghes_118_protected_branch_admin_enforced",
        "protected_branch_pull_request_review": "_ghes_119_protected_branch_pull_request_review",
        "branch_restriction_policy": "_ghes_120_branch_restriction_policy",
        "branch_protection": "_ghes_121_branch_protection",
        "short_branch": "_ghes_122_short_branch",
        "nullable_git_user": "_ghes_123_nullable_git_user",
        "verification": "_ghes_124_verification",
        "diff_entry": "_ghes_125_diff_entry",
        "commit": "_ghes_126_commit",
        "branch_with_protection": "_ghes_127_branch_with_protection",
        "status_check_policy": "_ghes_128_status_check_policy",
        "protected_branch": "_ghes_129_protected_branch",
        "deployment_simple": "_ghes_130_deployment_simple",
        "check_run": "_ghes_131_check_run",
        "check_annotation": "_ghes_132_check_annotation",
        "simple_commit": "_ghes_133_simple_commit",
        "check_suite": "_ghes_134_check_suite",
        "check_suite_preference": "_ghes_135_check_suite_preference",
        "code_scanning_analysis_tool_name": "_ghes_136_code_scanning_analysis_tool_name",
        "code_scanning_analysis_tool_guid": "_ghes_137_code_scanning_analysis_tool_guid",
        "code_scanning_ref": "_ghes_138_code_scanning_ref",
        "code_scanning_alert_state": "_ghes_139_code_scanning_alert_state",
        "alert_number": "_ghes_140_alert_number",
        "alert_created_at": "_ghes_141_alert_created_at",
        "alert_url": "_ghes_142_alert_url",
        "alert_html_url": "_ghes_143_alert_html_url",
        "alert_instances_url": "_ghes_144_alert_instances_url",
        "code_scanning_alert_dismissed_at": "_ghes_145_code_scanning_alert_dismissed_at",
        "code_scanning_alert_dismissed_reason": "_ghes_146_code_scanning_alert_dismissed_reason",
        "code_scanning_alert_rule_summary": "_ghes_147_code_scanning_alert_rule_summary",
        "code_scanning_analysis_tool_version": "_ghes_148_code_scanning_analysis_tool_version",
        "code_scanning_analysis_tool": "_ghes_149_code_scanning_analysis_tool",
        "code_scanning_analysis_analysis_key": "_ghes_150_code_scanning_analysis_analysis_key",
        "code_scanning_alert_environment": "_ghes_151_code_scanning_alert_environment",
        "code_scanning_analysis_category": "_ghes_152_code_scanning_analysis_category",
        "code_scanning_alert_location": "_ghes_153_code_scanning_alert_location",
        "code_scanning_alert_classification": "_ghes_154_code_scanning_alert_classification",
        "code_scanning_alert_instance": "_ghes_155_code_scanning_alert_instance",
        "code_scanning_alert_items": "_ghes_156_code_scanning_alert_items",
        "code_scanning_alert_rule": "_ghes_157_code_scanning_alert_rule",
        "code_scanning_alert": "_ghes_158_code_scanning_alert",
        "code_scanning_alert_set_state": "_ghes_159_code_scanning_alert_set_state",
        "code_scanning_analysis_sarif_id": "_ghes_160_code_scanning_analysis_sarif_id",
        "code_scanning_analysis_commit_sha": "_ghes_161_code_scanning_analysis_commit_sha",
        "code_scanning_analysis_environment": "_ghes_162_code_scanning_analysis_environment",
        "code_scanning_analysis_created_at": "_ghes_163_code_scanning_analysis_created_at",
        "code_scanning_analysis_url": "_ghes_164_code_scanning_analysis_url",
        "code_scanning_analysis": "_ghes_165_code_scanning_analysis",
        "code_scanning_analysis_sarif_file": "_ghes_166_code_scanning_analysis_sarif_file",
        "code_scanning_sarifs_receipt": "_ghes_167_code_scanning_sarifs_receipt",
        "collaborator": "_ghes_168_collaborator",
        "repository_invitation": "_ghes_169_repository_invitation",
        "nullable_collaborator": "_ghes_170_nullable_collaborator",
        "repository_collaborator_permission": "_ghes_171_repository_collaborator_permission",
        "commit_comment": "_ghes_172_commit_comment",
        "scim_error": "_ghes_173_scim_error",
        "branch_short": "_ghes_174_branch_short",
        "link": "_ghes_175_link",
        "pull_request_simple": "_ghes_176_pull_request_simple",
        "simple_commit_status": "_ghes_177_simple_commit_status",
        "combined_commit_status": "_ghes_178_combined_commit_status",
        "status": "_ghes_179_status",
        "commit_comparison": "_ghes_180_commit_comparison",
        "content_reference_attachment": "_ghes_181_content_reference_attachment",
        "content_tree": "_ghes_182_content_tree",
        "content_directory": "_ghes_183_content_directory",
        "content_file": "_ghes_184_content_file",
        "content_symlink": "_ghes_185_content_symlink",
        "content_submodule": "_ghes_186_content_submodule",
        "file_commit": "_ghes_187_file_commit",
        "contributor": "_ghes_188_contributor",
        "deployment": "_ghes_189_deployment",
        "deployment_status": "_ghes_190_deployment_status",
        "short_blob": "_ghes_191_short_blob",
        "blob": "_ghes_192_blob",
        "git_commit": "_ghes_193_git_commit",
        "git_ref": "_ghes_194_git_ref",
        "git_tag": "_ghes_195_git_tag",
        "git_tree": "_ghes_196_git_tree",
        "hook_response": "_ghes_197_hook_response",
        "hook": "_ghes_198_hook",
        "nullable_issue": "_ghes_199_nullable_issue",
        "issue_event_label": "_ghes_200_issue_event_label",
        "issue_event_dismissed_review": "_ghes_201_issue_event_dismissed_review",
        "issue_event_milestone": "_ghes_202_issue_event_milestone",
        "issue_event_project_card": "_ghes_203_issue_event_project_card",
        "issue_event_rename": "_ghes_204_issue_event_rename",
        "issue_event": "_ghes_205_issue_event",
        "labeled_issue_event": "_ghes_206_labeled_issue_event",
        "unlabeled_issue_event": "_ghes_207_unlabeled_issue_event",
        "assigned_issue_event": "_ghes_208_assigned_issue_event",
        "unassigned_issue_event": "_ghes_209_unassigned_issue_event",
        "milestoned_issue_event": "_ghes_210_milestoned_issue_event",
        "demilestoned_issue_event": "_ghes_211_demilestoned_issue_event",
        "renamed_issue_event": "_ghes_212_renamed_issue_event",
        "review_requested_issue_event": "_ghes_213_review_requested_issue_event",
        "review_request_removed_issue_event": "_ghes_214_review_request_removed_issue_event",
        "review_dismissed_issue_event": "_ghes_215_review_dismissed_issue_event",
        "locked_issue_event": "_ghes_216_locked_issue_event",
        "added_to_project_issue_event": "_ghes_217_added_to_project_issue_event",
        "moved_column_in_project_issue_event": "_ghes_218_moved_column_in_project_issue_event",
        "removed_from_project_issue_event": "_ghes_219_removed_from_project_issue_event",
        "converted_note_to_issue_issue_event": "_ghes_220_converted_note_to_issue_issue_event",
        "issue_event_for_issue": "_ghes_221_issue_event_for_issue",
        "label": "_ghes_222_label",
        "timeline_comment_event": "_ghes_223_timeline_comment_event",
        "timeline_cross_referenced_event": "_ghes_224_timeline_cross_referenced_event",
        "timeline_committed_event": "_ghes_225_timeline_committed_event",
        "timeline_reviewed_event": "_ghes_226_timeline_reviewed_event",
        "pull_request_review_comment": "_ghes_227_pull_request_review_comment",
        "timeline_line_commented_event": "_ghes_228_timeline_line_commented_event",
        "timeline_commit_commented_event": "_ghes_229_timeline_commit_commented_event",
        "timeline_assigned_issue_event": "_ghes_230_timeline_assigned_issue_event",
        "timeline_unassigned_issue_event": "_ghes_231_timeline_unassigned_issue_event",
        "state_change_issue_event": "_ghes_232_state_change_issue_event",
        "timeline_issue_events": "_ghes_233_timeline_issue_events",
        "deploy_key": "_ghes_234_deploy_key",
        "language": "_ghes_235_language",
        "license_content": "_ghes_236_license_content",
        "milestone": "_ghes_237_milestone",
        "pages_source_hash": "_ghes_238_pages_source_hash",
        "pages_https_certificate": "_ghes_239_pages_https_certificate",
        "page": "_ghes_240_page",
        "page_build": "_ghes_241_page_build",
        "page_build_status": "_ghes_242_page_build_status",
        "repository_pre_receive_hook": "_ghes_243_repository_pre_receive_hook",
        "team_simple": "_ghes_244_team_simple",
        "pull_request": "_ghes_245_pull_request",
        "pull_request_merge_result": "_ghes_246_pull_request_merge_result",
        "pull_request_review_request": "_ghes_247_pull_request_review_request",
        "pull_request_review": "_ghes_248_pull_request_review",
        "review_comment": "_ghes_249_review_comment",
        "release_asset": "_ghes_250_release_asset",
        "release": "_ghes_251_release",
        "stargazer": "_ghes_252_stargazer",
        "code_frequency_stat": "_ghes_253_code_frequency_stat",
        "commit_activity": "_ghes_254_commit_activity",
        "contributor_activity": "_ghes_255_contributor_activity",
        "participation_stats": "_ghes_256_participation_stats",
        "repository_subscription": "_ghes_257_repository_subscription",
        "tag": "_ghes_258_tag",
        "topic": "_ghes_259_topic",
        "search_result_text_matches": "_ghes_260_search_result_text_matches",
        "code_search_result_item": "_ghes_261_code_search_result_item",
        "commit_search_result_item": "_ghes_262_commit_search_result_item",
        "issue_search_result_item": "_ghes_263_issue_search_result_item",
        "label_search_result_item": "_ghes_264_label_search_result_item",
        "repo_search_result_item": "_ghes_265_repo_search_result_item",
        "topic_search_result_item": "_ghes_266_topic_search_result_item",
        "user_search_result_item": "_ghes_267_user_search_result_item",
        "configuration_status": "_ghes_268_configuration_status",
        "maintenance_status": "_ghes_269_maintenance_status",
        "enterprise_settings": "_ghes_270_enterprise_settings",
        "ssh_key": "_ghes_271_ssh_key",
        "private_user": "_ghes_272_private_user",
        "email": "_ghes_273_email",
        "gpg_key": "_ghes_274_gpg_key",
        "key": "_ghes_275_key",
        "starred_repository": "_ghes_276_starred_repository",
        "hovercard": "_ghes_277_hovercard",
        "key_simple": "_ghes_278_key_simple",
    }

    types = {}
    types["global_hook"] = t.struct(
        {
            "type": t.string().optional(),
            "id": t.integer().optional(),
            "name": t.string().optional(),
            "active": t.boolean().optional(),
            "events": t.array(t.string()).optional(),
            "config": t.struct(
                {
                    "url": t.string().optional(),
                    "content_type": t.string().optional(),
                    "insecure_ssl": t.string().optional(),
                    "secret": t.string().optional(),
                }
            ).optional(),
            "updated_at": t.string().optional(),
            "created_at": t.string().optional(),
            "url": t.string().optional(),
            "ping_url": t.string().optional(),
        }
    ).named(renames["global_hook"])
    types["global_hook_2"] = t.struct(
        {
            "type": t.string().optional(),
            "id": t.integer().optional(),
            "name": t.string().optional(),
            "active": t.boolean().optional(),
            "events": t.array(t.string()).optional(),
            "config": t.struct(
                {
                    "url": t.string().optional(),
                    "content_type": t.string().optional(),
                    "insecure_ssl": t.string().optional(),
                }
            ).optional(),
            "updated_at": t.string().optional(),
            "created_at": t.string().optional(),
            "url": t.string().optional(),
            "ping_url": t.string().optional(),
        }
    ).named(renames["global_hook_2"])
    types["public_key_full"] = t.struct(
        {
            "id": t.integer(),
            "key": t.string(),
            "user_id": t.integer().optional(),
            "repository_id": t.integer().optional(),
            "url": t.string(),
            "title": t.string(),
            "read_only": t.boolean(),
            "verified": t.boolean(),
            "created_at": t.string(),
            "last_used": t.string().optional(),
        }
    ).named(renames["public_key_full"])
    types["ldap_mapping_team"] = t.struct(
        {
            "ldap_dn": t.string().optional(),
            "id": t.integer().optional(),
            "node_id": t.string().optional(),
            "url": t.string().optional(),
            "html_url": t.string().optional(),
            "name": t.string().optional(),
            "slug": t.string().optional(),
            "description": t.string().optional(),
            "privacy": t.string().optional(),
            "permission": t.string().optional(),
            "members_url": t.string().optional(),
            "repositories_url": t.string().optional(),
            "parent": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["ldap_mapping_team"])
    types["ldap_mapping_user"] = t.struct(
        {
            "ldap_dn": t.string().optional(),
            "login": t.string(),
            "id": t.integer(),
            "node_id": t.string(),
            "avatar_url": t.string(),
            "gravatar_id": t.string().optional(),
            "url": t.string(),
            "html_url": t.string(),
            "followers_url": t.string(),
            "following_url": t.string(),
            "gists_url": t.string(),
            "starred_url": t.string(),
            "subscriptions_url": t.string(),
            "organizations_url": t.string(),
            "repos_url": t.string(),
            "events_url": t.string(),
            "received_events_url": t.string(),
            "type": t.string(),
            "site_admin": t.boolean(),
            "name": t.string().optional(),
            "company": t.string().optional(),
            "blog": t.string().optional(),
            "location": t.string().optional(),
            "email": t.string().optional(),
            "hireable": t.boolean().optional(),
            "bio": t.string().optional(),
            "twitter_username": t.string().optional(),
            "public_repos": t.integer(),
            "public_gists": t.integer(),
            "followers": t.integer(),
            "following": t.integer(),
            "created_at": t.string(),
            "updated_at": t.string(),
            "private_gists": t.integer(),
            "total_private_repos": t.integer(),
            "owned_private_repos": t.integer(),
            "disk_usage": t.integer(),
            "collaborators": t.integer(),
            "two_factor_authentication": t.boolean(),
            "plan": t.struct(
                {
                    "collaborators": t.integer(),
                    "name": t.string(),
                    "space": t.integer(),
                    "private_repos": t.integer(),
                }
            ).optional(),
            "suspended_at": t.string().optional(),
            "business_plus": t.boolean().optional(),
        }
    ).named(renames["ldap_mapping_user"])
    types["organization_simple"] = t.struct(
        {
            "login": t.string(),
            "id": t.integer(),
            "node_id": t.string(),
            "url": t.string(),
            "repos_url": t.string(),
            "events_url": t.string(),
            "hooks_url": t.string(),
            "issues_url": t.string(),
            "members_url": t.string(),
            "public_members_url": t.string(),
            "avatar_url": t.string(),
            "description": t.string().optional(),
        }
    ).named(renames["organization_simple"])
    types["pre_receive_environment"] = t.struct(
        {
            "id": t.integer().optional(),
            "name": t.string().optional(),
            "image_url": t.string().optional(),
            "url": t.string().optional(),
            "html_url": t.string().optional(),
            "default_environment": t.boolean().optional(),
            "created_at": t.string().optional(),
            "hooks_count": t.integer().optional(),
            "download": t.struct(
                {
                    "url": t.string().optional(),
                    "state": t.string().optional(),
                    "downloaded_at": t.string().optional(),
                    "message": t.string().optional(),
                }
            ).optional(),
        }
    ).named(renames["pre_receive_environment"])
    types["pre_receive_environment_download_status"] = t.struct(
        {
            "url": t.string().optional(),
            "state": t.string().optional(),
            "downloaded_at": t.string().optional(),
            "message": t.string().optional(),
        }
    ).named(renames["pre_receive_environment_download_status"])
    types["pre_receive_hook"] = t.struct(
        {
            "id": t.integer().optional(),
            "name": t.string().optional(),
            "enforcement": t.string().optional(),
            "script": t.string().optional(),
            "script_repository": t.struct(
                {
                    "id": t.integer().optional(),
                    "full_name": t.string().optional(),
                    "url": t.string().optional(),
                    "html_url": t.string().optional(),
                }
            ).optional(),
            "environment": t.struct(
                {
                    "id": t.integer().optional(),
                    "name": t.string().optional(),
                    "image_url": t.string().optional(),
                    "url": t.string().optional(),
                    "html_url": t.string().optional(),
                    "default_environment": t.boolean().optional(),
                    "created_at": t.string().optional(),
                    "hooks_count": t.integer().optional(),
                    "download": t.struct(
                        {
                            "url": t.string().optional(),
                            "state": t.string().optional(),
                            "downloaded_at": t.string().optional(),
                            "message": t.string().optional(),
                        }
                    ).optional(),
                }
            ).optional(),
            "allow_downstream_configuration": t.boolean().optional(),
        }
    ).named(renames["pre_receive_hook"])
    types["nullable_simple_user"] = (
        t.struct(
            {
                "name": t.string().optional(),
                "email": t.string().optional(),
                "login": t.string(),
                "id": t.integer(),
                "node_id": t.string(),
                "avatar_url": t.string(),
                "gravatar_id": t.string().optional(),
                "url": t.string(),
                "html_url": t.string(),
                "followers_url": t.string(),
                "following_url": t.string(),
                "gists_url": t.string(),
                "starred_url": t.string(),
                "subscriptions_url": t.string(),
                "organizations_url": t.string(),
                "repos_url": t.string(),
                "events_url": t.string(),
                "received_events_url": t.string(),
                "type": t.string(),
                "site_admin": t.boolean(),
                "starred_at": t.string().optional(),
            }
        )
        .optional()
        .named(renames["nullable_simple_user"])
    )
    types["app_permissions"] = t.struct(
        {
            "actions": t.string().optional(),
            "administration": t.string().optional(),
            "checks": t.string().optional(),
            "contents": t.string().optional(),
            "deployments": t.string().optional(),
            "environments": t.string().optional(),
            "issues": t.string().optional(),
            "metadata": t.string().optional(),
            "packages": t.string().optional(),
            "pages": t.string().optional(),
            "pull_requests": t.string().optional(),
            "repository_hooks": t.string().optional(),
            "repository_projects": t.string().optional(),
            "secret_scanning_alerts": t.string().optional(),
            "secrets": t.string().optional(),
            "security_events": t.string().optional(),
            "single_file": t.string().optional(),
            "statuses": t.string().optional(),
            "vulnerability_alerts": t.string().optional(),
            "workflows": t.string().optional(),
            "members": t.string().optional(),
            "organization_administration": t.string().optional(),
            "organization_hooks": t.string().optional(),
            "organization_plan": t.string().optional(),
            "organization_projects": t.string().optional(),
            "organization_packages": t.string().optional(),
            "organization_secrets": t.string().optional(),
            "organization_self_hosted_runners": t.string().optional(),
            "organization_user_blocking": t.string().optional(),
            "team_discussions": t.string().optional(),
            "content_references": t.string().optional(),
        }
    ).named(renames["app_permissions"])
    types["simple_user"] = t.struct(
        {
            "name": t.string().optional(),
            "email": t.string().optional(),
            "login": t.string(),
            "id": t.integer(),
            "node_id": t.string(),
            "avatar_url": t.string(),
            "gravatar_id": t.string().optional(),
            "url": t.string(),
            "html_url": t.string(),
            "followers_url": t.string(),
            "following_url": t.string(),
            "gists_url": t.string(),
            "starred_url": t.string(),
            "subscriptions_url": t.string(),
            "organizations_url": t.string(),
            "repos_url": t.string(),
            "events_url": t.string(),
            "received_events_url": t.string(),
            "type": t.string(),
            "site_admin": t.boolean(),
            "starred_at": t.string().optional(),
        }
    ).named(renames["simple_user"])
    types["nullable_scoped_installation"] = (
        t.struct(
            {
                "permissions": t.proxy(renames["app_permissions"]),
                "repository_selection": t.string(),
                "single_file_name": t.string().optional(),
                "has_multiple_single_files": t.boolean().optional(),
                "single_file_paths": t.array(t.string()).optional(),
                "repositories_url": t.string(),
                "account": t.proxy(renames["simple_user"]),
            }
        )
        .optional()
        .named(renames["nullable_scoped_installation"])
    )
    types["authorization"] = t.struct(
        {
            "id": t.integer(),
            "url": t.string(),
            "scopes": t.array(t.string()).optional(),
            "token": t.string(),
            "token_last_eight": t.string().optional(),
            "hashed_token": t.string().optional(),
            "app": t.struct(
                {"client_id": t.string(), "name": t.string(), "url": t.string()}
            ),
            "note": t.string().optional(),
            "note_url": t.string().optional(),
            "updated_at": t.string(),
            "created_at": t.string(),
            "fingerprint": t.string().optional(),
            "user": t.proxy(renames["nullable_simple_user"]).optional(),
            "installation": t.proxy(renames["nullable_scoped_installation"]).optional(),
        }
    ).named(renames["authorization"])
    types["integration"] = t.struct(
        {
            "id": t.integer(),
            "slug": t.string().optional(),
            "node_id": t.string(),
            "owner": t.proxy(renames["nullable_simple_user"]),
            "name": t.string(),
            "description": t.string().optional(),
            "external_url": t.string(),
            "html_url": t.string(),
            "created_at": t.string(),
            "updated_at": t.string(),
            "permissions": t.struct(
                {
                    "issues": t.string().optional(),
                    "checks": t.string().optional(),
                    "metadata": t.string().optional(),
                    "contents": t.string().optional(),
                    "deployments": t.string().optional(),
                }
            ),
            "events": t.array(t.string()),
            "installations_count": t.integer().optional(),
            "client_id": t.string().optional(),
            "client_secret": t.string().optional(),
            "webhook_secret": t.string().optional(),
            "pem": t.string().optional(),
        }
    ).named(renames["integration"])
    types["basic_error"] = t.struct(
        {
            "message": t.string().optional(),
            "documentation_url": t.string().optional(),
            "url": t.string().optional(),
            "status": t.string().optional(),
        }
    ).named(renames["basic_error"])
    types["validation_error_simple"] = t.struct(
        {
            "message": t.string(),
            "documentation_url": t.string(),
            "errors": t.array(t.string()).optional(),
        }
    ).named(renames["validation_error_simple"])
    types["webhook_config_url"] = t.string().named(renames["webhook_config_url"])
    types["webhook_config_content_type"] = t.string().named(
        renames["webhook_config_content_type"]
    )
    types["webhook_config_secret"] = t.string().named(renames["webhook_config_secret"])
    types["webhook_config_insecure_ssl"] = t.either([t.string(), t.number()]).named(
        renames["webhook_config_insecure_ssl"]
    )
    types["webhook_config"] = t.struct(
        {
            "url": t.proxy(renames["webhook_config_url"]).optional(),
            "content_type": t.proxy(renames["webhook_config_content_type"]).optional(),
            "secret": t.proxy(renames["webhook_config_secret"]).optional(),
            "insecure_ssl": t.proxy(renames["webhook_config_insecure_ssl"]).optional(),
        }
    ).named(renames["webhook_config"])
    types["enterprise"] = t.struct(
        {
            "description": t.string().optional(),
            "html_url": t.string(),
            "website_url": t.string().optional(),
            "id": t.integer(),
            "node_id": t.string(),
            "name": t.string(),
            "slug": t.string(),
            "created_at": t.string().optional(),
            "updated_at": t.string().optional(),
            "avatar_url": t.string(),
        }
    ).named(renames["enterprise"])
    types["installation"] = t.struct(
        {
            "id": t.integer(),
            "account": t.union(
                [t.proxy(renames["simple_user"]), t.proxy(renames["enterprise"])]
            ).optional(),
            "repository_selection": t.string(),
            "access_tokens_url": t.string(),
            "repositories_url": t.string(),
            "html_url": t.string(),
            "app_id": t.integer(),
            "target_id": t.integer(),
            "target_type": t.string(),
            "permissions": t.proxy(renames["app_permissions"]),
            "events": t.array(t.string()),
            "created_at": t.string(),
            "updated_at": t.string(),
            "single_file_name": t.string().optional(),
            "has_multiple_single_files": t.boolean().optional(),
            "single_file_paths": t.array(t.string()).optional(),
            "app_slug": t.string(),
            "suspended_by": t.proxy(renames["nullable_simple_user"]),
            "suspended_at": t.string().optional(),
            "contact_email": t.string().optional(),
        }
    ).named(renames["installation"])
    types["nullable_license_simple"] = (
        t.struct(
            {
                "key": t.string(),
                "name": t.string(),
                "url": t.string().optional(),
                "spdx_id": t.string().optional(),
                "node_id": t.string(),
                "html_url": t.string().optional(),
            }
        )
        .optional()
        .named(renames["nullable_license_simple"])
    )
    types["repository"] = t.struct(
        {
            "id": t.integer(),
            "node_id": t.string(),
            "name": t.string(),
            "full_name": t.string(),
            "license": t.proxy(renames["nullable_license_simple"]),
            "organization": t.proxy(renames["nullable_simple_user"]).optional(),
            "forks": t.integer(),
            "permissions": t.struct(
                {
                    "admin": t.boolean(),
                    "pull": t.boolean(),
                    "triage": t.boolean().optional(),
                    "push": t.boolean(),
                    "maintain": t.boolean().optional(),
                }
            ).optional(),
            "owner": t.proxy(renames["simple_user"]),
            "private": t.boolean(),
            "html_url": t.string(),
            "description": t.string().optional(),
            "fork": t.boolean(),
            "url": t.string(),
            "archive_url": t.string(),
            "assignees_url": t.string(),
            "blobs_url": t.string(),
            "branches_url": t.string(),
            "collaborators_url": t.string(),
            "comments_url": t.string(),
            "commits_url": t.string(),
            "compare_url": t.string(),
            "contents_url": t.string(),
            "contributors_url": t.string(),
            "deployments_url": t.string(),
            "downloads_url": t.string(),
            "events_url": t.string(),
            "forks_url": t.string(),
            "git_commits_url": t.string(),
            "git_refs_url": t.string(),
            "git_tags_url": t.string(),
            "git_url": t.string(),
            "issue_comment_url": t.string(),
            "issue_events_url": t.string(),
            "issues_url": t.string(),
            "keys_url": t.string(),
            "labels_url": t.string(),
            "languages_url": t.string(),
            "merges_url": t.string(),
            "milestones_url": t.string(),
            "notifications_url": t.string(),
            "pulls_url": t.string(),
            "releases_url": t.string(),
            "ssh_url": t.string(),
            "stargazers_url": t.string(),
            "statuses_url": t.string(),
            "subscribers_url": t.string(),
            "subscription_url": t.string(),
            "tags_url": t.string(),
            "teams_url": t.string(),
            "trees_url": t.string(),
            "clone_url": t.string(),
            "mirror_url": t.string().optional(),
            "hooks_url": t.string(),
            "svn_url": t.string(),
            "homepage": t.string().optional(),
            "language": t.string().optional(),
            "forks_count": t.integer(),
            "stargazers_count": t.integer(),
            "watchers_count": t.integer(),
            "size": t.integer(),
            "default_branch": t.string(),
            "open_issues_count": t.integer(),
            "is_template": t.boolean().optional(),
            "topics": t.array(t.string()).optional(),
            "has_issues": t.boolean(),
            "has_projects": t.boolean(),
            "has_wiki": t.boolean(),
            "has_pages": t.boolean(),
            "has_downloads": t.boolean(),
            "archived": t.boolean(),
            "disabled": t.boolean(),
            "visibility": t.string().optional(),
            "pushed_at": t.string().optional(),
            "created_at": t.string().optional(),
            "updated_at": t.string().optional(),
            "allow_rebase_merge": t.boolean().optional(),
            "template_repository": t.struct(
                {
                    "id": t.integer().optional(),
                    "node_id": t.string().optional(),
                    "name": t.string().optional(),
                    "full_name": t.string().optional(),
                    "owner": t.struct(
                        {
                            "login": t.string().optional(),
                            "id": t.integer().optional(),
                            "node_id": t.string().optional(),
                            "avatar_url": t.string().optional(),
                            "gravatar_id": t.string().optional(),
                            "url": t.string().optional(),
                            "html_url": t.string().optional(),
                            "followers_url": t.string().optional(),
                            "following_url": t.string().optional(),
                            "gists_url": t.string().optional(),
                            "starred_url": t.string().optional(),
                            "subscriptions_url": t.string().optional(),
                            "organizations_url": t.string().optional(),
                            "repos_url": t.string().optional(),
                            "events_url": t.string().optional(),
                            "received_events_url": t.string().optional(),
                            "type": t.string().optional(),
                            "site_admin": t.boolean().optional(),
                        }
                    ).optional(),
                    "private": t.boolean().optional(),
                    "html_url": t.string().optional(),
                    "description": t.string().optional(),
                    "fork": t.boolean().optional(),
                    "url": t.string().optional(),
                    "archive_url": t.string().optional(),
                    "assignees_url": t.string().optional(),
                    "blobs_url": t.string().optional(),
                    "branches_url": t.string().optional(),
                    "collaborators_url": t.string().optional(),
                    "comments_url": t.string().optional(),
                    "commits_url": t.string().optional(),
                    "compare_url": t.string().optional(),
                    "contents_url": t.string().optional(),
                    "contributors_url": t.string().optional(),
                    "deployments_url": t.string().optional(),
                    "downloads_url": t.string().optional(),
                    "events_url": t.string().optional(),
                    "forks_url": t.string().optional(),
                    "git_commits_url": t.string().optional(),
                    "git_refs_url": t.string().optional(),
                    "git_tags_url": t.string().optional(),
                    "git_url": t.string().optional(),
                    "issue_comment_url": t.string().optional(),
                    "issue_events_url": t.string().optional(),
                    "issues_url": t.string().optional(),
                    "keys_url": t.string().optional(),
                    "labels_url": t.string().optional(),
                    "languages_url": t.string().optional(),
                    "merges_url": t.string().optional(),
                    "milestones_url": t.string().optional(),
                    "notifications_url": t.string().optional(),
                    "pulls_url": t.string().optional(),
                    "releases_url": t.string().optional(),
                    "ssh_url": t.string().optional(),
                    "stargazers_url": t.string().optional(),
                    "statuses_url": t.string().optional(),
                    "subscribers_url": t.string().optional(),
                    "subscription_url": t.string().optional(),
                    "tags_url": t.string().optional(),
                    "teams_url": t.string().optional(),
                    "trees_url": t.string().optional(),
                    "clone_url": t.string().optional(),
                    "mirror_url": t.string().optional(),
                    "hooks_url": t.string().optional(),
                    "svn_url": t.string().optional(),
                    "homepage": t.string().optional(),
                    "language": t.string().optional(),
                    "forks_count": t.integer().optional(),
                    "stargazers_count": t.integer().optional(),
                    "watchers_count": t.integer().optional(),
                    "size": t.integer().optional(),
                    "default_branch": t.string().optional(),
                    "open_issues_count": t.integer().optional(),
                    "is_template": t.boolean().optional(),
                    "topics": t.array(t.string()).optional(),
                    "has_issues": t.boolean().optional(),
                    "has_projects": t.boolean().optional(),
                    "has_wiki": t.boolean().optional(),
                    "has_pages": t.boolean().optional(),
                    "has_downloads": t.boolean().optional(),
                    "archived": t.boolean().optional(),
                    "disabled": t.boolean().optional(),
                    "visibility": t.string().optional(),
                    "pushed_at": t.string().optional(),
                    "created_at": t.string().optional(),
                    "updated_at": t.string().optional(),
                    "permissions": t.struct(
                        {
                            "admin": t.boolean().optional(),
                            "maintain": t.boolean().optional(),
                            "push": t.boolean().optional(),
                            "triage": t.boolean().optional(),
                            "pull": t.boolean().optional(),
                        }
                    ).optional(),
                    "allow_rebase_merge": t.boolean().optional(),
                    "temp_clone_token": t.string().optional(),
                    "allow_squash_merge": t.boolean().optional(),
                    "delete_branch_on_merge": t.boolean().optional(),
                    "allow_update_branch": t.boolean().optional(),
                    "allow_merge_commit": t.boolean().optional(),
                    "subscribers_count": t.integer().optional(),
                    "network_count": t.integer().optional(),
                }
            ).optional(),
            "temp_clone_token": t.string().optional(),
            "allow_squash_merge": t.boolean().optional(),
            "delete_branch_on_merge": t.boolean().optional(),
            "allow_merge_commit": t.boolean().optional(),
            "allow_forking": t.boolean().optional(),
            "subscribers_count": t.integer().optional(),
            "network_count": t.integer().optional(),
            "open_issues": t.integer(),
            "watchers": t.integer(),
            "master_branch": t.string().optional(),
            "starred_at": t.string().optional(),
        }
    ).named(renames["repository"])
    types["installation_token"] = t.struct(
        {
            "token": t.string(),
            "expires_at": t.string(),
            "permissions": t.proxy(renames["app_permissions"]).optional(),
            "repository_selection": t.string().optional(),
            "repositories": t.array(t.proxy(renames["repository"])).optional(),
            "single_file": t.string().optional(),
            "has_multiple_single_files": t.boolean().optional(),
            "single_file_paths": t.array(t.string()).optional(),
        }
    ).named(renames["installation_token"])
    types["validation_error"] = t.struct(
        {
            "message": t.string(),
            "documentation_url": t.string(),
            "errors": t.array(
                t.struct(
                    {
                        "resource": t.string().optional(),
                        "field": t.string().optional(),
                        "message": t.string().optional(),
                        "code": t.string(),
                        "index": t.integer().optional(),
                        "value": t.either(
                            [
                                t.string().optional(),
                                t.integer().optional(),
                                t.array(t.string()).optional(),
                            ]
                        ).optional(),
                    }
                )
            ).optional(),
        }
    ).named(renames["validation_error"])
    types["application_grant"] = t.struct(
        {
            "id": t.integer(),
            "url": t.string(),
            "app": t.struct(
                {"client_id": t.string(), "name": t.string(), "url": t.string()}
            ),
            "created_at": t.string(),
            "updated_at": t.string(),
            "scopes": t.array(t.string()),
            "user": t.proxy(renames["nullable_simple_user"]).optional(),
        }
    ).named(renames["application_grant"])
    types["nullable_authorization"] = (
        t.struct(
            {
                "id": t.integer(),
                "url": t.string(),
                "scopes": t.array(t.string()).optional(),
                "token": t.string(),
                "token_last_eight": t.string().optional(),
                "hashed_token": t.string().optional(),
                "app": t.struct(
                    {"client_id": t.string(), "name": t.string(), "url": t.string()}
                ),
                "note": t.string().optional(),
                "note_url": t.string().optional(),
                "updated_at": t.string(),
                "created_at": t.string(),
                "fingerprint": t.string().optional(),
                "user": t.proxy(renames["nullable_simple_user"]).optional(),
                "installation": t.proxy(
                    renames["nullable_scoped_installation"]
                ).optional(),
            }
        )
        .optional()
        .named(renames["nullable_authorization"])
    )
    types["code_of_conduct"] = t.struct(
        {
            "key": t.string(),
            "name": t.string(),
            "url": t.string(),
            "body": t.string().optional(),
            "html_url": t.string().optional(),
        }
    ).named(renames["code_of_conduct"])
    types["announcement_message"] = t.string().named(renames["announcement_message"])
    types["announcement_expiration"] = (
        t.string().optional().named(renames["announcement_expiration"])
    )
    types["announcement"] = t.struct(
        {
            "announcement": t.proxy(renames["announcement_message"]),
            "expires_at": t.proxy(renames["announcement_expiration"]).optional(),
        }
    ).named(renames["announcement"])
    types["license_info"] = t.struct(
        {
            "seats": t.either([t.string(), t.integer()]).optional(),
            "seats_used": t.integer().optional(),
            "seats_available": t.either([t.string(), t.integer()]).optional(),
            "kind": t.string().optional(),
            "days_until_expiration": t.integer().optional(),
            "expire_at": t.string().optional(),
        }
    ).named(renames["license_info"])
    types["enterprise_repository_overview"] = t.struct(
        {
            "total_repos": t.integer(),
            "root_repos": t.integer(),
            "fork_repos": t.integer(),
            "org_repos": t.integer(),
            "total_pushes": t.integer(),
            "total_wikis": t.integer(),
        }
    ).named(renames["enterprise_repository_overview"])
    types["enterprise_hook_overview"] = t.struct(
        {
            "total_hooks": t.integer(),
            "active_hooks": t.integer(),
            "inactive_hooks": t.integer(),
        }
    ).named(renames["enterprise_hook_overview"])
    types["enterprise_page_overview"] = t.struct({"total_pages": t.integer()}).named(
        renames["enterprise_page_overview"]
    )
    types["enterprise_organization_overview"] = t.struct(
        {
            "total_orgs": t.integer(),
            "disabled_orgs": t.integer(),
            "total_teams": t.integer(),
            "total_team_members": t.integer(),
        }
    ).named(renames["enterprise_organization_overview"])
    types["enterprise_user_overview"] = t.struct(
        {
            "total_users": t.integer(),
            "admin_users": t.integer(),
            "suspended_users": t.integer(),
        }
    ).named(renames["enterprise_user_overview"])
    types["enterprise_pull_request_overview"] = t.struct(
        {
            "total_pulls": t.integer(),
            "merged_pulls": t.integer(),
            "mergeable_pulls": t.integer(),
            "unmergeable_pulls": t.integer(),
        }
    ).named(renames["enterprise_pull_request_overview"])
    types["enterprise_issue_overview"] = t.struct(
        {
            "total_issues": t.integer(),
            "open_issues": t.integer(),
            "closed_issues": t.integer(),
        }
    ).named(renames["enterprise_issue_overview"])
    types["enterprise_milestone_overview"] = t.struct(
        {
            "total_milestones": t.integer(),
            "open_milestones": t.integer(),
            "closed_milestones": t.integer(),
        }
    ).named(renames["enterprise_milestone_overview"])
    types["enterprise_gist_overview"] = t.struct(
        {
            "total_gists": t.integer(),
            "private_gists": t.integer(),
            "public_gists": t.integer(),
        }
    ).named(renames["enterprise_gist_overview"])
    types["enterprise_comment_overview"] = t.struct(
        {
            "total_commit_comments": t.integer(),
            "total_gist_comments": t.integer(),
            "total_issue_comments": t.integer(),
            "total_pull_request_comments": t.integer(),
        }
    ).named(renames["enterprise_comment_overview"])
    types["enterprise_overview"] = t.struct(
        {
            "repos": t.proxy(renames["enterprise_repository_overview"]).optional(),
            "hooks": t.proxy(renames["enterprise_hook_overview"]).optional(),
            "pages": t.proxy(renames["enterprise_page_overview"]).optional(),
            "orgs": t.proxy(renames["enterprise_organization_overview"]).optional(),
            "users": t.proxy(renames["enterprise_user_overview"]).optional(),
            "pulls": t.proxy(renames["enterprise_pull_request_overview"]).optional(),
            "issues": t.proxy(renames["enterprise_issue_overview"]).optional(),
            "milestones": t.proxy(renames["enterprise_milestone_overview"]).optional(),
            "gists": t.proxy(renames["enterprise_gist_overview"]).optional(),
            "comments": t.proxy(renames["enterprise_comment_overview"]).optional(),
        }
    ).named(renames["enterprise_overview"])
    types["enabled_organizations"] = t.string().named(renames["enabled_organizations"])
    types["allowed_actions"] = t.string().named(renames["allowed_actions"])
    types["selected_actions_url"] = t.string().named(renames["selected_actions_url"])
    types["actions_enterprise_permissions"] = t.struct(
        {
            "enabled_organizations": t.proxy(renames["enabled_organizations"]),
            "selected_organizations_url": t.string().optional(),
            "allowed_actions": t.proxy(renames["allowed_actions"]).optional(),
            "selected_actions_url": t.proxy(renames["selected_actions_url"]).optional(),
        }
    ).named(renames["actions_enterprise_permissions"])
    types["selected_actions"] = t.struct(
        {"github_owned_allowed": t.boolean(), "patterns_allowed": t.array(t.string())}
    ).named(renames["selected_actions"])
    types["runner_groups_enterprise"] = t.struct(
        {
            "id": t.number(),
            "name": t.string(),
            "visibility": t.string(),
            "default": t.boolean(),
            "selected_organizations_url": t.string().optional(),
            "runners_url": t.string(),
            "allows_public_repositories": t.boolean(),
        }
    ).named(renames["runner_groups_enterprise"])
    types["runner_label"] = t.struct(
        {
            "id": t.integer().optional(),
            "name": t.string(),
            "type": t.string().optional(),
        }
    ).named(renames["runner_label"])
    types["runner"] = t.struct(
        {
            "id": t.integer(),
            "name": t.string(),
            "os": t.string(),
            "status": t.string(),
            "busy": t.boolean(),
            "labels": t.array(t.proxy(renames["runner_label"])),
        }
    ).named(renames["runner"])
    types["runner_application"] = t.struct(
        {
            "os": t.string(),
            "architecture": t.string(),
            "download_url": t.string(),
            "filename": t.string(),
            "temp_download_token": t.string().optional(),
            "sha256_checksum": t.string().optional(),
        }
    ).named(renames["runner_application"])
    types["authentication_token"] = t.struct(
        {
            "token": t.string(),
            "expires_at": t.string(),
            "permissions": t.struct({}).optional(),
            "repositories": t.array(t.proxy(renames["repository"])).optional(),
            "single_file": t.string().optional(),
            "repository_selection": t.string().optional(),
        }
    ).named(renames["authentication_token"])
    types["actor"] = t.struct(
        {
            "id": t.integer(),
            "login": t.string(),
            "display_login": t.string().optional(),
            "gravatar_id": t.string().optional(),
            "url": t.string(),
            "avatar_url": t.string(),
        }
    ).named(renames["actor"])
    types["nullable_milestone"] = (
        t.struct(
            {
                "url": t.string(),
                "html_url": t.string(),
                "labels_url": t.string(),
                "id": t.integer(),
                "node_id": t.string(),
                "number": t.integer(),
                "state": t.string(),
                "title": t.string(),
                "description": t.string().optional(),
                "creator": t.proxy(renames["nullable_simple_user"]),
                "open_issues": t.integer(),
                "closed_issues": t.integer(),
                "created_at": t.string(),
                "updated_at": t.string(),
                "closed_at": t.string().optional(),
                "due_on": t.string().optional(),
            }
        )
        .optional()
        .named(renames["nullable_milestone"])
    )
    types["nullable_integration"] = (
        t.struct(
            {
                "id": t.integer(),
                "slug": t.string().optional(),
                "node_id": t.string(),
                "owner": t.proxy(renames["nullable_simple_user"]),
                "name": t.string(),
                "description": t.string().optional(),
                "external_url": t.string(),
                "html_url": t.string(),
                "created_at": t.string(),
                "updated_at": t.string(),
                "permissions": t.struct(
                    {
                        "issues": t.string().optional(),
                        "checks": t.string().optional(),
                        "metadata": t.string().optional(),
                        "contents": t.string().optional(),
                        "deployments": t.string().optional(),
                    }
                ),
                "events": t.array(t.string()),
                "installations_count": t.integer().optional(),
                "client_id": t.string().optional(),
                "client_secret": t.string().optional(),
                "webhook_secret": t.string().optional(),
                "pem": t.string().optional(),
            }
        )
        .optional()
        .named(renames["nullable_integration"])
    )
    types["author_association"] = t.string().named(renames["author_association"])
    types["reaction_rollup"] = t.struct(
        {
            "url": t.string(),
            "total_count": t.integer(),
            "+1": t.integer(),
            "-1": t.integer(),
            "laugh": t.integer(),
            "confused": t.integer(),
            "heart": t.integer(),
            "hooray": t.integer(),
            "eyes": t.integer(),
            "rocket": t.integer(),
        }
    ).named(renames["reaction_rollup"])
    types["issue"] = t.struct(
        {
            "id": t.integer(),
            "node_id": t.string(),
            "url": t.string(),
            "repository_url": t.string(),
            "labels_url": t.string(),
            "comments_url": t.string(),
            "events_url": t.string(),
            "html_url": t.string(),
            "number": t.integer(),
            "state": t.string(),
            "title": t.string(),
            "body": t.string().optional(),
            "user": t.proxy(renames["nullable_simple_user"]),
            "labels": t.array(
                t.either(
                    [
                        t.string(),
                        t.struct(
                            {
                                "id": t.integer().optional(),
                                "node_id": t.string().optional(),
                                "url": t.string().optional(),
                                "name": t.string().optional(),
                                "description": t.string().optional(),
                                "color": t.string().optional(),
                                "default": t.boolean().optional(),
                            }
                        ),
                    ]
                )
            ),
            "assignee": t.proxy(renames["nullable_simple_user"]),
            "assignees": t.array(t.proxy(renames["simple_user"])).optional(),
            "milestone": t.proxy(renames["nullable_milestone"]),
            "locked": t.boolean(),
            "active_lock_reason": t.string().optional(),
            "comments": t.integer(),
            "pull_request": t.struct(
                {
                    "merged_at": t.string().optional(),
                    "diff_url": t.string().optional(),
                    "html_url": t.string().optional(),
                    "patch_url": t.string().optional(),
                    "url": t.string().optional(),
                }
            ).optional(),
            "closed_at": t.string().optional(),
            "created_at": t.string(),
            "updated_at": t.string(),
            "draft": t.boolean().optional(),
            "closed_by": t.proxy(renames["nullable_simple_user"]).optional(),
            "body_html": t.string().optional(),
            "body_text": t.string().optional(),
            "timeline_url": t.string().optional(),
            "repository": t.proxy(renames["repository"]).optional(),
            "performed_via_github_app": t.proxy(
                renames["nullable_integration"]
            ).optional(),
            "author_association": t.proxy(renames["author_association"]),
            "reactions": t.proxy(renames["reaction_rollup"]).optional(),
        }
    ).named(renames["issue"])
    types["issue_comment"] = t.struct(
        {
            "id": t.integer(),
            "node_id": t.string(),
            "url": t.string(),
            "body": t.string().optional(),
            "body_text": t.string().optional(),
            "body_html": t.string().optional(),
            "html_url": t.string(),
            "user": t.proxy(renames["nullable_simple_user"]),
            "created_at": t.string(),
            "updated_at": t.string(),
            "issue_url": t.string(),
            "author_association": t.proxy(renames["author_association"]),
            "performed_via_github_app": t.proxy(
                renames["nullable_integration"]
            ).optional(),
            "reactions": t.proxy(renames["reaction_rollup"]).optional(),
        }
    ).named(renames["issue_comment"])
    types["event"] = t.struct(
        {
            "id": t.string(),
            "type": t.string().optional(),
            "actor": t.proxy(renames["actor"]),
            "repo": t.struct(
                {"id": t.integer(), "name": t.string(), "url": t.string()}
            ),
            "org": t.proxy(renames["actor"]).optional(),
            "payload": t.struct(
                {
                    "action": t.string().optional(),
                    "issue": t.proxy(renames["issue"]).optional(),
                    "comment": t.proxy(renames["issue_comment"]).optional(),
                    "pages": t.array(
                        t.struct(
                            {
                                "page_name": t.string().optional(),
                                "title": t.string().optional(),
                                "summary": t.string().optional(),
                                "action": t.string().optional(),
                                "sha": t.string().optional(),
                                "html_url": t.string().optional(),
                            }
                        )
                    ).optional(),
                }
            ),
            "public": t.boolean(),
            "created_at": t.string().optional(),
        }
    ).named(renames["event"])
    types["link_with_type"] = t.struct({"href": t.string(), "type": t.string()}).named(
        renames["link_with_type"]
    )
    types["feed"] = t.struct(
        {
            "timeline_url": t.string(),
            "user_url": t.string(),
            "current_user_public_url": t.string().optional(),
            "current_user_url": t.string().optional(),
            "current_user_actor_url": t.string().optional(),
            "current_user_organization_url": t.string().optional(),
            "current_user_organization_urls": t.array(t.string()).optional(),
            "_links": t.struct(
                {
                    "timeline": t.proxy(renames["link_with_type"]),
                    "user": t.proxy(renames["link_with_type"]),
                    "security_advisories": t.proxy(
                        renames["link_with_type"]
                    ).optional(),
                    "current_user": t.proxy(renames["link_with_type"]).optional(),
                    "current_user_public": t.proxy(
                        renames["link_with_type"]
                    ).optional(),
                    "current_user_actor": t.proxy(renames["link_with_type"]).optional(),
                    "current_user_organization": t.proxy(
                        renames["link_with_type"]
                    ).optional(),
                    "current_user_organizations": t.array(
                        t.proxy(renames["link_with_type"])
                    ).optional(),
                }
            ),
        }
    ).named(renames["feed"])
    types["base_gist"] = t.struct(
        {
            "url": t.string(),
            "forks_url": t.string(),
            "commits_url": t.string(),
            "id": t.string(),
            "node_id": t.string(),
            "git_pull_url": t.string(),
            "git_push_url": t.string(),
            "html_url": t.string(),
            "files": t.struct({}),
            "public": t.boolean(),
            "created_at": t.string(),
            "updated_at": t.string(),
            "description": t.string().optional(),
            "comments": t.integer(),
            "user": t.proxy(renames["nullable_simple_user"]),
            "comments_url": t.string(),
            "owner": t.proxy(renames["simple_user"]).optional(),
            "truncated": t.boolean().optional(),
            "forks": t.array(t.struct({"_": t.string().optional()})).optional(),
            "history": t.array(t.struct({"_": t.string().optional()})).optional(),
        }
    ).named(renames["base_gist"])
    types["public_user"] = t.struct(
        {
            "login": t.string(),
            "id": t.integer(),
            "node_id": t.string(),
            "avatar_url": t.string(),
            "gravatar_id": t.string().optional(),
            "url": t.string(),
            "html_url": t.string(),
            "followers_url": t.string(),
            "following_url": t.string(),
            "gists_url": t.string(),
            "starred_url": t.string(),
            "subscriptions_url": t.string(),
            "organizations_url": t.string(),
            "repos_url": t.string(),
            "events_url": t.string(),
            "received_events_url": t.string(),
            "type": t.string(),
            "site_admin": t.boolean(),
            "name": t.string().optional(),
            "company": t.string().optional(),
            "blog": t.string().optional(),
            "location": t.string().optional(),
            "email": t.string().optional(),
            "hireable": t.boolean().optional(),
            "bio": t.string().optional(),
            "public_repos": t.integer(),
            "public_gists": t.integer(),
            "followers": t.integer(),
            "following": t.integer(),
            "created_at": t.string(),
            "updated_at": t.string(),
            "plan": t.struct(
                {
                    "collaborators": t.integer(),
                    "name": t.string(),
                    "space": t.integer(),
                    "private_repos": t.integer(),
                }
            ).optional(),
            "suspended_at": t.string().optional(),
            "private_gists": t.integer().optional(),
            "total_private_repos": t.integer().optional(),
            "owned_private_repos": t.integer().optional(),
            "disk_usage": t.integer().optional(),
            "collaborators": t.integer().optional(),
        }
    ).named(renames["public_user"])
    types["gist_history"] = t.struct(
        {
            "user": t.proxy(renames["nullable_simple_user"]).optional(),
            "version": t.string().optional(),
            "committed_at": t.string().optional(),
            "change_status": t.struct(
                {
                    "total": t.integer().optional(),
                    "additions": t.integer().optional(),
                    "deletions": t.integer().optional(),
                }
            ).optional(),
            "url": t.string().optional(),
        }
    ).named(renames["gist_history"])
    types["gist_simple"] = t.struct(
        {
            "forks": t.array(
                t.struct(
                    {
                        "id": t.string().optional(),
                        "url": t.string().optional(),
                        "user": t.proxy(renames["public_user"]).optional(),
                        "created_at": t.string().optional(),
                        "updated_at": t.string().optional(),
                    }
                )
            ).optional(),
            "history": t.array(t.proxy(renames["gist_history"])).optional(),
            "fork_of": t.struct(
                {
                    "url": t.string(),
                    "forks_url": t.string(),
                    "commits_url": t.string(),
                    "id": t.string(),
                    "node_id": t.string(),
                    "git_pull_url": t.string(),
                    "git_push_url": t.string(),
                    "html_url": t.string(),
                    "files": t.struct({}),
                    "public": t.boolean(),
                    "created_at": t.string(),
                    "updated_at": t.string(),
                    "description": t.string().optional(),
                    "comments": t.integer(),
                    "user": t.proxy(renames["nullable_simple_user"]),
                    "comments_url": t.string(),
                    "owner": t.proxy(renames["nullable_simple_user"]).optional(),
                    "truncated": t.boolean().optional(),
                    "forks": t.array(t.struct({"_": t.string().optional()})).optional(),
                    "history": t.array(
                        t.struct({"_": t.string().optional()})
                    ).optional(),
                }
            ).optional(),
            "url": t.string().optional(),
            "forks_url": t.string().optional(),
            "commits_url": t.string().optional(),
            "id": t.string().optional(),
            "node_id": t.string().optional(),
            "git_pull_url": t.string().optional(),
            "git_push_url": t.string().optional(),
            "html_url": t.string().optional(),
            "files": t.struct({}).optional(),
            "public": t.boolean().optional(),
            "created_at": t.string().optional(),
            "updated_at": t.string().optional(),
            "description": t.string().optional(),
            "comments": t.integer().optional(),
            "user": t.string().optional(),
            "comments_url": t.string().optional(),
            "owner": t.proxy(renames["simple_user"]).optional(),
            "truncated": t.boolean().optional(),
        }
    ).named(renames["gist_simple"])
    types["gist_comment"] = t.struct(
        {
            "id": t.integer(),
            "node_id": t.string(),
            "url": t.string(),
            "body": t.string(),
            "user": t.proxy(renames["nullable_simple_user"]),
            "created_at": t.string(),
            "updated_at": t.string(),
            "author_association": t.proxy(renames["author_association"]),
        }
    ).named(renames["gist_comment"])
    types["gist_commit"] = t.struct(
        {
            "url": t.string(),
            "version": t.string(),
            "user": t.proxy(renames["nullable_simple_user"]),
            "change_status": t.struct(
                {
                    "total": t.integer().optional(),
                    "additions": t.integer().optional(),
                    "deletions": t.integer().optional(),
                }
            ),
            "committed_at": t.string(),
        }
    ).named(renames["gist_commit"])
    types["gitignore_template"] = t.struct(
        {"name": t.string(), "source": t.string()}
    ).named(renames["gitignore_template"])
    types["license_simple"] = t.struct(
        {
            "key": t.string(),
            "name": t.string(),
            "url": t.string().optional(),
            "spdx_id": t.string().optional(),
            "node_id": t.string(),
            "html_url": t.string().optional(),
        }
    ).named(renames["license_simple"])
    types["license"] = t.struct(
        {
            "key": t.string(),
            "name": t.string(),
            "spdx_id": t.string().optional(),
            "url": t.string().optional(),
            "node_id": t.string(),
            "html_url": t.string(),
            "description": t.string(),
            "implementation": t.string(),
            "permissions": t.array(t.string()),
            "conditions": t.array(t.string()),
            "limitations": t.array(t.string()),
            "body": t.string(),
            "featured": t.boolean(),
        }
    ).named(renames["license"])
    types["api_overview"] = t.struct(
        {
            "verifiable_password_authentication": t.boolean(),
            "packages": t.array(t.string()).optional(),
            "dependabot": t.array(t.string()).optional(),
            "installed_version": t.string().optional(),
        }
    ).named(renames["api_overview"])
    types["nullable_repository"] = (
        t.struct(
            {
                "id": t.integer(),
                "node_id": t.string(),
                "name": t.string(),
                "full_name": t.string(),
                "license": t.proxy(renames["nullable_license_simple"]),
                "organization": t.proxy(renames["nullable_simple_user"]).optional(),
                "forks": t.integer(),
                "permissions": t.struct(
                    {
                        "admin": t.boolean(),
                        "pull": t.boolean(),
                        "triage": t.boolean().optional(),
                        "push": t.boolean(),
                        "maintain": t.boolean().optional(),
                    }
                ).optional(),
                "owner": t.proxy(renames["simple_user"]),
                "private": t.boolean(),
                "html_url": t.string(),
                "description": t.string().optional(),
                "fork": t.boolean(),
                "url": t.string(),
                "archive_url": t.string(),
                "assignees_url": t.string(),
                "blobs_url": t.string(),
                "branches_url": t.string(),
                "collaborators_url": t.string(),
                "comments_url": t.string(),
                "commits_url": t.string(),
                "compare_url": t.string(),
                "contents_url": t.string(),
                "contributors_url": t.string(),
                "deployments_url": t.string(),
                "downloads_url": t.string(),
                "events_url": t.string(),
                "forks_url": t.string(),
                "git_commits_url": t.string(),
                "git_refs_url": t.string(),
                "git_tags_url": t.string(),
                "git_url": t.string(),
                "issue_comment_url": t.string(),
                "issue_events_url": t.string(),
                "issues_url": t.string(),
                "keys_url": t.string(),
                "labels_url": t.string(),
                "languages_url": t.string(),
                "merges_url": t.string(),
                "milestones_url": t.string(),
                "notifications_url": t.string(),
                "pulls_url": t.string(),
                "releases_url": t.string(),
                "ssh_url": t.string(),
                "stargazers_url": t.string(),
                "statuses_url": t.string(),
                "subscribers_url": t.string(),
                "subscription_url": t.string(),
                "tags_url": t.string(),
                "teams_url": t.string(),
                "trees_url": t.string(),
                "clone_url": t.string(),
                "mirror_url": t.string().optional(),
                "hooks_url": t.string(),
                "svn_url": t.string(),
                "homepage": t.string().optional(),
                "language": t.string().optional(),
                "forks_count": t.integer(),
                "stargazers_count": t.integer(),
                "watchers_count": t.integer(),
                "size": t.integer(),
                "default_branch": t.string(),
                "open_issues_count": t.integer(),
                "is_template": t.boolean().optional(),
                "topics": t.array(t.string()).optional(),
                "has_issues": t.boolean(),
                "has_projects": t.boolean(),
                "has_wiki": t.boolean(),
                "has_pages": t.boolean(),
                "has_downloads": t.boolean(),
                "archived": t.boolean(),
                "disabled": t.boolean(),
                "visibility": t.string().optional(),
                "pushed_at": t.string().optional(),
                "created_at": t.string().optional(),
                "updated_at": t.string().optional(),
                "allow_rebase_merge": t.boolean().optional(),
                "template_repository": t.struct(
                    {
                        "id": t.integer().optional(),
                        "node_id": t.string().optional(),
                        "name": t.string().optional(),
                        "full_name": t.string().optional(),
                        "owner": t.struct(
                            {
                                "login": t.string().optional(),
                                "id": t.integer().optional(),
                                "node_id": t.string().optional(),
                                "avatar_url": t.string().optional(),
                                "gravatar_id": t.string().optional(),
                                "url": t.string().optional(),
                                "html_url": t.string().optional(),
                                "followers_url": t.string().optional(),
                                "following_url": t.string().optional(),
                                "gists_url": t.string().optional(),
                                "starred_url": t.string().optional(),
                                "subscriptions_url": t.string().optional(),
                                "organizations_url": t.string().optional(),
                                "repos_url": t.string().optional(),
                                "events_url": t.string().optional(),
                                "received_events_url": t.string().optional(),
                                "type": t.string().optional(),
                                "site_admin": t.boolean().optional(),
                            }
                        ).optional(),
                        "private": t.boolean().optional(),
                        "html_url": t.string().optional(),
                        "description": t.string().optional(),
                        "fork": t.boolean().optional(),
                        "url": t.string().optional(),
                        "archive_url": t.string().optional(),
                        "assignees_url": t.string().optional(),
                        "blobs_url": t.string().optional(),
                        "branches_url": t.string().optional(),
                        "collaborators_url": t.string().optional(),
                        "comments_url": t.string().optional(),
                        "commits_url": t.string().optional(),
                        "compare_url": t.string().optional(),
                        "contents_url": t.string().optional(),
                        "contributors_url": t.string().optional(),
                        "deployments_url": t.string().optional(),
                        "downloads_url": t.string().optional(),
                        "events_url": t.string().optional(),
                        "forks_url": t.string().optional(),
                        "git_commits_url": t.string().optional(),
                        "git_refs_url": t.string().optional(),
                        "git_tags_url": t.string().optional(),
                        "git_url": t.string().optional(),
                        "issue_comment_url": t.string().optional(),
                        "issue_events_url": t.string().optional(),
                        "issues_url": t.string().optional(),
                        "keys_url": t.string().optional(),
                        "labels_url": t.string().optional(),
                        "languages_url": t.string().optional(),
                        "merges_url": t.string().optional(),
                        "milestones_url": t.string().optional(),
                        "notifications_url": t.string().optional(),
                        "pulls_url": t.string().optional(),
                        "releases_url": t.string().optional(),
                        "ssh_url": t.string().optional(),
                        "stargazers_url": t.string().optional(),
                        "statuses_url": t.string().optional(),
                        "subscribers_url": t.string().optional(),
                        "subscription_url": t.string().optional(),
                        "tags_url": t.string().optional(),
                        "teams_url": t.string().optional(),
                        "trees_url": t.string().optional(),
                        "clone_url": t.string().optional(),
                        "mirror_url": t.string().optional(),
                        "hooks_url": t.string().optional(),
                        "svn_url": t.string().optional(),
                        "homepage": t.string().optional(),
                        "language": t.string().optional(),
                        "forks_count": t.integer().optional(),
                        "stargazers_count": t.integer().optional(),
                        "watchers_count": t.integer().optional(),
                        "size": t.integer().optional(),
                        "default_branch": t.string().optional(),
                        "open_issues_count": t.integer().optional(),
                        "is_template": t.boolean().optional(),
                        "topics": t.array(t.string()).optional(),
                        "has_issues": t.boolean().optional(),
                        "has_projects": t.boolean().optional(),
                        "has_wiki": t.boolean().optional(),
                        "has_pages": t.boolean().optional(),
                        "has_downloads": t.boolean().optional(),
                        "archived": t.boolean().optional(),
                        "disabled": t.boolean().optional(),
                        "visibility": t.string().optional(),
                        "pushed_at": t.string().optional(),
                        "created_at": t.string().optional(),
                        "updated_at": t.string().optional(),
                        "permissions": t.struct(
                            {
                                "admin": t.boolean().optional(),
                                "maintain": t.boolean().optional(),
                                "push": t.boolean().optional(),
                                "triage": t.boolean().optional(),
                                "pull": t.boolean().optional(),
                            }
                        ).optional(),
                        "allow_rebase_merge": t.boolean().optional(),
                        "temp_clone_token": t.string().optional(),
                        "allow_squash_merge": t.boolean().optional(),
                        "delete_branch_on_merge": t.boolean().optional(),
                        "allow_update_branch": t.boolean().optional(),
                        "allow_merge_commit": t.boolean().optional(),
                        "subscribers_count": t.integer().optional(),
                        "network_count": t.integer().optional(),
                    }
                ).optional(),
                "temp_clone_token": t.string().optional(),
                "allow_squash_merge": t.boolean().optional(),
                "delete_branch_on_merge": t.boolean().optional(),
                "allow_merge_commit": t.boolean().optional(),
                "allow_forking": t.boolean().optional(),
                "subscribers_count": t.integer().optional(),
                "network_count": t.integer().optional(),
                "open_issues": t.integer(),
                "watchers": t.integer(),
                "master_branch": t.string().optional(),
                "starred_at": t.string().optional(),
            }
        )
        .optional()
        .named(renames["nullable_repository"])
    )
    types["minimal_repository"] = t.struct(
        {
            "id": t.integer(),
            "node_id": t.string(),
            "name": t.string(),
            "full_name": t.string(),
            "owner": t.proxy(renames["simple_user"]),
            "private": t.boolean(),
            "html_url": t.string(),
            "description": t.string().optional(),
            "fork": t.boolean(),
            "url": t.string(),
            "archive_url": t.string(),
            "assignees_url": t.string(),
            "blobs_url": t.string(),
            "branches_url": t.string(),
            "collaborators_url": t.string(),
            "comments_url": t.string(),
            "commits_url": t.string(),
            "compare_url": t.string(),
            "contents_url": t.string(),
            "contributors_url": t.string(),
            "deployments_url": t.string(),
            "downloads_url": t.string(),
            "events_url": t.string(),
            "forks_url": t.string(),
            "git_commits_url": t.string(),
            "git_refs_url": t.string(),
            "git_tags_url": t.string(),
            "git_url": t.string().optional(),
            "issue_comment_url": t.string(),
            "issue_events_url": t.string(),
            "issues_url": t.string(),
            "keys_url": t.string(),
            "labels_url": t.string(),
            "languages_url": t.string(),
            "merges_url": t.string(),
            "milestones_url": t.string(),
            "notifications_url": t.string(),
            "pulls_url": t.string(),
            "releases_url": t.string(),
            "ssh_url": t.string().optional(),
            "stargazers_url": t.string(),
            "statuses_url": t.string(),
            "subscribers_url": t.string(),
            "subscription_url": t.string(),
            "tags_url": t.string(),
            "teams_url": t.string(),
            "trees_url": t.string(),
            "clone_url": t.string().optional(),
            "mirror_url": t.string().optional(),
            "hooks_url": t.string(),
            "svn_url": t.string().optional(),
            "homepage": t.string().optional(),
            "language": t.string().optional(),
            "forks_count": t.integer().optional(),
            "stargazers_count": t.integer().optional(),
            "watchers_count": t.integer().optional(),
            "size": t.integer().optional(),
            "default_branch": t.string().optional(),
            "open_issues_count": t.integer().optional(),
            "is_template": t.boolean().optional(),
            "topics": t.array(t.string()).optional(),
            "has_issues": t.boolean().optional(),
            "has_projects": t.boolean().optional(),
            "has_wiki": t.boolean().optional(),
            "has_pages": t.boolean().optional(),
            "has_downloads": t.boolean().optional(),
            "archived": t.boolean().optional(),
            "disabled": t.boolean().optional(),
            "visibility": t.string().optional(),
            "pushed_at": t.string().optional(),
            "created_at": t.string().optional(),
            "updated_at": t.string().optional(),
            "permissions": t.struct(
                {
                    "admin": t.boolean().optional(),
                    "maintain": t.boolean().optional(),
                    "push": t.boolean().optional(),
                    "triage": t.boolean().optional(),
                    "pull": t.boolean().optional(),
                }
            ).optional(),
            "template_repository": t.proxy(renames["nullable_repository"]).optional(),
            "temp_clone_token": t.string().optional(),
            "delete_branch_on_merge": t.boolean().optional(),
            "subscribers_count": t.integer().optional(),
            "network_count": t.integer().optional(),
            "code_of_conduct": t.proxy(renames["code_of_conduct"]).optional(),
            "license": t.struct(
                {
                    "key": t.string().optional(),
                    "name": t.string().optional(),
                    "spdx_id": t.string().optional(),
                    "url": t.string().optional(),
                    "node_id": t.string().optional(),
                }
            ).optional(),
            "forks": t.integer().optional(),
            "open_issues": t.integer().optional(),
            "watchers": t.integer().optional(),
            "allow_forking": t.boolean().optional(),
        }
    ).named(renames["minimal_repository"])
    types["thread"] = t.struct(
        {
            "id": t.string(),
            "repository": t.proxy(renames["minimal_repository"]),
            "subject": t.struct(
                {
                    "title": t.string(),
                    "url": t.string(),
                    "latest_comment_url": t.string(),
                    "type": t.string(),
                }
            ),
            "reason": t.string(),
            "unread": t.boolean(),
            "updated_at": t.string(),
            "last_read_at": t.string().optional(),
            "url": t.string(),
            "subscription_url": t.string(),
        }
    ).named(renames["thread"])
    types["thread_subscription"] = t.struct(
        {
            "subscribed": t.boolean(),
            "ignored": t.boolean(),
            "reason": t.string().optional(),
            "created_at": t.string().optional(),
            "url": t.string(),
            "thread_url": t.string().optional(),
            "repository_url": t.string().optional(),
        }
    ).named(renames["thread_subscription"])
    types["organization_full"] = t.struct(
        {
            "login": t.string(),
            "id": t.integer(),
            "node_id": t.string(),
            "url": t.string(),
            "repos_url": t.string(),
            "events_url": t.string(),
            "hooks_url": t.string(),
            "issues_url": t.string(),
            "members_url": t.string(),
            "public_members_url": t.string(),
            "avatar_url": t.string(),
            "description": t.string().optional(),
            "name": t.string().optional(),
            "company": t.string().optional(),
            "blog": t.string().optional(),
            "location": t.string().optional(),
            "email": t.string().optional(),
            "twitter_username": t.string().optional(),
            "is_verified": t.boolean().optional(),
            "has_organization_projects": t.boolean(),
            "has_repository_projects": t.boolean(),
            "public_repos": t.integer(),
            "public_gists": t.integer(),
            "followers": t.integer(),
            "following": t.integer(),
            "html_url": t.string(),
            "created_at": t.string(),
            "type": t.string(),
            "total_private_repos": t.integer().optional(),
            "owned_private_repos": t.integer().optional(),
            "private_gists": t.integer().optional(),
            "disk_usage": t.integer().optional(),
            "collaborators": t.integer().optional(),
            "billing_email": t.string().optional(),
            "plan": t.struct(
                {
                    "name": t.string(),
                    "space": t.integer(),
                    "private_repos": t.integer(),
                    "filled_seats": t.integer().optional(),
                    "seats": t.integer().optional(),
                }
            ).optional(),
            "default_repository_permission": t.string().optional(),
            "members_can_create_repositories": t.boolean().optional(),
            "two_factor_requirement_enabled": t.boolean().optional(),
            "members_allowed_repository_creation_type": t.string().optional(),
            "members_can_create_public_repositories": t.boolean().optional(),
            "members_can_create_private_repositories": t.boolean().optional(),
            "members_can_create_internal_repositories": t.boolean().optional(),
            "members_can_create_pages": t.boolean().optional(),
            "members_can_create_public_pages": t.boolean().optional(),
            "members_can_create_private_pages": t.boolean().optional(),
            "members_can_fork_private_repositories": t.boolean().optional(),
            "updated_at": t.string(),
        }
    ).named(renames["organization_full"])
    types["enabled_repositories"] = t.string().named(renames["enabled_repositories"])
    types["actions_organization_permissions"] = t.struct(
        {
            "enabled_repositories": t.proxy(renames["enabled_repositories"]),
            "selected_repositories_url": t.string().optional(),
            "allowed_actions": t.proxy(renames["allowed_actions"]).optional(),
            "selected_actions_url": t.proxy(renames["selected_actions_url"]).optional(),
        }
    ).named(renames["actions_organization_permissions"])
    types["runner_groups_org"] = t.struct(
        {
            "id": t.number(),
            "name": t.string(),
            "visibility": t.string(),
            "default": t.boolean(),
            "selected_repositories_url": t.string().optional(),
            "runners_url": t.string(),
            "inherited": t.boolean(),
            "inherited_allows_public_repositories": t.boolean().optional(),
            "allows_public_repositories": t.boolean(),
        }
    ).named(renames["runner_groups_org"])
    types["organization_actions_secret"] = t.struct(
        {
            "name": t.string(),
            "created_at": t.string(),
            "updated_at": t.string(),
            "visibility": t.string(),
            "selected_repositories_url": t.string().optional(),
        }
    ).named(renames["organization_actions_secret"])
    types["actions_public_key"] = t.struct(
        {
            "key_id": t.string(),
            "key": t.string(),
            "id": t.integer().optional(),
            "url": t.string().optional(),
            "title": t.string().optional(),
            "created_at": t.string().optional(),
        }
    ).named(renames["actions_public_key"])
    types["empty_object"] = t.struct({}).named(renames["empty_object"])
    types["org_hook"] = t.struct(
        {
            "id": t.integer(),
            "url": t.string(),
            "ping_url": t.string(),
            "name": t.string(),
            "events": t.array(t.string()),
            "active": t.boolean(),
            "config": t.struct(
                {
                    "url": t.string().optional(),
                    "insecure_ssl": t.string().optional(),
                    "content_type": t.string().optional(),
                    "secret": t.string().optional(),
                }
            ),
            "updated_at": t.string(),
            "created_at": t.string(),
            "type": t.string(),
        }
    ).named(renames["org_hook"])
    types["org_membership"] = t.struct(
        {
            "url": t.string(),
            "state": t.string(),
            "role": t.string(),
            "organization_url": t.string(),
            "organization": t.proxy(renames["organization_simple"]),
            "user": t.proxy(renames["nullable_simple_user"]),
            "permissions": t.struct({"can_create_repository": t.boolean()}).optional(),
        }
    ).named(renames["org_membership"])
    types["org_pre_receive_hook"] = t.struct(
        {
            "id": t.integer().optional(),
            "name": t.string().optional(),
            "enforcement": t.string().optional(),
            "configuration_url": t.string().optional(),
            "allow_downstream_configuration": t.boolean().optional(),
        }
    ).named(renames["org_pre_receive_hook"])
    types["project"] = t.struct(
        {
            "owner_url": t.string(),
            "url": t.string(),
            "html_url": t.string(),
            "columns_url": t.string(),
            "id": t.integer(),
            "node_id": t.string(),
            "name": t.string(),
            "body": t.string().optional(),
            "number": t.integer(),
            "state": t.string(),
            "creator": t.proxy(renames["nullable_simple_user"]),
            "created_at": t.string(),
            "updated_at": t.string(),
            "organization_permission": t.string().optional(),
            "private": t.boolean().optional(),
        }
    ).named(renames["project"])
    types["nullable_team_simple"] = (
        t.struct(
            {
                "id": t.integer(),
                "node_id": t.string(),
                "url": t.string(),
                "members_url": t.string(),
                "name": t.string(),
                "description": t.string().optional(),
                "permission": t.string(),
                "privacy": t.string().optional(),
                "html_url": t.string(),
                "repositories_url": t.string(),
                "slug": t.string(),
                "ldap_dn": t.string().optional(),
            }
        )
        .optional()
        .named(renames["nullable_team_simple"])
    )
    types["team"] = t.struct(
        {
            "id": t.integer(),
            "node_id": t.string(),
            "name": t.string(),
            "slug": t.string(),
            "description": t.string().optional(),
            "privacy": t.string().optional(),
            "permission": t.string(),
            "permissions": t.struct(
                {
                    "pull": t.boolean(),
                    "triage": t.boolean(),
                    "push": t.boolean(),
                    "maintain": t.boolean(),
                    "admin": t.boolean(),
                }
            ).optional(),
            "url": t.string(),
            "html_url": t.string(),
            "members_url": t.string(),
            "repositories_url": t.string(),
            "parent": t.proxy(renames["nullable_team_simple"]),
        }
    ).named(renames["team"])
    types["team_full"] = t.struct(
        {
            "id": t.integer(),
            "node_id": t.string(),
            "url": t.string(),
            "html_url": t.string(),
            "name": t.string(),
            "slug": t.string(),
            "description": t.string().optional(),
            "privacy": t.string().optional(),
            "permission": t.string(),
            "members_url": t.string(),
            "repositories_url": t.string(),
            "parent": t.proxy(renames["nullable_team_simple"]).optional(),
            "members_count": t.integer(),
            "repos_count": t.integer(),
            "created_at": t.string(),
            "updated_at": t.string(),
            "organization": t.proxy(renames["organization_full"]),
            "ldap_dn": t.string().optional(),
        }
    ).named(renames["team_full"])
    types["team_discussion"] = t.struct(
        {
            "author": t.proxy(renames["nullable_simple_user"]),
            "body": t.string(),
            "body_html": t.string(),
            "body_version": t.string(),
            "comments_count": t.integer(),
            "comments_url": t.string(),
            "created_at": t.string(),
            "last_edited_at": t.string().optional(),
            "html_url": t.string(),
            "node_id": t.string(),
            "number": t.integer(),
            "pinned": t.boolean(),
            "private": t.boolean(),
            "team_url": t.string(),
            "title": t.string(),
            "updated_at": t.string(),
            "url": t.string(),
            "reactions": t.proxy(renames["reaction_rollup"]).optional(),
        }
    ).named(renames["team_discussion"])
    types["team_discussion_comment"] = t.struct(
        {
            "author": t.proxy(renames["nullable_simple_user"]),
            "body": t.string(),
            "body_html": t.string(),
            "body_version": t.string(),
            "created_at": t.string(),
            "last_edited_at": t.string().optional(),
            "discussion_url": t.string(),
            "html_url": t.string(),
            "node_id": t.string(),
            "number": t.integer(),
            "updated_at": t.string(),
            "url": t.string(),
            "reactions": t.proxy(renames["reaction_rollup"]).optional(),
        }
    ).named(renames["team_discussion_comment"])
    types["reaction"] = t.struct(
        {
            "id": t.integer(),
            "node_id": t.string(),
            "user": t.proxy(renames["nullable_simple_user"]),
            "content": t.string(),
            "created_at": t.string(),
        }
    ).named(renames["reaction"])
    types["team_membership"] = t.struct(
        {"url": t.string(), "role": t.string(), "state": t.string()}
    ).named(renames["team_membership"])
    types["team_project"] = t.struct(
        {
            "owner_url": t.string(),
            "url": t.string(),
            "html_url": t.string(),
            "columns_url": t.string(),
            "id": t.integer(),
            "node_id": t.string(),
            "name": t.string(),
            "body": t.string().optional(),
            "number": t.integer(),
            "state": t.string(),
            "creator": t.proxy(renames["simple_user"]),
            "created_at": t.string(),
            "updated_at": t.string(),
            "organization_permission": t.string().optional(),
            "private": t.boolean().optional(),
            "permissions": t.struct(
                {"read": t.boolean(), "write": t.boolean(), "admin": t.boolean()}
            ),
        }
    ).named(renames["team_project"])
    types["team_repository"] = t.struct(
        {
            "id": t.integer(),
            "node_id": t.string(),
            "name": t.string(),
            "full_name": t.string(),
            "license": t.proxy(renames["nullable_license_simple"]),
            "forks": t.integer(),
            "permissions": t.struct(
                {
                    "admin": t.boolean(),
                    "pull": t.boolean(),
                    "triage": t.boolean().optional(),
                    "push": t.boolean(),
                    "maintain": t.boolean().optional(),
                }
            ).optional(),
            "owner": t.proxy(renames["nullable_simple_user"]),
            "private": t.boolean(),
            "html_url": t.string(),
            "description": t.string().optional(),
            "fork": t.boolean(),
            "url": t.string(),
            "archive_url": t.string(),
            "assignees_url": t.string(),
            "blobs_url": t.string(),
            "branches_url": t.string(),
            "collaborators_url": t.string(),
            "comments_url": t.string(),
            "commits_url": t.string(),
            "compare_url": t.string(),
            "contents_url": t.string(),
            "contributors_url": t.string(),
            "deployments_url": t.string(),
            "downloads_url": t.string(),
            "events_url": t.string(),
            "forks_url": t.string(),
            "git_commits_url": t.string(),
            "git_refs_url": t.string(),
            "git_tags_url": t.string(),
            "git_url": t.string(),
            "issue_comment_url": t.string(),
            "issue_events_url": t.string(),
            "issues_url": t.string(),
            "keys_url": t.string(),
            "labels_url": t.string(),
            "languages_url": t.string(),
            "merges_url": t.string(),
            "milestones_url": t.string(),
            "notifications_url": t.string(),
            "pulls_url": t.string(),
            "releases_url": t.string(),
            "ssh_url": t.string(),
            "stargazers_url": t.string(),
            "statuses_url": t.string(),
            "subscribers_url": t.string(),
            "subscription_url": t.string(),
            "tags_url": t.string(),
            "teams_url": t.string(),
            "trees_url": t.string(),
            "clone_url": t.string(),
            "mirror_url": t.string().optional(),
            "hooks_url": t.string(),
            "svn_url": t.string(),
            "homepage": t.string().optional(),
            "language": t.string().optional(),
            "forks_count": t.integer(),
            "stargazers_count": t.integer(),
            "watchers_count": t.integer(),
            "size": t.integer(),
            "default_branch": t.string(),
            "open_issues_count": t.integer(),
            "is_template": t.boolean().optional(),
            "topics": t.array(t.string()).optional(),
            "has_issues": t.boolean(),
            "has_projects": t.boolean(),
            "has_wiki": t.boolean(),
            "has_pages": t.boolean(),
            "has_downloads": t.boolean(),
            "archived": t.boolean(),
            "disabled": t.boolean(),
            "visibility": t.string().optional(),
            "pushed_at": t.string().optional(),
            "created_at": t.string().optional(),
            "updated_at": t.string().optional(),
            "allow_rebase_merge": t.boolean().optional(),
            "template_repository": t.proxy(renames["nullable_repository"]).optional(),
            "temp_clone_token": t.string().optional(),
            "allow_squash_merge": t.boolean().optional(),
            "delete_branch_on_merge": t.boolean().optional(),
            "allow_merge_commit": t.boolean().optional(),
            "allow_forking": t.boolean().optional(),
            "subscribers_count": t.integer().optional(),
            "network_count": t.integer().optional(),
            "open_issues": t.integer(),
            "watchers": t.integer(),
            "master_branch": t.string().optional(),
        }
    ).named(renames["team_repository"])
    types["project_card"] = t.struct(
        {
            "url": t.string(),
            "id": t.integer(),
            "node_id": t.string(),
            "note": t.string().optional(),
            "creator": t.proxy(renames["nullable_simple_user"]),
            "created_at": t.string(),
            "updated_at": t.string(),
            "archived": t.boolean().optional(),
            "column_name": t.string().optional(),
            "project_id": t.string().optional(),
            "column_url": t.string(),
            "content_url": t.string().optional(),
            "project_url": t.string(),
        }
    ).named(renames["project_card"])
    types["project_column"] = t.struct(
        {
            "url": t.string(),
            "project_url": t.string(),
            "cards_url": t.string(),
            "id": t.integer(),
            "node_id": t.string(),
            "name": t.string(),
            "created_at": t.string(),
            "updated_at": t.string(),
        }
    ).named(renames["project_column"])
    types["project_collaborator_permission"] = t.struct(
        {"permission": t.string(), "user": t.proxy(renames["nullable_simple_user"])}
    ).named(renames["project_collaborator_permission"])
    types["rate_limit"] = t.struct(
        {
            "limit": t.integer(),
            "remaining": t.integer(),
            "reset": t.integer(),
            "used": t.integer(),
        }
    ).named(renames["rate_limit"])
    types["rate_limit_overview"] = t.struct(
        {
            "resources": t.struct(
                {
                    "core": t.proxy(renames["rate_limit"]),
                    "graphql": t.proxy(renames["rate_limit"]).optional(),
                    "search": t.proxy(renames["rate_limit"]),
                    "source_import": t.proxy(renames["rate_limit"]).optional(),
                    "integration_manifest": t.proxy(renames["rate_limit"]).optional(),
                    "code_scanning_upload": t.proxy(renames["rate_limit"]).optional(),
                    "actions_runner_registration": t.proxy(
                        renames["rate_limit"]
                    ).optional(),
                    "scim": t.proxy(renames["rate_limit"]).optional(),
                }
            ),
            "rate": t.proxy(renames["rate_limit"]),
        }
    ).named(renames["rate_limit_overview"])
    types["code_of_conduct_simple"] = t.struct(
        {
            "url": t.string(),
            "key": t.string(),
            "name": t.string(),
            "html_url": t.string().optional(),
        }
    ).named(renames["code_of_conduct_simple"])
    types["full_repository"] = t.struct(
        {
            "id": t.integer(),
            "node_id": t.string(),
            "name": t.string(),
            "full_name": t.string(),
            "owner": t.proxy(renames["simple_user"]),
            "private": t.boolean(),
            "html_url": t.string(),
            "description": t.string().optional(),
            "fork": t.boolean(),
            "url": t.string(),
            "archive_url": t.string(),
            "assignees_url": t.string(),
            "blobs_url": t.string(),
            "branches_url": t.string(),
            "collaborators_url": t.string(),
            "comments_url": t.string(),
            "commits_url": t.string(),
            "compare_url": t.string(),
            "contents_url": t.string(),
            "contributors_url": t.string(),
            "deployments_url": t.string(),
            "downloads_url": t.string(),
            "events_url": t.string(),
            "forks_url": t.string(),
            "git_commits_url": t.string(),
            "git_refs_url": t.string(),
            "git_tags_url": t.string(),
            "git_url": t.string(),
            "issue_comment_url": t.string(),
            "issue_events_url": t.string(),
            "issues_url": t.string(),
            "keys_url": t.string(),
            "labels_url": t.string(),
            "languages_url": t.string(),
            "merges_url": t.string(),
            "milestones_url": t.string(),
            "notifications_url": t.string(),
            "pulls_url": t.string(),
            "releases_url": t.string(),
            "ssh_url": t.string(),
            "stargazers_url": t.string(),
            "statuses_url": t.string(),
            "subscribers_url": t.string(),
            "subscription_url": t.string(),
            "tags_url": t.string(),
            "teams_url": t.string(),
            "trees_url": t.string(),
            "clone_url": t.string(),
            "mirror_url": t.string().optional(),
            "hooks_url": t.string(),
            "svn_url": t.string(),
            "homepage": t.string().optional(),
            "language": t.string().optional(),
            "forks_count": t.integer(),
            "stargazers_count": t.integer(),
            "watchers_count": t.integer(),
            "size": t.integer(),
            "default_branch": t.string(),
            "open_issues_count": t.integer(),
            "is_template": t.boolean().optional(),
            "topics": t.array(t.string()).optional(),
            "has_issues": t.boolean(),
            "has_projects": t.boolean(),
            "has_wiki": t.boolean(),
            "has_pages": t.boolean(),
            "has_downloads": t.boolean(),
            "archived": t.boolean(),
            "disabled": t.boolean(),
            "visibility": t.string().optional(),
            "pushed_at": t.string(),
            "created_at": t.string(),
            "updated_at": t.string(),
            "permissions": t.struct(
                {
                    "admin": t.boolean(),
                    "maintain": t.boolean().optional(),
                    "push": t.boolean(),
                    "triage": t.boolean().optional(),
                    "pull": t.boolean(),
                }
            ).optional(),
            "allow_rebase_merge": t.boolean().optional(),
            "template_repository": t.proxy(renames["nullable_repository"]).optional(),
            "temp_clone_token": t.string().optional(),
            "allow_squash_merge": t.boolean().optional(),
            "delete_branch_on_merge": t.boolean().optional(),
            "allow_merge_commit": t.boolean().optional(),
            "allow_forking": t.boolean().optional(),
            "subscribers_count": t.integer(),
            "network_count": t.integer(),
            "license": t.proxy(renames["nullable_license_simple"]),
            "organization": t.proxy(renames["nullable_simple_user"]).optional(),
            "parent": t.proxy(renames["repository"]).optional(),
            "source": t.proxy(renames["repository"]).optional(),
            "forks": t.integer(),
            "master_branch": t.string().optional(),
            "open_issues": t.integer(),
            "watchers": t.integer(),
            "anonymous_access_enabled": t.boolean().optional(),
            "code_of_conduct": t.proxy(renames["code_of_conduct_simple"]).optional(),
        }
    ).named(renames["full_repository"])
    types["artifact"] = t.struct(
        {
            "id": t.integer(),
            "node_id": t.string(),
            "name": t.string(),
            "size_in_bytes": t.integer(),
            "url": t.string(),
            "archive_download_url": t.string(),
            "expired": t.boolean(),
            "created_at": t.string().optional(),
            "expires_at": t.string().optional(),
            "updated_at": t.string().optional(),
        }
    ).named(renames["artifact"])
    types["job"] = t.struct(
        {
            "id": t.integer(),
            "run_id": t.integer(),
            "run_url": t.string(),
            "run_attempt": t.integer().optional(),
            "node_id": t.string(),
            "head_sha": t.string(),
            "url": t.string(),
            "html_url": t.string().optional(),
            "status": t.string(),
            "conclusion": t.string().optional(),
            "started_at": t.string(),
            "completed_at": t.string().optional(),
            "name": t.string(),
            "steps": t.array(
                t.struct(
                    {
                        "status": t.string(),
                        "conclusion": t.string().optional(),
                        "name": t.string(),
                        "number": t.integer(),
                        "started_at": t.string().optional(),
                        "completed_at": t.string().optional(),
                    }
                )
            ).optional(),
            "check_run_url": t.string(),
        }
    ).named(renames["job"])
    types["actions_enabled"] = t.boolean().named(renames["actions_enabled"])
    types["actions_repository_permissions"] = t.struct(
        {
            "enabled": t.proxy(renames["actions_enabled"]),
            "allowed_actions": t.proxy(renames["allowed_actions"]).optional(),
            "selected_actions_url": t.proxy(renames["selected_actions_url"]).optional(),
        }
    ).named(renames["actions_repository_permissions"])
    types["pull_request_minimal"] = t.struct(
        {
            "id": t.integer(),
            "number": t.integer(),
            "url": t.string(),
            "head": t.struct(
                {
                    "ref": t.string(),
                    "sha": t.string(),
                    "repo": t.struct(
                        {"id": t.integer(), "url": t.string(), "name": t.string()}
                    ),
                }
            ),
            "base": t.struct(
                {
                    "ref": t.string(),
                    "sha": t.string(),
                    "repo": t.struct(
                        {"id": t.integer(), "url": t.string(), "name": t.string()}
                    ),
                }
            ),
        }
    ).named(renames["pull_request_minimal"])
    types["nullable_simple_commit"] = (
        t.struct(
            {
                "id": t.string(),
                "tree_id": t.string(),
                "message": t.string(),
                "timestamp": t.string(),
                "author": t.struct(
                    {"name": t.string(), "email": t.string()}
                ).optional(),
                "committer": t.struct(
                    {"name": t.string(), "email": t.string()}
                ).optional(),
            }
        )
        .optional()
        .named(renames["nullable_simple_commit"])
    )
    types["workflow_run"] = t.struct(
        {
            "id": t.integer(),
            "name": t.string().optional(),
            "node_id": t.string(),
            "check_suite_id": t.integer().optional(),
            "check_suite_node_id": t.string().optional(),
            "head_branch": t.string().optional(),
            "head_sha": t.string(),
            "run_number": t.integer(),
            "run_attempt": t.integer().optional(),
            "event": t.string(),
            "status": t.string().optional(),
            "conclusion": t.string().optional(),
            "workflow_id": t.integer(),
            "url": t.string(),
            "html_url": t.string(),
            "pull_requests": t.array(
                t.proxy(renames["pull_request_minimal"])
            ).optional(),
            "created_at": t.string(),
            "updated_at": t.string(),
            "run_started_at": t.string().optional(),
            "jobs_url": t.string(),
            "logs_url": t.string(),
            "check_suite_url": t.string(),
            "artifacts_url": t.string(),
            "cancel_url": t.string(),
            "rerun_url": t.string(),
            "previous_attempt_url": t.string().optional(),
            "workflow_url": t.string(),
            "head_commit": t.proxy(renames["nullable_simple_commit"]),
            "repository": t.proxy(renames["minimal_repository"]),
            "head_repository": t.proxy(renames["minimal_repository"]),
            "head_repository_id": t.integer().optional(),
        }
    ).named(renames["workflow_run"])
    types["actions_secret"] = t.struct(
        {"name": t.string(), "created_at": t.string(), "updated_at": t.string()}
    ).named(renames["actions_secret"])
    types["workflow"] = t.struct(
        {
            "id": t.integer(),
            "node_id": t.string(),
            "name": t.string(),
            "path": t.string(),
            "state": t.string(),
            "created_at": t.string(),
            "updated_at": t.string(),
            "url": t.string(),
            "html_url": t.string(),
            "badge_url": t.string(),
            "deleted_at": t.string().optional(),
        }
    ).named(renames["workflow"])
    types["protected_branch_required_status_check"] = t.struct(
        {
            "url": t.string().optional(),
            "enforcement_level": t.string().optional(),
            "contexts": t.array(t.string()),
            "contexts_url": t.string().optional(),
            "strict": t.boolean().optional(),
        }
    ).named(renames["protected_branch_required_status_check"])
    types["protected_branch_admin_enforced"] = t.struct(
        {"url": t.string(), "enabled": t.boolean()}
    ).named(renames["protected_branch_admin_enforced"])
    types["protected_branch_pull_request_review"] = t.struct(
        {
            "url": t.string().optional(),
            "dismissal_restrictions": t.struct(
                {
                    "users": t.array(t.proxy(renames["simple_user"])).optional(),
                    "teams": t.array(t.proxy(renames["team"])).optional(),
                    "url": t.string().optional(),
                    "users_url": t.string().optional(),
                    "teams_url": t.string().optional(),
                }
            ).optional(),
            "dismiss_stale_reviews": t.boolean(),
            "require_code_owner_reviews": t.boolean(),
            "required_approving_review_count": t.integer().optional(),
        }
    ).named(renames["protected_branch_pull_request_review"])
    types["branch_restriction_policy"] = t.struct(
        {
            "url": t.string(),
            "users_url": t.string(),
            "teams_url": t.string(),
            "apps_url": t.string(),
            "users": t.array(
                t.struct(
                    {
                        "login": t.string().optional(),
                        "id": t.integer().optional(),
                        "node_id": t.string().optional(),
                        "avatar_url": t.string().optional(),
                        "gravatar_id": t.string().optional(),
                        "url": t.string().optional(),
                        "html_url": t.string().optional(),
                        "followers_url": t.string().optional(),
                        "following_url": t.string().optional(),
                        "gists_url": t.string().optional(),
                        "starred_url": t.string().optional(),
                        "subscriptions_url": t.string().optional(),
                        "organizations_url": t.string().optional(),
                        "repos_url": t.string().optional(),
                        "events_url": t.string().optional(),
                        "received_events_url": t.string().optional(),
                        "type": t.string().optional(),
                        "site_admin": t.boolean().optional(),
                    }
                )
            ),
            "teams": t.array(
                t.struct(
                    {
                        "id": t.integer().optional(),
                        "node_id": t.string().optional(),
                        "url": t.string().optional(),
                        "html_url": t.string().optional(),
                        "name": t.string().optional(),
                        "slug": t.string().optional(),
                        "description": t.string().optional(),
                        "privacy": t.string().optional(),
                        "permission": t.string().optional(),
                        "members_url": t.string().optional(),
                        "repositories_url": t.string().optional(),
                        "parent": t.string().optional(),
                    }
                )
            ),
            "apps": t.array(
                t.struct(
                    {
                        "id": t.integer().optional(),
                        "slug": t.string().optional(),
                        "node_id": t.string().optional(),
                        "owner": t.struct(
                            {
                                "login": t.string().optional(),
                                "id": t.integer().optional(),
                                "node_id": t.string().optional(),
                                "url": t.string().optional(),
                                "repos_url": t.string().optional(),
                                "events_url": t.string().optional(),
                                "hooks_url": t.string().optional(),
                                "issues_url": t.string().optional(),
                                "members_url": t.string().optional(),
                                "public_members_url": t.string().optional(),
                                "avatar_url": t.string().optional(),
                                "description": t.string().optional(),
                                "gravatar_id": t.string().optional(),
                                "html_url": t.string().optional(),
                                "followers_url": t.string().optional(),
                                "following_url": t.string().optional(),
                                "gists_url": t.string().optional(),
                                "starred_url": t.string().optional(),
                                "subscriptions_url": t.string().optional(),
                                "organizations_url": t.string().optional(),
                                "received_events_url": t.string().optional(),
                                "type": t.string().optional(),
                                "site_admin": t.boolean().optional(),
                            }
                        ).optional(),
                        "name": t.string().optional(),
                        "description": t.string().optional(),
                        "external_url": t.string().optional(),
                        "html_url": t.string().optional(),
                        "created_at": t.string().optional(),
                        "updated_at": t.string().optional(),
                        "permissions": t.struct(
                            {
                                "metadata": t.string().optional(),
                                "contents": t.string().optional(),
                                "issues": t.string().optional(),
                                "single_file": t.string().optional(),
                            }
                        ).optional(),
                        "events": t.array(t.string()).optional(),
                    }
                )
            ),
        }
    ).named(renames["branch_restriction_policy"])
    types["branch_protection"] = t.struct(
        {
            "url": t.string().optional(),
            "enabled": t.boolean().optional(),
            "required_status_checks": t.proxy(
                renames["protected_branch_required_status_check"]
            ).optional(),
            "enforce_admins": t.proxy(
                renames["protected_branch_admin_enforced"]
            ).optional(),
            "required_pull_request_reviews": t.proxy(
                renames["protected_branch_pull_request_review"]
            ).optional(),
            "restrictions": t.proxy(renames["branch_restriction_policy"]).optional(),
            "required_linear_history": t.struct(
                {"enabled": t.boolean().optional()}
            ).optional(),
            "allow_force_pushes": t.struct(
                {"enabled": t.boolean().optional()}
            ).optional(),
            "allow_deletions": t.struct({"enabled": t.boolean().optional()}).optional(),
            "required_conversation_resolution": t.struct(
                {"enabled": t.boolean().optional()}
            ).optional(),
            "name": t.string().optional(),
            "protection_url": t.string().optional(),
            "required_signatures": t.struct(
                {"url": t.string(), "enabled": t.boolean()}
            ).optional(),
        }
    ).named(renames["branch_protection"])
    types["short_branch"] = t.struct(
        {
            "name": t.string(),
            "commit": t.struct({"sha": t.string(), "url": t.string()}),
            "protected": t.boolean(),
            "protection": t.proxy(renames["branch_protection"]).optional(),
            "protection_url": t.string().optional(),
        }
    ).named(renames["short_branch"])
    types["nullable_git_user"] = (
        t.struct(
            {
                "name": t.string().optional(),
                "email": t.string().optional(),
                "date": t.string().optional(),
            }
        )
        .optional()
        .named(renames["nullable_git_user"])
    )
    types["verification"] = t.struct(
        {
            "verified": t.boolean(),
            "reason": t.string(),
            "payload": t.string().optional(),
            "signature": t.string().optional(),
        }
    ).named(renames["verification"])
    types["diff_entry"] = t.struct(
        {
            "sha": t.string(),
            "filename": t.string(),
            "status": t.string(),
            "additions": t.integer(),
            "deletions": t.integer(),
            "changes": t.integer(),
            "blob_url": t.string(),
            "raw_url": t.string(),
            "contents_url": t.string(),
            "patch": t.string().optional(),
            "previous_filename": t.string().optional(),
        }
    ).named(renames["diff_entry"])
    types["commit"] = t.struct(
        {
            "url": t.string(),
            "sha": t.string(),
            "node_id": t.string(),
            "html_url": t.string(),
            "comments_url": t.string(),
            "commit": t.struct(
                {
                    "url": t.string(),
                    "author": t.proxy(renames["nullable_git_user"]),
                    "committer": t.proxy(renames["nullable_git_user"]),
                    "message": t.string(),
                    "comment_count": t.integer(),
                    "tree": t.struct({"sha": t.string(), "url": t.string()}),
                    "verification": t.proxy(renames["verification"]).optional(),
                }
            ),
            "author": t.proxy(renames["nullable_simple_user"]),
            "committer": t.proxy(renames["nullable_simple_user"]),
            "parents": t.array(
                t.struct(
                    {
                        "sha": t.string(),
                        "url": t.string(),
                        "html_url": t.string().optional(),
                    }
                )
            ),
            "stats": t.struct(
                {
                    "additions": t.integer().optional(),
                    "deletions": t.integer().optional(),
                    "total": t.integer().optional(),
                }
            ).optional(),
            "files": t.array(t.proxy(renames["diff_entry"])).optional(),
        }
    ).named(renames["commit"])
    types["branch_with_protection"] = t.struct(
        {
            "name": t.string(),
            "commit": t.proxy(renames["commit"]),
            "_links": t.struct({"html": t.string(), "self": t.string()}),
            "protected": t.boolean(),
            "protection": t.proxy(renames["branch_protection"]),
            "protection_url": t.string(),
            "pattern": t.string().optional(),
            "required_approving_review_count": t.integer().optional(),
        }
    ).named(renames["branch_with_protection"])
    types["status_check_policy"] = t.struct(
        {
            "url": t.string(),
            "strict": t.boolean(),
            "contexts": t.array(t.string()),
            "contexts_url": t.string(),
        }
    ).named(renames["status_check_policy"])
    types["protected_branch"] = t.struct(
        {
            "url": t.string(),
            "required_status_checks": t.proxy(
                renames["status_check_policy"]
            ).optional(),
            "required_pull_request_reviews": t.struct(
                {
                    "url": t.string(),
                    "dismiss_stale_reviews": t.boolean().optional(),
                    "require_code_owner_reviews": t.boolean().optional(),
                    "required_approving_review_count": t.integer().optional(),
                    "dismissal_restrictions": t.struct(
                        {
                            "url": t.string(),
                            "users_url": t.string(),
                            "teams_url": t.string(),
                            "users": t.array(t.proxy(renames["simple_user"])),
                            "teams": t.array(t.proxy(renames["team"])),
                        }
                    ).optional(),
                }
            ).optional(),
            "required_signatures": t.struct(
                {"url": t.string(), "enabled": t.boolean()}
            ).optional(),
            "enforce_admins": t.struct(
                {"url": t.string(), "enabled": t.boolean()}
            ).optional(),
            "required_linear_history": t.struct({"enabled": t.boolean()}).optional(),
            "allow_force_pushes": t.struct({"enabled": t.boolean()}).optional(),
            "allow_deletions": t.struct({"enabled": t.boolean()}).optional(),
            "restrictions": t.proxy(renames["branch_restriction_policy"]).optional(),
            "required_conversation_resolution": t.struct(
                {"enabled": t.boolean().optional()}
            ).optional(),
        }
    ).named(renames["protected_branch"])
    types["deployment_simple"] = t.struct(
        {
            "url": t.string(),
            "id": t.integer(),
            "node_id": t.string(),
            "task": t.string(),
            "original_environment": t.string().optional(),
            "environment": t.string(),
            "description": t.string().optional(),
            "created_at": t.string(),
            "updated_at": t.string(),
            "statuses_url": t.string(),
            "repository_url": t.string(),
            "transient_environment": t.boolean().optional(),
            "production_environment": t.boolean().optional(),
            "performed_via_github_app": t.proxy(
                renames["nullable_integration"]
            ).optional(),
        }
    ).named(renames["deployment_simple"])
    types["check_run"] = t.struct(
        {
            "id": t.integer(),
            "head_sha": t.string(),
            "node_id": t.string(),
            "external_id": t.string().optional(),
            "url": t.string(),
            "html_url": t.string().optional(),
            "details_url": t.string().optional(),
            "status": t.string(),
            "conclusion": t.string().optional(),
            "started_at": t.string().optional(),
            "completed_at": t.string().optional(),
            "output": t.struct(
                {
                    "title": t.string().optional(),
                    "summary": t.string().optional(),
                    "text": t.string().optional(),
                    "annotations_count": t.integer(),
                    "annotations_url": t.string(),
                }
            ),
            "name": t.string(),
            "check_suite": t.struct({"id": t.integer()}).optional(),
            "app": t.proxy(renames["nullable_integration"]),
            "pull_requests": t.array(t.proxy(renames["pull_request_minimal"])),
            "deployment": t.proxy(renames["deployment_simple"]).optional(),
        }
    ).named(renames["check_run"])
    types["check_annotation"] = t.struct(
        {
            "path": t.string(),
            "start_line": t.integer(),
            "end_line": t.integer(),
            "start_column": t.integer().optional(),
            "end_column": t.integer().optional(),
            "annotation_level": t.string().optional(),
            "title": t.string().optional(),
            "message": t.string().optional(),
            "raw_details": t.string().optional(),
            "blob_href": t.string(),
        }
    ).named(renames["check_annotation"])
    types["simple_commit"] = t.struct(
        {
            "id": t.string(),
            "tree_id": t.string(),
            "message": t.string(),
            "timestamp": t.string(),
            "author": t.struct({"name": t.string(), "email": t.string()}).optional(),
            "committer": t.struct({"name": t.string(), "email": t.string()}).optional(),
        }
    ).named(renames["simple_commit"])
    types["check_suite"] = t.struct(
        {
            "id": t.integer(),
            "node_id": t.string(),
            "head_branch": t.string().optional(),
            "head_sha": t.string(),
            "status": t.string().optional(),
            "conclusion": t.string().optional(),
            "url": t.string().optional(),
            "before": t.string().optional(),
            "after": t.string().optional(),
            "pull_requests": t.array(
                t.proxy(renames["pull_request_minimal"])
            ).optional(),
            "app": t.proxy(renames["nullable_integration"]),
            "repository": t.proxy(renames["minimal_repository"]),
            "created_at": t.string().optional(),
            "updated_at": t.string().optional(),
            "head_commit": t.proxy(renames["simple_commit"]),
            "latest_check_runs_count": t.integer(),
            "check_runs_url": t.string(),
            "rerequestable": t.boolean().optional(),
            "runs_rerequestable": t.boolean().optional(),
        }
    ).named(renames["check_suite"])
    types["check_suite_preference"] = t.struct(
        {
            "preferences": t.struct(
                {
                    "auto_trigger_checks": t.array(
                        t.struct({"app_id": t.integer(), "setting": t.boolean()})
                    ).optional()
                }
            ),
            "repository": t.proxy(renames["minimal_repository"]),
        }
    ).named(renames["check_suite_preference"])
    types["code_scanning_analysis_tool_name"] = t.string().named(
        renames["code_scanning_analysis_tool_name"]
    )
    types["code_scanning_analysis_tool_guid"] = (
        t.string().optional().named(renames["code_scanning_analysis_tool_guid"])
    )
    types["code_scanning_ref"] = t.string().named(renames["code_scanning_ref"])
    types["code_scanning_alert_state"] = t.string().named(
        renames["code_scanning_alert_state"]
    )
    types["alert_number"] = t.integer().named(renames["alert_number"])
    types["alert_created_at"] = t.string().named(renames["alert_created_at"])
    types["alert_url"] = t.string().named(renames["alert_url"])
    types["alert_html_url"] = t.string().named(renames["alert_html_url"])
    types["alert_instances_url"] = t.string().named(renames["alert_instances_url"])
    types["code_scanning_alert_dismissed_at"] = (
        t.string().optional().named(renames["code_scanning_alert_dismissed_at"])
    )
    types["code_scanning_alert_dismissed_reason"] = (
        t.string().optional().named(renames["code_scanning_alert_dismissed_reason"])
    )
    types["code_scanning_alert_rule_summary"] = t.struct(
        {
            "id": t.string().optional(),
            "name": t.string().optional(),
            "severity": t.string().optional(),
            "description": t.string().optional(),
        }
    ).named(renames["code_scanning_alert_rule_summary"])
    types["code_scanning_analysis_tool_version"] = (
        t.string().optional().named(renames["code_scanning_analysis_tool_version"])
    )
    types["code_scanning_analysis_tool"] = t.struct(
        {
            "name": t.proxy(renames["code_scanning_analysis_tool_name"]).optional(),
            "version": t.proxy(
                renames["code_scanning_analysis_tool_version"]
            ).optional(),
            "guid": t.proxy(renames["code_scanning_analysis_tool_guid"]).optional(),
        }
    ).named(renames["code_scanning_analysis_tool"])
    types["code_scanning_analysis_analysis_key"] = t.string().named(
        renames["code_scanning_analysis_analysis_key"]
    )
    types["code_scanning_alert_environment"] = t.string().named(
        renames["code_scanning_alert_environment"]
    )
    types["code_scanning_analysis_category"] = t.string().named(
        renames["code_scanning_analysis_category"]
    )
    types["code_scanning_alert_location"] = t.struct(
        {
            "path": t.string().optional(),
            "start_line": t.integer().optional(),
            "end_line": t.integer().optional(),
            "start_column": t.integer().optional(),
            "end_column": t.integer().optional(),
        }
    ).named(renames["code_scanning_alert_location"])
    types["code_scanning_alert_classification"] = (
        t.string().optional().named(renames["code_scanning_alert_classification"])
    )
    types["code_scanning_alert_instance"] = t.struct(
        {
            "ref": t.proxy(renames["code_scanning_ref"]).optional(),
            "analysis_key": t.proxy(
                renames["code_scanning_analysis_analysis_key"]
            ).optional(),
            "environment": t.proxy(
                renames["code_scanning_alert_environment"]
            ).optional(),
            "category": t.proxy(renames["code_scanning_analysis_category"]).optional(),
            "state": t.proxy(renames["code_scanning_alert_state"]).optional(),
            "commit_sha": t.string().optional(),
            "message": t.struct({"text": t.string().optional()}).optional(),
            "location": t.proxy(renames["code_scanning_alert_location"]).optional(),
            "html_url": t.string().optional(),
            "classifications": t.array(
                t.proxy(renames["code_scanning_alert_classification"])
            ).optional(),
        }
    ).named(renames["code_scanning_alert_instance"])
    types["code_scanning_alert_items"] = t.struct(
        {
            "number": t.proxy(renames["alert_number"]),
            "created_at": t.proxy(renames["alert_created_at"]),
            "url": t.proxy(renames["alert_url"]),
            "html_url": t.proxy(renames["alert_html_url"]),
            "instances_url": t.proxy(renames["alert_instances_url"]),
            "state": t.proxy(renames["code_scanning_alert_state"]),
            "dismissed_by": t.proxy(renames["nullable_simple_user"]),
            "dismissed_at": t.proxy(renames["code_scanning_alert_dismissed_at"]),
            "dismissed_reason": t.proxy(
                renames["code_scanning_alert_dismissed_reason"]
            ),
            "rule": t.proxy(renames["code_scanning_alert_rule_summary"]),
            "tool": t.proxy(renames["code_scanning_analysis_tool"]),
            "most_recent_instance": t.proxy(renames["code_scanning_alert_instance"]),
        }
    ).named(renames["code_scanning_alert_items"])
    types["code_scanning_alert_rule"] = t.struct(
        {
            "id": t.string().optional(),
            "name": t.string().optional(),
            "severity": t.string().optional(),
            "description": t.string().optional(),
            "full_description": t.string().optional(),
            "tags": t.array(t.string()).optional(),
            "help": t.string().optional(),
        }
    ).named(renames["code_scanning_alert_rule"])
    types["code_scanning_alert"] = t.struct(
        {
            "number": t.proxy(renames["alert_number"]),
            "created_at": t.proxy(renames["alert_created_at"]),
            "url": t.proxy(renames["alert_url"]),
            "html_url": t.proxy(renames["alert_html_url"]),
            "instances_url": t.proxy(renames["alert_instances_url"]),
            "state": t.proxy(renames["code_scanning_alert_state"]),
            "dismissed_by": t.proxy(renames["nullable_simple_user"]),
            "dismissed_at": t.proxy(renames["code_scanning_alert_dismissed_at"]),
            "dismissed_reason": t.proxy(
                renames["code_scanning_alert_dismissed_reason"]
            ),
            "rule": t.proxy(renames["code_scanning_alert_rule"]),
            "tool": t.proxy(renames["code_scanning_analysis_tool"]),
            "most_recent_instance": t.proxy(renames["code_scanning_alert_instance"]),
            "instances": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["code_scanning_alert"])
    types["code_scanning_alert_set_state"] = t.string().named(
        renames["code_scanning_alert_set_state"]
    )
    types["code_scanning_analysis_sarif_id"] = t.string().named(
        renames["code_scanning_analysis_sarif_id"]
    )
    types["code_scanning_analysis_commit_sha"] = t.string().named(
        renames["code_scanning_analysis_commit_sha"]
    )
    types["code_scanning_analysis_environment"] = t.string().named(
        renames["code_scanning_analysis_environment"]
    )
    types["code_scanning_analysis_created_at"] = t.string().named(
        renames["code_scanning_analysis_created_at"]
    )
    types["code_scanning_analysis_url"] = t.string().named(
        renames["code_scanning_analysis_url"]
    )
    types["code_scanning_analysis"] = t.struct(
        {
            "ref": t.proxy(renames["code_scanning_ref"]),
            "commit_sha": t.proxy(renames["code_scanning_analysis_commit_sha"]),
            "analysis_key": t.proxy(renames["code_scanning_analysis_analysis_key"]),
            "environment": t.proxy(renames["code_scanning_analysis_environment"]),
            "category": t.proxy(renames["code_scanning_analysis_category"]).optional(),
            "error": t.string(),
            "created_at": t.proxy(renames["code_scanning_analysis_created_at"]),
            "results_count": t.integer(),
            "rules_count": t.integer(),
            "id": t.integer(),
            "url": t.proxy(renames["code_scanning_analysis_url"]),
            "sarif_id": t.proxy(renames["code_scanning_analysis_sarif_id"]),
            "tool": t.proxy(renames["code_scanning_analysis_tool"]),
            "deletable": t.boolean(),
            "warning": t.string(),
            "tool_name": t.string().optional(),
        }
    ).named(renames["code_scanning_analysis"])
    types["code_scanning_analysis_sarif_file"] = t.string().named(
        renames["code_scanning_analysis_sarif_file"]
    )
    types["code_scanning_sarifs_receipt"] = t.struct(
        {
            "id": t.proxy(renames["code_scanning_analysis_sarif_id"]).optional(),
            "url": t.string().optional(),
        }
    ).named(renames["code_scanning_sarifs_receipt"])
    types["collaborator"] = t.struct(
        {
            "login": t.string(),
            "id": t.integer(),
            "email": t.string().optional(),
            "name": t.string().optional(),
            "node_id": t.string(),
            "avatar_url": t.string(),
            "gravatar_id": t.string().optional(),
            "url": t.string(),
            "html_url": t.string(),
            "followers_url": t.string(),
            "following_url": t.string(),
            "gists_url": t.string(),
            "starred_url": t.string(),
            "subscriptions_url": t.string(),
            "organizations_url": t.string(),
            "repos_url": t.string(),
            "events_url": t.string(),
            "received_events_url": t.string(),
            "type": t.string(),
            "site_admin": t.boolean(),
            "permissions": t.struct(
                {
                    "pull": t.boolean(),
                    "triage": t.boolean().optional(),
                    "push": t.boolean(),
                    "maintain": t.boolean().optional(),
                    "admin": t.boolean(),
                }
            ).optional(),
        }
    ).named(renames["collaborator"])
    types["repository_invitation"] = t.struct(
        {
            "id": t.integer(),
            "repository": t.proxy(renames["minimal_repository"]),
            "invitee": t.proxy(renames["nullable_simple_user"]),
            "inviter": t.proxy(renames["nullable_simple_user"]),
            "permissions": t.string(),
            "created_at": t.string(),
            "expired": t.boolean().optional(),
            "url": t.string(),
            "html_url": t.string(),
            "node_id": t.string(),
        }
    ).named(renames["repository_invitation"])
    types["nullable_collaborator"] = (
        t.struct(
            {
                "login": t.string(),
                "id": t.integer(),
                "email": t.string().optional(),
                "name": t.string().optional(),
                "node_id": t.string(),
                "avatar_url": t.string(),
                "gravatar_id": t.string().optional(),
                "url": t.string(),
                "html_url": t.string(),
                "followers_url": t.string(),
                "following_url": t.string(),
                "gists_url": t.string(),
                "starred_url": t.string(),
                "subscriptions_url": t.string(),
                "organizations_url": t.string(),
                "repos_url": t.string(),
                "events_url": t.string(),
                "received_events_url": t.string(),
                "type": t.string(),
                "site_admin": t.boolean(),
                "permissions": t.struct(
                    {
                        "pull": t.boolean(),
                        "triage": t.boolean().optional(),
                        "push": t.boolean(),
                        "maintain": t.boolean().optional(),
                        "admin": t.boolean(),
                    }
                ).optional(),
            }
        )
        .optional()
        .named(renames["nullable_collaborator"])
    )
    types["repository_collaborator_permission"] = t.struct(
        {"permission": t.string(), "user": t.proxy(renames["nullable_collaborator"])}
    ).named(renames["repository_collaborator_permission"])
    types["commit_comment"] = t.struct(
        {
            "html_url": t.string(),
            "url": t.string(),
            "id": t.integer(),
            "node_id": t.string(),
            "body": t.string(),
            "path": t.string().optional(),
            "position": t.integer().optional(),
            "line": t.integer().optional(),
            "commit_id": t.string(),
            "user": t.proxy(renames["nullable_simple_user"]),
            "created_at": t.string(),
            "updated_at": t.string(),
            "author_association": t.proxy(renames["author_association"]),
            "reactions": t.proxy(renames["reaction_rollup"]).optional(),
        }
    ).named(renames["commit_comment"])
    types["scim_error"] = t.struct(
        {
            "message": t.string().optional(),
            "documentation_url": t.string().optional(),
            "detail": t.string().optional(),
            "status": t.integer().optional(),
            "scimType": t.string().optional(),
            "schemas": t.array(t.string()).optional(),
        }
    ).named(renames["scim_error"])
    types["branch_short"] = t.struct(
        {
            "name": t.string(),
            "commit": t.struct({"sha": t.string(), "url": t.string()}),
            "protected": t.boolean(),
        }
    ).named(renames["branch_short"])
    types["link"] = t.struct({"href": t.string()}).named(renames["link"])
    types["pull_request_simple"] = t.struct(
        {
            "url": t.string(),
            "id": t.integer(),
            "node_id": t.string(),
            "html_url": t.string(),
            "diff_url": t.string(),
            "patch_url": t.string(),
            "issue_url": t.string(),
            "commits_url": t.string(),
            "review_comments_url": t.string(),
            "review_comment_url": t.string(),
            "comments_url": t.string(),
            "statuses_url": t.string(),
            "number": t.integer(),
            "state": t.string(),
            "locked": t.boolean(),
            "title": t.string(),
            "user": t.proxy(renames["nullable_simple_user"]),
            "body": t.string().optional(),
            "labels": t.array(
                t.struct(
                    {
                        "id": t.integer(),
                        "node_id": t.string(),
                        "url": t.string(),
                        "name": t.string(),
                        "description": t.string(),
                        "color": t.string(),
                        "default": t.boolean(),
                    }
                )
            ),
            "milestone": t.proxy(renames["nullable_milestone"]),
            "active_lock_reason": t.string().optional(),
            "created_at": t.string(),
            "updated_at": t.string(),
            "closed_at": t.string().optional(),
            "merged_at": t.string().optional(),
            "merge_commit_sha": t.string().optional(),
            "assignee": t.proxy(renames["nullable_simple_user"]),
            "assignees": t.array(t.proxy(renames["simple_user"])).optional(),
            "requested_reviewers": t.array(t.proxy(renames["simple_user"])).optional(),
            "requested_teams": t.array(t.proxy(renames["team"])).optional(),
            "head": t.struct(
                {
                    "label": t.string(),
                    "ref": t.string(),
                    "repo": t.proxy(renames["repository"]),
                    "sha": t.string(),
                    "user": t.proxy(renames["nullable_simple_user"]),
                }
            ),
            "base": t.struct(
                {
                    "label": t.string(),
                    "ref": t.string(),
                    "repo": t.proxy(renames["repository"]),
                    "sha": t.string(),
                    "user": t.proxy(renames["nullable_simple_user"]),
                }
            ),
            "_links": t.struct(
                {
                    "comments": t.proxy(renames["link"]),
                    "commits": t.proxy(renames["link"]),
                    "statuses": t.proxy(renames["link"]),
                    "html": t.proxy(renames["link"]),
                    "issue": t.proxy(renames["link"]),
                    "review_comments": t.proxy(renames["link"]),
                    "review_comment": t.proxy(renames["link"]),
                    "self": t.proxy(renames["link"]),
                }
            ),
            "author_association": t.proxy(renames["author_association"]),
            "draft": t.boolean().optional(),
        }
    ).named(renames["pull_request_simple"])
    types["simple_commit_status"] = t.struct(
        {
            "description": t.string().optional(),
            "id": t.integer(),
            "node_id": t.string(),
            "state": t.string(),
            "context": t.string(),
            "target_url": t.string(),
            "required": t.boolean().optional(),
            "avatar_url": t.string().optional(),
            "url": t.string(),
            "created_at": t.string(),
            "updated_at": t.string(),
        }
    ).named(renames["simple_commit_status"])
    types["combined_commit_status"] = t.struct(
        {
            "state": t.string(),
            "statuses": t.array(t.proxy(renames["simple_commit_status"])),
            "sha": t.string(),
            "total_count": t.integer(),
            "repository": t.proxy(renames["minimal_repository"]),
            "commit_url": t.string(),
            "url": t.string(),
        }
    ).named(renames["combined_commit_status"])
    types["status"] = t.struct(
        {
            "url": t.string(),
            "avatar_url": t.string().optional(),
            "id": t.integer(),
            "node_id": t.string(),
            "state": t.string(),
            "description": t.string(),
            "target_url": t.string(),
            "context": t.string(),
            "created_at": t.string(),
            "updated_at": t.string(),
            "creator": t.proxy(renames["nullable_simple_user"]),
        }
    ).named(renames["status"])
    types["commit_comparison"] = t.struct(
        {
            "url": t.string(),
            "html_url": t.string(),
            "permalink_url": t.string(),
            "diff_url": t.string(),
            "patch_url": t.string(),
            "base_commit": t.proxy(renames["commit"]),
            "merge_base_commit": t.proxy(renames["commit"]),
            "status": t.string(),
            "ahead_by": t.integer(),
            "behind_by": t.integer(),
            "total_commits": t.integer(),
            "commits": t.array(t.proxy(renames["commit"])),
            "files": t.array(t.proxy(renames["diff_entry"])).optional(),
        }
    ).named(renames["commit_comparison"])
    types["content_reference_attachment"] = t.struct(
        {
            "id": t.integer(),
            "title": t.string(),
            "body": t.string(),
            "node_id": t.string().optional(),
        }
    ).named(renames["content_reference_attachment"])
    types["content_tree"] = t.struct(
        {
            "type": t.string(),
            "size": t.integer(),
            "name": t.string(),
            "path": t.string(),
            "sha": t.string(),
            "url": t.string(),
            "git_url": t.string().optional(),
            "html_url": t.string().optional(),
            "download_url": t.string().optional(),
            "entries": t.array(
                t.struct(
                    {
                        "type": t.string(),
                        "size": t.integer(),
                        "name": t.string(),
                        "path": t.string(),
                        "content": t.string().optional(),
                        "sha": t.string(),
                        "url": t.string(),
                        "git_url": t.string().optional(),
                        "html_url": t.string().optional(),
                        "download_url": t.string().optional(),
                        "_links": t.struct(
                            {
                                "git": t.string().optional(),
                                "html": t.string().optional(),
                                "self": t.string(),
                            }
                        ),
                    }
                )
            ).optional(),
            "_links": t.struct(
                {
                    "git": t.string().optional(),
                    "html": t.string().optional(),
                    "self": t.string(),
                }
            ),
        }
    ).named(renames["content_tree"])
    types["content_directory"] = t.array(
        t.struct(
            {
                "type": t.string(),
                "size": t.integer(),
                "name": t.string(),
                "path": t.string(),
                "content": t.string().optional(),
                "sha": t.string(),
                "url": t.string(),
                "git_url": t.string().optional(),
                "html_url": t.string().optional(),
                "download_url": t.string().optional(),
                "_links": t.struct(
                    {
                        "git": t.string().optional(),
                        "html": t.string().optional(),
                        "self": t.string(),
                    }
                ),
            }
        )
    ).named(renames["content_directory"])
    types["content_file"] = t.struct(
        {
            "type": t.string(),
            "encoding": t.string(),
            "size": t.integer(),
            "name": t.string(),
            "path": t.string(),
            "content": t.string(),
            "sha": t.string(),
            "url": t.string(),
            "git_url": t.string().optional(),
            "html_url": t.string().optional(),
            "download_url": t.string().optional(),
            "_links": t.struct(
                {
                    "git": t.string().optional(),
                    "html": t.string().optional(),
                    "self": t.string(),
                }
            ),
            "target": t.string().optional(),
            "submodule_git_url": t.string().optional(),
        }
    ).named(renames["content_file"])
    types["content_symlink"] = t.struct(
        {
            "type": t.string(),
            "target": t.string(),
            "size": t.integer(),
            "name": t.string(),
            "path": t.string(),
            "sha": t.string(),
            "url": t.string(),
            "git_url": t.string().optional(),
            "html_url": t.string().optional(),
            "download_url": t.string().optional(),
            "_links": t.struct(
                {
                    "git": t.string().optional(),
                    "html": t.string().optional(),
                    "self": t.string(),
                }
            ),
        }
    ).named(renames["content_symlink"])
    types["content_submodule"] = t.struct(
        {
            "type": t.string(),
            "submodule_git_url": t.string(),
            "size": t.integer(),
            "name": t.string(),
            "path": t.string(),
            "sha": t.string(),
            "url": t.string(),
            "git_url": t.string().optional(),
            "html_url": t.string().optional(),
            "download_url": t.string().optional(),
            "_links": t.struct(
                {
                    "git": t.string().optional(),
                    "html": t.string().optional(),
                    "self": t.string(),
                }
            ),
        }
    ).named(renames["content_submodule"])
    types["file_commit"] = t.struct(
        {
            "content": t.struct(
                {
                    "name": t.string().optional(),
                    "path": t.string().optional(),
                    "sha": t.string().optional(),
                    "size": t.integer().optional(),
                    "url": t.string().optional(),
                    "html_url": t.string().optional(),
                    "git_url": t.string().optional(),
                    "download_url": t.string().optional(),
                    "type": t.string().optional(),
                    "_links": t.struct(
                        {
                            "self": t.string().optional(),
                            "git": t.string().optional(),
                            "html": t.string().optional(),
                        }
                    ).optional(),
                }
            ).optional(),
            "commit": t.struct(
                {
                    "sha": t.string().optional(),
                    "node_id": t.string().optional(),
                    "url": t.string().optional(),
                    "html_url": t.string().optional(),
                    "author": t.struct(
                        {
                            "date": t.string().optional(),
                            "name": t.string().optional(),
                            "email": t.string().optional(),
                        }
                    ).optional(),
                    "committer": t.struct(
                        {
                            "date": t.string().optional(),
                            "name": t.string().optional(),
                            "email": t.string().optional(),
                        }
                    ).optional(),
                    "message": t.string().optional(),
                    "tree": t.struct(
                        {"url": t.string().optional(), "sha": t.string().optional()}
                    ).optional(),
                    "parents": t.array(
                        t.struct(
                            {
                                "url": t.string().optional(),
                                "html_url": t.string().optional(),
                                "sha": t.string().optional(),
                            }
                        )
                    ).optional(),
                    "verification": t.struct(
                        {
                            "verified": t.boolean().optional(),
                            "reason": t.string().optional(),
                            "signature": t.string().optional(),
                            "payload": t.string().optional(),
                        }
                    ).optional(),
                }
            ),
        }
    ).named(renames["file_commit"])
    types["contributor"] = t.struct(
        {
            "login": t.string().optional(),
            "id": t.integer().optional(),
            "node_id": t.string().optional(),
            "avatar_url": t.string().optional(),
            "gravatar_id": t.string().optional(),
            "url": t.string().optional(),
            "html_url": t.string().optional(),
            "followers_url": t.string().optional(),
            "following_url": t.string().optional(),
            "gists_url": t.string().optional(),
            "starred_url": t.string().optional(),
            "subscriptions_url": t.string().optional(),
            "organizations_url": t.string().optional(),
            "repos_url": t.string().optional(),
            "events_url": t.string().optional(),
            "received_events_url": t.string().optional(),
            "type": t.string(),
            "site_admin": t.boolean().optional(),
            "contributions": t.integer(),
            "email": t.string().optional(),
            "name": t.string().optional(),
        }
    ).named(renames["contributor"])
    types["deployment"] = t.struct(
        {
            "url": t.string(),
            "id": t.integer(),
            "node_id": t.string(),
            "sha": t.string(),
            "ref": t.string(),
            "task": t.string(),
            "payload": t.either([t.struct({}), t.string()]),
            "original_environment": t.string().optional(),
            "environment": t.string(),
            "description": t.string().optional(),
            "creator": t.proxy(renames["nullable_simple_user"]),
            "created_at": t.string(),
            "updated_at": t.string(),
            "statuses_url": t.string(),
            "repository_url": t.string(),
            "transient_environment": t.boolean().optional(),
            "production_environment": t.boolean().optional(),
            "performed_via_github_app": t.proxy(
                renames["nullable_integration"]
            ).optional(),
        }
    ).named(renames["deployment"])
    types["deployment_status"] = t.struct(
        {
            "url": t.string(),
            "id": t.integer(),
            "node_id": t.string(),
            "state": t.string(),
            "creator": t.proxy(renames["nullable_simple_user"]),
            "description": t.string(),
            "environment": t.string().optional(),
            "target_url": t.string(),
            "created_at": t.string(),
            "updated_at": t.string(),
            "deployment_url": t.string(),
            "repository_url": t.string(),
            "environment_url": t.string().optional(),
            "log_url": t.string().optional(),
            "performed_via_github_app": t.proxy(
                renames["nullable_integration"]
            ).optional(),
        }
    ).named(renames["deployment_status"])
    types["short_blob"] = t.struct({"url": t.string(), "sha": t.string()}).named(
        renames["short_blob"]
    )
    types["blob"] = t.struct(
        {
            "content": t.string(),
            "encoding": t.string(),
            "url": t.string(),
            "sha": t.string(),
            "size": t.integer().optional(),
            "node_id": t.string(),
            "highlighted_content": t.string().optional(),
        }
    ).named(renames["blob"])
    types["git_commit"] = t.struct(
        {
            "sha": t.string(),
            "node_id": t.string(),
            "url": t.string(),
            "author": t.struct(
                {"date": t.string(), "email": t.string(), "name": t.string()}
            ),
            "committer": t.struct(
                {"date": t.string(), "email": t.string(), "name": t.string()}
            ),
            "message": t.string(),
            "tree": t.struct({"sha": t.string(), "url": t.string()}),
            "parents": t.array(
                t.struct({"sha": t.string(), "url": t.string(), "html_url": t.string()})
            ),
            "verification": t.struct(
                {
                    "verified": t.boolean(),
                    "reason": t.string(),
                    "signature": t.string().optional(),
                    "payload": t.string().optional(),
                }
            ),
            "html_url": t.string(),
        }
    ).named(renames["git_commit"])
    types["git_ref"] = t.struct(
        {
            "ref": t.string(),
            "node_id": t.string(),
            "url": t.string(),
            "object": t.struct(
                {"type": t.string(), "sha": t.string(), "url": t.string()}
            ),
        }
    ).named(renames["git_ref"])
    types["git_tag"] = t.struct(
        {
            "node_id": t.string(),
            "tag": t.string(),
            "sha": t.string(),
            "url": t.string(),
            "message": t.string(),
            "tagger": t.struct(
                {"date": t.string(), "email": t.string(), "name": t.string()}
            ),
            "object": t.struct(
                {"sha": t.string(), "type": t.string(), "url": t.string()}
            ),
            "verification": t.proxy(renames["verification"]).optional(),
        }
    ).named(renames["git_tag"])
    types["git_tree"] = t.struct(
        {
            "sha": t.string(),
            "url": t.string(),
            "truncated": t.boolean(),
            "tree": t.array(
                t.struct(
                    {
                        "path": t.string().optional(),
                        "mode": t.string().optional(),
                        "type": t.string().optional(),
                        "sha": t.string().optional(),
                        "size": t.integer().optional(),
                        "url": t.string().optional(),
                    }
                )
            ),
        }
    ).named(renames["git_tree"])
    types["hook_response"] = t.struct(
        {
            "code": t.integer().optional(),
            "status": t.string().optional(),
            "message": t.string().optional(),
        }
    ).named(renames["hook_response"])
    types["hook"] = t.struct(
        {
            "type": t.string(),
            "id": t.integer(),
            "name": t.string(),
            "active": t.boolean(),
            "events": t.array(t.string()),
            "config": t.struct(
                {
                    "email": t.string().optional(),
                    "password": t.string().optional(),
                    "room": t.string().optional(),
                    "subdomain": t.string().optional(),
                    "url": t.proxy(renames["webhook_config_url"]).optional(),
                    "insecure_ssl": t.proxy(
                        renames["webhook_config_insecure_ssl"]
                    ).optional(),
                    "content_type": t.proxy(
                        renames["webhook_config_content_type"]
                    ).optional(),
                    "digest": t.string().optional(),
                    "secret": t.proxy(renames["webhook_config_secret"]).optional(),
                    "token": t.string().optional(),
                }
            ),
            "updated_at": t.string(),
            "created_at": t.string(),
            "url": t.string(),
            "test_url": t.string(),
            "ping_url": t.string(),
            "last_response": t.proxy(renames["hook_response"]),
        }
    ).named(renames["hook"])
    types["nullable_issue"] = (
        t.struct(
            {
                "id": t.integer(),
                "node_id": t.string(),
                "url": t.string(),
                "repository_url": t.string(),
                "labels_url": t.string(),
                "comments_url": t.string(),
                "events_url": t.string(),
                "html_url": t.string(),
                "number": t.integer(),
                "state": t.string(),
                "title": t.string(),
                "body": t.string().optional(),
                "user": t.proxy(renames["nullable_simple_user"]),
                "labels": t.array(
                    t.either(
                        [
                            t.string(),
                            t.struct(
                                {
                                    "id": t.integer().optional(),
                                    "node_id": t.string().optional(),
                                    "url": t.string().optional(),
                                    "name": t.string().optional(),
                                    "description": t.string().optional(),
                                    "color": t.string().optional(),
                                    "default": t.boolean().optional(),
                                }
                            ),
                        ]
                    )
                ),
                "assignee": t.proxy(renames["nullable_simple_user"]),
                "assignees": t.array(t.proxy(renames["simple_user"])).optional(),
                "milestone": t.proxy(renames["nullable_milestone"]),
                "locked": t.boolean(),
                "active_lock_reason": t.string().optional(),
                "comments": t.integer(),
                "pull_request": t.struct(
                    {
                        "merged_at": t.string().optional(),
                        "diff_url": t.string().optional(),
                        "html_url": t.string().optional(),
                        "patch_url": t.string().optional(),
                        "url": t.string().optional(),
                    }
                ).optional(),
                "closed_at": t.string().optional(),
                "created_at": t.string(),
                "updated_at": t.string(),
                "draft": t.boolean().optional(),
                "closed_by": t.proxy(renames["nullable_simple_user"]).optional(),
                "body_html": t.string().optional(),
                "body_text": t.string().optional(),
                "timeline_url": t.string().optional(),
                "repository": t.proxy(renames["repository"]).optional(),
                "performed_via_github_app": t.proxy(
                    renames["nullable_integration"]
                ).optional(),
                "author_association": t.proxy(renames["author_association"]),
                "reactions": t.proxy(renames["reaction_rollup"]).optional(),
            }
        )
        .optional()
        .named(renames["nullable_issue"])
    )
    types["issue_event_label"] = t.struct(
        {"name": t.string().optional(), "color": t.string().optional()}
    ).named(renames["issue_event_label"])
    types["issue_event_dismissed_review"] = t.struct(
        {
            "state": t.string(),
            "review_id": t.integer(),
            "dismissal_message": t.string().optional(),
            "dismissal_commit_id": t.string().optional(),
        }
    ).named(renames["issue_event_dismissed_review"])
    types["issue_event_milestone"] = t.struct({"title": t.string()}).named(
        renames["issue_event_milestone"]
    )
    types["issue_event_project_card"] = t.struct(
        {
            "url": t.string(),
            "id": t.integer(),
            "project_url": t.string(),
            "project_id": t.integer(),
            "column_name": t.string(),
            "previous_column_name": t.string().optional(),
        }
    ).named(renames["issue_event_project_card"])
    types["issue_event_rename"] = t.struct(
        {"from": t.string(), "to": t.string()}
    ).named(renames["issue_event_rename"])
    types["issue_event"] = t.struct(
        {
            "id": t.integer(),
            "node_id": t.string(),
            "url": t.string(),
            "actor": t.proxy(renames["nullable_simple_user"]),
            "event": t.string(),
            "commit_id": t.string().optional(),
            "commit_url": t.string().optional(),
            "created_at": t.string(),
            "issue": t.proxy(renames["nullable_issue"]).optional(),
            "label": t.proxy(renames["issue_event_label"]).optional(),
            "assignee": t.proxy(renames["nullable_simple_user"]).optional(),
            "assigner": t.proxy(renames["nullable_simple_user"]).optional(),
            "review_requester": t.proxy(renames["nullable_simple_user"]).optional(),
            "requested_reviewer": t.proxy(renames["nullable_simple_user"]).optional(),
            "requested_team": t.proxy(renames["team"]).optional(),
            "dismissed_review": t.proxy(
                renames["issue_event_dismissed_review"]
            ).optional(),
            "milestone": t.proxy(renames["issue_event_milestone"]).optional(),
            "project_card": t.proxy(renames["issue_event_project_card"]).optional(),
            "rename": t.proxy(renames["issue_event_rename"]).optional(),
            "author_association": t.proxy(renames["author_association"]).optional(),
            "lock_reason": t.string().optional(),
            "performed_via_github_app": t.proxy(
                renames["nullable_integration"]
            ).optional(),
        }
    ).named(renames["issue_event"])
    types["labeled_issue_event"] = t.struct(
        {
            "id": t.integer(),
            "node_id": t.string(),
            "url": t.string(),
            "actor": t.proxy(renames["simple_user"]),
            "event": t.string(),
            "commit_id": t.string().optional(),
            "commit_url": t.string().optional(),
            "created_at": t.string(),
            "performed_via_github_app": t.proxy(renames["nullable_integration"]),
            "label": t.struct({"name": t.string(), "color": t.string()}),
        }
    ).named(renames["labeled_issue_event"])
    types["unlabeled_issue_event"] = t.struct(
        {
            "id": t.integer(),
            "node_id": t.string(),
            "url": t.string(),
            "actor": t.proxy(renames["simple_user"]),
            "event": t.string(),
            "commit_id": t.string().optional(),
            "commit_url": t.string().optional(),
            "created_at": t.string(),
            "performed_via_github_app": t.proxy(renames["nullable_integration"]),
            "label": t.struct({"name": t.string(), "color": t.string()}),
        }
    ).named(renames["unlabeled_issue_event"])
    types["assigned_issue_event"] = t.struct(
        {
            "id": t.integer(),
            "node_id": t.string(),
            "url": t.string(),
            "actor": t.proxy(renames["simple_user"]),
            "event": t.string(),
            "commit_id": t.string().optional(),
            "commit_url": t.string().optional(),
            "created_at": t.string(),
            "performed_via_github_app": t.proxy(renames["integration"]),
            "assignee": t.proxy(renames["simple_user"]),
            "assigner": t.proxy(renames["simple_user"]),
        }
    ).named(renames["assigned_issue_event"])
    types["unassigned_issue_event"] = t.struct(
        {
            "id": t.integer(),
            "node_id": t.string(),
            "url": t.string(),
            "actor": t.proxy(renames["simple_user"]),
            "event": t.string(),
            "commit_id": t.string().optional(),
            "commit_url": t.string().optional(),
            "created_at": t.string(),
            "performed_via_github_app": t.proxy(renames["nullable_integration"]),
            "assignee": t.proxy(renames["simple_user"]),
            "assigner": t.proxy(renames["simple_user"]),
        }
    ).named(renames["unassigned_issue_event"])
    types["milestoned_issue_event"] = t.struct(
        {
            "id": t.integer(),
            "node_id": t.string(),
            "url": t.string(),
            "actor": t.proxy(renames["simple_user"]),
            "event": t.string(),
            "commit_id": t.string().optional(),
            "commit_url": t.string().optional(),
            "created_at": t.string(),
            "performed_via_github_app": t.proxy(renames["nullable_integration"]),
            "milestone": t.struct({"title": t.string()}),
        }
    ).named(renames["milestoned_issue_event"])
    types["demilestoned_issue_event"] = t.struct(
        {
            "id": t.integer(),
            "node_id": t.string(),
            "url": t.string(),
            "actor": t.proxy(renames["simple_user"]),
            "event": t.string(),
            "commit_id": t.string().optional(),
            "commit_url": t.string().optional(),
            "created_at": t.string(),
            "performed_via_github_app": t.proxy(renames["nullable_integration"]),
            "milestone": t.struct({"title": t.string()}),
        }
    ).named(renames["demilestoned_issue_event"])
    types["renamed_issue_event"] = t.struct(
        {
            "id": t.integer(),
            "node_id": t.string(),
            "url": t.string(),
            "actor": t.proxy(renames["simple_user"]),
            "event": t.string(),
            "commit_id": t.string().optional(),
            "commit_url": t.string().optional(),
            "created_at": t.string(),
            "performed_via_github_app": t.proxy(renames["nullable_integration"]),
            "rename": t.struct({"from": t.string(), "to": t.string()}),
        }
    ).named(renames["renamed_issue_event"])
    types["review_requested_issue_event"] = t.struct(
        {
            "id": t.integer(),
            "node_id": t.string(),
            "url": t.string(),
            "actor": t.proxy(renames["simple_user"]),
            "event": t.string(),
            "commit_id": t.string().optional(),
            "commit_url": t.string().optional(),
            "created_at": t.string(),
            "performed_via_github_app": t.proxy(renames["nullable_integration"]),
            "review_requester": t.proxy(renames["simple_user"]),
            "requested_team": t.proxy(renames["team"]).optional(),
            "requested_reviewer": t.proxy(renames["simple_user"]).optional(),
        }
    ).named(renames["review_requested_issue_event"])
    types["review_request_removed_issue_event"] = t.struct(
        {
            "id": t.integer(),
            "node_id": t.string(),
            "url": t.string(),
            "actor": t.proxy(renames["simple_user"]),
            "event": t.string(),
            "commit_id": t.string().optional(),
            "commit_url": t.string().optional(),
            "created_at": t.string(),
            "performed_via_github_app": t.proxy(renames["nullable_integration"]),
            "review_requester": t.proxy(renames["simple_user"]),
            "requested_team": t.proxy(renames["team"]).optional(),
            "requested_reviewer": t.proxy(renames["simple_user"]).optional(),
        }
    ).named(renames["review_request_removed_issue_event"])
    types["review_dismissed_issue_event"] = t.struct(
        {
            "id": t.integer(),
            "node_id": t.string(),
            "url": t.string(),
            "actor": t.proxy(renames["simple_user"]),
            "event": t.string(),
            "commit_id": t.string().optional(),
            "commit_url": t.string().optional(),
            "created_at": t.string(),
            "performed_via_github_app": t.proxy(renames["nullable_integration"]),
            "dismissed_review": t.struct(
                {
                    "state": t.string(),
                    "review_id": t.integer(),
                    "dismissal_message": t.string().optional(),
                    "dismissal_commit_id": t.string().optional(),
                }
            ),
        }
    ).named(renames["review_dismissed_issue_event"])
    types["locked_issue_event"] = t.struct(
        {
            "id": t.integer(),
            "node_id": t.string(),
            "url": t.string(),
            "actor": t.proxy(renames["simple_user"]),
            "event": t.string(),
            "commit_id": t.string().optional(),
            "commit_url": t.string().optional(),
            "created_at": t.string(),
            "performed_via_github_app": t.proxy(renames["nullable_integration"]),
            "lock_reason": t.string().optional(),
        }
    ).named(renames["locked_issue_event"])
    types["added_to_project_issue_event"] = t.struct(
        {
            "id": t.integer(),
            "node_id": t.string(),
            "url": t.string(),
            "actor": t.proxy(renames["simple_user"]),
            "event": t.string(),
            "commit_id": t.string().optional(),
            "commit_url": t.string().optional(),
            "created_at": t.string(),
            "performed_via_github_app": t.proxy(renames["nullable_integration"]),
            "project_card": t.struct(
                {
                    "id": t.integer(),
                    "url": t.string(),
                    "project_id": t.integer(),
                    "project_url": t.string(),
                    "column_name": t.string(),
                    "previous_column_name": t.string().optional(),
                }
            ).optional(),
        }
    ).named(renames["added_to_project_issue_event"])
    types["moved_column_in_project_issue_event"] = t.struct(
        {
            "id": t.integer(),
            "node_id": t.string(),
            "url": t.string(),
            "actor": t.proxy(renames["simple_user"]),
            "event": t.string(),
            "commit_id": t.string().optional(),
            "commit_url": t.string().optional(),
            "created_at": t.string(),
            "performed_via_github_app": t.proxy(renames["nullable_integration"]),
            "project_card": t.struct(
                {
                    "id": t.integer(),
                    "url": t.string(),
                    "project_id": t.integer(),
                    "project_url": t.string(),
                    "column_name": t.string(),
                    "previous_column_name": t.string().optional(),
                }
            ).optional(),
        }
    ).named(renames["moved_column_in_project_issue_event"])
    types["removed_from_project_issue_event"] = t.struct(
        {
            "id": t.integer(),
            "node_id": t.string(),
            "url": t.string(),
            "actor": t.proxy(renames["simple_user"]),
            "event": t.string(),
            "commit_id": t.string().optional(),
            "commit_url": t.string().optional(),
            "created_at": t.string(),
            "performed_via_github_app": t.proxy(renames["nullable_integration"]),
            "project_card": t.struct(
                {
                    "id": t.integer(),
                    "url": t.string(),
                    "project_id": t.integer(),
                    "project_url": t.string(),
                    "column_name": t.string(),
                    "previous_column_name": t.string().optional(),
                }
            ).optional(),
        }
    ).named(renames["removed_from_project_issue_event"])
    types["converted_note_to_issue_issue_event"] = t.struct(
        {
            "id": t.integer(),
            "node_id": t.string(),
            "url": t.string(),
            "actor": t.proxy(renames["simple_user"]),
            "event": t.string(),
            "commit_id": t.string().optional(),
            "commit_url": t.string().optional(),
            "created_at": t.string(),
            "performed_via_github_app": t.proxy(renames["integration"]),
            "project_card": t.struct(
                {
                    "id": t.integer(),
                    "url": t.string(),
                    "project_id": t.integer(),
                    "project_url": t.string(),
                    "column_name": t.string(),
                    "previous_column_name": t.string().optional(),
                }
            ).optional(),
        }
    ).named(renames["converted_note_to_issue_issue_event"])
    types["issue_event_for_issue"] = t.union(
        [
            t.proxy(renames["labeled_issue_event"]),
            t.proxy(renames["unlabeled_issue_event"]),
            t.proxy(renames["assigned_issue_event"]),
            t.proxy(renames["unassigned_issue_event"]),
            t.proxy(renames["milestoned_issue_event"]),
            t.proxy(renames["demilestoned_issue_event"]),
            t.proxy(renames["renamed_issue_event"]),
            t.proxy(renames["review_requested_issue_event"]),
            t.proxy(renames["review_request_removed_issue_event"]),
            t.proxy(renames["review_dismissed_issue_event"]),
            t.proxy(renames["locked_issue_event"]),
            t.proxy(renames["added_to_project_issue_event"]),
            t.proxy(renames["moved_column_in_project_issue_event"]),
            t.proxy(renames["removed_from_project_issue_event"]),
            t.proxy(renames["converted_note_to_issue_issue_event"]),
        ]
    ).named(renames["issue_event_for_issue"])
    types["label"] = t.struct(
        {
            "id": t.integer(),
            "node_id": t.string(),
            "url": t.string(),
            "name": t.string(),
            "description": t.string().optional(),
            "color": t.string(),
            "default": t.boolean(),
        }
    ).named(renames["label"])
    types["timeline_comment_event"] = t.struct(
        {
            "event": t.string(),
            "actor": t.proxy(renames["simple_user"]),
            "id": t.integer(),
            "node_id": t.string(),
            "url": t.string(),
            "body": t.string().optional(),
            "body_text": t.string().optional(),
            "body_html": t.string().optional(),
            "html_url": t.string(),
            "user": t.proxy(renames["simple_user"]),
            "created_at": t.string(),
            "updated_at": t.string(),
            "issue_url": t.string(),
            "author_association": t.proxy(renames["author_association"]),
            "performed_via_github_app": t.proxy(
                renames["nullable_integration"]
            ).optional(),
            "reactions": t.proxy(renames["reaction_rollup"]).optional(),
        }
    ).named(renames["timeline_comment_event"])
    types["timeline_cross_referenced_event"] = t.struct(
        {
            "event": t.string(),
            "actor": t.proxy(renames["simple_user"]).optional(),
            "created_at": t.string(),
            "updated_at": t.string(),
            "source": t.struct(
                {
                    "type": t.string().optional(),
                    "issue": t.proxy(renames["issue"]).optional(),
                }
            ),
        }
    ).named(renames["timeline_cross_referenced_event"])
    types["timeline_committed_event"] = t.struct(
        {
            "event": t.string().optional(),
            "sha": t.string(),
            "node_id": t.string(),
            "url": t.string(),
            "author": t.struct(
                {"date": t.string(), "email": t.string(), "name": t.string()}
            ),
            "committer": t.struct(
                {"date": t.string(), "email": t.string(), "name": t.string()}
            ),
            "message": t.string(),
            "tree": t.struct({"sha": t.string(), "url": t.string()}),
            "parents": t.array(
                t.struct({"sha": t.string(), "url": t.string(), "html_url": t.string()})
            ),
            "verification": t.struct(
                {
                    "verified": t.boolean(),
                    "reason": t.string(),
                    "signature": t.string().optional(),
                    "payload": t.string().optional(),
                }
            ),
            "html_url": t.string(),
        }
    ).named(renames["timeline_committed_event"])
    types["timeline_reviewed_event"] = t.struct(
        {
            "event": t.string(),
            "id": t.integer(),
            "node_id": t.string(),
            "user": t.proxy(renames["simple_user"]),
            "body": t.string().optional(),
            "state": t.string(),
            "html_url": t.string(),
            "pull_request_url": t.string(),
            "_links": t.struct(
                {
                    "html": t.struct({"href": t.string()}),
                    "pull_request": t.struct({"href": t.string()}),
                }
            ),
            "submitted_at": t.string().optional(),
            "commit_id": t.string(),
            "body_html": t.string().optional(),
            "body_text": t.string().optional(),
            "author_association": t.proxy(renames["author_association"]),
        }
    ).named(renames["timeline_reviewed_event"])
    types["pull_request_review_comment"] = t.struct(
        {
            "url": t.string(),
            "pull_request_review_id": t.integer().optional(),
            "id": t.integer(),
            "node_id": t.string(),
            "diff_hunk": t.string(),
            "path": t.string(),
            "position": t.integer(),
            "original_position": t.integer(),
            "commit_id": t.string(),
            "original_commit_id": t.string(),
            "in_reply_to_id": t.integer().optional(),
            "user": t.proxy(renames["simple_user"]),
            "body": t.string(),
            "created_at": t.string(),
            "updated_at": t.string(),
            "html_url": t.string(),
            "pull_request_url": t.string(),
            "author_association": t.proxy(renames["author_association"]),
            "_links": t.struct(
                {
                    "self": t.struct({"href": t.string()}),
                    "html": t.struct({"href": t.string()}),
                    "pull_request": t.struct({"href": t.string()}),
                }
            ),
            "start_line": t.integer().optional(),
            "original_start_line": t.integer().optional(),
            "start_side": t.string().optional(),
            "line": t.integer().optional(),
            "original_line": t.integer().optional(),
            "side": t.string().optional(),
            "reactions": t.proxy(renames["reaction_rollup"]).optional(),
            "body_html": t.string().optional(),
            "body_text": t.string().optional(),
        }
    ).named(renames["pull_request_review_comment"])
    types["timeline_line_commented_event"] = t.struct(
        {
            "event": t.string().optional(),
            "node_id": t.string().optional(),
            "comments": t.array(
                t.proxy(renames["pull_request_review_comment"])
            ).optional(),
        }
    ).named(renames["timeline_line_commented_event"])
    types["timeline_commit_commented_event"] = t.struct(
        {
            "event": t.string().optional(),
            "node_id": t.string().optional(),
            "commit_id": t.string().optional(),
            "comments": t.array(t.proxy(renames["commit_comment"])).optional(),
        }
    ).named(renames["timeline_commit_commented_event"])
    types["timeline_assigned_issue_event"] = t.struct(
        {
            "id": t.integer(),
            "node_id": t.string(),
            "url": t.string(),
            "actor": t.proxy(renames["simple_user"]),
            "event": t.string(),
            "commit_id": t.string().optional(),
            "commit_url": t.string().optional(),
            "created_at": t.string(),
            "performed_via_github_app": t.proxy(renames["nullable_integration"]),
            "assignee": t.proxy(renames["simple_user"]),
        }
    ).named(renames["timeline_assigned_issue_event"])
    types["timeline_unassigned_issue_event"] = t.struct(
        {
            "id": t.integer(),
            "node_id": t.string(),
            "url": t.string(),
            "actor": t.proxy(renames["simple_user"]),
            "event": t.string(),
            "commit_id": t.string().optional(),
            "commit_url": t.string().optional(),
            "created_at": t.string(),
            "performed_via_github_app": t.proxy(renames["nullable_integration"]),
            "assignee": t.proxy(renames["simple_user"]),
        }
    ).named(renames["timeline_unassigned_issue_event"])
    types["state_change_issue_event"] = t.struct(
        {
            "id": t.integer(),
            "node_id": t.string(),
            "url": t.string(),
            "actor": t.proxy(renames["simple_user"]),
            "event": t.string(),
            "commit_id": t.string().optional(),
            "commit_url": t.string().optional(),
            "created_at": t.string(),
            "performed_via_github_app": t.proxy(renames["nullable_integration"]),
        }
    ).named(renames["state_change_issue_event"])
    types["timeline_issue_events"] = t.union(
        [
            t.proxy(renames["labeled_issue_event"]),
            t.proxy(renames["unlabeled_issue_event"]),
            t.proxy(renames["milestoned_issue_event"]),
            t.proxy(renames["demilestoned_issue_event"]),
            t.proxy(renames["renamed_issue_event"]),
            t.proxy(renames["review_requested_issue_event"]),
            t.proxy(renames["review_request_removed_issue_event"]),
            t.proxy(renames["review_dismissed_issue_event"]),
            t.proxy(renames["locked_issue_event"]),
            t.proxy(renames["added_to_project_issue_event"]),
            t.proxy(renames["moved_column_in_project_issue_event"]),
            t.proxy(renames["removed_from_project_issue_event"]),
            t.proxy(renames["converted_note_to_issue_issue_event"]),
            t.proxy(renames["timeline_comment_event"]),
            t.proxy(renames["timeline_cross_referenced_event"]),
            t.proxy(renames["timeline_committed_event"]),
            t.proxy(renames["timeline_reviewed_event"]),
            t.proxy(renames["timeline_line_commented_event"]),
            t.proxy(renames["timeline_commit_commented_event"]),
            t.proxy(renames["timeline_assigned_issue_event"]),
            t.proxy(renames["timeline_unassigned_issue_event"]),
            t.proxy(renames["state_change_issue_event"]),
        ]
    ).named(renames["timeline_issue_events"])
    types["deploy_key"] = t.struct(
        {
            "id": t.integer(),
            "key": t.string(),
            "url": t.string(),
            "title": t.string(),
            "verified": t.boolean(),
            "created_at": t.string(),
            "read_only": t.boolean(),
        }
    ).named(renames["deploy_key"])
    types["language"] = t.struct({}).named(renames["language"])
    types["license_content"] = t.struct(
        {
            "name": t.string(),
            "path": t.string(),
            "sha": t.string(),
            "size": t.integer(),
            "url": t.string(),
            "html_url": t.string().optional(),
            "git_url": t.string().optional(),
            "download_url": t.string().optional(),
            "type": t.string(),
            "content": t.string(),
            "encoding": t.string(),
            "_links": t.struct(
                {
                    "git": t.string().optional(),
                    "html": t.string().optional(),
                    "self": t.string(),
                }
            ),
            "license": t.proxy(renames["nullable_license_simple"]),
        }
    ).named(renames["license_content"])
    types["milestone"] = t.struct(
        {
            "url": t.string(),
            "html_url": t.string(),
            "labels_url": t.string(),
            "id": t.integer(),
            "node_id": t.string(),
            "number": t.integer(),
            "state": t.string(),
            "title": t.string(),
            "description": t.string().optional(),
            "creator": t.proxy(renames["nullable_simple_user"]),
            "open_issues": t.integer(),
            "closed_issues": t.integer(),
            "created_at": t.string(),
            "updated_at": t.string(),
            "closed_at": t.string().optional(),
            "due_on": t.string().optional(),
        }
    ).named(renames["milestone"])
    types["pages_source_hash"] = t.struct(
        {"branch": t.string(), "path": t.string()}
    ).named(renames["pages_source_hash"])
    types["pages_https_certificate"] = t.struct(
        {
            "state": t.string(),
            "description": t.string(),
            "domains": t.array(t.string()),
            "expires_at": t.string().optional(),
        }
    ).named(renames["pages_https_certificate"])
    types["page"] = t.struct(
        {
            "url": t.string(),
            "status": t.string().optional(),
            "cname": t.string().optional(),
            "protected_domain_state": t.string().optional(),
            "pending_domain_unverified_at": t.string().optional(),
            "custom_404": t.boolean(),
            "html_url": t.string().optional(),
            "source": t.proxy(renames["pages_source_hash"]).optional(),
            "public": t.boolean(),
            "https_certificate": t.proxy(renames["pages_https_certificate"]).optional(),
            "https_enforced": t.boolean().optional(),
        }
    ).named(renames["page"])
    types["page_build"] = t.struct(
        {
            "url": t.string(),
            "status": t.string(),
            "error": t.struct({"message": t.string().optional()}),
            "pusher": t.proxy(renames["nullable_simple_user"]),
            "commit": t.string(),
            "duration": t.integer(),
            "created_at": t.string(),
            "updated_at": t.string(),
        }
    ).named(renames["page_build"])
    types["page_build_status"] = t.struct(
        {"url": t.string(), "status": t.string()}
    ).named(renames["page_build_status"])
    types["repository_pre_receive_hook"] = t.struct(
        {
            "id": t.integer().optional(),
            "name": t.string().optional(),
            "enforcement": t.string().optional(),
            "configuration_url": t.string().optional(),
        }
    ).named(renames["repository_pre_receive_hook"])
    types["team_simple"] = t.struct(
        {
            "id": t.integer(),
            "node_id": t.string(),
            "url": t.string(),
            "members_url": t.string(),
            "name": t.string(),
            "description": t.string().optional(),
            "permission": t.string(),
            "privacy": t.string().optional(),
            "html_url": t.string(),
            "repositories_url": t.string(),
            "slug": t.string(),
            "ldap_dn": t.string().optional(),
        }
    ).named(renames["team_simple"])
    types["pull_request"] = t.struct(
        {
            "url": t.string(),
            "id": t.integer(),
            "node_id": t.string(),
            "html_url": t.string(),
            "diff_url": t.string(),
            "patch_url": t.string(),
            "issue_url": t.string(),
            "commits_url": t.string(),
            "review_comments_url": t.string(),
            "review_comment_url": t.string(),
            "comments_url": t.string(),
            "statuses_url": t.string(),
            "number": t.integer(),
            "state": t.string(),
            "locked": t.boolean(),
            "title": t.string(),
            "user": t.proxy(renames["nullable_simple_user"]),
            "body": t.string().optional(),
            "labels": t.array(
                t.struct(
                    {
                        "id": t.integer(),
                        "node_id": t.string(),
                        "url": t.string(),
                        "name": t.string(),
                        "description": t.string().optional(),
                        "color": t.string(),
                        "default": t.boolean(),
                    }
                )
            ),
            "milestone": t.proxy(renames["nullable_milestone"]),
            "active_lock_reason": t.string().optional(),
            "created_at": t.string(),
            "updated_at": t.string(),
            "closed_at": t.string().optional(),
            "merged_at": t.string().optional(),
            "merge_commit_sha": t.string().optional(),
            "assignee": t.proxy(renames["nullable_simple_user"]),
            "assignees": t.array(t.proxy(renames["simple_user"])).optional(),
            "requested_reviewers": t.array(t.proxy(renames["simple_user"])).optional(),
            "requested_teams": t.array(t.proxy(renames["team_simple"])).optional(),
            "head": t.struct(
                {
                    "label": t.string(),
                    "ref": t.string(),
                    "repo": t.struct(
                        {
                            "archive_url": t.string(),
                            "assignees_url": t.string(),
                            "blobs_url": t.string(),
                            "branches_url": t.string(),
                            "collaborators_url": t.string(),
                            "comments_url": t.string(),
                            "commits_url": t.string(),
                            "compare_url": t.string(),
                            "contents_url": t.string(),
                            "contributors_url": t.string(),
                            "deployments_url": t.string(),
                            "description": t.string().optional(),
                            "downloads_url": t.string(),
                            "events_url": t.string(),
                            "fork": t.boolean(),
                            "forks_url": t.string(),
                            "full_name": t.string(),
                            "git_commits_url": t.string(),
                            "git_refs_url": t.string(),
                            "git_tags_url": t.string(),
                            "hooks_url": t.string(),
                            "html_url": t.string(),
                            "id": t.integer(),
                            "node_id": t.string(),
                            "issue_comment_url": t.string(),
                            "issue_events_url": t.string(),
                            "issues_url": t.string(),
                            "keys_url": t.string(),
                            "labels_url": t.string(),
                            "languages_url": t.string(),
                            "merges_url": t.string(),
                            "milestones_url": t.string(),
                            "name": t.string(),
                            "notifications_url": t.string(),
                            "owner": t.struct(
                                {
                                    "avatar_url": t.string(),
                                    "events_url": t.string(),
                                    "followers_url": t.string(),
                                    "following_url": t.string(),
                                    "gists_url": t.string(),
                                    "gravatar_id": t.string().optional(),
                                    "html_url": t.string(),
                                    "id": t.integer(),
                                    "node_id": t.string(),
                                    "login": t.string(),
                                    "organizations_url": t.string(),
                                    "received_events_url": t.string(),
                                    "repos_url": t.string(),
                                    "site_admin": t.boolean(),
                                    "starred_url": t.string(),
                                    "subscriptions_url": t.string(),
                                    "type": t.string(),
                                    "url": t.string(),
                                }
                            ),
                            "private": t.boolean(),
                            "pulls_url": t.string(),
                            "releases_url": t.string(),
                            "stargazers_url": t.string(),
                            "statuses_url": t.string(),
                            "subscribers_url": t.string(),
                            "subscription_url": t.string(),
                            "tags_url": t.string(),
                            "teams_url": t.string(),
                            "trees_url": t.string(),
                            "url": t.string(),
                            "clone_url": t.string(),
                            "default_branch": t.string(),
                            "forks": t.integer(),
                            "forks_count": t.integer(),
                            "git_url": t.string(),
                            "has_downloads": t.boolean(),
                            "has_issues": t.boolean(),
                            "has_projects": t.boolean(),
                            "has_wiki": t.boolean(),
                            "has_pages": t.boolean(),
                            "homepage": t.string().optional(),
                            "language": t.string().optional(),
                            "master_branch": t.string().optional(),
                            "archived": t.boolean(),
                            "disabled": t.boolean(),
                            "visibility": t.string().optional(),
                            "mirror_url": t.string().optional(),
                            "open_issues": t.integer(),
                            "open_issues_count": t.integer(),
                            "permissions": t.struct(
                                {
                                    "admin": t.boolean(),
                                    "maintain": t.boolean().optional(),
                                    "push": t.boolean(),
                                    "triage": t.boolean().optional(),
                                    "pull": t.boolean(),
                                }
                            ).optional(),
                            "temp_clone_token": t.string().optional(),
                            "allow_merge_commit": t.boolean().optional(),
                            "allow_squash_merge": t.boolean().optional(),
                            "allow_rebase_merge": t.boolean().optional(),
                            "license": t.struct(
                                {
                                    "key": t.string(),
                                    "name": t.string(),
                                    "url": t.string().optional(),
                                    "spdx_id": t.string().optional(),
                                    "node_id": t.string(),
                                }
                            ).optional(),
                            "pushed_at": t.string(),
                            "size": t.integer(),
                            "ssh_url": t.string(),
                            "stargazers_count": t.integer(),
                            "svn_url": t.string(),
                            "topics": t.array(t.string()).optional(),
                            "watchers": t.integer(),
                            "watchers_count": t.integer(),
                            "created_at": t.string(),
                            "updated_at": t.string(),
                            "allow_forking": t.boolean().optional(),
                            "is_template": t.boolean().optional(),
                        }
                    ).optional(),
                    "sha": t.string(),
                    "user": t.struct(
                        {
                            "avatar_url": t.string(),
                            "events_url": t.string(),
                            "followers_url": t.string(),
                            "following_url": t.string(),
                            "gists_url": t.string(),
                            "gravatar_id": t.string().optional(),
                            "html_url": t.string(),
                            "id": t.integer(),
                            "node_id": t.string(),
                            "login": t.string(),
                            "organizations_url": t.string(),
                            "received_events_url": t.string(),
                            "repos_url": t.string(),
                            "site_admin": t.boolean(),
                            "starred_url": t.string(),
                            "subscriptions_url": t.string(),
                            "type": t.string(),
                            "url": t.string(),
                        }
                    ),
                }
            ),
            "base": t.struct(
                {
                    "label": t.string(),
                    "ref": t.string(),
                    "repo": t.struct(
                        {
                            "archive_url": t.string(),
                            "assignees_url": t.string(),
                            "blobs_url": t.string(),
                            "branches_url": t.string(),
                            "collaborators_url": t.string(),
                            "comments_url": t.string(),
                            "commits_url": t.string(),
                            "compare_url": t.string(),
                            "contents_url": t.string(),
                            "contributors_url": t.string(),
                            "deployments_url": t.string(),
                            "description": t.string().optional(),
                            "downloads_url": t.string(),
                            "events_url": t.string(),
                            "fork": t.boolean(),
                            "forks_url": t.string(),
                            "full_name": t.string(),
                            "git_commits_url": t.string(),
                            "git_refs_url": t.string(),
                            "git_tags_url": t.string(),
                            "hooks_url": t.string(),
                            "html_url": t.string(),
                            "id": t.integer(),
                            "is_template": t.boolean().optional(),
                            "node_id": t.string(),
                            "issue_comment_url": t.string(),
                            "issue_events_url": t.string(),
                            "issues_url": t.string(),
                            "keys_url": t.string(),
                            "labels_url": t.string(),
                            "languages_url": t.string(),
                            "merges_url": t.string(),
                            "milestones_url": t.string(),
                            "name": t.string(),
                            "notifications_url": t.string(),
                            "owner": t.struct(
                                {
                                    "avatar_url": t.string(),
                                    "events_url": t.string(),
                                    "followers_url": t.string(),
                                    "following_url": t.string(),
                                    "gists_url": t.string(),
                                    "gravatar_id": t.string().optional(),
                                    "html_url": t.string(),
                                    "id": t.integer(),
                                    "node_id": t.string(),
                                    "login": t.string(),
                                    "organizations_url": t.string(),
                                    "received_events_url": t.string(),
                                    "repos_url": t.string(),
                                    "site_admin": t.boolean(),
                                    "starred_url": t.string(),
                                    "subscriptions_url": t.string(),
                                    "type": t.string(),
                                    "url": t.string(),
                                }
                            ),
                            "private": t.boolean(),
                            "pulls_url": t.string(),
                            "releases_url": t.string(),
                            "stargazers_url": t.string(),
                            "statuses_url": t.string(),
                            "subscribers_url": t.string(),
                            "subscription_url": t.string(),
                            "tags_url": t.string(),
                            "teams_url": t.string(),
                            "trees_url": t.string(),
                            "url": t.string(),
                            "clone_url": t.string(),
                            "default_branch": t.string(),
                            "forks": t.integer(),
                            "forks_count": t.integer(),
                            "git_url": t.string(),
                            "has_downloads": t.boolean(),
                            "has_issues": t.boolean(),
                            "has_projects": t.boolean(),
                            "has_wiki": t.boolean(),
                            "has_pages": t.boolean(),
                            "homepage": t.string().optional(),
                            "language": t.string().optional(),
                            "master_branch": t.string().optional(),
                            "archived": t.boolean(),
                            "disabled": t.boolean(),
                            "visibility": t.string().optional(),
                            "mirror_url": t.string().optional(),
                            "open_issues": t.integer(),
                            "open_issues_count": t.integer(),
                            "permissions": t.struct(
                                {
                                    "admin": t.boolean(),
                                    "maintain": t.boolean().optional(),
                                    "push": t.boolean(),
                                    "triage": t.boolean().optional(),
                                    "pull": t.boolean(),
                                }
                            ).optional(),
                            "temp_clone_token": t.string().optional(),
                            "allow_merge_commit": t.boolean().optional(),
                            "allow_squash_merge": t.boolean().optional(),
                            "allow_rebase_merge": t.boolean().optional(),
                            "license": t.proxy(renames["nullable_license_simple"]),
                            "pushed_at": t.string(),
                            "size": t.integer(),
                            "ssh_url": t.string(),
                            "stargazers_count": t.integer(),
                            "svn_url": t.string(),
                            "topics": t.array(t.string()).optional(),
                            "watchers": t.integer(),
                            "watchers_count": t.integer(),
                            "created_at": t.string(),
                            "updated_at": t.string(),
                            "allow_forking": t.boolean().optional(),
                        }
                    ),
                    "sha": t.string(),
                    "user": t.struct(
                        {
                            "avatar_url": t.string(),
                            "events_url": t.string(),
                            "followers_url": t.string(),
                            "following_url": t.string(),
                            "gists_url": t.string(),
                            "gravatar_id": t.string().optional(),
                            "html_url": t.string(),
                            "id": t.integer(),
                            "node_id": t.string(),
                            "login": t.string(),
                            "organizations_url": t.string(),
                            "received_events_url": t.string(),
                            "repos_url": t.string(),
                            "site_admin": t.boolean(),
                            "starred_url": t.string(),
                            "subscriptions_url": t.string(),
                            "type": t.string(),
                            "url": t.string(),
                        }
                    ),
                }
            ),
            "_links": t.struct(
                {
                    "comments": t.proxy(renames["link"]),
                    "commits": t.proxy(renames["link"]),
                    "statuses": t.proxy(renames["link"]),
                    "html": t.proxy(renames["link"]),
                    "issue": t.proxy(renames["link"]),
                    "review_comments": t.proxy(renames["link"]),
                    "review_comment": t.proxy(renames["link"]),
                    "self": t.proxy(renames["link"]),
                }
            ),
            "author_association": t.proxy(renames["author_association"]),
            "draft": t.boolean().optional(),
            "merged": t.boolean(),
            "mergeable": t.boolean().optional(),
            "rebaseable": t.boolean().optional(),
            "mergeable_state": t.string(),
            "merged_by": t.proxy(renames["nullable_simple_user"]),
            "comments": t.integer(),
            "review_comments": t.integer(),
            "maintainer_can_modify": t.boolean(),
            "commits": t.integer(),
            "additions": t.integer(),
            "deletions": t.integer(),
            "changed_files": t.integer(),
        }
    ).named(renames["pull_request"])
    types["pull_request_merge_result"] = t.struct(
        {"sha": t.string(), "merged": t.boolean(), "message": t.string()}
    ).named(renames["pull_request_merge_result"])
    types["pull_request_review_request"] = t.struct(
        {
            "users": t.array(t.proxy(renames["simple_user"])),
            "teams": t.array(t.proxy(renames["team"])),
        }
    ).named(renames["pull_request_review_request"])
    types["pull_request_review"] = t.struct(
        {
            "id": t.integer(),
            "node_id": t.string(),
            "user": t.proxy(renames["nullable_simple_user"]),
            "body": t.string(),
            "state": t.string(),
            "html_url": t.string(),
            "pull_request_url": t.string(),
            "_links": t.struct(
                {
                    "html": t.struct({"href": t.string()}),
                    "pull_request": t.struct({"href": t.string()}),
                }
            ),
            "submitted_at": t.string().optional(),
            "commit_id": t.string(),
            "body_html": t.string().optional(),
            "body_text": t.string().optional(),
            "author_association": t.proxy(renames["author_association"]),
        }
    ).named(renames["pull_request_review"])
    types["review_comment"] = t.struct(
        {
            "url": t.string(),
            "pull_request_review_id": t.integer().optional(),
            "id": t.integer(),
            "node_id": t.string(),
            "diff_hunk": t.string(),
            "path": t.string(),
            "position": t.integer().optional(),
            "original_position": t.integer(),
            "commit_id": t.string(),
            "original_commit_id": t.string(),
            "in_reply_to_id": t.integer().optional(),
            "user": t.proxy(renames["nullable_simple_user"]),
            "body": t.string(),
            "created_at": t.string(),
            "updated_at": t.string(),
            "html_url": t.string(),
            "pull_request_url": t.string(),
            "author_association": t.proxy(renames["author_association"]),
            "_links": t.struct(
                {
                    "self": t.proxy(renames["link"]),
                    "html": t.proxy(renames["link"]),
                    "pull_request": t.proxy(renames["link"]),
                }
            ),
            "body_text": t.string().optional(),
            "body_html": t.string().optional(),
            "reactions": t.proxy(renames["reaction_rollup"]).optional(),
            "side": t.string().optional(),
            "start_side": t.string().optional(),
            "line": t.integer().optional(),
            "original_line": t.integer().optional(),
            "start_line": t.integer().optional(),
            "original_start_line": t.integer().optional(),
        }
    ).named(renames["review_comment"])
    types["release_asset"] = t.struct(
        {
            "url": t.string(),
            "browser_download_url": t.string(),
            "id": t.integer(),
            "node_id": t.string(),
            "name": t.string(),
            "label": t.string().optional(),
            "state": t.string(),
            "content_type": t.string(),
            "size": t.integer(),
            "download_count": t.integer(),
            "created_at": t.string(),
            "updated_at": t.string(),
            "uploader": t.proxy(renames["nullable_simple_user"]),
        }
    ).named(renames["release_asset"])
    types["release"] = t.struct(
        {
            "url": t.string(),
            "html_url": t.string(),
            "assets_url": t.string(),
            "upload_url": t.string(),
            "tarball_url": t.string().optional(),
            "zipball_url": t.string().optional(),
            "id": t.integer(),
            "node_id": t.string(),
            "tag_name": t.string(),
            "target_commitish": t.string(),
            "name": t.string().optional(),
            "body": t.string().optional(),
            "draft": t.boolean(),
            "prerelease": t.boolean(),
            "created_at": t.string(),
            "published_at": t.string().optional(),
            "author": t.proxy(renames["simple_user"]),
            "assets": t.array(t.proxy(renames["release_asset"])),
            "body_html": t.string().optional(),
            "body_text": t.string().optional(),
            "reactions": t.proxy(renames["reaction_rollup"]).optional(),
        }
    ).named(renames["release"])
    types["stargazer"] = t.struct(
        {"starred_at": t.string(), "user": t.proxy(renames["nullable_simple_user"])}
    ).named(renames["stargazer"])
    types["code_frequency_stat"] = t.array(t.integer()).named(
        renames["code_frequency_stat"]
    )
    types["commit_activity"] = t.struct(
        {"days": t.array(t.integer()), "total": t.integer(), "week": t.integer()}
    ).named(renames["commit_activity"])
    types["contributor_activity"] = t.struct(
        {
            "author": t.proxy(renames["nullable_simple_user"]),
            "total": t.integer(),
            "weeks": t.array(
                t.struct(
                    {
                        "w": t.integer().optional(),
                        "a": t.integer().optional(),
                        "d": t.integer().optional(),
                        "c": t.integer().optional(),
                    }
                )
            ),
        }
    ).named(renames["contributor_activity"])
    types["participation_stats"] = t.struct(
        {"all": t.array(t.integer()), "owner": t.array(t.integer())}
    ).named(renames["participation_stats"])
    types["repository_subscription"] = t.struct(
        {
            "subscribed": t.boolean(),
            "ignored": t.boolean(),
            "reason": t.string().optional(),
            "created_at": t.string(),
            "url": t.string(),
            "repository_url": t.string(),
        }
    ).named(renames["repository_subscription"])
    types["tag"] = t.struct(
        {
            "name": t.string(),
            "commit": t.struct({"sha": t.string(), "url": t.string()}),
            "zipball_url": t.string(),
            "tarball_url": t.string(),
            "node_id": t.string(),
        }
    ).named(renames["tag"])
    types["topic"] = t.struct({"names": t.array(t.string())}).named(renames["topic"])
    types["search_result_text_matches"] = t.array(
        t.struct(
            {
                "object_url": t.string().optional(),
                "object_type": t.string().optional(),
                "property": t.string().optional(),
                "fragment": t.string().optional(),
                "matches": t.array(
                    t.struct(
                        {
                            "text": t.string().optional(),
                            "indices": t.array(t.integer()).optional(),
                        }
                    )
                ).optional(),
            }
        )
    ).named(renames["search_result_text_matches"])
    types["code_search_result_item"] = t.struct(
        {
            "name": t.string(),
            "path": t.string(),
            "sha": t.string(),
            "url": t.string(),
            "git_url": t.string(),
            "html_url": t.string(),
            "repository": t.proxy(renames["minimal_repository"]),
            "score": t.number(),
            "file_size": t.integer().optional(),
            "language": t.string().optional(),
            "last_modified_at": t.string().optional(),
            "line_numbers": t.array(t.string()).optional(),
            "text_matches": t.proxy(renames["search_result_text_matches"]).optional(),
        }
    ).named(renames["code_search_result_item"])
    types["commit_search_result_item"] = t.struct(
        {
            "url": t.string(),
            "sha": t.string(),
            "html_url": t.string(),
            "comments_url": t.string(),
            "commit": t.struct(
                {
                    "author": t.struct(
                        {"name": t.string(), "email": t.string(), "date": t.string()}
                    ),
                    "committer": t.proxy(renames["nullable_git_user"]),
                    "comment_count": t.integer(),
                    "message": t.string(),
                    "tree": t.struct({"sha": t.string(), "url": t.string()}),
                    "url": t.string(),
                    "verification": t.proxy(renames["verification"]).optional(),
                }
            ),
            "author": t.proxy(renames["nullable_simple_user"]),
            "committer": t.proxy(renames["nullable_git_user"]),
            "parents": t.array(
                t.struct(
                    {
                        "url": t.string().optional(),
                        "html_url": t.string().optional(),
                        "sha": t.string().optional(),
                    }
                )
            ),
            "repository": t.proxy(renames["minimal_repository"]),
            "score": t.number(),
            "node_id": t.string(),
            "text_matches": t.proxy(renames["search_result_text_matches"]).optional(),
        }
    ).named(renames["commit_search_result_item"])
    types["issue_search_result_item"] = t.struct(
        {
            "url": t.string(),
            "repository_url": t.string(),
            "labels_url": t.string(),
            "comments_url": t.string(),
            "events_url": t.string(),
            "html_url": t.string(),
            "id": t.integer(),
            "node_id": t.string(),
            "number": t.integer(),
            "title": t.string(),
            "locked": t.boolean(),
            "active_lock_reason": t.string().optional(),
            "assignees": t.array(t.proxy(renames["simple_user"])).optional(),
            "user": t.proxy(renames["nullable_simple_user"]),
            "labels": t.array(
                t.struct(
                    {
                        "id": t.integer().optional(),
                        "node_id": t.string().optional(),
                        "url": t.string().optional(),
                        "name": t.string().optional(),
                        "color": t.string().optional(),
                        "default": t.boolean().optional(),
                        "description": t.string().optional(),
                    }
                )
            ),
            "state": t.string(),
            "assignee": t.proxy(renames["nullable_simple_user"]),
            "milestone": t.proxy(renames["nullable_milestone"]),
            "comments": t.integer(),
            "created_at": t.string(),
            "updated_at": t.string(),
            "closed_at": t.string().optional(),
            "text_matches": t.proxy(renames["search_result_text_matches"]).optional(),
            "pull_request": t.struct(
                {
                    "merged_at": t.string().optional(),
                    "diff_url": t.string().optional(),
                    "html_url": t.string().optional(),
                    "patch_url": t.string().optional(),
                    "url": t.string().optional(),
                }
            ).optional(),
            "body": t.string().optional(),
            "score": t.number(),
            "author_association": t.proxy(renames["author_association"]),
            "draft": t.boolean().optional(),
            "repository": t.proxy(renames["repository"]).optional(),
            "body_html": t.string().optional(),
            "body_text": t.string().optional(),
            "timeline_url": t.string().optional(),
            "performed_via_github_app": t.proxy(
                renames["nullable_integration"]
            ).optional(),
            "reactions": t.proxy(renames["reaction_rollup"]).optional(),
        }
    ).named(renames["issue_search_result_item"])
    types["label_search_result_item"] = t.struct(
        {
            "id": t.integer(),
            "node_id": t.string(),
            "url": t.string(),
            "name": t.string(),
            "color": t.string(),
            "default": t.boolean(),
            "description": t.string().optional(),
            "score": t.number(),
            "text_matches": t.proxy(renames["search_result_text_matches"]).optional(),
        }
    ).named(renames["label_search_result_item"])
    types["repo_search_result_item"] = t.struct(
        {
            "id": t.integer(),
            "node_id": t.string(),
            "name": t.string(),
            "full_name": t.string(),
            "owner": t.proxy(renames["nullable_simple_user"]),
            "private": t.boolean(),
            "html_url": t.string(),
            "description": t.string().optional(),
            "fork": t.boolean(),
            "url": t.string(),
            "created_at": t.string(),
            "updated_at": t.string(),
            "pushed_at": t.string(),
            "homepage": t.string().optional(),
            "size": t.integer(),
            "stargazers_count": t.integer(),
            "watchers_count": t.integer(),
            "language": t.string().optional(),
            "forks_count": t.integer(),
            "open_issues_count": t.integer(),
            "master_branch": t.string().optional(),
            "default_branch": t.string(),
            "score": t.number(),
            "forks_url": t.string(),
            "keys_url": t.string(),
            "collaborators_url": t.string(),
            "teams_url": t.string(),
            "hooks_url": t.string(),
            "issue_events_url": t.string(),
            "events_url": t.string(),
            "assignees_url": t.string(),
            "branches_url": t.string(),
            "tags_url": t.string(),
            "blobs_url": t.string(),
            "git_tags_url": t.string(),
            "git_refs_url": t.string(),
            "trees_url": t.string(),
            "statuses_url": t.string(),
            "languages_url": t.string(),
            "stargazers_url": t.string(),
            "contributors_url": t.string(),
            "subscribers_url": t.string(),
            "subscription_url": t.string(),
            "commits_url": t.string(),
            "git_commits_url": t.string(),
            "comments_url": t.string(),
            "issue_comment_url": t.string(),
            "contents_url": t.string(),
            "compare_url": t.string(),
            "merges_url": t.string(),
            "archive_url": t.string(),
            "downloads_url": t.string(),
            "issues_url": t.string(),
            "pulls_url": t.string(),
            "milestones_url": t.string(),
            "notifications_url": t.string(),
            "labels_url": t.string(),
            "releases_url": t.string(),
            "deployments_url": t.string(),
            "git_url": t.string(),
            "ssh_url": t.string(),
            "clone_url": t.string(),
            "svn_url": t.string(),
            "forks": t.integer(),
            "open_issues": t.integer(),
            "watchers": t.integer(),
            "topics": t.array(t.string()).optional(),
            "mirror_url": t.string().optional(),
            "has_issues": t.boolean(),
            "has_projects": t.boolean(),
            "has_pages": t.boolean(),
            "has_wiki": t.boolean(),
            "has_downloads": t.boolean(),
            "archived": t.boolean(),
            "disabled": t.boolean(),
            "visibility": t.string().optional(),
            "license": t.proxy(renames["nullable_license_simple"]),
            "permissions": t.struct(
                {
                    "admin": t.boolean(),
                    "maintain": t.boolean().optional(),
                    "push": t.boolean(),
                    "triage": t.boolean().optional(),
                    "pull": t.boolean(),
                }
            ).optional(),
            "text_matches": t.proxy(renames["search_result_text_matches"]).optional(),
            "temp_clone_token": t.string().optional(),
            "allow_merge_commit": t.boolean().optional(),
            "allow_squash_merge": t.boolean().optional(),
            "allow_rebase_merge": t.boolean().optional(),
            "delete_branch_on_merge": t.boolean().optional(),
            "allow_forking": t.boolean().optional(),
            "is_template": t.boolean().optional(),
        }
    ).named(renames["repo_search_result_item"])
    types["topic_search_result_item"] = t.struct(
        {
            "name": t.string(),
            "display_name": t.string().optional(),
            "short_description": t.string().optional(),
            "description": t.string().optional(),
            "created_by": t.string().optional(),
            "released": t.string().optional(),
            "created_at": t.string(),
            "updated_at": t.string(),
            "featured": t.boolean(),
            "curated": t.boolean(),
            "score": t.number(),
            "repository_count": t.integer().optional(),
            "logo_url": t.string().optional(),
            "text_matches": t.proxy(renames["search_result_text_matches"]).optional(),
            "related": t.array(
                t.struct(
                    {
                        "topic_relation": t.struct(
                            {
                                "id": t.integer().optional(),
                                "name": t.string().optional(),
                                "topic_id": t.integer().optional(),
                                "relation_type": t.string().optional(),
                            }
                        ).optional()
                    }
                )
            ).optional(),
            "aliases": t.array(
                t.struct(
                    {
                        "topic_relation": t.struct(
                            {
                                "id": t.integer().optional(),
                                "name": t.string().optional(),
                                "topic_id": t.integer().optional(),
                                "relation_type": t.string().optional(),
                            }
                        ).optional()
                    }
                )
            ).optional(),
        }
    ).named(renames["topic_search_result_item"])
    types["user_search_result_item"] = t.struct(
        {
            "login": t.string(),
            "id": t.integer(),
            "node_id": t.string(),
            "avatar_url": t.string(),
            "gravatar_id": t.string().optional(),
            "url": t.string(),
            "html_url": t.string(),
            "followers_url": t.string(),
            "subscriptions_url": t.string(),
            "organizations_url": t.string(),
            "repos_url": t.string(),
            "received_events_url": t.string(),
            "type": t.string(),
            "score": t.number(),
            "following_url": t.string(),
            "gists_url": t.string(),
            "starred_url": t.string(),
            "events_url": t.string(),
            "public_repos": t.integer().optional(),
            "public_gists": t.integer().optional(),
            "followers": t.integer().optional(),
            "following": t.integer().optional(),
            "created_at": t.string().optional(),
            "updated_at": t.string().optional(),
            "name": t.string().optional(),
            "bio": t.string().optional(),
            "email": t.string().optional(),
            "location": t.string().optional(),
            "site_admin": t.boolean(),
            "hireable": t.boolean().optional(),
            "text_matches": t.proxy(renames["search_result_text_matches"]).optional(),
            "blog": t.string().optional(),
            "company": t.string().optional(),
            "suspended_at": t.string().optional(),
        }
    ).named(renames["user_search_result_item"])
    types["configuration_status"] = t.struct(
        {
            "status": t.string().optional(),
            "progress": t.array(
                t.struct({"status": t.string(), "key": t.string()})
            ).optional(),
        }
    ).named(renames["configuration_status"])
    types["maintenance_status"] = t.struct(
        {
            "status": t.string().optional(),
            "scheduled_time": t.string().optional(),
            "connection_services": t.array(
                t.struct({"name": t.string(), "number": t.integer()})
            ).optional(),
        }
    ).named(renames["maintenance_status"])
    types["enterprise_settings"] = t.struct(
        {
            "enterprise": t.struct(
                {
                    "private_mode": t.boolean().optional(),
                    "public_pages": t.boolean().optional(),
                    "subdomain_isolation": t.boolean().optional(),
                    "signup_enabled": t.boolean().optional(),
                    "github_hostname": t.string().optional(),
                    "identicons_host": t.string().optional(),
                    "http_proxy": t.string().optional(),
                    "auth_mode": t.string().optional(),
                    "expire_sessions": t.boolean().optional(),
                    "admin_password": t.string().optional(),
                    "configuration_id": t.integer().optional(),
                    "configuration_run_count": t.integer().optional(),
                    "avatar": t.struct(
                        {
                            "enabled": t.boolean().optional(),
                            "uri": t.string().optional(),
                        }
                    ).optional(),
                    "customer": t.struct(
                        {
                            "name": t.string().optional(),
                            "email": t.string().optional(),
                            "uuid": t.string().optional(),
                            "secret_key_data": t.string().optional(),
                            "public_key_data": t.string().optional(),
                        }
                    ).optional(),
                    "license": t.struct(
                        {
                            "seats": t.integer().optional(),
                            "evaluation": t.boolean().optional(),
                            "perpetual": t.boolean().optional(),
                            "unlimited_seating": t.boolean().optional(),
                            "support_key": t.string().optional(),
                            "ssh_allowed": t.boolean().optional(),
                            "cluster_support": t.boolean().optional(),
                            "expire_at": t.string().optional(),
                        }
                    ).optional(),
                    "github_ssl": t.struct(
                        {
                            "enabled": t.boolean().optional(),
                            "cert": t.string().optional(),
                            "key": t.string().optional(),
                        }
                    ).optional(),
                    "ldap": t.struct(
                        {
                            "host": t.string().optional(),
                            "port": t.integer().optional(),
                            "base": t.array(
                                t.struct({"_": t.string().optional()})
                            ).optional(),
                            "uid": t.string().optional(),
                            "bind_dn": t.string().optional(),
                            "password": t.string().optional(),
                            "method": t.string().optional(),
                            "search_strategy": t.string().optional(),
                            "user_groups": t.array(
                                t.struct({"_": t.string().optional()})
                            ).optional(),
                            "admin_group": t.string().optional(),
                            "virtual_attribute_enabled": t.boolean().optional(),
                            "recursive_group_search": t.boolean().optional(),
                            "posix_support": t.boolean().optional(),
                            "user_sync_emails": t.boolean().optional(),
                            "user_sync_keys": t.boolean().optional(),
                            "user_sync_interval": t.integer().optional(),
                            "team_sync_interval": t.integer().optional(),
                            "sync_enabled": t.boolean().optional(),
                            "reconciliation": t.struct(
                                {
                                    "user": t.string().optional(),
                                    "org": t.string().optional(),
                                }
                            ).optional(),
                            "profile": t.struct(
                                {
                                    "uid": t.string().optional(),
                                    "name": t.string().optional(),
                                    "mail": t.string().optional(),
                                    "key": t.string().optional(),
                                }
                            ).optional(),
                        }
                    ).optional(),
                    "cas": t.struct({"url": t.string().optional()}).optional(),
                    "saml": t.struct(
                        {
                            "sso_url": t.string().optional(),
                            "certificate": t.string().optional(),
                            "certificate_path": t.string().optional(),
                            "issuer": t.string().optional(),
                            "idp_initiated_sso": t.boolean().optional(),
                            "disable_admin_demote": t.boolean().optional(),
                        }
                    ).optional(),
                    "github_oauth": t.struct(
                        {
                            "client_id": t.string().optional(),
                            "client_secret": t.string().optional(),
                            "organization_name": t.string().optional(),
                            "organization_team": t.string().optional(),
                        }
                    ).optional(),
                    "smtp": t.struct(
                        {
                            "enabled": t.boolean().optional(),
                            "address": t.string().optional(),
                            "authentication": t.string().optional(),
                            "port": t.string().optional(),
                            "domain": t.string().optional(),
                            "username": t.string().optional(),
                            "user_name": t.string().optional(),
                            "enable_starttls_auto": t.boolean().optional(),
                            "password": t.string().optional(),
                            "discard-to-noreply-address": t.boolean().optional(),
                            "support_address": t.string().optional(),
                            "support_address_type": t.string().optional(),
                            "noreply_address": t.string().optional(),
                        }
                    ).optional(),
                    "ntp": t.struct(
                        {
                            "primary_server": t.string().optional(),
                            "secondary_server": t.string().optional(),
                        }
                    ).optional(),
                    "timezone": t.string().optional(),
                    "snmp": t.struct(
                        {
                            "enabled": t.boolean().optional(),
                            "community": t.string().optional(),
                        }
                    ).optional(),
                    "syslog": t.struct(
                        {
                            "enabled": t.boolean().optional(),
                            "server": t.string().optional(),
                            "protocol_name": t.string().optional(),
                        }
                    ).optional(),
                    "assets": t.string().optional(),
                    "pages": t.struct({"enabled": t.boolean().optional()}).optional(),
                    "collectd": t.struct(
                        {
                            "enabled": t.boolean().optional(),
                            "server": t.string().optional(),
                            "port": t.integer().optional(),
                            "encryption": t.string().optional(),
                            "username": t.string().optional(),
                            "password": t.string().optional(),
                        }
                    ).optional(),
                    "mapping": t.struct(
                        {
                            "enabled": t.boolean().optional(),
                            "tileserver": t.string().optional(),
                            "basemap": t.string().optional(),
                            "token": t.string().optional(),
                        }
                    ).optional(),
                    "load_balancer": t.string().optional(),
                }
            ).optional(),
            "run_list": t.array(t.string()).optional(),
        }
    ).named(renames["enterprise_settings"])
    types["ssh_key"] = t.struct(
        {"key": t.string().optional(), "pretty-print": t.string().optional()}
    ).named(renames["ssh_key"])
    types["private_user"] = t.struct(
        {
            "login": t.string(),
            "id": t.integer(),
            "node_id": t.string(),
            "avatar_url": t.string(),
            "gravatar_id": t.string().optional(),
            "url": t.string(),
            "html_url": t.string(),
            "followers_url": t.string(),
            "following_url": t.string(),
            "gists_url": t.string(),
            "starred_url": t.string(),
            "subscriptions_url": t.string(),
            "organizations_url": t.string(),
            "repos_url": t.string(),
            "events_url": t.string(),
            "received_events_url": t.string(),
            "type": t.string(),
            "site_admin": t.boolean(),
            "name": t.string().optional(),
            "company": t.string().optional(),
            "blog": t.string().optional(),
            "location": t.string().optional(),
            "email": t.string().optional(),
            "hireable": t.boolean().optional(),
            "bio": t.string().optional(),
            "public_repos": t.integer(),
            "public_gists": t.integer(),
            "followers": t.integer(),
            "following": t.integer(),
            "created_at": t.string(),
            "updated_at": t.string(),
            "private_gists": t.integer(),
            "total_private_repos": t.integer(),
            "owned_private_repos": t.integer(),
            "disk_usage": t.integer(),
            "collaborators": t.integer(),
            "two_factor_authentication": t.boolean(),
            "plan": t.struct(
                {
                    "collaborators": t.integer(),
                    "name": t.string(),
                    "space": t.integer(),
                    "private_repos": t.integer(),
                }
            ).optional(),
            "suspended_at": t.string().optional(),
            "business_plus": t.boolean().optional(),
            "ldap_dn": t.string().optional(),
        }
    ).named(renames["private_user"])
    types["email"] = t.struct(
        {
            "email": t.string(),
            "primary": t.boolean(),
            "verified": t.boolean(),
            "visibility": t.string().optional(),
        }
    ).named(renames["email"])
    types["gpg_key"] = t.struct(
        {
            "id": t.integer(),
            "primary_key_id": t.integer().optional(),
            "key_id": t.string(),
            "public_key": t.string(),
            "emails": t.array(
                t.struct(
                    {"email": t.string().optional(), "verified": t.boolean().optional()}
                )
            ),
            "subkeys": t.array(
                t.struct(
                    {
                        "id": t.integer().optional(),
                        "primary_key_id": t.integer().optional(),
                        "key_id": t.string().optional(),
                        "public_key": t.string().optional(),
                        "emails": t.array(
                            t.struct({"_": t.string().optional()})
                        ).optional(),
                        "subkeys": t.array(
                            t.struct({"_": t.string().optional()})
                        ).optional(),
                        "can_sign": t.boolean().optional(),
                        "can_encrypt_comms": t.boolean().optional(),
                        "can_encrypt_storage": t.boolean().optional(),
                        "can_certify": t.boolean().optional(),
                        "created_at": t.string().optional(),
                        "expires_at": t.string().optional(),
                        "raw_key": t.string().optional(),
                    }
                )
            ),
            "can_sign": t.boolean(),
            "can_encrypt_comms": t.boolean(),
            "can_encrypt_storage": t.boolean(),
            "can_certify": t.boolean(),
            "created_at": t.string(),
            "expires_at": t.string().optional(),
            "raw_key": t.string().optional(),
        }
    ).named(renames["gpg_key"])
    types["key"] = t.struct(
        {
            "key": t.string(),
            "id": t.integer(),
            "url": t.string(),
            "title": t.string(),
            "created_at": t.string(),
            "verified": t.boolean(),
            "read_only": t.boolean(),
        }
    ).named(renames["key"])
    types["starred_repository"] = t.struct(
        {"starred_at": t.string(), "repo": t.proxy(renames["repository"])}
    ).named(renames["starred_repository"])
    types["hovercard"] = t.struct(
        {"contexts": t.array(t.struct({"message": t.string(), "octicon": t.string()}))}
    ).named(renames["hovercard"])
    types["key_simple"] = t.struct({"id": t.integer(), "key": t.string()}).named(
        renames["key_simple"]
    )

    functions = {}
    functions["meta_root"] = ghes.get(
        "/",
        t.struct({}),
        t.struct(
            {
                "current_user_url": t.string(),
                "current_user_authorizations_html_url": t.string(),
                "authorizations_url": t.string(),
                "code_search_url": t.string(),
                "commit_search_url": t.string(),
                "emails_url": t.string(),
                "emojis_url": t.string(),
                "events_url": t.string(),
                "feeds_url": t.string(),
                "followers_url": t.string(),
                "following_url": t.string(),
                "gists_url": t.string(),
                "hub_url": t.string(),
                "issue_search_url": t.string(),
                "issues_url": t.string(),
                "keys_url": t.string(),
                "label_search_url": t.string(),
                "notifications_url": t.string(),
                "organization_url": t.string(),
                "organization_repositories_url": t.string(),
                "organization_teams_url": t.string(),
                "public_gists_url": t.string(),
                "rate_limit_url": t.string(),
                "repository_url": t.string(),
                "repository_search_url": t.string(),
                "current_user_repositories_url": t.string(),
                "starred_url": t.string(),
                "starred_gists_url": t.string(),
                "topic_search_url": t.string().optional(),
                "user_url": t.string(),
                "user_organizations_url": t.string(),
                "user_repositories_url": t.string(),
                "user_search_url": t.string(),
            }
        ),
    )
    functions["enterprise_admin_list_global_webhooks"] = ghes.get(
        "/admin/hooks",
        t.struct({"accept": t.string(), "per_page": t.integer(), "page": t.integer()}),
        t.array(t.proxy(renames["global_hook"])),
    )
    functions["enterprise_admin_create_global_webhook"] = ghes.post(
        "/admin/hooks",
        t.struct(
            {
                "accept": t.string(),
                "name": t.string(),
                "config": t.struct(
                    {
                        "url": t.string(),
                        "content_type": t.string().optional(),
                        "secret": t.string().optional(),
                        "insecure_ssl": t.string().optional(),
                    }
                ),
                "events": t.array(t.string()).optional(),
                "active": t.boolean().optional(),
            }
        ),
        t.proxy(renames["global_hook"]),
        content_type="application/json",
        body_fields=("name", "config", "events", "active"),
    )
    functions["enterprise_admin_get_global_webhook"] = ghes.get(
        "/admin/hooks/{hook_id}",
        t.struct({"accept": t.string(), "hook_id": t.integer()}),
        t.proxy(renames["global_hook"]),
    )
    functions["enterprise_admin_update_global_webhook"] = ghes.patch(
        "/admin/hooks/{hook_id}",
        t.struct(
            {
                "accept": t.string(),
                "hook_id": t.integer(),
                "config": t.struct(
                    {
                        "url": t.string(),
                        "content_type": t.string().optional(),
                        "secret": t.string().optional(),
                        "insecure_ssl": t.string().optional(),
                    }
                ).optional(),
                "events": t.array(t.string()).optional(),
                "active": t.boolean().optional(),
            }
        ),
        t.proxy(renames["global_hook_2"]),
        content_type="application/json",
        body_fields=("config", "events", "active"),
    )
    functions["enterprise_admin_delete_global_webhook"] = ghes.delete(
        "/admin/hooks/{hook_id}",
        t.struct({"accept": t.string(), "hook_id": t.integer()}),
        t.boolean(),
    )
    functions["enterprise_admin_ping_global_webhook"] = ghes.post(
        "/admin/hooks/{hook_id}/pings",
        t.struct({"accept": t.string(), "hook_id": t.integer()}),
        t.boolean(),
    )
    functions["enterprise_admin_list_public_keys"] = ghes.get(
        "/admin/keys",
        t.struct(
            {
                "per_page": t.integer(),
                "page": t.integer(),
                "direction": t.string(),
                "sort": t.string(),
                "since": t.string(),
            }
        ),
        t.array(t.proxy(renames["public_key_full"])),
    )
    functions["enterprise_admin_delete_public_key"] = ghes.delete(
        "/admin/keys/{key_ids}",
        t.struct({"key_ids": t.string()}),
        t.boolean(),
    )
    functions["enterprise_admin_update_ldap_mapping_for_team"] = ghes.patch(
        "/admin/ldap/teams/{team_id}/mapping",
        t.struct({"team_id": t.integer(), "ldap_dn": t.string()}),
        t.proxy(renames["ldap_mapping_team"]),
        content_type="application/json",
        body_fields=("ldap_dn",),
    )
    functions["enterprise_admin_sync_ldap_mapping_for_team"] = ghes.post(
        "/admin/ldap/teams/{team_id}/sync",
        t.struct({"team_id": t.integer()}),
        t.struct({"status": t.string().optional()}),
    )
    functions["enterprise_admin_update_ldap_mapping_for_user"] = ghes.patch(
        "/admin/ldap/users/{username}/mapping",
        t.struct({"username": t.string(), "ldap_dn": t.string()}),
        t.proxy(renames["ldap_mapping_user"]),
        content_type="application/json",
        body_fields=("ldap_dn",),
    )
    functions["enterprise_admin_sync_ldap_mapping_for_user"] = ghes.post(
        "/admin/ldap/users/{username}/sync",
        t.struct({"username": t.string()}),
        t.struct({"status": t.string().optional()}),
    )
    functions["enterprise_admin_create_org"] = ghes.post(
        "/admin/organizations",
        t.struct(
            {
                "login": t.string(),
                "admin": t.string(),
                "profile_name": t.string().optional(),
            }
        ),
        t.proxy(renames["organization_simple"]),
        content_type="application/json",
        body_fields=("login", "admin", "profile_name"),
    )
    functions["enterprise_admin_update_org_name"] = ghes.patch(
        "/admin/organizations/{org}",
        t.struct({"org": t.string(), "login": t.string()}),
        t.struct({"message": t.string().optional(), "url": t.string().optional()}),
        content_type="application/json",
        body_fields=("login",),
    )
    functions["enterprise_admin_list_pre_receive_environments"] = ghes.get(
        "/admin/pre-receive-environments",
        t.struct(
            {
                "per_page": t.integer(),
                "page": t.integer(),
                "direction": t.string(),
                "sort": t.string(),
            }
        ),
        t.array(t.proxy(renames["pre_receive_environment"])),
    )
    functions["enterprise_admin_create_pre_receive_environment"] = ghes.post(
        "/admin/pre-receive-environments",
        t.struct({"name": t.string(), "image_url": t.string()}),
        t.proxy(renames["pre_receive_environment"]),
        content_type="application/json",
        body_fields=("name", "image_url"),
    )
    functions["enterprise_admin_get_pre_receive_environment"] = ghes.get(
        "/admin/pre-receive-environments/{pre_receive_environment_id}",
        t.struct({"pre_receive_environment_id": t.integer()}),
        t.proxy(renames["pre_receive_environment"]),
    )
    functions["enterprise_admin_update_pre_receive_environment"] = ghes.patch(
        "/admin/pre-receive-environments/{pre_receive_environment_id}",
        t.struct(
            {
                "pre_receive_environment_id": t.integer(),
                "name": t.string().optional(),
                "image_url": t.string().optional(),
            }
        ),
        t.proxy(renames["pre_receive_environment"]),
        content_type="application/json",
        body_fields=("name", "image_url"),
    )
    functions["enterprise_admin_delete_pre_receive_environment"] = ghes.delete(
        "/admin/pre-receive-environments/{pre_receive_environment_id}",
        t.struct({"pre_receive_environment_id": t.integer()}),
        t.boolean(),
    )
    functions["enterprise_admin_start_pre_receive_environment_download"] = ghes.post(
        "/admin/pre-receive-environments/{pre_receive_environment_id}/downloads",
        t.struct({"pre_receive_environment_id": t.integer()}),
        t.proxy(renames["pre_receive_environment_download_status"]),
    )
    functions[
        "enterprise_admin_get_download_status_for_pre_receive_environment"
    ] = ghes.get(
        "/admin/pre-receive-environments/{pre_receive_environment_id}/downloads/latest",
        t.struct({"pre_receive_environment_id": t.integer()}),
        t.proxy(renames["pre_receive_environment_download_status"]),
    )
    functions["enterprise_admin_list_pre_receive_hooks"] = ghes.get(
        "/admin/pre-receive-hooks",
        t.struct(
            {
                "per_page": t.integer(),
                "page": t.integer(),
                "direction": t.string(),
                "sort": t.string(),
            }
        ),
        t.array(t.proxy(renames["pre_receive_hook"])),
    )
    functions["enterprise_admin_create_pre_receive_hook"] = ghes.post(
        "/admin/pre-receive-hooks",
        t.struct(
            {
                "name": t.string(),
                "script": t.string(),
                "script_repository": t.struct({}),
                "environment": t.struct({}),
                "enforcement": t.string().optional(),
                "allow_downstream_configuration": t.boolean().optional(),
            }
        ),
        t.proxy(renames["pre_receive_hook"]),
        content_type="application/json",
        body_fields=(
            "name",
            "script",
            "script_repository",
            "environment",
            "enforcement",
            "allow_downstream_configuration",
        ),
    )
    functions["enterprise_admin_get_pre_receive_hook"] = ghes.get(
        "/admin/pre-receive-hooks/{pre_receive_hook_id}",
        t.struct({"pre_receive_hook_id": t.integer()}),
        t.proxy(renames["pre_receive_hook"]),
    )
    functions["enterprise_admin_update_pre_receive_hook"] = ghes.patch(
        "/admin/pre-receive-hooks/{pre_receive_hook_id}",
        t.struct(
            {
                "pre_receive_hook_id": t.integer(),
                "name": t.string().optional(),
                "script": t.string().optional(),
                "script_repository": t.struct({}).optional(),
                "environment": t.struct({}).optional(),
                "enforcement": t.string().optional(),
                "allow_downstream_configuration": t.boolean().optional(),
            }
        ),
        t.proxy(renames["pre_receive_hook"]),
        content_type="application/json",
        body_fields=(
            "name",
            "script",
            "script_repository",
            "environment",
            "enforcement",
            "allow_downstream_configuration",
        ),
    )
    functions["enterprise_admin_delete_pre_receive_hook"] = ghes.delete(
        "/admin/pre-receive-hooks/{pre_receive_hook_id}",
        t.struct({"pre_receive_hook_id": t.integer()}),
        t.boolean(),
    )
    functions["enterprise_admin_list_personal_access_tokens"] = ghes.get(
        "/admin/tokens",
        t.struct({"per_page": t.integer(), "page": t.integer()}),
        t.array(t.proxy(renames["authorization"])),
    )
    functions["enterprise_admin_delete_personal_access_token"] = ghes.delete(
        "/admin/tokens/{token_id}",
        t.struct({"token_id": t.integer()}),
        t.boolean(),
    )
    functions["enterprise_admin_create_user"] = ghes.post(
        "/admin/users",
        t.struct({"login": t.string(), "email": t.string().optional()}),
        t.proxy(renames["simple_user"]),
        content_type="application/json",
        body_fields=("login", "email"),
    )
    functions["enterprise_admin_update_username_for_user"] = ghes.patch(
        "/admin/users/{username}",
        t.struct({"username": t.string(), "login": t.string()}),
        t.struct({"message": t.string().optional(), "url": t.string().optional()}),
        content_type="application/json",
        body_fields=("login",),
    )
    functions["enterprise_admin_delete_user"] = ghes.delete(
        "/admin/users/{username}",
        t.struct({"username": t.string()}),
        t.boolean(),
    )
    functions["enterprise_admin_create_impersonation_o_auth_token"] = ghes.post(
        "/admin/users/{username}/authorizations",
        t.struct({"username": t.string(), "scopes": t.array(t.string()).optional()}),
        t.proxy(renames["authorization"]),
        content_type="application/json",
        body_fields=("scopes",),
    )
    functions["enterprise_admin_delete_impersonation_o_auth_token"] = ghes.delete(
        "/admin/users/{username}/authorizations",
        t.struct({"username": t.string()}),
        t.boolean(),
    )
    functions["apps_get_authenticated"] = ghes.get(
        "/app",
        t.struct({}),
        t.proxy(renames["integration"]),
    )
    functions["apps_get_webhook_config_for_app"] = ghes.get(
        "/app/hook/config",
        t.struct({}),
        t.proxy(renames["webhook_config"]),
    )
    functions["apps_update_webhook_config_for_app"] = ghes.patch(
        "/app/hook/config",
        t.struct(
            {
                "url": t.proxy(renames["webhook_config_url"]).optional(),
                "content_type": t.proxy(
                    renames["webhook_config_content_type"]
                ).optional(),
                "secret": t.proxy(renames["webhook_config_secret"]).optional(),
                "insecure_ssl": t.proxy(
                    renames["webhook_config_insecure_ssl"]
                ).optional(),
            }
        ),
        t.proxy(renames["webhook_config"]),
        content_type="application/json",
        body_fields=("url", "content_type", "secret", "insecure_ssl"),
    )
    functions["apps_list_installations"] = ghes.get(
        "/app/installations",
        t.struct(
            {
                "per_page": t.integer(),
                "page": t.integer(),
                "since": t.string(),
                "outdated": t.string(),
            }
        ),
        t.array(t.proxy(renames["installation"])),
    )
    functions["apps_get_installation"] = ghes.get(
        "/app/installations/{installation_id}",
        t.struct({"installation_id": t.integer()}),
        t.proxy(renames["installation"]).optional(),
    )
    functions["apps_delete_installation"] = ghes.delete(
        "/app/installations/{installation_id}",
        t.struct({"installation_id": t.integer()}),
        t.boolean().optional(),
    )
    functions["apps_create_installation_access_token"] = ghes.post(
        "/app/installations/{installation_id}/access_tokens",
        t.struct(
            {
                "installation_id": t.integer(),
                "repositories": t.array(t.string()).optional(),
                "repository_ids": t.array(t.integer()).optional(),
                "permissions": t.proxy(renames["app_permissions"]).optional(),
            }
        ),
        t.proxy(renames["installation_token"]).optional(),
        content_type="application/json",
        body_fields=("repositories", "repository_ids", "permissions"),
    )
    functions["apps_suspend_installation"] = ghes.put(
        "/app/installations/{installation_id}/suspended",
        t.struct({"installation_id": t.integer()}),
        t.boolean().optional(),
    )
    functions["apps_unsuspend_installation"] = ghes.delete(
        "/app/installations/{installation_id}/suspended",
        t.struct({"installation_id": t.integer()}),
        t.boolean().optional(),
    )
    functions["oauth_authorizations_list_grants"] = ghes.get(
        "/applications/grants",
        t.struct(
            {"per_page": t.integer(), "page": t.integer(), "client_id": t.string()}
        ),
        t.array(t.proxy(renames["application_grant"])).optional(),
    )
    functions["oauth_authorizations_get_grant"] = ghes.get(
        "/applications/grants/{grant_id}",
        t.struct({"grant_id": t.integer()}),
        t.proxy(renames["application_grant"]),
    )
    functions["oauth_authorizations_delete_grant"] = ghes.delete(
        "/applications/grants/{grant_id}",
        t.struct({"grant_id": t.integer()}),
        t.boolean(),
    )
    functions["apps_delete_authorization"] = ghes.delete(
        "/applications/{client_id}/grant",
        t.struct({"client_id": t.string(), "access_token": t.string()}),
        t.boolean(),
        content_type="application/json",
        body_fields=("access_token",),
    )
    functions["apps_revoke_grant_for_application"] = ghes.delete(
        "/applications/{client_id}/grants/{access_token}",
        t.struct({"client_id": t.string(), "access_token": t.string()}),
        t.boolean(),
    )
    functions["apps_check_token"] = ghes.post(
        "/applications/{client_id}/token",
        t.struct({"client_id": t.string(), "access_token": t.string()}),
        t.proxy(renames["authorization"]).optional(),
        content_type="application/json",
        body_fields=("access_token",),
    )
    functions["apps_reset_token"] = ghes.patch(
        "/applications/{client_id}/token",
        t.struct({"client_id": t.string(), "access_token": t.string()}),
        t.proxy(renames["authorization"]),
        content_type="application/json",
        body_fields=("access_token",),
    )
    functions["apps_delete_token"] = ghes.delete(
        "/applications/{client_id}/token",
        t.struct({"client_id": t.string(), "access_token": t.string()}),
        t.boolean(),
        content_type="application/json",
        body_fields=("access_token",),
    )
    functions["apps_scope_token"] = ghes.post(
        "/applications/{client_id}/token/scoped",
        t.struct(
            {
                "client_id": t.string(),
                "access_token": t.string(),
                "target": t.string().optional(),
                "target_id": t.integer().optional(),
                "repositories": t.array(t.string()).optional(),
                "repository_ids": t.array(t.integer()).optional(),
                "permissions": t.proxy(renames["app_permissions"]).optional(),
            }
        ),
        t.proxy(renames["authorization"]).optional(),
        content_type="application/json",
        body_fields=(
            "access_token",
            "target",
            "target_id",
            "repositories",
            "repository_ids",
            "permissions",
        ),
    )
    functions["apps_check_authorization"] = ghes.get(
        "/applications/{client_id}/tokens/{access_token}",
        t.struct({"client_id": t.string(), "access_token": t.string()}),
        t.proxy(renames["nullable_authorization"]).optional(),
    )
    functions["apps_reset_authorization"] = ghes.post(
        "/applications/{client_id}/tokens/{access_token}",
        t.struct({"client_id": t.string(), "access_token": t.string()}),
        t.proxy(renames["authorization"]),
    )
    functions["apps_revoke_authorization_for_application"] = ghes.delete(
        "/applications/{client_id}/tokens/{access_token}",
        t.struct({"client_id": t.string(), "access_token": t.string()}),
        t.boolean(),
    )
    functions["apps_get_by_slug"] = ghes.get(
        "/apps/{app_slug}",
        t.struct({"app_slug": t.string()}),
        t.proxy(renames["integration"]).optional(),
    )
    functions["oauth_authorizations_list_authorizations"] = ghes.get(
        "/authorizations",
        t.struct(
            {"per_page": t.integer(), "page": t.integer(), "client_id": t.string()}
        ),
        t.array(t.proxy(renames["authorization"])).optional(),
    )
    functions["oauth_authorizations_create_authorization"] = ghes.post(
        "/authorizations",
        t.struct(
            {
                "scopes": t.array(t.string()).optional(),
                "note": t.string().optional(),
                "note_url": t.string().optional(),
                "client_id": t.string().optional(),
                "client_secret": t.string().optional(),
                "fingerprint": t.string().optional(),
            }
        ),
        t.proxy(renames["authorization"]),
        content_type="application/json",
        body_fields=(
            "scopes",
            "note",
            "note_url",
            "client_id",
            "client_secret",
            "fingerprint",
        ),
    )
    functions["oauth_authorizations_get_or_create_authorization_for_app"] = ghes.put(
        "/authorizations/clients/{client_id}",
        t.struct(
            {
                "client_id": t.string(),
                "client_secret": t.string(),
                "scopes": t.array(t.string()).optional(),
                "note": t.string().optional(),
                "note_url": t.string().optional(),
                "fingerprint": t.string().optional(),
            }
        ),
        t.proxy(renames["authorization"]),
        content_type="application/json",
        body_fields=("client_secret", "scopes", "note", "note_url", "fingerprint"),
    )
    functions[
        "oauth_authorizations_get_or_create_authorization_for_app_and_fingerprint"
    ] = ghes.put(
        "/authorizations/clients/{client_id}/{fingerprint}",
        t.struct(
            {
                "client_id": t.string(),
                "fingerprint": t.string(),
                "client_secret": t.string(),
                "scopes": t.array(t.string()).optional(),
                "note": t.string().optional(),
                "note_url": t.string().optional(),
            }
        ),
        t.proxy(renames["authorization"]),
        content_type="application/json",
        body_fields=("client_secret", "scopes", "note", "note_url"),
    )
    functions["oauth_authorizations_get_authorization"] = ghes.get(
        "/authorizations/{authorization_id}",
        t.struct({"authorization_id": t.integer()}),
        t.proxy(renames["authorization"]),
    )
    functions["oauth_authorizations_update_authorization"] = ghes.patch(
        "/authorizations/{authorization_id}",
        t.struct(
            {
                "authorization_id": t.integer(),
                "scopes": t.array(t.string()).optional(),
                "add_scopes": t.array(t.string()).optional(),
                "remove_scopes": t.array(t.string()).optional(),
                "note": t.string().optional(),
                "note_url": t.string().optional(),
                "fingerprint": t.string().optional(),
            }
        ),
        t.proxy(renames["authorization"]),
        content_type="application/json",
        body_fields=(
            "scopes",
            "add_scopes",
            "remove_scopes",
            "note",
            "note_url",
            "fingerprint",
        ),
    )
    functions["oauth_authorizations_delete_authorization"] = ghes.delete(
        "/authorizations/{authorization_id}",
        t.struct({"authorization_id": t.integer()}),
        t.boolean(),
    )
    functions["codes_of_conduct_get_all_codes_of_conduct"] = ghes.get(
        "/codes_of_conduct",
        t.struct({}),
        t.array(t.proxy(renames["code_of_conduct"])),
    )
    functions["codes_of_conduct_get_conduct_code"] = ghes.get(
        "/codes_of_conduct/{key}",
        t.struct({"key": t.string()}),
        t.proxy(renames["code_of_conduct"]).optional(),
    )
    functions["emojis_get"] = ghes.get(
        "/emojis",
        t.struct({}),
        t.struct({}),
    )
    functions["enterprise_admin_get_announcement"] = ghes.get(
        "/enterprise/announcement",
        t.struct({}),
        t.proxy(renames["announcement"]),
    )
    functions["enterprise_admin_set_announcement"] = ghes.patch(
        "/enterprise/announcement",
        t.struct(
            {
                "announcement": t.proxy(renames["announcement_message"]),
                "expires_at": t.proxy(renames["announcement_expiration"]).optional(),
            }
        ),
        t.proxy(renames["announcement"]),
        content_type="application/json",
        body_fields=("announcement", "expires_at"),
    )
    functions["enterprise_admin_remove_announcement"] = ghes.delete(
        "/enterprise/announcement",
        t.struct({}),
        t.boolean(),
    )
    functions["enterprise_admin_get_license_information"] = ghes.get(
        "/enterprise/settings/license",
        t.struct({}),
        t.proxy(renames["license_info"]),
    )
    functions["enterprise_admin_get_all_stats"] = ghes.get(
        "/enterprise/stats/all",
        t.struct({}),
        t.proxy(renames["enterprise_overview"]),
    )
    functions["enterprise_admin_get_comment_stats"] = ghes.get(
        "/enterprise/stats/comments",
        t.struct({}),
        t.proxy(renames["enterprise_comment_overview"]),
    )
    functions["enterprise_admin_get_gist_stats"] = ghes.get(
        "/enterprise/stats/gists",
        t.struct({}),
        t.proxy(renames["enterprise_gist_overview"]),
    )
    functions["enterprise_admin_get_hooks_stats"] = ghes.get(
        "/enterprise/stats/hooks",
        t.struct({}),
        t.proxy(renames["enterprise_hook_overview"]),
    )
    functions["enterprise_admin_get_issue_stats"] = ghes.get(
        "/enterprise/stats/issues",
        t.struct({}),
        t.proxy(renames["enterprise_issue_overview"]),
    )
    functions["enterprise_admin_get_milestone_stats"] = ghes.get(
        "/enterprise/stats/milestones",
        t.struct({}),
        t.proxy(renames["enterprise_milestone_overview"]),
    )
    functions["enterprise_admin_get_org_stats"] = ghes.get(
        "/enterprise/stats/orgs",
        t.struct({}),
        t.proxy(renames["enterprise_organization_overview"]),
    )
    functions["enterprise_admin_get_pages_stats"] = ghes.get(
        "/enterprise/stats/pages",
        t.struct({}),
        t.proxy(renames["enterprise_page_overview"]),
    )
    functions["enterprise_admin_get_pull_request_stats"] = ghes.get(
        "/enterprise/stats/pulls",
        t.struct({}),
        t.proxy(renames["enterprise_pull_request_overview"]),
    )
    functions["enterprise_admin_get_repo_stats"] = ghes.get(
        "/enterprise/stats/repos",
        t.struct({}),
        t.proxy(renames["enterprise_repository_overview"]),
    )
    functions["enterprise_admin_get_user_stats"] = ghes.get(
        "/enterprise/stats/users",
        t.struct({}),
        t.proxy(renames["enterprise_user_overview"]),
    )
    functions["enterprise_admin_get_github_actions_permissions_enterprise"] = ghes.get(
        "/enterprises/{enterprise}/actions/permissions",
        t.struct({"enterprise": t.string()}),
        t.proxy(renames["actions_enterprise_permissions"]),
    )
    functions["enterprise_admin_set_github_actions_permissions_enterprise"] = ghes.put(
        "/enterprises/{enterprise}/actions/permissions",
        t.struct(
            {
                "enterprise": t.string(),
                "enabled_organizations": t.proxy(renames["enabled_organizations"]),
                "allowed_actions": t.proxy(renames["allowed_actions"]).optional(),
            }
        ),
        t.boolean(),
        content_type="application/json",
        body_fields=("enabled_organizations", "allowed_actions"),
    )
    functions[
        "enterprise_admin_list_selected_organizations_enabled_github_actions_enterprise"
    ] = ghes.get(
        "/enterprises/{enterprise}/actions/permissions/organizations",
        t.struct(
            {"enterprise": t.string(), "per_page": t.integer(), "page": t.integer()}
        ),
        t.struct(
            {
                "total_count": t.number(),
                "organizations": t.array(t.proxy(renames["organization_simple"])),
            }
        ),
    )
    functions[
        "enterprise_admin_set_selected_organizations_enabled_github_actions_enterprise"
    ] = ghes.put(
        "/enterprises/{enterprise}/actions/permissions/organizations",
        t.struct(
            {
                "enterprise": t.string(),
                "selected_organization_ids": t.array(t.integer()),
            }
        ),
        t.boolean(),
        content_type="application/json",
        body_fields=("selected_organization_ids",),
    )
    functions[
        "enterprise_admin_enable_selected_organization_github_actions_enterprise"
    ] = ghes.put(
        "/enterprises/{enterprise}/actions/permissions/organizations/{org_id}",
        t.struct({"enterprise": t.string(), "org_id": t.integer()}),
        t.boolean(),
    )
    functions[
        "enterprise_admin_disable_selected_organization_github_actions_enterprise"
    ] = ghes.delete(
        "/enterprises/{enterprise}/actions/permissions/organizations/{org_id}",
        t.struct({"enterprise": t.string(), "org_id": t.integer()}),
        t.boolean(),
    )
    functions["enterprise_admin_get_allowed_actions_enterprise"] = ghes.get(
        "/enterprises/{enterprise}/actions/permissions/selected-actions",
        t.struct({"enterprise": t.string()}),
        t.proxy(renames["selected_actions"]),
    )
    functions["enterprise_admin_set_allowed_actions_enterprise"] = ghes.put(
        "/enterprises/{enterprise}/actions/permissions/selected-actions",
        t.struct(
            {
                "enterprise": t.string(),
                "github_owned_allowed": t.boolean(),
                "patterns_allowed": t.array(t.string()),
            }
        ),
        t.boolean(),
        content_type="application/json",
        body_fields=("github_owned_allowed", "patterns_allowed"),
    )
    functions[
        "enterprise_admin_list_self_hosted_runner_groups_for_enterprise"
    ] = ghes.get(
        "/enterprises/{enterprise}/actions/runner-groups",
        t.struct(
            {"enterprise": t.string(), "per_page": t.integer(), "page": t.integer()}
        ),
        t.struct(
            {
                "total_count": t.number(),
                "runner_groups": t.array(t.proxy(renames["runner_groups_enterprise"])),
            }
        ),
    )
    functions[
        "enterprise_admin_create_self_hosted_runner_group_for_enterprise"
    ] = ghes.post(
        "/enterprises/{enterprise}/actions/runner-groups",
        t.struct(
            {
                "enterprise": t.string(),
                "name": t.string(),
                "visibility": t.string().optional(),
                "selected_organization_ids": t.array(t.integer()).optional(),
                "runners": t.array(t.integer()).optional(),
                "allows_public_repositories": t.boolean().optional(),
            }
        ),
        t.proxy(renames["runner_groups_enterprise"]),
        content_type="application/json",
        body_fields=(
            "name",
            "visibility",
            "selected_organization_ids",
            "runners",
            "allows_public_repositories",
        ),
    )
    functions[
        "enterprise_admin_get_self_hosted_runner_group_for_enterprise"
    ] = ghes.get(
        "/enterprises/{enterprise}/actions/runner-groups/{runner_group_id}",
        t.struct({"enterprise": t.string(), "runner_group_id": t.integer()}),
        t.proxy(renames["runner_groups_enterprise"]),
    )
    functions[
        "enterprise_admin_update_self_hosted_runner_group_for_enterprise"
    ] = ghes.patch(
        "/enterprises/{enterprise}/actions/runner-groups/{runner_group_id}",
        t.struct(
            {
                "enterprise": t.string(),
                "runner_group_id": t.integer(),
                "name": t.string().optional(),
                "visibility": t.string().optional(),
                "allows_public_repositories": t.boolean().optional(),
            }
        ),
        t.proxy(renames["runner_groups_enterprise"]),
        content_type="application/json",
        body_fields=("name", "visibility", "allows_public_repositories"),
    )
    functions[
        "enterprise_admin_delete_self_hosted_runner_group_from_enterprise"
    ] = ghes.delete(
        "/enterprises/{enterprise}/actions/runner-groups/{runner_group_id}",
        t.struct({"enterprise": t.string(), "runner_group_id": t.integer()}),
        t.boolean(),
    )
    functions[
        "enterprise_admin_list_org_access_to_self_hosted_runner_group_in_enterprise"
    ] = ghes.get(
        "/enterprises/{enterprise}/actions/runner-groups/{runner_group_id}/organizations",
        t.struct(
            {
                "enterprise": t.string(),
                "runner_group_id": t.integer(),
                "per_page": t.integer(),
                "page": t.integer(),
            }
        ),
        t.struct(
            {
                "total_count": t.number(),
                "organizations": t.array(t.proxy(renames["organization_simple"])),
            }
        ),
    )
    functions[
        "enterprise_admin_set_org_access_to_self_hosted_runner_group_in_enterprise"
    ] = ghes.put(
        "/enterprises/{enterprise}/actions/runner-groups/{runner_group_id}/organizations",
        t.struct(
            {
                "enterprise": t.string(),
                "runner_group_id": t.integer(),
                "selected_organization_ids": t.array(t.integer()),
            }
        ),
        t.boolean(),
        content_type="application/json",
        body_fields=("selected_organization_ids",),
    )
    functions[
        "enterprise_admin_add_org_access_to_self_hosted_runner_group_in_enterprise"
    ] = ghes.put(
        "/enterprises/{enterprise}/actions/runner-groups/{runner_group_id}/organizations/{org_id}",
        t.struct(
            {
                "enterprise": t.string(),
                "runner_group_id": t.integer(),
                "org_id": t.integer(),
            }
        ),
        t.boolean(),
    )
    functions[
        "enterprise_admin_remove_org_access_to_self_hosted_runner_group_in_enterprise"
    ] = ghes.delete(
        "/enterprises/{enterprise}/actions/runner-groups/{runner_group_id}/organizations/{org_id}",
        t.struct(
            {
                "enterprise": t.string(),
                "runner_group_id": t.integer(),
                "org_id": t.integer(),
            }
        ),
        t.boolean(),
    )
    functions[
        "enterprise_admin_list_self_hosted_runners_in_group_for_enterprise"
    ] = ghes.get(
        "/enterprises/{enterprise}/actions/runner-groups/{runner_group_id}/runners",
        t.struct(
            {
                "enterprise": t.string(),
                "runner_group_id": t.integer(),
                "per_page": t.integer(),
                "page": t.integer(),
            }
        ),
        t.struct(
            {"total_count": t.number(), "runners": t.array(t.proxy(renames["runner"]))}
        ),
    )
    functions[
        "enterprise_admin_set_self_hosted_runners_in_group_for_enterprise"
    ] = ghes.put(
        "/enterprises/{enterprise}/actions/runner-groups/{runner_group_id}/runners",
        t.struct(
            {
                "enterprise": t.string(),
                "runner_group_id": t.integer(),
                "runners": t.array(t.integer()),
            }
        ),
        t.boolean(),
        content_type="application/json",
        body_fields=("runners",),
    )
    functions[
        "enterprise_admin_add_self_hosted_runner_to_group_for_enterprise"
    ] = ghes.put(
        "/enterprises/{enterprise}/actions/runner-groups/{runner_group_id}/runners/{runner_id}",
        t.struct(
            {
                "enterprise": t.string(),
                "runner_group_id": t.integer(),
                "runner_id": t.integer(),
            }
        ),
        t.boolean(),
    )
    functions[
        "enterprise_admin_remove_self_hosted_runner_from_group_for_enterprise"
    ] = ghes.delete(
        "/enterprises/{enterprise}/actions/runner-groups/{runner_group_id}/runners/{runner_id}",
        t.struct(
            {
                "enterprise": t.string(),
                "runner_group_id": t.integer(),
                "runner_id": t.integer(),
            }
        ),
        t.boolean(),
    )
    functions["enterprise_admin_list_self_hosted_runners_for_enterprise"] = ghes.get(
        "/enterprises/{enterprise}/actions/runners",
        t.struct(
            {"enterprise": t.string(), "per_page": t.integer(), "page": t.integer()}
        ),
        t.struct(
            {
                "total_count": t.number().optional(),
                "runners": t.array(t.proxy(renames["runner"])).optional(),
            }
        ),
    )
    functions["enterprise_admin_list_runner_applications_for_enterprise"] = ghes.get(
        "/enterprises/{enterprise}/actions/runners/downloads",
        t.struct({"enterprise": t.string()}),
        t.array(t.proxy(renames["runner_application"])),
    )
    functions["enterprise_admin_create_registration_token_for_enterprise"] = ghes.post(
        "/enterprises/{enterprise}/actions/runners/registration-token",
        t.struct({"enterprise": t.string()}),
        t.proxy(renames["authentication_token"]),
    )
    functions["enterprise_admin_create_remove_token_for_enterprise"] = ghes.post(
        "/enterprises/{enterprise}/actions/runners/remove-token",
        t.struct({"enterprise": t.string()}),
        t.proxy(renames["authentication_token"]),
    )
    functions["enterprise_admin_get_self_hosted_runner_for_enterprise"] = ghes.get(
        "/enterprises/{enterprise}/actions/runners/{runner_id}",
        t.struct({"enterprise": t.string(), "runner_id": t.integer()}),
        t.proxy(renames["runner"]),
    )
    functions[
        "enterprise_admin_delete_self_hosted_runner_from_enterprise"
    ] = ghes.delete(
        "/enterprises/{enterprise}/actions/runners/{runner_id}",
        t.struct({"enterprise": t.string(), "runner_id": t.integer()}),
        t.boolean(),
    )
    functions["activity_list_public_events"] = ghes.get(
        "/events",
        t.struct({"per_page": t.integer(), "page": t.integer()}),
        t.array(t.proxy(renames["event"])),
    )
    functions["activity_get_feeds"] = ghes.get(
        "/feeds",
        t.struct({}),
        t.proxy(renames["feed"]),
    )
    functions["gists_list"] = ghes.get(
        "/gists",
        t.struct({"since": t.string(), "per_page": t.integer(), "page": t.integer()}),
        t.array(t.proxy(renames["base_gist"])),
    )
    functions["gists_create"] = ghes.post(
        "/gists",
        t.struct(
            {
                "description": t.string().optional(),
                "files": t.struct({}),
                "public": t.either([t.boolean(), t.string()]).optional(),
            }
        ),
        t.proxy(renames["gist_simple"]).optional(),
        content_type="application/json",
        body_fields=("description", "files", "public"),
    )
    functions["gists_list_public"] = ghes.get(
        "/gists/public",
        t.struct({"since": t.string(), "per_page": t.integer(), "page": t.integer()}),
        t.array(t.proxy(renames["base_gist"])),
    )
    functions["gists_list_starred"] = ghes.get(
        "/gists/starred",
        t.struct({"since": t.string(), "per_page": t.integer(), "page": t.integer()}),
        t.array(t.proxy(renames["base_gist"])),
    )
    functions["gists_get"] = ghes.get(
        "/gists/{gist_id}",
        t.struct({"gist_id": t.string()}),
        t.proxy(renames["gist_simple"]).optional(),
    )
    functions["gists_delete"] = ghes.delete(
        "/gists/{gist_id}",
        t.struct({"gist_id": t.string()}),
        t.boolean().optional(),
    )
    functions["gists_list_comments"] = ghes.get(
        "/gists/{gist_id}/comments",
        t.struct({"gist_id": t.string(), "per_page": t.integer(), "page": t.integer()}),
        t.array(t.proxy(renames["gist_comment"])).optional(),
    )
    functions["gists_create_comment"] = ghes.post(
        "/gists/{gist_id}/comments",
        t.struct({"gist_id": t.string(), "body": t.string()}),
        t.proxy(renames["gist_comment"]).optional(),
        content_type="application/json",
        body_fields=("body",),
    )
    functions["gists_get_comment"] = ghes.get(
        "/gists/{gist_id}/comments/{comment_id}",
        t.struct({"gist_id": t.string(), "comment_id": t.integer()}),
        t.proxy(renames["gist_comment"]).optional(),
    )
    functions["gists_update_comment"] = ghes.patch(
        "/gists/{gist_id}/comments/{comment_id}",
        t.struct(
            {"gist_id": t.string(), "comment_id": t.integer(), "body": t.string()}
        ),
        t.proxy(renames["gist_comment"]).optional(),
        content_type="application/json",
        body_fields=("body",),
    )
    functions["gists_delete_comment"] = ghes.delete(
        "/gists/{gist_id}/comments/{comment_id}",
        t.struct({"gist_id": t.string(), "comment_id": t.integer()}),
        t.boolean().optional(),
    )
    functions["gists_list_commits"] = ghes.get(
        "/gists/{gist_id}/commits",
        t.struct({"gist_id": t.string(), "per_page": t.integer(), "page": t.integer()}),
        t.array(t.proxy(renames["gist_commit"])).optional(),
    )
    functions["gists_list_forks"] = ghes.get(
        "/gists/{gist_id}/forks",
        t.struct({"gist_id": t.string(), "per_page": t.integer(), "page": t.integer()}),
        t.array(t.proxy(renames["gist_simple"])).optional(),
    )
    functions["gists_fork"] = ghes.post(
        "/gists/{gist_id}/forks",
        t.struct({"gist_id": t.string()}),
        t.proxy(renames["base_gist"]).optional(),
    )
    functions["gists_check_is_starred"] = ghes.get(
        "/gists/{gist_id}/star",
        t.struct({"gist_id": t.string()}),
        t.boolean().optional(),
    )
    functions["gists_star"] = ghes.put(
        "/gists/{gist_id}/star",
        t.struct({"gist_id": t.string()}),
        t.boolean().optional(),
    )
    functions["gists_unstar"] = ghes.delete(
        "/gists/{gist_id}/star",
        t.struct({"gist_id": t.string()}),
        t.boolean().optional(),
    )
    functions["gists_get_revision"] = ghes.get(
        "/gists/{gist_id}/{sha}",
        t.struct({"gist_id": t.string(), "sha": t.string()}),
        t.proxy(renames["gist_simple"]).optional(),
    )
    functions["gitignore_get_all_templates"] = ghes.get(
        "/gitignore/templates",
        t.struct({}),
        t.array(t.string()),
    )
    functions["gitignore_get_template"] = ghes.get(
        "/gitignore/templates/{name}",
        t.struct({"name": t.string()}),
        t.proxy(renames["gitignore_template"]),
    )
    functions["apps_list_repos_accessible_to_installation"] = ghes.get(
        "/installation/repositories",
        t.struct({"per_page": t.integer(), "page": t.integer()}),
        t.struct(
            {
                "total_count": t.integer(),
                "repositories": t.array(t.proxy(renames["repository"])),
                "repository_selection": t.string().optional(),
            }
        ),
    )
    functions["apps_revoke_installation_access_token"] = ghes.delete(
        "/installation/token",
        t.struct({}),
        t.boolean(),
    )
    functions["issues_list"] = ghes.get(
        "/issues",
        t.struct(
            {
                "filter": t.string(),
                "state": t.string(),
                "labels": t.string(),
                "sort": t.string(),
                "direction": t.string(),
                "since": t.string(),
                "collab": t.boolean(),
                "orgs": t.boolean(),
                "owned": t.boolean(),
                "pulls": t.boolean(),
                "per_page": t.integer(),
                "page": t.integer(),
            }
        ),
        t.array(t.proxy(renames["issue"])).optional(),
    )
    functions["licenses_get_all_commonly_used"] = ghes.get(
        "/licenses",
        t.struct(
            {"featured": t.boolean(), "per_page": t.integer(), "page": t.integer()}
        ),
        t.array(t.proxy(renames["license_simple"])),
    )
    functions["licenses_get"] = ghes.get(
        "/licenses/{license}",
        t.struct({"license": t.string()}),
        t.proxy(renames["license"]).optional(),
    )
    functions["meta_get"] = ghes.get(
        "/meta",
        t.struct({}),
        t.proxy(renames["api_overview"]),
    )
    functions["activity_list_public_events_for_repo_network"] = ghes.get(
        "/networks/{owner}/{repo}/events",
        t.struct(
            {
                "owner": t.string(),
                "repo": t.string(),
                "per_page": t.integer(),
                "page": t.integer(),
            }
        ),
        t.array(t.proxy(renames["event"])).optional(),
    )
    functions["activity_list_notifications_for_authenticated_user"] = ghes.get(
        "/notifications",
        t.struct(
            {
                "all": t.boolean(),
                "participating": t.boolean(),
                "since": t.string(),
                "before": t.string(),
                "per_page": t.integer(),
                "page": t.integer(),
            }
        ),
        t.array(t.proxy(renames["thread"])),
    )
    functions["activity_mark_notifications_as_read"] = ghes.put(
        "/notifications",
        t.struct(
            {"last_read_at": t.string().optional(), "read": t.boolean().optional()}
        ),
        t.struct({"message": t.string().optional()}),
        content_type="application/json",
        body_fields=("last_read_at", "read"),
    )
    functions["activity_get_thread"] = ghes.get(
        "/notifications/threads/{thread_id}",
        t.struct({"thread_id": t.integer()}),
        t.proxy(renames["thread"]),
    )
    functions["activity_mark_thread_as_read"] = ghes.patch(
        "/notifications/threads/{thread_id}",
        t.struct({"thread_id": t.integer()}),
        t.struct({}),
    )
    functions["activity_get_thread_subscription_for_authenticated_user"] = ghes.get(
        "/notifications/threads/{thread_id}/subscription",
        t.struct({"thread_id": t.integer()}),
        t.proxy(renames["thread_subscription"]),
    )
    functions["activity_set_thread_subscription"] = ghes.put(
        "/notifications/threads/{thread_id}/subscription",
        t.struct({"thread_id": t.integer(), "ignored": t.boolean().optional()}),
        t.proxy(renames["thread_subscription"]),
        content_type="application/json",
        body_fields=("ignored",),
    )
    functions["activity_delete_thread_subscription"] = ghes.delete(
        "/notifications/threads/{thread_id}/subscription",
        t.struct({"thread_id": t.integer()}),
        t.boolean(),
    )
    functions["orgs_list"] = ghes.get(
        "/organizations",
        t.struct({"since": t.integer(), "per_page": t.integer()}),
        t.array(t.proxy(renames["organization_simple"])),
    )
    functions["orgs_get"] = ghes.get(
        "/orgs/{org}",
        t.struct({"org": t.string()}),
        t.proxy(renames["organization_full"]).optional(),
    )
    functions["orgs_update"] = ghes.patch(
        "/orgs/{org}",
        t.struct(
            {
                "org": t.string(),
                "billing_email": t.string().optional(),
                "company": t.string().optional(),
                "email": t.string().optional(),
                "twitter_username": t.string().optional(),
                "location": t.string().optional(),
                "name": t.string().optional(),
                "description": t.string().optional(),
                "has_organization_projects": t.boolean().optional(),
                "has_repository_projects": t.boolean().optional(),
                "default_repository_permission": t.string().optional(),
                "members_can_create_repositories": t.boolean().optional(),
                "members_can_create_internal_repositories": t.boolean().optional(),
                "members_can_create_private_repositories": t.boolean().optional(),
                "members_can_create_public_repositories": t.boolean().optional(),
                "members_allowed_repository_creation_type": t.string().optional(),
                "members_can_create_pages": t.boolean().optional(),
                "members_can_fork_private_repositories": t.boolean().optional(),
                "blog": t.string().optional(),
            }
        ),
        t.proxy(renames["organization_full"]),
        content_type="application/json",
        body_fields=(
            "billing_email",
            "company",
            "email",
            "twitter_username",
            "location",
            "name",
            "description",
            "has_organization_projects",
            "has_repository_projects",
            "default_repository_permission",
            "members_can_create_repositories",
            "members_can_create_internal_repositories",
            "members_can_create_private_repositories",
            "members_can_create_public_repositories",
            "members_allowed_repository_creation_type",
            "members_can_create_pages",
            "members_can_fork_private_repositories",
            "blog",
        ),
    )
    functions["actions_get_github_actions_permissions_organization"] = ghes.get(
        "/orgs/{org}/actions/permissions",
        t.struct({"org": t.string()}),
        t.proxy(renames["actions_organization_permissions"]),
    )
    functions["actions_set_github_actions_permissions_organization"] = ghes.put(
        "/orgs/{org}/actions/permissions",
        t.struct(
            {
                "org": t.string(),
                "enabled_repositories": t.proxy(renames["enabled_repositories"]),
                "allowed_actions": t.proxy(renames["allowed_actions"]).optional(),
            }
        ),
        t.boolean(),
        content_type="application/json",
        body_fields=("enabled_repositories", "allowed_actions"),
    )
    functions[
        "actions_list_selected_repositories_enabled_github_actions_organization"
    ] = ghes.get(
        "/orgs/{org}/actions/permissions/repositories",
        t.struct({"org": t.string(), "per_page": t.integer(), "page": t.integer()}),
        t.struct(
            {
                "total_count": t.number(),
                "repositories": t.array(t.proxy(renames["repository"])),
            }
        ),
    )
    functions[
        "actions_set_selected_repositories_enabled_github_actions_organization"
    ] = ghes.put(
        "/orgs/{org}/actions/permissions/repositories",
        t.struct({"org": t.string(), "selected_repository_ids": t.array(t.integer())}),
        t.boolean(),
        content_type="application/json",
        body_fields=("selected_repository_ids",),
    )
    functions[
        "actions_enable_selected_repository_github_actions_organization"
    ] = ghes.put(
        "/orgs/{org}/actions/permissions/repositories/{repository_id}",
        t.struct({"org": t.string(), "repository_id": t.integer()}),
        t.boolean(),
    )
    functions[
        "actions_disable_selected_repository_github_actions_organization"
    ] = ghes.delete(
        "/orgs/{org}/actions/permissions/repositories/{repository_id}",
        t.struct({"org": t.string(), "repository_id": t.integer()}),
        t.boolean(),
    )
    functions["actions_get_allowed_actions_organization"] = ghes.get(
        "/orgs/{org}/actions/permissions/selected-actions",
        t.struct({"org": t.string()}),
        t.proxy(renames["selected_actions"]),
    )
    functions["actions_set_allowed_actions_organization"] = ghes.put(
        "/orgs/{org}/actions/permissions/selected-actions",
        t.struct(
            {
                "org": t.string(),
                "github_owned_allowed": t.boolean(),
                "patterns_allowed": t.array(t.string()),
            }
        ),
        t.boolean(),
        content_type="application/json",
        body_fields=("github_owned_allowed", "patterns_allowed"),
    )
    functions["actions_list_self_hosted_runner_groups_for_org"] = ghes.get(
        "/orgs/{org}/actions/runner-groups",
        t.struct({"org": t.string(), "per_page": t.integer(), "page": t.integer()}),
        t.struct(
            {
                "total_count": t.number(),
                "runner_groups": t.array(t.proxy(renames["runner_groups_org"])),
            }
        ),
    )
    functions["actions_create_self_hosted_runner_group_for_org"] = ghes.post(
        "/orgs/{org}/actions/runner-groups",
        t.struct(
            {
                "org": t.string(),
                "name": t.string(),
                "visibility": t.string().optional(),
                "selected_repository_ids": t.array(t.integer()).optional(),
                "runners": t.array(t.integer()).optional(),
                "allows_public_repositories": t.boolean().optional(),
            }
        ),
        t.proxy(renames["runner_groups_org"]),
        content_type="application/json",
        body_fields=(
            "name",
            "visibility",
            "selected_repository_ids",
            "runners",
            "allows_public_repositories",
        ),
    )
    functions["actions_get_self_hosted_runner_group_for_org"] = ghes.get(
        "/orgs/{org}/actions/runner-groups/{runner_group_id}",
        t.struct({"org": t.string(), "runner_group_id": t.integer()}),
        t.proxy(renames["runner_groups_org"]),
    )
    functions["actions_update_self_hosted_runner_group_for_org"] = ghes.patch(
        "/orgs/{org}/actions/runner-groups/{runner_group_id}",
        t.struct(
            {
                "org": t.string(),
                "runner_group_id": t.integer(),
                "name": t.string(),
                "visibility": t.string().optional(),
                "allows_public_repositories": t.boolean().optional(),
            }
        ),
        t.proxy(renames["runner_groups_org"]),
        content_type="application/json",
        body_fields=("name", "visibility", "allows_public_repositories"),
    )
    functions["actions_delete_self_hosted_runner_group_from_org"] = ghes.delete(
        "/orgs/{org}/actions/runner-groups/{runner_group_id}",
        t.struct({"org": t.string(), "runner_group_id": t.integer()}),
        t.boolean(),
    )
    functions["actions_list_repo_access_to_self_hosted_runner_group_in_org"] = ghes.get(
        "/orgs/{org}/actions/runner-groups/{runner_group_id}/repositories",
        t.struct(
            {
                "org": t.string(),
                "runner_group_id": t.integer(),
                "page": t.integer(),
                "per_page": t.integer(),
            }
        ),
        t.struct(
            {
                "total_count": t.number(),
                "repositories": t.array(t.proxy(renames["minimal_repository"])),
            }
        ),
    )
    functions["actions_set_repo_access_to_self_hosted_runner_group_in_org"] = ghes.put(
        "/orgs/{org}/actions/runner-groups/{runner_group_id}/repositories",
        t.struct(
            {
                "org": t.string(),
                "runner_group_id": t.integer(),
                "selected_repository_ids": t.array(t.integer()),
            }
        ),
        t.boolean(),
        content_type="application/json",
        body_fields=("selected_repository_ids",),
    )
    functions["actions_add_repo_access_to_self_hosted_runner_group_in_org"] = ghes.put(
        "/orgs/{org}/actions/runner-groups/{runner_group_id}/repositories/{repository_id}",
        t.struct(
            {
                "org": t.string(),
                "runner_group_id": t.integer(),
                "repository_id": t.integer(),
            }
        ),
        t.boolean(),
    )
    functions[
        "actions_remove_repo_access_to_self_hosted_runner_group_in_org"
    ] = ghes.delete(
        "/orgs/{org}/actions/runner-groups/{runner_group_id}/repositories/{repository_id}",
        t.struct(
            {
                "org": t.string(),
                "runner_group_id": t.integer(),
                "repository_id": t.integer(),
            }
        ),
        t.boolean(),
    )
    functions["actions_list_self_hosted_runners_in_group_for_org"] = ghes.get(
        "/orgs/{org}/actions/runner-groups/{runner_group_id}/runners",
        t.struct(
            {
                "org": t.string(),
                "runner_group_id": t.integer(),
                "per_page": t.integer(),
                "page": t.integer(),
            }
        ),
        t.struct(
            {"total_count": t.number(), "runners": t.array(t.proxy(renames["runner"]))}
        ),
    )
    functions["actions_set_self_hosted_runners_in_group_for_org"] = ghes.put(
        "/orgs/{org}/actions/runner-groups/{runner_group_id}/runners",
        t.struct(
            {
                "org": t.string(),
                "runner_group_id": t.integer(),
                "runners": t.array(t.integer()),
            }
        ),
        t.boolean(),
        content_type="application/json",
        body_fields=("runners",),
    )
    functions["actions_add_self_hosted_runner_to_group_for_org"] = ghes.put(
        "/orgs/{org}/actions/runner-groups/{runner_group_id}/runners/{runner_id}",
        t.struct(
            {
                "org": t.string(),
                "runner_group_id": t.integer(),
                "runner_id": t.integer(),
            }
        ),
        t.boolean(),
    )
    functions["actions_remove_self_hosted_runner_from_group_for_org"] = ghes.delete(
        "/orgs/{org}/actions/runner-groups/{runner_group_id}/runners/{runner_id}",
        t.struct(
            {
                "org": t.string(),
                "runner_group_id": t.integer(),
                "runner_id": t.integer(),
            }
        ),
        t.boolean(),
    )
    functions["actions_list_self_hosted_runners_for_org"] = ghes.get(
        "/orgs/{org}/actions/runners",
        t.struct({"org": t.string(), "per_page": t.integer(), "page": t.integer()}),
        t.struct(
            {"total_count": t.integer(), "runners": t.array(t.proxy(renames["runner"]))}
        ),
    )
    functions["actions_list_runner_applications_for_org"] = ghes.get(
        "/orgs/{org}/actions/runners/downloads",
        t.struct({"org": t.string()}),
        t.array(t.proxy(renames["runner_application"])),
    )
    functions["actions_create_registration_token_for_org"] = ghes.post(
        "/orgs/{org}/actions/runners/registration-token",
        t.struct({"org": t.string()}),
        t.proxy(renames["authentication_token"]),
    )
    functions["actions_create_remove_token_for_org"] = ghes.post(
        "/orgs/{org}/actions/runners/remove-token",
        t.struct({"org": t.string()}),
        t.proxy(renames["authentication_token"]),
    )
    functions["actions_get_self_hosted_runner_for_org"] = ghes.get(
        "/orgs/{org}/actions/runners/{runner_id}",
        t.struct({"org": t.string(), "runner_id": t.integer()}),
        t.proxy(renames["runner"]),
    )
    functions["actions_delete_self_hosted_runner_from_org"] = ghes.delete(
        "/orgs/{org}/actions/runners/{runner_id}",
        t.struct({"org": t.string(), "runner_id": t.integer()}),
        t.boolean(),
    )
    functions["actions_list_org_secrets"] = ghes.get(
        "/orgs/{org}/actions/secrets",
        t.struct({"org": t.string(), "per_page": t.integer(), "page": t.integer()}),
        t.struct(
            {
                "total_count": t.integer(),
                "secrets": t.array(t.proxy(renames["organization_actions_secret"])),
            }
        ),
    )
    functions["actions_get_org_public_key"] = ghes.get(
        "/orgs/{org}/actions/secrets/public-key",
        t.struct({"org": t.string()}),
        t.proxy(renames["actions_public_key"]),
    )
    functions["actions_get_org_secret"] = ghes.get(
        "/orgs/{org}/actions/secrets/{secret_name}",
        t.struct({"org": t.string(), "secret_name": t.string()}),
        t.proxy(renames["organization_actions_secret"]),
    )
    functions["actions_create_or_update_org_secret"] = ghes.put(
        "/orgs/{org}/actions/secrets/{secret_name}",
        t.struct(
            {
                "org": t.string(),
                "secret_name": t.string(),
                "encrypted_value": t.string().optional(),
                "key_id": t.string().optional(),
                "visibility": t.string(),
                "selected_repository_ids": t.array(t.string()).optional(),
            }
        ),
        t.proxy(renames["empty_object"]),
        content_type="application/json",
        body_fields=(
            "encrypted_value",
            "key_id",
            "visibility",
            "selected_repository_ids",
        ),
    )
    functions["actions_delete_org_secret"] = ghes.delete(
        "/orgs/{org}/actions/secrets/{secret_name}",
        t.struct({"org": t.string(), "secret_name": t.string()}),
        t.boolean(),
    )
    functions["actions_list_selected_repos_for_org_secret"] = ghes.get(
        "/orgs/{org}/actions/secrets/{secret_name}/repositories",
        t.struct(
            {
                "org": t.string(),
                "secret_name": t.string(),
                "page": t.integer(),
                "per_page": t.integer(),
            }
        ),
        t.struct(
            {
                "total_count": t.integer(),
                "repositories": t.array(t.proxy(renames["minimal_repository"])),
            }
        ),
    )
    functions["actions_set_selected_repos_for_org_secret"] = ghes.put(
        "/orgs/{org}/actions/secrets/{secret_name}/repositories",
        t.struct(
            {
                "org": t.string(),
                "secret_name": t.string(),
                "selected_repository_ids": t.array(t.integer()),
            }
        ),
        t.boolean(),
        content_type="application/json",
        body_fields=("selected_repository_ids",),
    )
    functions["actions_add_selected_repo_to_org_secret"] = ghes.put(
        "/orgs/{org}/actions/secrets/{secret_name}/repositories/{repository_id}",
        t.struct(
            {"org": t.string(), "secret_name": t.string(), "repository_id": t.integer()}
        ),
        t.boolean(),
    )
    functions["actions_remove_selected_repo_from_org_secret"] = ghes.delete(
        "/orgs/{org}/actions/secrets/{secret_name}/repositories/{repository_id}",
        t.struct(
            {"org": t.string(), "secret_name": t.string(), "repository_id": t.integer()}
        ),
        t.boolean(),
    )
    functions["activity_list_public_org_events"] = ghes.get(
        "/orgs/{org}/events",
        t.struct({"org": t.string(), "per_page": t.integer(), "page": t.integer()}),
        t.array(t.proxy(renames["event"])),
    )
    functions["orgs_list_webhooks"] = ghes.get(
        "/orgs/{org}/hooks",
        t.struct({"org": t.string(), "per_page": t.integer(), "page": t.integer()}),
        t.array(t.proxy(renames["org_hook"])).optional(),
    )
    functions["orgs_create_webhook"] = ghes.post(
        "/orgs/{org}/hooks",
        t.struct(
            {
                "org": t.string(),
                "name": t.string(),
                "config": t.struct(
                    {
                        "url": t.proxy(renames["webhook_config_url"]),
                        "content_type": t.proxy(
                            renames["webhook_config_content_type"]
                        ).optional(),
                        "secret": t.proxy(renames["webhook_config_secret"]).optional(),
                        "insecure_ssl": t.proxy(
                            renames["webhook_config_insecure_ssl"]
                        ).optional(),
                        "username": t.string().optional(),
                        "password": t.string().optional(),
                    }
                ),
                "events": t.array(t.string()).optional(),
                "active": t.boolean().optional(),
            }
        ),
        t.proxy(renames["org_hook"]).optional(),
        content_type="application/json",
        body_fields=("name", "config", "events", "active"),
    )
    functions["orgs_get_webhook"] = ghes.get(
        "/orgs/{org}/hooks/{hook_id}",
        t.struct({"org": t.string(), "hook_id": t.integer()}),
        t.proxy(renames["org_hook"]).optional(),
    )
    functions["orgs_update_webhook"] = ghes.patch(
        "/orgs/{org}/hooks/{hook_id}",
        t.struct(
            {
                "org": t.string(),
                "hook_id": t.integer(),
                "config": t.struct(
                    {
                        "url": t.proxy(renames["webhook_config_url"]),
                        "content_type": t.proxy(
                            renames["webhook_config_content_type"]
                        ).optional(),
                        "secret": t.proxy(renames["webhook_config_secret"]).optional(),
                        "insecure_ssl": t.proxy(
                            renames["webhook_config_insecure_ssl"]
                        ).optional(),
                    }
                ).optional(),
                "events": t.array(t.string()).optional(),
                "active": t.boolean().optional(),
                "name": t.string().optional(),
            }
        ),
        t.proxy(renames["org_hook"]).optional(),
        content_type="application/json",
        body_fields=("config", "events", "active", "name"),
    )
    functions["orgs_delete_webhook"] = ghes.delete(
        "/orgs/{org}/hooks/{hook_id}",
        t.struct({"org": t.string(), "hook_id": t.integer()}),
        t.boolean().optional(),
    )
    functions["orgs_get_webhook_config_for_org"] = ghes.get(
        "/orgs/{org}/hooks/{hook_id}/config",
        t.struct({"org": t.string(), "hook_id": t.integer()}),
        t.proxy(renames["webhook_config"]),
    )
    functions["orgs_update_webhook_config_for_org"] = ghes.patch(
        "/orgs/{org}/hooks/{hook_id}/config",
        t.struct(
            {
                "org": t.string(),
                "hook_id": t.integer(),
                "url": t.proxy(renames["webhook_config_url"]).optional(),
                "content_type": t.proxy(
                    renames["webhook_config_content_type"]
                ).optional(),
                "secret": t.proxy(renames["webhook_config_secret"]).optional(),
                "insecure_ssl": t.proxy(
                    renames["webhook_config_insecure_ssl"]
                ).optional(),
            }
        ),
        t.proxy(renames["webhook_config"]),
        content_type="application/json",
        body_fields=("url", "content_type", "secret", "insecure_ssl"),
    )
    functions["orgs_ping_webhook"] = ghes.post(
        "/orgs/{org}/hooks/{hook_id}/pings",
        t.struct({"org": t.string(), "hook_id": t.integer()}),
        t.boolean().optional(),
    )
    functions["apps_get_org_installation"] = ghes.get(
        "/orgs/{org}/installation",
        t.struct({"org": t.string()}),
        t.proxy(renames["installation"]),
    )
    functions["orgs_list_app_installations"] = ghes.get(
        "/orgs/{org}/installations",
        t.struct({"org": t.string(), "per_page": t.integer(), "page": t.integer()}),
        t.struct(
            {
                "total_count": t.integer(),
                "installations": t.array(t.proxy(renames["installation"])),
            }
        ),
    )
    functions["issues_list_for_org"] = ghes.get(
        "/orgs/{org}/issues",
        t.struct(
            {
                "org": t.string(),
                "filter": t.string(),
                "state": t.string(),
                "labels": t.string(),
                "sort": t.string(),
                "direction": t.string(),
                "since": t.string(),
                "per_page": t.integer(),
                "page": t.integer(),
            }
        ),
        t.array(t.proxy(renames["issue"])).optional(),
    )
    functions["orgs_list_members"] = ghes.get(
        "/orgs/{org}/members",
        t.struct(
            {
                "org": t.string(),
                "filter": t.string(),
                "role": t.string(),
                "per_page": t.integer(),
                "page": t.integer(),
            }
        ),
        t.array(t.proxy(renames["simple_user"])),
    )
    functions["orgs_check_membership_for_user"] = ghes.get(
        "/orgs/{org}/members/{username}",
        t.struct({"org": t.string(), "username": t.string()}),
        t.boolean().optional(),
    )
    functions["orgs_remove_member"] = ghes.delete(
        "/orgs/{org}/members/{username}",
        t.struct({"org": t.string(), "username": t.string()}),
        t.boolean(),
    )
    functions["orgs_get_membership_for_user"] = ghes.get(
        "/orgs/{org}/memberships/{username}",
        t.struct({"org": t.string(), "username": t.string()}),
        t.proxy(renames["org_membership"]).optional(),
    )
    functions["orgs_set_membership_for_user"] = ghes.put(
        "/orgs/{org}/memberships/{username}",
        t.struct(
            {"org": t.string(), "username": t.string(), "role": t.string().optional()}
        ),
        t.proxy(renames["org_membership"]),
        content_type="application/json",
        body_fields=("role",),
    )
    functions["orgs_remove_membership_for_user"] = ghes.delete(
        "/orgs/{org}/memberships/{username}",
        t.struct({"org": t.string(), "username": t.string()}),
        t.boolean().optional(),
    )
    functions["orgs_list_outside_collaborators"] = ghes.get(
        "/orgs/{org}/outside_collaborators",
        t.struct(
            {
                "org": t.string(),
                "filter": t.string(),
                "per_page": t.integer(),
                "page": t.integer(),
            }
        ),
        t.array(t.proxy(renames["simple_user"])),
    )
    functions["orgs_convert_member_to_outside_collaborator"] = ghes.put(
        "/orgs/{org}/outside_collaborators/{username}",
        t.struct({"org": t.string(), "username": t.string()}),
        t.struct({}).optional(),
    )
    functions["orgs_remove_outside_collaborator"] = ghes.delete(
        "/orgs/{org}/outside_collaborators/{username}",
        t.struct({"org": t.string(), "username": t.string()}),
        t.boolean(),
    )
    functions["enterprise_admin_list_pre_receive_hooks_for_org"] = ghes.get(
        "/orgs/{org}/pre-receive-hooks",
        t.struct(
            {
                "org": t.string(),
                "per_page": t.integer(),
                "page": t.integer(),
                "direction": t.string(),
                "sort": t.string(),
            }
        ),
        t.array(t.proxy(renames["org_pre_receive_hook"])),
    )
    functions["enterprise_admin_get_pre_receive_hook_for_org"] = ghes.get(
        "/orgs/{org}/pre-receive-hooks/{pre_receive_hook_id}",
        t.struct({"org": t.string(), "pre_receive_hook_id": t.integer()}),
        t.proxy(renames["org_pre_receive_hook"]),
    )
    functions[
        "enterprise_admin_update_pre_receive_hook_enforcement_for_org"
    ] = ghes.patch(
        "/orgs/{org}/pre-receive-hooks/{pre_receive_hook_id}",
        t.struct(
            {
                "org": t.string(),
                "pre_receive_hook_id": t.integer(),
                "enforcement": t.string().optional(),
                "allow_downstream_configuration": t.boolean().optional(),
            }
        ),
        t.proxy(renames["org_pre_receive_hook"]),
        content_type="application/json",
        body_fields=("enforcement", "allow_downstream_configuration"),
    )
    functions[
        "enterprise_admin_remove_pre_receive_hook_enforcement_for_org"
    ] = ghes.delete(
        "/orgs/{org}/pre-receive-hooks/{pre_receive_hook_id}",
        t.struct({"org": t.string(), "pre_receive_hook_id": t.integer()}),
        t.proxy(renames["org_pre_receive_hook"]),
    )
    functions["projects_list_for_org"] = ghes.get(
        "/orgs/{org}/projects",
        t.struct(
            {
                "org": t.string(),
                "state": t.string(),
                "per_page": t.integer(),
                "page": t.integer(),
            }
        ),
        t.array(t.proxy(renames["project"])),
    )
    functions["projects_create_for_org"] = ghes.post(
        "/orgs/{org}/projects",
        t.struct(
            {"org": t.string(), "name": t.string(), "body": t.string().optional()}
        ),
        t.proxy(renames["project"]).optional(),
        content_type="application/json",
        body_fields=("name", "body"),
    )
    functions["orgs_list_public_members"] = ghes.get(
        "/orgs/{org}/public_members",
        t.struct({"org": t.string(), "per_page": t.integer(), "page": t.integer()}),
        t.array(t.proxy(renames["simple_user"])),
    )
    functions["orgs_check_public_membership_for_user"] = ghes.get(
        "/orgs/{org}/public_members/{username}",
        t.struct({"org": t.string(), "username": t.string()}),
        t.boolean().optional(),
    )
    functions["orgs_set_public_membership_for_authenticated_user"] = ghes.put(
        "/orgs/{org}/public_members/{username}",
        t.struct({"org": t.string(), "username": t.string()}),
        t.boolean(),
    )
    functions["orgs_remove_public_membership_for_authenticated_user"] = ghes.delete(
        "/orgs/{org}/public_members/{username}",
        t.struct({"org": t.string(), "username": t.string()}),
        t.boolean(),
    )
    functions["repos_list_for_org"] = ghes.get(
        "/orgs/{org}/repos",
        t.struct(
            {
                "org": t.string(),
                "type": t.string(),
                "sort": t.string(),
                "direction": t.string(),
                "per_page": t.integer(),
                "page": t.integer(),
            }
        ),
        t.array(t.proxy(renames["minimal_repository"])),
    )
    functions["repos_create_in_org"] = ghes.post(
        "/orgs/{org}/repos",
        t.struct(
            {
                "org": t.string(),
                "name": t.string(),
                "description": t.string().optional(),
                "homepage": t.string().optional(),
                "private": t.boolean().optional(),
                "visibility": t.string().optional(),
                "has_issues": t.boolean().optional(),
                "has_projects": t.boolean().optional(),
                "has_wiki": t.boolean().optional(),
                "is_template": t.boolean().optional(),
                "team_id": t.integer().optional(),
                "auto_init": t.boolean().optional(),
                "gitignore_template": t.string().optional(),
                "license_template": t.string().optional(),
                "allow_squash_merge": t.boolean().optional(),
                "allow_merge_commit": t.boolean().optional(),
                "allow_rebase_merge": t.boolean().optional(),
                "delete_branch_on_merge": t.boolean().optional(),
            }
        ),
        t.proxy(renames["repository"]),
        content_type="application/json",
        body_fields=(
            "name",
            "description",
            "homepage",
            "private",
            "visibility",
            "has_issues",
            "has_projects",
            "has_wiki",
            "is_template",
            "team_id",
            "auto_init",
            "gitignore_template",
            "license_template",
            "allow_squash_merge",
            "allow_merge_commit",
            "allow_rebase_merge",
            "delete_branch_on_merge",
        ),
    )
    functions["teams_list"] = ghes.get(
        "/orgs/{org}/teams",
        t.struct({"org": t.string(), "per_page": t.integer(), "page": t.integer()}),
        t.array(t.proxy(renames["team"])),
    )
    functions["teams_create"] = ghes.post(
        "/orgs/{org}/teams",
        t.struct(
            {
                "org": t.string(),
                "name": t.string(),
                "description": t.string().optional(),
                "maintainers": t.array(t.string()).optional(),
                "repo_names": t.array(t.string()).optional(),
                "privacy": t.string().optional(),
                "permission": t.string().optional(),
                "parent_team_id": t.integer().optional(),
                "ldap_dn": t.string().optional(),
            }
        ),
        t.proxy(renames["team_full"]),
        content_type="application/json",
        body_fields=(
            "name",
            "description",
            "maintainers",
            "repo_names",
            "privacy",
            "permission",
            "parent_team_id",
            "ldap_dn",
        ),
    )
    functions["teams_get_by_name"] = ghes.get(
        "/orgs/{org}/teams/{team_slug}",
        t.struct({"org": t.string(), "team_slug": t.string()}),
        t.proxy(renames["team_full"]).optional(),
    )
    functions["teams_update_in_org"] = ghes.patch(
        "/orgs/{org}/teams/{team_slug}",
        t.struct(
            {
                "org": t.string(),
                "team_slug": t.string(),
                "name": t.string().optional(),
                "description": t.string().optional(),
                "privacy": t.string().optional(),
                "permission": t.string().optional(),
                "parent_team_id": t.integer().optional(),
            }
        ),
        t.proxy(renames["team_full"]),
        content_type="application/json",
        body_fields=("name", "description", "privacy", "permission", "parent_team_id"),
    )
    functions["teams_delete_in_org"] = ghes.delete(
        "/orgs/{org}/teams/{team_slug}",
        t.struct({"org": t.string(), "team_slug": t.string()}),
        t.boolean(),
    )
    functions["teams_list_discussions_in_org"] = ghes.get(
        "/orgs/{org}/teams/{team_slug}/discussions",
        t.struct(
            {
                "org": t.string(),
                "team_slug": t.string(),
                "direction": t.string(),
                "per_page": t.integer(),
                "page": t.integer(),
                "pinned": t.string(),
            }
        ),
        t.array(t.proxy(renames["team_discussion"])),
    )
    functions["teams_create_discussion_in_org"] = ghes.post(
        "/orgs/{org}/teams/{team_slug}/discussions",
        t.struct(
            {
                "org": t.string(),
                "team_slug": t.string(),
                "title": t.string(),
                "body": t.string(),
                "private": t.boolean().optional(),
            }
        ),
        t.proxy(renames["team_discussion"]),
        content_type="application/json",
        body_fields=("title", "body", "private"),
    )
    functions["teams_get_discussion_in_org"] = ghes.get(
        "/orgs/{org}/teams/{team_slug}/discussions/{discussion_number}",
        t.struct(
            {
                "org": t.string(),
                "team_slug": t.string(),
                "discussion_number": t.integer(),
            }
        ),
        t.proxy(renames["team_discussion"]),
    )
    functions["teams_update_discussion_in_org"] = ghes.patch(
        "/orgs/{org}/teams/{team_slug}/discussions/{discussion_number}",
        t.struct(
            {
                "org": t.string(),
                "team_slug": t.string(),
                "discussion_number": t.integer(),
                "title": t.string().optional(),
                "body": t.string().optional(),
            }
        ),
        t.proxy(renames["team_discussion"]),
        content_type="application/json",
        body_fields=("title", "body"),
    )
    functions["teams_delete_discussion_in_org"] = ghes.delete(
        "/orgs/{org}/teams/{team_slug}/discussions/{discussion_number}",
        t.struct(
            {
                "org": t.string(),
                "team_slug": t.string(),
                "discussion_number": t.integer(),
            }
        ),
        t.boolean(),
    )
    functions["teams_list_discussion_comments_in_org"] = ghes.get(
        "/orgs/{org}/teams/{team_slug}/discussions/{discussion_number}/comments",
        t.struct(
            {
                "org": t.string(),
                "team_slug": t.string(),
                "discussion_number": t.integer(),
                "direction": t.string(),
                "per_page": t.integer(),
                "page": t.integer(),
            }
        ),
        t.array(t.proxy(renames["team_discussion_comment"])),
    )
    functions["teams_create_discussion_comment_in_org"] = ghes.post(
        "/orgs/{org}/teams/{team_slug}/discussions/{discussion_number}/comments",
        t.struct(
            {
                "org": t.string(),
                "team_slug": t.string(),
                "discussion_number": t.integer(),
                "body": t.string(),
            }
        ),
        t.proxy(renames["team_discussion_comment"]),
        content_type="application/json",
        body_fields=("body",),
    )
    functions["teams_get_discussion_comment_in_org"] = ghes.get(
        "/orgs/{org}/teams/{team_slug}/discussions/{discussion_number}/comments/{comment_number}",
        t.struct(
            {
                "org": t.string(),
                "team_slug": t.string(),
                "discussion_number": t.integer(),
                "comment_number": t.integer(),
            }
        ),
        t.proxy(renames["team_discussion_comment"]),
    )
    functions["teams_update_discussion_comment_in_org"] = ghes.patch(
        "/orgs/{org}/teams/{team_slug}/discussions/{discussion_number}/comments/{comment_number}",
        t.struct(
            {
                "org": t.string(),
                "team_slug": t.string(),
                "discussion_number": t.integer(),
                "comment_number": t.integer(),
                "body": t.string(),
            }
        ),
        t.proxy(renames["team_discussion_comment"]),
        content_type="application/json",
        body_fields=("body",),
    )
    functions["teams_delete_discussion_comment_in_org"] = ghes.delete(
        "/orgs/{org}/teams/{team_slug}/discussions/{discussion_number}/comments/{comment_number}",
        t.struct(
            {
                "org": t.string(),
                "team_slug": t.string(),
                "discussion_number": t.integer(),
                "comment_number": t.integer(),
            }
        ),
        t.boolean(),
    )
    functions["reactions_list_for_team_discussion_comment_in_org"] = ghes.get(
        "/orgs/{org}/teams/{team_slug}/discussions/{discussion_number}/comments/{comment_number}/reactions",
        t.struct(
            {
                "org": t.string(),
                "team_slug": t.string(),
                "discussion_number": t.integer(),
                "comment_number": t.integer(),
                "content": t.string(),
                "per_page": t.integer(),
                "page": t.integer(),
            }
        ),
        t.array(t.proxy(renames["reaction"])),
    )
    functions["reactions_create_for_team_discussion_comment_in_org"] = ghes.post(
        "/orgs/{org}/teams/{team_slug}/discussions/{discussion_number}/comments/{comment_number}/reactions",
        t.struct(
            {
                "org": t.string(),
                "team_slug": t.string(),
                "discussion_number": t.integer(),
                "comment_number": t.integer(),
                "content": t.string(),
            }
        ),
        t.proxy(renames["reaction"]),
        content_type="application/json",
        body_fields=("content",),
    )
    functions["reactions_delete_for_team_discussion_comment"] = ghes.delete(
        "/orgs/{org}/teams/{team_slug}/discussions/{discussion_number}/comments/{comment_number}/reactions/{reaction_id}",
        t.struct(
            {
                "org": t.string(),
                "team_slug": t.string(),
                "discussion_number": t.integer(),
                "comment_number": t.integer(),
                "reaction_id": t.integer(),
            }
        ),
        t.boolean(),
    )
    functions["reactions_list_for_team_discussion_in_org"] = ghes.get(
        "/orgs/{org}/teams/{team_slug}/discussions/{discussion_number}/reactions",
        t.struct(
            {
                "org": t.string(),
                "team_slug": t.string(),
                "discussion_number": t.integer(),
                "content": t.string(),
                "per_page": t.integer(),
                "page": t.integer(),
            }
        ),
        t.array(t.proxy(renames["reaction"])),
    )
    functions["reactions_create_for_team_discussion_in_org"] = ghes.post(
        "/orgs/{org}/teams/{team_slug}/discussions/{discussion_number}/reactions",
        t.struct(
            {
                "org": t.string(),
                "team_slug": t.string(),
                "discussion_number": t.integer(),
                "content": t.string(),
            }
        ),
        t.proxy(renames["reaction"]),
        content_type="application/json",
        body_fields=("content",),
    )
    functions["reactions_delete_for_team_discussion"] = ghes.delete(
        "/orgs/{org}/teams/{team_slug}/discussions/{discussion_number}/reactions/{reaction_id}",
        t.struct(
            {
                "org": t.string(),
                "team_slug": t.string(),
                "discussion_number": t.integer(),
                "reaction_id": t.integer(),
            }
        ),
        t.boolean(),
    )
    functions["teams_list_members_in_org"] = ghes.get(
        "/orgs/{org}/teams/{team_slug}/members",
        t.struct(
            {
                "org": t.string(),
                "team_slug": t.string(),
                "role": t.string(),
                "per_page": t.integer(),
                "page": t.integer(),
            }
        ),
        t.array(t.proxy(renames["simple_user"])),
    )
    functions["teams_get_membership_for_user_in_org"] = ghes.get(
        "/orgs/{org}/teams/{team_slug}/memberships/{username}",
        t.struct({"org": t.string(), "team_slug": t.string(), "username": t.string()}),
        t.proxy(renames["team_membership"]).optional(),
    )
    functions["teams_add_or_update_membership_for_user_in_org"] = ghes.put(
        "/orgs/{org}/teams/{team_slug}/memberships/{username}",
        t.struct(
            {
                "org": t.string(),
                "team_slug": t.string(),
                "username": t.string(),
                "role": t.string().optional(),
            }
        ),
        t.proxy(renames["team_membership"]),
        content_type="application/json",
        body_fields=("role",),
    )
    functions["teams_remove_membership_for_user_in_org"] = ghes.delete(
        "/orgs/{org}/teams/{team_slug}/memberships/{username}",
        t.struct({"org": t.string(), "team_slug": t.string(), "username": t.string()}),
        t.boolean(),
    )
    functions["teams_list_projects_in_org"] = ghes.get(
        "/orgs/{org}/teams/{team_slug}/projects",
        t.struct(
            {
                "org": t.string(),
                "team_slug": t.string(),
                "per_page": t.integer(),
                "page": t.integer(),
            }
        ),
        t.array(t.proxy(renames["team_project"])),
    )
    functions["teams_check_permissions_for_project_in_org"] = ghes.get(
        "/orgs/{org}/teams/{team_slug}/projects/{project_id}",
        t.struct(
            {"org": t.string(), "team_slug": t.string(), "project_id": t.integer()}
        ),
        t.proxy(renames["team_project"]).optional(),
    )
    functions["teams_add_or_update_project_permissions_in_org"] = ghes.put(
        "/orgs/{org}/teams/{team_slug}/projects/{project_id}",
        t.struct(
            {
                "org": t.string(),
                "team_slug": t.string(),
                "project_id": t.integer(),
                "permission": t.string().optional(),
            }
        ),
        t.boolean(),
        content_type="application/json",
        body_fields=("permission",),
    )
    functions["teams_remove_project_in_org"] = ghes.delete(
        "/orgs/{org}/teams/{team_slug}/projects/{project_id}",
        t.struct(
            {"org": t.string(), "team_slug": t.string(), "project_id": t.integer()}
        ),
        t.boolean(),
    )
    functions["teams_list_repos_in_org"] = ghes.get(
        "/orgs/{org}/teams/{team_slug}/repos",
        t.struct(
            {
                "org": t.string(),
                "team_slug": t.string(),
                "per_page": t.integer(),
                "page": t.integer(),
            }
        ),
        t.array(t.proxy(renames["minimal_repository"])),
    )
    functions["teams_check_permissions_for_repo_in_org"] = ghes.get(
        "/orgs/{org}/teams/{team_slug}/repos/{owner}/{repo}",
        t.struct(
            {
                "org": t.string(),
                "team_slug": t.string(),
                "owner": t.string(),
                "repo": t.string(),
            }
        ),
        t.proxy(renames["team_repository"]).optional(),
    )
    functions["teams_add_or_update_repo_permissions_in_org"] = ghes.put(
        "/orgs/{org}/teams/{team_slug}/repos/{owner}/{repo}",
        t.struct(
            {
                "org": t.string(),
                "team_slug": t.string(),
                "owner": t.string(),
                "repo": t.string(),
                "permission": t.string().optional(),
            }
        ),
        t.boolean(),
        content_type="application/json",
        body_fields=("permission",),
    )
    functions["teams_remove_repo_in_org"] = ghes.delete(
        "/orgs/{org}/teams/{team_slug}/repos/{owner}/{repo}",
        t.struct(
            {
                "org": t.string(),
                "team_slug": t.string(),
                "owner": t.string(),
                "repo": t.string(),
            }
        ),
        t.boolean(),
    )
    functions["teams_list_child_in_org"] = ghes.get(
        "/orgs/{org}/teams/{team_slug}/teams",
        t.struct(
            {
                "org": t.string(),
                "team_slug": t.string(),
                "per_page": t.integer(),
                "page": t.integer(),
            }
        ),
        t.array(t.proxy(renames["team"])),
    )
    functions["projects_get_card"] = ghes.get(
        "/projects/columns/cards/{card_id}",
        t.struct({"card_id": t.integer()}),
        t.proxy(renames["project_card"]).optional(),
    )
    functions["projects_update_card"] = ghes.patch(
        "/projects/columns/cards/{card_id}",
        t.struct(
            {
                "card_id": t.integer(),
                "note": t.string().optional(),
                "archived": t.boolean().optional(),
            }
        ),
        t.proxy(renames["project_card"]).optional(),
        content_type="application/json",
        body_fields=("note", "archived"),
    )
    functions["projects_delete_card"] = ghes.delete(
        "/projects/columns/cards/{card_id}",
        t.struct({"card_id": t.integer()}),
        t.boolean().optional(),
    )
    functions["projects_move_card"] = ghes.post(
        "/projects/columns/cards/{card_id}/moves",
        t.struct(
            {
                "card_id": t.integer(),
                "position": t.string(),
                "column_id": t.integer().optional(),
            }
        ),
        t.struct({}),
        content_type="application/json",
        body_fields=("position", "column_id"),
    )
    functions["projects_get_column"] = ghes.get(
        "/projects/columns/{column_id}",
        t.struct({"column_id": t.integer()}),
        t.proxy(renames["project_column"]).optional(),
    )
    functions["projects_update_column"] = ghes.patch(
        "/projects/columns/{column_id}",
        t.struct({"column_id": t.integer(), "name": t.string()}),
        t.proxy(renames["project_column"]),
        content_type="application/json",
        body_fields=("name",),
    )
    functions["projects_delete_column"] = ghes.delete(
        "/projects/columns/{column_id}",
        t.struct({"column_id": t.integer()}),
        t.boolean(),
    )
    functions["projects_list_cards"] = ghes.get(
        "/projects/columns/{column_id}/cards",
        t.struct(
            {
                "column_id": t.integer(),
                "archived_state": t.string(),
                "per_page": t.integer(),
                "page": t.integer(),
            }
        ),
        t.array(t.proxy(renames["project_card"])),
    )
    functions["projects_move_column"] = ghes.post(
        "/projects/columns/{column_id}/moves",
        t.struct({"column_id": t.integer(), "position": t.string()}),
        t.struct({}),
        content_type="application/json",
        body_fields=("position",),
    )
    functions["projects_get"] = ghes.get(
        "/projects/{project_id}",
        t.struct({"project_id": t.integer()}),
        t.proxy(renames["project"]),
    )
    functions["projects_update"] = ghes.patch(
        "/projects/{project_id}",
        t.struct(
            {
                "project_id": t.integer(),
                "name": t.string().optional(),
                "body": t.string().optional(),
                "state": t.string().optional(),
                "organization_permission": t.string().optional(),
                "private": t.boolean().optional(),
            }
        ),
        t.proxy(renames["project"]).optional(),
        content_type="application/json",
        body_fields=("name", "body", "state", "organization_permission", "private"),
    )
    functions["projects_delete"] = ghes.delete(
        "/projects/{project_id}",
        t.struct({"project_id": t.integer()}),
        t.boolean().optional(),
    )
    functions["projects_list_collaborators"] = ghes.get(
        "/projects/{project_id}/collaborators",
        t.struct(
            {
                "project_id": t.integer(),
                "affiliation": t.string(),
                "per_page": t.integer(),
                "page": t.integer(),
            }
        ),
        t.array(t.proxy(renames["simple_user"])).optional(),
    )
    functions["projects_add_collaborator"] = ghes.put(
        "/projects/{project_id}/collaborators/{username}",
        t.struct(
            {
                "project_id": t.integer(),
                "username": t.string(),
                "permission": t.string().optional(),
            }
        ),
        t.boolean().optional(),
        content_type="application/json",
        body_fields=("permission",),
    )
    functions["projects_remove_collaborator"] = ghes.delete(
        "/projects/{project_id}/collaborators/{username}",
        t.struct({"project_id": t.integer(), "username": t.string()}),
        t.boolean().optional(),
    )
    functions["projects_get_permission_for_user"] = ghes.get(
        "/projects/{project_id}/collaborators/{username}/permission",
        t.struct({"project_id": t.integer(), "username": t.string()}),
        t.proxy(renames["project_collaborator_permission"]).optional(),
    )
    functions["projects_list_columns"] = ghes.get(
        "/projects/{project_id}/columns",
        t.struct(
            {"project_id": t.integer(), "per_page": t.integer(), "page": t.integer()}
        ),
        t.array(t.proxy(renames["project_column"])),
    )
    functions["projects_create_column"] = ghes.post(
        "/projects/{project_id}/columns",
        t.struct({"project_id": t.integer(), "name": t.string()}),
        t.proxy(renames["project_column"]),
        content_type="application/json",
        body_fields=("name",),
    )
    functions["rate_limit_get"] = ghes.get(
        "/rate_limit",
        t.struct({}),
        t.proxy(renames["rate_limit_overview"]).optional(),
    )
    functions["reactions_delete_legacy"] = ghes.delete(
        "/reactions/{reaction_id}",
        t.struct({"reaction_id": t.integer()}),
        t.boolean(),
    )
    functions["repos_get"] = ghes.get(
        "/repos/{owner}/{repo}",
        t.struct({"owner": t.string(), "repo": t.string()}),
        t.proxy(renames["full_repository"]).optional(),
    )
    functions["repos_update"] = ghes.patch(
        "/repos/{owner}/{repo}",
        t.struct(
            {
                "owner": t.string(),
                "repo": t.string(),
                "name": t.string().optional(),
                "description": t.string().optional(),
                "homepage": t.string().optional(),
                "private": t.boolean().optional(),
                "visibility": t.string().optional(),
                "has_issues": t.boolean().optional(),
                "has_projects": t.boolean().optional(),
                "has_wiki": t.boolean().optional(),
                "is_template": t.boolean().optional(),
                "default_branch": t.string().optional(),
                "allow_squash_merge": t.boolean().optional(),
                "allow_merge_commit": t.boolean().optional(),
                "allow_rebase_merge": t.boolean().optional(),
                "delete_branch_on_merge": t.boolean().optional(),
                "archived": t.boolean().optional(),
                "allow_forking": t.boolean().optional(),
            }
        ),
        t.proxy(renames["full_repository"]).optional(),
        content_type="application/json",
        body_fields=(
            "name",
            "description",
            "homepage",
            "private",
            "visibility",
            "has_issues",
            "has_projects",
            "has_wiki",
            "is_template",
            "default_branch",
            "allow_squash_merge",
            "allow_merge_commit",
            "allow_rebase_merge",
            "delete_branch_on_merge",
            "archived",
            "allow_forking",
        ),
    )
    functions["repos_delete"] = ghes.delete(
        "/repos/{owner}/{repo}",
        t.struct({"owner": t.string(), "repo": t.string()}),
        t.boolean().optional(),
    )
    functions["actions_list_artifacts_for_repo"] = ghes.get(
        "/repos/{owner}/{repo}/actions/artifacts",
        t.struct(
            {
                "owner": t.string(),
                "repo": t.string(),
                "per_page": t.integer(),
                "page": t.integer(),
            }
        ),
        t.struct(
            {
                "total_count": t.integer(),
                "artifacts": t.array(t.proxy(renames["artifact"])),
            }
        ),
    )
    functions["actions_get_artifact"] = ghes.get(
        "/repos/{owner}/{repo}/actions/artifacts/{artifact_id}",
        t.struct({"owner": t.string(), "repo": t.string(), "artifact_id": t.integer()}),
        t.proxy(renames["artifact"]),
    )
    functions["actions_delete_artifact"] = ghes.delete(
        "/repos/{owner}/{repo}/actions/artifacts/{artifact_id}",
        t.struct({"owner": t.string(), "repo": t.string(), "artifact_id": t.integer()}),
        t.boolean(),
    )
    functions["actions_download_artifact"] = ghes.get(
        "/repos/{owner}/{repo}/actions/artifacts/{artifact_id}/{archive_format}",
        t.struct(
            {
                "owner": t.string(),
                "repo": t.string(),
                "artifact_id": t.integer(),
                "archive_format": t.string(),
            }
        ),
        t.struct({}),
    )
    functions["actions_get_job_for_workflow_run"] = ghes.get(
        "/repos/{owner}/{repo}/actions/jobs/{job_id}",
        t.struct({"owner": t.string(), "repo": t.string(), "job_id": t.integer()}),
        t.proxy(renames["job"]),
    )
    functions["actions_download_job_logs_for_workflow_run"] = ghes.get(
        "/repos/{owner}/{repo}/actions/jobs/{job_id}/logs",
        t.struct({"owner": t.string(), "repo": t.string(), "job_id": t.integer()}),
        t.struct({}),
    )
    functions["actions_get_github_actions_permissions_repository"] = ghes.get(
        "/repos/{owner}/{repo}/actions/permissions",
        t.struct({"owner": t.string(), "repo": t.string()}),
        t.proxy(renames["actions_repository_permissions"]),
    )
    functions["actions_set_github_actions_permissions_repository"] = ghes.put(
        "/repos/{owner}/{repo}/actions/permissions",
        t.struct(
            {
                "owner": t.string(),
                "repo": t.string(),
                "enabled": t.proxy(renames["actions_enabled"]),
                "allowed_actions": t.proxy(renames["allowed_actions"]).optional(),
            }
        ),
        t.boolean(),
        content_type="application/json",
        body_fields=("enabled", "allowed_actions"),
    )
    functions["actions_get_allowed_actions_repository"] = ghes.get(
        "/repos/{owner}/{repo}/actions/permissions/selected-actions",
        t.struct({"owner": t.string(), "repo": t.string()}),
        t.proxy(renames["selected_actions"]),
    )
    functions["actions_set_allowed_actions_repository"] = ghes.put(
        "/repos/{owner}/{repo}/actions/permissions/selected-actions",
        t.struct(
            {
                "owner": t.string(),
                "repo": t.string(),
                "github_owned_allowed": t.boolean(),
                "patterns_allowed": t.array(t.string()),
            }
        ),
        t.boolean(),
        content_type="application/json",
        body_fields=("github_owned_allowed", "patterns_allowed"),
    )
    functions["actions_list_self_hosted_runners_for_repo"] = ghes.get(
        "/repos/{owner}/{repo}/actions/runners",
        t.struct(
            {
                "owner": t.string(),
                "repo": t.string(),
                "per_page": t.integer(),
                "page": t.integer(),
            }
        ),
        t.struct(
            {"total_count": t.integer(), "runners": t.array(t.proxy(renames["runner"]))}
        ),
    )
    functions["actions_list_runner_applications_for_repo"] = ghes.get(
        "/repos/{owner}/{repo}/actions/runners/downloads",
        t.struct({"owner": t.string(), "repo": t.string()}),
        t.array(t.proxy(renames["runner_application"])),
    )
    functions["actions_create_registration_token_for_repo"] = ghes.post(
        "/repos/{owner}/{repo}/actions/runners/registration-token",
        t.struct({"owner": t.string(), "repo": t.string()}),
        t.proxy(renames["authentication_token"]),
    )
    functions["actions_create_remove_token_for_repo"] = ghes.post(
        "/repos/{owner}/{repo}/actions/runners/remove-token",
        t.struct({"owner": t.string(), "repo": t.string()}),
        t.proxy(renames["authentication_token"]),
    )
    functions["actions_get_self_hosted_runner_for_repo"] = ghes.get(
        "/repos/{owner}/{repo}/actions/runners/{runner_id}",
        t.struct({"owner": t.string(), "repo": t.string(), "runner_id": t.integer()}),
        t.proxy(renames["runner"]),
    )
    functions["actions_delete_self_hosted_runner_from_repo"] = ghes.delete(
        "/repos/{owner}/{repo}/actions/runners/{runner_id}",
        t.struct({"owner": t.string(), "repo": t.string(), "runner_id": t.integer()}),
        t.boolean(),
    )
    functions["actions_list_workflow_runs_for_repo"] = ghes.get(
        "/repos/{owner}/{repo}/actions/runs",
        t.struct(
            {
                "owner": t.string(),
                "repo": t.string(),
                "actor": t.string(),
                "branch": t.string(),
                "event": t.string(),
                "status": t.string(),
                "per_page": t.integer(),
                "page": t.integer(),
                "created": t.string(),
                "exclude_pull_requests": t.boolean(),
            }
        ),
        t.struct(
            {
                "total_count": t.integer(),
                "workflow_runs": t.array(t.proxy(renames["workflow_run"])),
            }
        ),
    )
    functions["actions_get_workflow_run"] = ghes.get(
        "/repos/{owner}/{repo}/actions/runs/{run_id}",
        t.struct(
            {
                "owner": t.string(),
                "repo": t.string(),
                "run_id": t.integer(),
                "exclude_pull_requests": t.boolean(),
            }
        ),
        t.proxy(renames["workflow_run"]),
    )
    functions["actions_delete_workflow_run"] = ghes.delete(
        "/repos/{owner}/{repo}/actions/runs/{run_id}",
        t.struct({"owner": t.string(), "repo": t.string(), "run_id": t.integer()}),
        t.boolean(),
    )
    functions["actions_list_workflow_run_artifacts"] = ghes.get(
        "/repos/{owner}/{repo}/actions/runs/{run_id}/artifacts",
        t.struct(
            {
                "owner": t.string(),
                "repo": t.string(),
                "run_id": t.integer(),
                "per_page": t.integer(),
                "page": t.integer(),
            }
        ),
        t.struct(
            {
                "total_count": t.integer(),
                "artifacts": t.array(t.proxy(renames["artifact"])),
            }
        ),
    )
    functions["actions_cancel_workflow_run"] = ghes.post(
        "/repos/{owner}/{repo}/actions/runs/{run_id}/cancel",
        t.struct({"owner": t.string(), "repo": t.string(), "run_id": t.integer()}),
        t.struct({}),
    )
    functions["actions_list_jobs_for_workflow_run"] = ghes.get(
        "/repos/{owner}/{repo}/actions/runs/{run_id}/jobs",
        t.struct(
            {
                "owner": t.string(),
                "repo": t.string(),
                "run_id": t.integer(),
                "filter": t.string(),
                "per_page": t.integer(),
                "page": t.integer(),
            }
        ),
        t.struct(
            {"total_count": t.integer(), "jobs": t.array(t.proxy(renames["job"]))}
        ),
    )
    functions["actions_download_workflow_run_logs"] = ghes.get(
        "/repos/{owner}/{repo}/actions/runs/{run_id}/logs",
        t.struct({"owner": t.string(), "repo": t.string(), "run_id": t.integer()}),
        t.struct({}),
    )
    functions["actions_delete_workflow_run_logs"] = ghes.delete(
        "/repos/{owner}/{repo}/actions/runs/{run_id}/logs",
        t.struct({"owner": t.string(), "repo": t.string(), "run_id": t.integer()}),
        t.boolean(),
    )
    functions["actions_re_run_workflow"] = ghes.post(
        "/repos/{owner}/{repo}/actions/runs/{run_id}/rerun",
        t.struct({"owner": t.string(), "repo": t.string(), "run_id": t.integer()}),
        t.struct({}),
    )
    functions["actions_list_repo_secrets"] = ghes.get(
        "/repos/{owner}/{repo}/actions/secrets",
        t.struct(
            {
                "owner": t.string(),
                "repo": t.string(),
                "per_page": t.integer(),
                "page": t.integer(),
            }
        ),
        t.struct(
            {
                "total_count": t.integer(),
                "secrets": t.array(t.proxy(renames["actions_secret"])),
            }
        ),
    )
    functions["actions_get_repo_public_key"] = ghes.get(
        "/repos/{owner}/{repo}/actions/secrets/public-key",
        t.struct({"owner": t.string(), "repo": t.string()}),
        t.proxy(renames["actions_public_key"]),
    )
    functions["actions_get_repo_secret"] = ghes.get(
        "/repos/{owner}/{repo}/actions/secrets/{secret_name}",
        t.struct({"owner": t.string(), "repo": t.string(), "secret_name": t.string()}),
        t.proxy(renames["actions_secret"]),
    )
    functions["actions_create_or_update_repo_secret"] = ghes.put(
        "/repos/{owner}/{repo}/actions/secrets/{secret_name}",
        t.struct(
            {
                "owner": t.string(),
                "repo": t.string(),
                "secret_name": t.string(),
                "encrypted_value": t.string().optional(),
                "key_id": t.string().optional(),
            }
        ),
        t.struct({}),
        content_type="application/json",
        body_fields=("encrypted_value", "key_id"),
    )
    functions["actions_delete_repo_secret"] = ghes.delete(
        "/repos/{owner}/{repo}/actions/secrets/{secret_name}",
        t.struct({"owner": t.string(), "repo": t.string(), "secret_name": t.string()}),
        t.boolean(),
    )
    functions["actions_list_repo_workflows"] = ghes.get(
        "/repos/{owner}/{repo}/actions/workflows",
        t.struct(
            {
                "owner": t.string(),
                "repo": t.string(),
                "per_page": t.integer(),
                "page": t.integer(),
            }
        ),
        t.struct(
            {
                "total_count": t.integer(),
                "workflows": t.array(t.proxy(renames["workflow"])),
            }
        ),
    )
    functions["actions_get_workflow"] = ghes.get(
        "/repos/{owner}/{repo}/actions/workflows/{workflow_id}",
        t.struct(
            {
                "owner": t.string(),
                "repo": t.string(),
                "workflow_id": t.either([t.integer(), t.string()]),
            }
        ),
        t.proxy(renames["workflow"]),
    )
    functions["actions_disable_workflow"] = ghes.put(
        "/repos/{owner}/{repo}/actions/workflows/{workflow_id}/disable",
        t.struct(
            {
                "owner": t.string(),
                "repo": t.string(),
                "workflow_id": t.either([t.integer(), t.string()]),
            }
        ),
        t.boolean(),
    )
    functions["actions_create_workflow_dispatch"] = ghes.post(
        "/repos/{owner}/{repo}/actions/workflows/{workflow_id}/dispatches",
        t.struct(
            {
                "owner": t.string(),
                "repo": t.string(),
                "workflow_id": t.either([t.integer(), t.string()]),
                "ref": t.string(),
                "inputs": t.struct({}).optional(),
            }
        ),
        t.boolean(),
        content_type="application/json",
        body_fields=("ref", "inputs"),
    )
    functions["actions_enable_workflow"] = ghes.put(
        "/repos/{owner}/{repo}/actions/workflows/{workflow_id}/enable",
        t.struct(
            {
                "owner": t.string(),
                "repo": t.string(),
                "workflow_id": t.either([t.integer(), t.string()]),
            }
        ),
        t.boolean(),
    )
    functions["actions_list_workflow_runs"] = ghes.get(
        "/repos/{owner}/{repo}/actions/workflows/{workflow_id}/runs",
        t.struct(
            {
                "owner": t.string(),
                "repo": t.string(),
                "workflow_id": t.either([t.integer(), t.string()]),
                "actor": t.string(),
                "branch": t.string(),
                "event": t.string(),
                "status": t.string(),
                "per_page": t.integer(),
                "page": t.integer(),
                "created": t.string(),
                "exclude_pull_requests": t.boolean(),
            }
        ),
        t.struct(
            {
                "total_count": t.integer(),
                "workflow_runs": t.array(t.proxy(renames["workflow_run"])),
            }
        ),
    )
    functions["issues_list_assignees"] = ghes.get(
        "/repos/{owner}/{repo}/assignees",
        t.struct(
            {
                "owner": t.string(),
                "repo": t.string(),
                "per_page": t.integer(),
                "page": t.integer(),
            }
        ),
        t.array(t.proxy(renames["simple_user"])).optional(),
    )
    functions["issues_check_user_can_be_assigned"] = ghes.get(
        "/repos/{owner}/{repo}/assignees/{assignee}",
        t.struct({"owner": t.string(), "repo": t.string(), "assignee": t.string()}),
        t.boolean().optional(),
    )
    functions["repos_list_branches"] = ghes.get(
        "/repos/{owner}/{repo}/branches",
        t.struct(
            {
                "owner": t.string(),
                "repo": t.string(),
                "protected": t.boolean(),
                "per_page": t.integer(),
                "page": t.integer(),
            }
        ),
        t.array(t.proxy(renames["short_branch"])).optional(),
    )
    functions["repos_get_branch"] = ghes.get(
        "/repos/{owner}/{repo}/branches/{branch}",
        t.struct({"owner": t.string(), "repo": t.string(), "branch": t.string()}),
        t.proxy(renames["branch_with_protection"]).optional(),
    )
    functions["repos_get_branch_protection"] = ghes.get(
        "/repos/{owner}/{repo}/branches/{branch}/protection",
        t.struct({"owner": t.string(), "repo": t.string(), "branch": t.string()}),
        t.proxy(renames["branch_protection"]).optional(),
    )
    functions["repos_update_branch_protection"] = ghes.put(
        "/repos/{owner}/{repo}/branches/{branch}/protection",
        t.struct(
            {
                "owner": t.string(),
                "repo": t.string(),
                "branch": t.string(),
                "required_status_checks": t.struct(
                    {
                        "strict": t.boolean(),
                        "contexts": t.array(t.string()),
                        "checks": t.array(
                            t.struct(
                                {
                                    "context": t.string(),
                                    "app_id": t.integer().optional(),
                                }
                            )
                        ).optional(),
                    }
                ).optional(),
                "enforce_admins": t.boolean().optional(),
                "required_pull_request_reviews": t.struct(
                    {
                        "dismissal_restrictions": t.struct(
                            {
                                "users": t.array(t.string()).optional(),
                                "teams": t.array(t.string()).optional(),
                            }
                        ).optional(),
                        "dismiss_stale_reviews": t.boolean().optional(),
                        "require_code_owner_reviews": t.boolean().optional(),
                        "required_approving_review_count": t.integer().optional(),
                    }
                ).optional(),
                "restrictions": t.struct(
                    {
                        "users": t.array(t.string()),
                        "teams": t.array(t.string()),
                        "apps": t.array(t.string()).optional(),
                    }
                ).optional(),
                "required_linear_history": t.boolean().optional(),
                "allow_force_pushes": t.boolean().optional(),
                "allow_deletions": t.boolean().optional(),
                "required_conversation_resolution": t.boolean().optional(),
                "contexts": t.array(t.string()).optional(),
            }
        ),
        t.proxy(renames["protected_branch"]).optional(),
        content_type="application/json",
        body_fields=(
            "required_status_checks",
            "enforce_admins",
            "required_pull_request_reviews",
            "restrictions",
            "required_linear_history",
            "allow_force_pushes",
            "allow_deletions",
            "required_conversation_resolution",
            "contexts",
        ),
    )
    functions["repos_delete_branch_protection"] = ghes.delete(
        "/repos/{owner}/{repo}/branches/{branch}/protection",
        t.struct({"owner": t.string(), "repo": t.string(), "branch": t.string()}),
        t.boolean(),
    )
    functions["repos_get_admin_branch_protection"] = ghes.get(
        "/repos/{owner}/{repo}/branches/{branch}/protection/enforce_admins",
        t.struct({"owner": t.string(), "repo": t.string(), "branch": t.string()}),
        t.proxy(renames["protected_branch_admin_enforced"]),
    )
    functions["repos_set_admin_branch_protection"] = ghes.post(
        "/repos/{owner}/{repo}/branches/{branch}/protection/enforce_admins",
        t.struct({"owner": t.string(), "repo": t.string(), "branch": t.string()}),
        t.proxy(renames["protected_branch_admin_enforced"]),
    )
    functions["repos_delete_admin_branch_protection"] = ghes.delete(
        "/repos/{owner}/{repo}/branches/{branch}/protection/enforce_admins",
        t.struct({"owner": t.string(), "repo": t.string(), "branch": t.string()}),
        t.boolean().optional(),
    )
    functions["repos_get_pull_request_review_protection"] = ghes.get(
        "/repos/{owner}/{repo}/branches/{branch}/protection/required_pull_request_reviews",
        t.struct({"owner": t.string(), "repo": t.string(), "branch": t.string()}),
        t.proxy(renames["protected_branch_pull_request_review"]),
    )
    functions["repos_update_pull_request_review_protection"] = ghes.patch(
        "/repos/{owner}/{repo}/branches/{branch}/protection/required_pull_request_reviews",
        t.struct(
            {
                "owner": t.string(),
                "repo": t.string(),
                "branch": t.string(),
                "dismissal_restrictions": t.struct(
                    {
                        "users": t.array(t.string()).optional(),
                        "teams": t.array(t.string()).optional(),
                    }
                ).optional(),
                "dismiss_stale_reviews": t.boolean().optional(),
                "require_code_owner_reviews": t.boolean().optional(),
                "required_approving_review_count": t.integer().optional(),
            }
        ),
        t.proxy(renames["protected_branch_pull_request_review"]),
        content_type="application/json",
        body_fields=(
            "dismissal_restrictions",
            "dismiss_stale_reviews",
            "require_code_owner_reviews",
            "required_approving_review_count",
        ),
    )
    functions["repos_delete_pull_request_review_protection"] = ghes.delete(
        "/repos/{owner}/{repo}/branches/{branch}/protection/required_pull_request_reviews",
        t.struct({"owner": t.string(), "repo": t.string(), "branch": t.string()}),
        t.boolean().optional(),
    )
    functions["repos_get_commit_signature_protection"] = ghes.get(
        "/repos/{owner}/{repo}/branches/{branch}/protection/required_signatures",
        t.struct({"owner": t.string(), "repo": t.string(), "branch": t.string()}),
        t.proxy(renames["protected_branch_admin_enforced"]).optional(),
    )
    functions["repos_create_commit_signature_protection"] = ghes.post(
        "/repos/{owner}/{repo}/branches/{branch}/protection/required_signatures",
        t.struct({"owner": t.string(), "repo": t.string(), "branch": t.string()}),
        t.proxy(renames["protected_branch_admin_enforced"]).optional(),
    )
    functions["repos_delete_commit_signature_protection"] = ghes.delete(
        "/repos/{owner}/{repo}/branches/{branch}/protection/required_signatures",
        t.struct({"owner": t.string(), "repo": t.string(), "branch": t.string()}),
        t.boolean().optional(),
    )
    functions["repos_get_status_checks_protection"] = ghes.get(
        "/repos/{owner}/{repo}/branches/{branch}/protection/required_status_checks",
        t.struct({"owner": t.string(), "repo": t.string(), "branch": t.string()}),
        t.proxy(renames["status_check_policy"]).optional(),
    )
    functions["repos_update_status_check_protection"] = ghes.patch(
        "/repos/{owner}/{repo}/branches/{branch}/protection/required_status_checks",
        t.struct(
            {
                "owner": t.string(),
                "repo": t.string(),
                "branch": t.string(),
                "strict": t.boolean().optional(),
                "contexts": t.array(t.string()).optional(),
            }
        ),
        t.proxy(renames["status_check_policy"]).optional(),
        content_type="application/json",
        body_fields=("strict", "contexts"),
    )
    functions["repos_remove_status_check_protection"] = ghes.delete(
        "/repos/{owner}/{repo}/branches/{branch}/protection/required_status_checks",
        t.struct({"owner": t.string(), "repo": t.string(), "branch": t.string()}),
        t.boolean(),
    )
    functions["repos_get_all_status_check_contexts"] = ghes.get(
        "/repos/{owner}/{repo}/branches/{branch}/protection/required_status_checks/contexts",
        t.struct({"owner": t.string(), "repo": t.string(), "branch": t.string()}),
        t.array(t.string()).optional(),
    )
    functions["repos_get_access_restrictions"] = ghes.get(
        "/repos/{owner}/{repo}/branches/{branch}/protection/restrictions",
        t.struct({"owner": t.string(), "repo": t.string(), "branch": t.string()}),
        t.proxy(renames["branch_restriction_policy"]).optional(),
    )
    functions["repos_delete_access_restrictions"] = ghes.delete(
        "/repos/{owner}/{repo}/branches/{branch}/protection/restrictions",
        t.struct({"owner": t.string(), "repo": t.string(), "branch": t.string()}),
        t.boolean(),
    )
    functions["repos_get_apps_with_access_to_protected_branch"] = ghes.get(
        "/repos/{owner}/{repo}/branches/{branch}/protection/restrictions/apps",
        t.struct({"owner": t.string(), "repo": t.string(), "branch": t.string()}),
        t.array(t.proxy(renames["integration"])).optional(),
    )
    functions["repos_get_teams_with_access_to_protected_branch"] = ghes.get(
        "/repos/{owner}/{repo}/branches/{branch}/protection/restrictions/teams",
        t.struct({"owner": t.string(), "repo": t.string(), "branch": t.string()}),
        t.array(t.proxy(renames["team"])).optional(),
    )
    functions["repos_get_users_with_access_to_protected_branch"] = ghes.get(
        "/repos/{owner}/{repo}/branches/{branch}/protection/restrictions/users",
        t.struct({"owner": t.string(), "repo": t.string(), "branch": t.string()}),
        t.array(t.proxy(renames["simple_user"])).optional(),
    )
    functions["checks_get"] = ghes.get(
        "/repos/{owner}/{repo}/check-runs/{check_run_id}",
        t.struct(
            {"owner": t.string(), "repo": t.string(), "check_run_id": t.integer()}
        ),
        t.proxy(renames["check_run"]),
    )
    functions["checks_list_annotations"] = ghes.get(
        "/repos/{owner}/{repo}/check-runs/{check_run_id}/annotations",
        t.struct(
            {
                "owner": t.string(),
                "repo": t.string(),
                "check_run_id": t.integer(),
                "per_page": t.integer(),
                "page": t.integer(),
            }
        ),
        t.array(t.proxy(renames["check_annotation"])),
    )
    functions["checks_create_suite"] = ghes.post(
        "/repos/{owner}/{repo}/check-suites",
        t.struct({"owner": t.string(), "repo": t.string(), "head_sha": t.string()}),
        t.proxy(renames["check_suite"]),
        content_type="application/json",
        body_fields=("head_sha",),
    )
    functions["checks_set_suites_preferences"] = ghes.patch(
        "/repos/{owner}/{repo}/check-suites/preferences",
        t.struct(
            {
                "owner": t.string(),
                "repo": t.string(),
                "auto_trigger_checks": t.array(
                    t.struct({"app_id": t.integer(), "setting": t.boolean()})
                ).optional(),
            }
        ),
        t.proxy(renames["check_suite_preference"]),
        content_type="application/json",
        body_fields=("auto_trigger_checks",),
    )
    functions["checks_get_suite"] = ghes.get(
        "/repos/{owner}/{repo}/check-suites/{check_suite_id}",
        t.struct(
            {"owner": t.string(), "repo": t.string(), "check_suite_id": t.integer()}
        ),
        t.proxy(renames["check_suite"]),
    )
    functions["checks_list_for_suite"] = ghes.get(
        "/repos/{owner}/{repo}/check-suites/{check_suite_id}/check-runs",
        t.struct(
            {
                "owner": t.string(),
                "repo": t.string(),
                "check_suite_id": t.integer(),
                "check_name": t.string(),
                "status": t.string(),
                "filter": t.string(),
                "per_page": t.integer(),
                "page": t.integer(),
            }
        ),
        t.struct(
            {
                "total_count": t.integer(),
                "check_runs": t.array(t.proxy(renames["check_run"])),
            }
        ),
    )
    functions["checks_rerequest_suite"] = ghes.post(
        "/repos/{owner}/{repo}/check-suites/{check_suite_id}/rerequest",
        t.struct(
            {"owner": t.string(), "repo": t.string(), "check_suite_id": t.integer()}
        ),
        t.struct({}),
    )
    functions["code_scanning_list_alerts_for_repo"] = ghes.get(
        "/repos/{owner}/{repo}/code-scanning/alerts",
        t.struct(
            {
                "owner": t.string(),
                "repo": t.string(),
                "tool_name": t.proxy(renames["code_scanning_analysis_tool_name"]),
                "tool_guid": t.proxy(renames["code_scanning_analysis_tool_guid"]),
                "page": t.integer(),
                "per_page": t.integer(),
                "ref": t.proxy(renames["code_scanning_ref"]),
                "state": t.proxy(renames["code_scanning_alert_state"]),
            }
        ),
        t.array(t.proxy(renames["code_scanning_alert_items"])).optional(),
    )
    functions["code_scanning_get_alert"] = ghes.get(
        "/repos/{owner}/{repo}/code-scanning/alerts/{alert_number}",
        t.struct(
            {
                "owner": t.string(),
                "repo": t.string(),
                "alert_number": t.proxy(renames["alert_number"]),
            }
        ),
        t.proxy(renames["code_scanning_alert"]).optional(),
    )
    functions["code_scanning_update_alert"] = ghes.patch(
        "/repos/{owner}/{repo}/code-scanning/alerts/{alert_number}",
        t.struct(
            {
                "owner": t.string(),
                "repo": t.string(),
                "alert_number": t.proxy(renames["alert_number"]),
                "state": t.proxy(renames["code_scanning_alert_set_state"]),
                "dismissed_reason": t.proxy(
                    renames["code_scanning_alert_dismissed_reason"]
                ).optional(),
            }
        ),
        t.proxy(renames["code_scanning_alert"]).optional(),
        content_type="application/json",
        body_fields=("state", "dismissed_reason"),
    )
    functions["code_scanning_list_recent_analyses"] = ghes.get(
        "/repos/{owner}/{repo}/code-scanning/analyses",
        t.struct(
            {
                "owner": t.string(),
                "repo": t.string(),
                "tool_name": t.proxy(renames["code_scanning_analysis_tool_name"]),
                "tool_guid": t.proxy(renames["code_scanning_analysis_tool_guid"]),
                "page": t.integer(),
                "per_page": t.integer(),
                "ref": t.proxy(renames["code_scanning_ref"]),
                "sarif_id": t.proxy(renames["code_scanning_analysis_sarif_id"]),
            }
        ),
        t.array(t.proxy(renames["code_scanning_analysis"])).optional(),
    )
    functions["code_scanning_upload_sarif"] = ghes.post(
        "/repos/{owner}/{repo}/code-scanning/sarifs",
        t.struct(
            {
                "owner": t.string(),
                "repo": t.string(),
                "commit_sha": t.proxy(renames["code_scanning_analysis_commit_sha"]),
                "ref": t.proxy(renames["code_scanning_ref"]),
                "sarif": t.proxy(renames["code_scanning_analysis_sarif_file"]),
                "checkout_uri": t.string().optional(),
                "started_at": t.string().optional(),
                "tool_name": t.string().optional(),
            }
        ),
        t.proxy(renames["code_scanning_sarifs_receipt"]).optional(),
        content_type="application/json",
        body_fields=(
            "commit_sha",
            "ref",
            "sarif",
            "checkout_uri",
            "started_at",
            "tool_name",
        ),
    )
    functions["repos_list_collaborators"] = ghes.get(
        "/repos/{owner}/{repo}/collaborators",
        t.struct(
            {
                "owner": t.string(),
                "repo": t.string(),
                "affiliation": t.string(),
                "per_page": t.integer(),
                "page": t.integer(),
            }
        ),
        t.array(t.proxy(renames["collaborator"])).optional(),
    )
    functions["repos_check_collaborator"] = ghes.get(
        "/repos/{owner}/{repo}/collaborators/{username}",
        t.struct({"owner": t.string(), "repo": t.string(), "username": t.string()}),
        t.boolean().optional(),
    )
    functions["repos_add_collaborator"] = ghes.put(
        "/repos/{owner}/{repo}/collaborators/{username}",
        t.struct(
            {
                "owner": t.string(),
                "repo": t.string(),
                "username": t.string(),
                "permission": t.string().optional(),
                "permissions": t.string().optional(),
            }
        ),
        t.proxy(renames["repository_invitation"]),
        content_type="application/json",
        body_fields=("permission", "permissions"),
    )
    functions["repos_remove_collaborator"] = ghes.delete(
        "/repos/{owner}/{repo}/collaborators/{username}",
        t.struct({"owner": t.string(), "repo": t.string(), "username": t.string()}),
        t.boolean(),
    )
    functions["repos_get_collaborator_permission_level"] = ghes.get(
        "/repos/{owner}/{repo}/collaborators/{username}/permission",
        t.struct({"owner": t.string(), "repo": t.string(), "username": t.string()}),
        t.proxy(renames["repository_collaborator_permission"]).optional(),
    )
    functions["repos_list_commit_comments_for_repo"] = ghes.get(
        "/repos/{owner}/{repo}/comments",
        t.struct(
            {
                "owner": t.string(),
                "repo": t.string(),
                "per_page": t.integer(),
                "page": t.integer(),
            }
        ),
        t.array(t.proxy(renames["commit_comment"])),
    )
    functions["repos_get_commit_comment"] = ghes.get(
        "/repos/{owner}/{repo}/comments/{comment_id}",
        t.struct({"owner": t.string(), "repo": t.string(), "comment_id": t.integer()}),
        t.proxy(renames["commit_comment"]).optional(),
    )
    functions["repos_update_commit_comment"] = ghes.patch(
        "/repos/{owner}/{repo}/comments/{comment_id}",
        t.struct(
            {
                "owner": t.string(),
                "repo": t.string(),
                "comment_id": t.integer(),
                "body": t.string(),
            }
        ),
        t.proxy(renames["commit_comment"]).optional(),
        content_type="application/json",
        body_fields=("body",),
    )
    functions["repos_delete_commit_comment"] = ghes.delete(
        "/repos/{owner}/{repo}/comments/{comment_id}",
        t.struct({"owner": t.string(), "repo": t.string(), "comment_id": t.integer()}),
        t.boolean().optional(),
    )
    functions["reactions_list_for_commit_comment"] = ghes.get(
        "/repos/{owner}/{repo}/comments/{comment_id}/reactions",
        t.struct(
            {
                "owner": t.string(),
                "repo": t.string(),
                "comment_id": t.integer(),
                "content": t.string(),
                "per_page": t.integer(),
                "page": t.integer(),
            }
        ),
        t.array(t.proxy(renames["reaction"])).optional(),
    )
    functions["reactions_create_for_commit_comment"] = ghes.post(
        "/repos/{owner}/{repo}/comments/{comment_id}/reactions",
        t.struct(
            {
                "owner": t.string(),
                "repo": t.string(),
                "comment_id": t.integer(),
                "content": t.string(),
            }
        ),
        t.proxy(renames["reaction"]),
        content_type="application/json",
        body_fields=("content",),
    )
    functions["reactions_delete_for_commit_comment"] = ghes.delete(
        "/repos/{owner}/{repo}/comments/{comment_id}/reactions/{reaction_id}",
        t.struct(
            {
                "owner": t.string(),
                "repo": t.string(),
                "comment_id": t.integer(),
                "reaction_id": t.integer(),
            }
        ),
        t.boolean(),
    )
    functions["repos_list_commits"] = ghes.get(
        "/repos/{owner}/{repo}/commits",
        t.struct(
            {
                "owner": t.string(),
                "repo": t.string(),
                "sha": t.string(),
                "path": t.string(),
                "author": t.string(),
                "since": t.string(),
                "until": t.string(),
                "per_page": t.integer(),
                "page": t.integer(),
            }
        ),
        t.array(t.proxy(renames["commit"])).optional(),
    )
    functions["repos_list_branches_for_head_commit"] = ghes.get(
        "/repos/{owner}/{repo}/commits/{commit_sha}/branches-where-head",
        t.struct({"owner": t.string(), "repo": t.string(), "commit_sha": t.string()}),
        t.array(t.proxy(renames["branch_short"])),
    )
    functions["repos_list_comments_for_commit"] = ghes.get(
        "/repos/{owner}/{repo}/commits/{commit_sha}/comments",
        t.struct(
            {
                "owner": t.string(),
                "repo": t.string(),
                "commit_sha": t.string(),
                "per_page": t.integer(),
                "page": t.integer(),
            }
        ),
        t.array(t.proxy(renames["commit_comment"])),
    )
    functions["repos_create_commit_comment"] = ghes.post(
        "/repos/{owner}/{repo}/commits/{commit_sha}/comments",
        t.struct(
            {
                "owner": t.string(),
                "repo": t.string(),
                "commit_sha": t.string(),
                "body": t.string(),
                "path": t.string().optional(),
                "position": t.integer().optional(),
                "line": t.integer().optional(),
            }
        ),
        t.proxy(renames["commit_comment"]),
        content_type="application/json",
        body_fields=("body", "path", "position", "line"),
    )
    functions["repos_list_pull_requests_associated_with_commit"] = ghes.get(
        "/repos/{owner}/{repo}/commits/{commit_sha}/pulls",
        t.struct(
            {
                "owner": t.string(),
                "repo": t.string(),
                "commit_sha": t.string(),
                "per_page": t.integer(),
                "page": t.integer(),
            }
        ),
        t.array(t.proxy(renames["pull_request_simple"])),
    )
    functions["repos_get_commit"] = ghes.get(
        "/repos/{owner}/{repo}/commits/{ref}",
        t.struct(
            {
                "owner": t.string(),
                "repo": t.string(),
                "page": t.integer(),
                "per_page": t.integer(),
                "ref": t.string(),
            }
        ),
        t.proxy(renames["commit"]).optional(),
    )
    functions["checks_list_for_ref"] = ghes.get(
        "/repos/{owner}/{repo}/commits/{ref}/check-runs",
        t.struct(
            {
                "owner": t.string(),
                "repo": t.string(),
                "ref": t.string(),
                "check_name": t.string(),
                "status": t.string(),
                "filter": t.string(),
                "per_page": t.integer(),
                "page": t.integer(),
                "app_id": t.integer(),
            }
        ),
        t.struct(
            {
                "total_count": t.integer(),
                "check_runs": t.array(t.proxy(renames["check_run"])),
            }
        ),
    )
    functions["checks_list_suites_for_ref"] = ghes.get(
        "/repos/{owner}/{repo}/commits/{ref}/check-suites",
        t.struct(
            {
                "owner": t.string(),
                "repo": t.string(),
                "ref": t.string(),
                "app_id": t.integer(),
                "check_name": t.string(),
                "per_page": t.integer(),
                "page": t.integer(),
            }
        ),
        t.struct(
            {
                "total_count": t.integer(),
                "check_suites": t.array(t.proxy(renames["check_suite"])),
            }
        ),
    )
    functions["repos_get_combined_status_for_ref"] = ghes.get(
        "/repos/{owner}/{repo}/commits/{ref}/status",
        t.struct(
            {
                "owner": t.string(),
                "repo": t.string(),
                "ref": t.string(),
                "per_page": t.integer(),
                "page": t.integer(),
            }
        ),
        t.proxy(renames["combined_commit_status"]).optional(),
    )
    functions["repos_list_commit_statuses_for_ref"] = ghes.get(
        "/repos/{owner}/{repo}/commits/{ref}/statuses",
        t.struct(
            {
                "owner": t.string(),
                "repo": t.string(),
                "ref": t.string(),
                "per_page": t.integer(),
                "page": t.integer(),
            }
        ),
        t.array(t.proxy(renames["status"])),
    )
    functions["repos_compare_commits"] = ghes.get(
        "/repos/{owner}/{repo}/compare/{basehead}",
        t.struct({"owner": t.string(), "repo": t.string(), "basehead": t.string()}),
        t.proxy(renames["commit_comparison"]).optional(),
    )
    functions["apps_create_content_attachment"] = ghes.post(
        "/repos/{owner}/{repo}/content_references/{content_reference_id}/attachments",
        t.struct(
            {
                "owner": t.string(),
                "repo": t.string(),
                "content_reference_id": t.integer(),
                "title": t.string(),
                "body": t.string(),
            }
        ),
        t.proxy(renames["content_reference_attachment"]).optional(),
        content_type="application/json",
        body_fields=("title", "body"),
    )
    functions["repos_get_content"] = ghes.get(
        "/repos/{owner}/{repo}/contents/{path}",
        t.struct(
            {
                "owner": t.string(),
                "repo": t.string(),
                "path": t.string(),
                "ref": t.string(),
            }
        ),
        t.either(
            [
                t.proxy(renames["content_directory"]),
                t.proxy(renames["content_file"]),
                t.proxy(renames["content_symlink"]),
                t.proxy(renames["content_submodule"]),
            ]
        ).optional(),
    )
    functions["repos_create_or_update_file_contents"] = ghes.put(
        "/repos/{owner}/{repo}/contents/{path}",
        t.struct(
            {
                "owner": t.string(),
                "repo": t.string(),
                "path": t.string(),
                "message": t.string(),
                "content": t.string(),
                "sha": t.string().optional(),
                "branch": t.string().optional(),
                "committer": t.struct(
                    {
                        "name": t.string(),
                        "email": t.string(),
                        "date": t.string().optional(),
                    }
                ).optional(),
                "author": t.struct(
                    {
                        "name": t.string(),
                        "email": t.string(),
                        "date": t.string().optional(),
                    }
                ).optional(),
            }
        ),
        t.proxy(renames["file_commit"]).optional(),
        content_type="application/json",
        body_fields=("message", "content", "sha", "branch", "committer", "author"),
    )
    functions["repos_delete_file"] = ghes.delete(
        "/repos/{owner}/{repo}/contents/{path}",
        t.struct(
            {
                "owner": t.string(),
                "repo": t.string(),
                "path": t.string(),
                "message": t.string(),
                "sha": t.string(),
                "branch": t.string().optional(),
                "committer": t.struct(
                    {"name": t.string().optional(), "email": t.string().optional()}
                ).optional(),
                "author": t.struct(
                    {"name": t.string().optional(), "email": t.string().optional()}
                ).optional(),
            }
        ),
        t.proxy(renames["file_commit"]).optional(),
        content_type="application/json",
        body_fields=("message", "sha", "branch", "committer", "author"),
    )
    functions["repos_list_contributors"] = ghes.get(
        "/repos/{owner}/{repo}/contributors",
        t.struct(
            {
                "owner": t.string(),
                "repo": t.string(),
                "anon": t.string(),
                "per_page": t.integer(),
                "page": t.integer(),
            }
        ),
        t.array(t.proxy(renames["contributor"])).optional(),
    )
    functions["repos_list_deployments"] = ghes.get(
        "/repos/{owner}/{repo}/deployments",
        t.struct(
            {
                "owner": t.string(),
                "repo": t.string(),
                "sha": t.string(),
                "ref": t.string(),
                "task": t.string(),
                "environment": t.string().optional(),
                "per_page": t.integer(),
                "page": t.integer(),
            }
        ),
        t.array(t.proxy(renames["deployment"])),
    )
    functions["repos_create_deployment"] = ghes.post(
        "/repos/{owner}/{repo}/deployments",
        t.struct(
            {
                "owner": t.string(),
                "repo": t.string(),
                "ref": t.string(),
                "task": t.string().optional(),
                "auto_merge": t.boolean().optional(),
                "required_contexts": t.array(t.string()).optional(),
                "payload": t.either([t.struct({}), t.string()]).optional(),
                "environment": t.string().optional(),
                "description": t.string().optional(),
                "transient_environment": t.boolean().optional(),
                "production_environment": t.boolean().optional(),
            }
        ),
        t.proxy(renames["deployment"]),
        content_type="application/json",
        body_fields=(
            "ref",
            "task",
            "auto_merge",
            "required_contexts",
            "payload",
            "environment",
            "description",
            "transient_environment",
            "production_environment",
        ),
    )
    functions["repos_get_deployment"] = ghes.get(
        "/repos/{owner}/{repo}/deployments/{deployment_id}",
        t.struct(
            {"owner": t.string(), "repo": t.string(), "deployment_id": t.integer()}
        ),
        t.proxy(renames["deployment"]).optional(),
    )
    functions["repos_delete_deployment"] = ghes.delete(
        "/repos/{owner}/{repo}/deployments/{deployment_id}",
        t.struct(
            {"owner": t.string(), "repo": t.string(), "deployment_id": t.integer()}
        ),
        t.boolean().optional(),
    )
    functions["repos_list_deployment_statuses"] = ghes.get(
        "/repos/{owner}/{repo}/deployments/{deployment_id}/statuses",
        t.struct(
            {
                "owner": t.string(),
                "repo": t.string(),
                "deployment_id": t.integer(),
                "per_page": t.integer(),
                "page": t.integer(),
            }
        ),
        t.array(t.proxy(renames["deployment_status"])).optional(),
    )
    functions["repos_create_deployment_status"] = ghes.post(
        "/repos/{owner}/{repo}/deployments/{deployment_id}/statuses",
        t.struct(
            {
                "owner": t.string(),
                "repo": t.string(),
                "deployment_id": t.integer(),
                "state": t.string(),
                "target_url": t.string().optional(),
                "log_url": t.string().optional(),
                "description": t.string().optional(),
                "environment": t.string().optional(),
                "environment_url": t.string().optional(),
                "auto_inactive": t.boolean().optional(),
            }
        ),
        t.proxy(renames["deployment_status"]),
        content_type="application/json",
        body_fields=(
            "state",
            "target_url",
            "log_url",
            "description",
            "environment",
            "environment_url",
            "auto_inactive",
        ),
    )
    functions["repos_get_deployment_status"] = ghes.get(
        "/repos/{owner}/{repo}/deployments/{deployment_id}/statuses/{status_id}",
        t.struct(
            {
                "owner": t.string(),
                "repo": t.string(),
                "deployment_id": t.integer(),
                "status_id": t.integer(),
            }
        ),
        t.proxy(renames["deployment_status"]).optional(),
    )
    functions["repos_create_dispatch_event"] = ghes.post(
        "/repos/{owner}/{repo}/dispatches",
        t.struct(
            {
                "owner": t.string(),
                "repo": t.string(),
                "event_type": t.string(),
                "client_payload": t.struct({}).optional(),
            }
        ),
        t.boolean(),
        content_type="application/json",
        body_fields=("event_type", "client_payload"),
    )
    functions["activity_list_repo_events"] = ghes.get(
        "/repos/{owner}/{repo}/events",
        t.struct(
            {
                "owner": t.string(),
                "repo": t.string(),
                "per_page": t.integer(),
                "page": t.integer(),
            }
        ),
        t.array(t.proxy(renames["event"])),
    )
    functions["repos_list_forks"] = ghes.get(
        "/repos/{owner}/{repo}/forks",
        t.struct(
            {
                "owner": t.string(),
                "repo": t.string(),
                "sort": t.string(),
                "per_page": t.integer(),
                "page": t.integer(),
            }
        ),
        t.array(t.proxy(renames["minimal_repository"])),
    )
    functions["repos_create_fork"] = ghes.post(
        "/repos/{owner}/{repo}/forks",
        t.struct(
            {
                "owner": t.string(),
                "repo": t.string(),
                "organization": t.string().optional(),
            }
        ),
        t.proxy(renames["full_repository"]).optional(),
        content_type="application/json",
        body_fields=("organization",),
    )
    functions["git_create_blob"] = ghes.post(
        "/repos/{owner}/{repo}/git/blobs",
        t.struct(
            {
                "owner": t.string(),
                "repo": t.string(),
                "content": t.string(),
                "encoding": t.string().optional(),
            }
        ),
        t.proxy(renames["short_blob"]).optional(),
        content_type="application/json",
        body_fields=("content", "encoding"),
    )
    functions["git_get_blob"] = ghes.get(
        "/repos/{owner}/{repo}/git/blobs/{file_sha}",
        t.struct({"owner": t.string(), "repo": t.string(), "file_sha": t.string()}),
        t.proxy(renames["blob"]).optional(),
    )
    functions["git_create_commit"] = ghes.post(
        "/repos/{owner}/{repo}/git/commits",
        t.struct(
            {
                "owner": t.string(),
                "repo": t.string(),
                "message": t.string(),
                "tree": t.string(),
                "parents": t.array(t.string()).optional(),
                "author": t.struct(
                    {
                        "name": t.string(),
                        "email": t.string(),
                        "date": t.string().optional(),
                    }
                ).optional(),
                "committer": t.struct(
                    {
                        "name": t.string().optional(),
                        "email": t.string().optional(),
                        "date": t.string().optional(),
                    }
                ).optional(),
                "signature": t.string().optional(),
            }
        ),
        t.proxy(renames["git_commit"]).optional(),
        content_type="application/json",
        body_fields=("message", "tree", "parents", "author", "committer", "signature"),
    )
    functions["git_get_commit"] = ghes.get(
        "/repos/{owner}/{repo}/git/commits/{commit_sha}",
        t.struct({"owner": t.string(), "repo": t.string(), "commit_sha": t.string()}),
        t.proxy(renames["git_commit"]).optional(),
    )
    functions["git_list_matching_refs"] = ghes.get(
        "/repos/{owner}/{repo}/git/matching-refs/{ref}",
        t.struct(
            {
                "owner": t.string(),
                "repo": t.string(),
                "ref": t.string(),
                "per_page": t.integer(),
                "page": t.integer(),
            }
        ),
        t.array(t.proxy(renames["git_ref"])),
    )
    functions["git_get_ref"] = ghes.get(
        "/repos/{owner}/{repo}/git/ref/{ref}",
        t.struct({"owner": t.string(), "repo": t.string(), "ref": t.string()}),
        t.proxy(renames["git_ref"]).optional(),
    )
    functions["git_create_ref"] = ghes.post(
        "/repos/{owner}/{repo}/git/refs",
        t.struct(
            {
                "owner": t.string(),
                "repo": t.string(),
                "ref": t.string(),
                "sha": t.string(),
                "key": t.string().optional(),
            }
        ),
        t.proxy(renames["git_ref"]),
        content_type="application/json",
        body_fields=("ref", "sha", "key"),
    )
    functions["git_update_ref"] = ghes.patch(
        "/repos/{owner}/{repo}/git/refs/{ref}",
        t.struct(
            {
                "owner": t.string(),
                "repo": t.string(),
                "ref": t.string(),
                "sha": t.string(),
                "force": t.boolean().optional(),
            }
        ),
        t.proxy(renames["git_ref"]),
        content_type="application/json",
        body_fields=("sha", "force"),
    )
    functions["git_delete_ref"] = ghes.delete(
        "/repos/{owner}/{repo}/git/refs/{ref}",
        t.struct({"owner": t.string(), "repo": t.string(), "ref": t.string()}),
        t.boolean(),
    )
    functions["git_create_tag"] = ghes.post(
        "/repos/{owner}/{repo}/git/tags",
        t.struct(
            {
                "owner": t.string(),
                "repo": t.string(),
                "tag": t.string(),
                "message": t.string(),
                "object": t.string(),
                "type": t.string(),
                "tagger": t.struct(
                    {
                        "name": t.string(),
                        "email": t.string(),
                        "date": t.string().optional(),
                    }
                ).optional(),
            }
        ),
        t.proxy(renames["git_tag"]),
        content_type="application/json",
        body_fields=("tag", "message", "object", "type", "tagger"),
    )
    functions["git_get_tag"] = ghes.get(
        "/repos/{owner}/{repo}/git/tags/{tag_sha}",
        t.struct({"owner": t.string(), "repo": t.string(), "tag_sha": t.string()}),
        t.proxy(renames["git_tag"]).optional(),
    )
    functions["git_create_tree"] = ghes.post(
        "/repos/{owner}/{repo}/git/trees",
        t.struct(
            {
                "owner": t.string(),
                "repo": t.string(),
                "tree": t.array(
                    t.struct(
                        {
                            "path": t.string().optional(),
                            "mode": t.string().optional(),
                            "type": t.string().optional(),
                            "sha": t.string().optional(),
                            "content": t.string().optional(),
                        }
                    )
                ),
                "base_tree": t.string().optional(),
            }
        ),
        t.proxy(renames["git_tree"]).optional(),
        content_type="application/json",
        body_fields=("tree", "base_tree"),
    )
    functions["git_get_tree"] = ghes.get(
        "/repos/{owner}/{repo}/git/trees/{tree_sha}",
        t.struct(
            {
                "owner": t.string(),
                "repo": t.string(),
                "tree_sha": t.string(),
                "recursive": t.string(),
            }
        ),
        t.proxy(renames["git_tree"]).optional(),
    )
    functions["repos_list_webhooks"] = ghes.get(
        "/repos/{owner}/{repo}/hooks",
        t.struct(
            {
                "owner": t.string(),
                "repo": t.string(),
                "per_page": t.integer(),
                "page": t.integer(),
            }
        ),
        t.array(t.proxy(renames["hook"])).optional(),
    )
    functions["repos_create_webhook"] = ghes.post(
        "/repos/{owner}/{repo}/hooks",
        t.struct(
            {
                "owner": t.string(),
                "repo": t.string(),
                "name": t.string().optional(),
                "config": t.struct(
                    {
                        "url": t.proxy(renames["webhook_config_url"]).optional(),
                        "content_type": t.proxy(
                            renames["webhook_config_content_type"]
                        ).optional(),
                        "secret": t.proxy(renames["webhook_config_secret"]).optional(),
                        "insecure_ssl": t.proxy(
                            renames["webhook_config_insecure_ssl"]
                        ).optional(),
                        "token": t.string().optional(),
                        "digest": t.string().optional(),
                    }
                ).optional(),
                "events": t.array(t.string()).optional(),
                "active": t.boolean().optional(),
            }
        ),
        t.proxy(renames["hook"]).optional(),
        content_type="application/json",
        body_fields=("name", "config", "events", "active"),
    )
    functions["repos_get_webhook"] = ghes.get(
        "/repos/{owner}/{repo}/hooks/{hook_id}",
        t.struct({"owner": t.string(), "repo": t.string(), "hook_id": t.integer()}),
        t.proxy(renames["hook"]).optional(),
    )
    functions["repos_update_webhook"] = ghes.patch(
        "/repos/{owner}/{repo}/hooks/{hook_id}",
        t.struct(
            {
                "owner": t.string(),
                "repo": t.string(),
                "hook_id": t.integer(),
                "config": t.struct(
                    {
                        "url": t.proxy(renames["webhook_config_url"]),
                        "content_type": t.proxy(
                            renames["webhook_config_content_type"]
                        ).optional(),
                        "secret": t.proxy(renames["webhook_config_secret"]).optional(),
                        "insecure_ssl": t.proxy(
                            renames["webhook_config_insecure_ssl"]
                        ).optional(),
                        "address": t.string().optional(),
                        "room": t.string().optional(),
                    }
                ).optional(),
                "events": t.array(t.string()).optional(),
                "add_events": t.array(t.string()).optional(),
                "remove_events": t.array(t.string()).optional(),
                "active": t.boolean().optional(),
            }
        ),
        t.proxy(renames["hook"]).optional(),
        content_type="application/json",
        body_fields=("config", "events", "add_events", "remove_events", "active"),
    )
    functions["repos_delete_webhook"] = ghes.delete(
        "/repos/{owner}/{repo}/hooks/{hook_id}",
        t.struct({"owner": t.string(), "repo": t.string(), "hook_id": t.integer()}),
        t.boolean().optional(),
    )
    functions["repos_get_webhook_config_for_repo"] = ghes.get(
        "/repos/{owner}/{repo}/hooks/{hook_id}/config",
        t.struct({"owner": t.string(), "repo": t.string(), "hook_id": t.integer()}),
        t.proxy(renames["webhook_config"]),
    )
    functions["repos_update_webhook_config_for_repo"] = ghes.patch(
        "/repos/{owner}/{repo}/hooks/{hook_id}/config",
        t.struct(
            {
                "owner": t.string(),
                "repo": t.string(),
                "hook_id": t.integer(),
                "url": t.proxy(renames["webhook_config_url"]).optional(),
                "content_type": t.proxy(
                    renames["webhook_config_content_type"]
                ).optional(),
                "secret": t.proxy(renames["webhook_config_secret"]).optional(),
                "insecure_ssl": t.proxy(
                    renames["webhook_config_insecure_ssl"]
                ).optional(),
            }
        ),
        t.proxy(renames["webhook_config"]),
        content_type="application/json",
        body_fields=("url", "content_type", "secret", "insecure_ssl"),
    )
    functions["repos_ping_webhook"] = ghes.post(
        "/repos/{owner}/{repo}/hooks/{hook_id}/pings",
        t.struct({"owner": t.string(), "repo": t.string(), "hook_id": t.integer()}),
        t.boolean().optional(),
    )
    functions["repos_test_push_webhook"] = ghes.post(
        "/repos/{owner}/{repo}/hooks/{hook_id}/tests",
        t.struct({"owner": t.string(), "repo": t.string(), "hook_id": t.integer()}),
        t.boolean().optional(),
    )
    functions["apps_get_repo_installation"] = ghes.get(
        "/repos/{owner}/{repo}/installation",
        t.struct({"owner": t.string(), "repo": t.string()}),
        t.proxy(renames["installation"]).optional(),
    )
    functions["repos_list_invitations"] = ghes.get(
        "/repos/{owner}/{repo}/invitations",
        t.struct(
            {
                "owner": t.string(),
                "repo": t.string(),
                "per_page": t.integer(),
                "page": t.integer(),
            }
        ),
        t.array(t.proxy(renames["repository_invitation"])),
    )
    functions["repos_update_invitation"] = ghes.patch(
        "/repos/{owner}/{repo}/invitations/{invitation_id}",
        t.struct(
            {
                "owner": t.string(),
                "repo": t.string(),
                "invitation_id": t.integer(),
                "permissions": t.string().optional(),
            }
        ),
        t.proxy(renames["repository_invitation"]),
        content_type="application/json",
        body_fields=("permissions",),
    )
    functions["repos_delete_invitation"] = ghes.delete(
        "/repos/{owner}/{repo}/invitations/{invitation_id}",
        t.struct(
            {"owner": t.string(), "repo": t.string(), "invitation_id": t.integer()}
        ),
        t.boolean(),
    )
    functions["issues_list_for_repo"] = ghes.get(
        "/repos/{owner}/{repo}/issues",
        t.struct(
            {
                "owner": t.string(),
                "repo": t.string(),
                "milestone": t.string(),
                "state": t.string(),
                "assignee": t.string(),
                "creator": t.string(),
                "mentioned": t.string(),
                "labels": t.string(),
                "sort": t.string(),
                "direction": t.string(),
                "since": t.string(),
                "per_page": t.integer(),
                "page": t.integer(),
            }
        ),
        t.array(t.proxy(renames["issue"])).optional(),
    )
    functions["issues_create"] = ghes.post(
        "/repos/{owner}/{repo}/issues",
        t.struct(
            {
                "owner": t.string(),
                "repo": t.string(),
                "title": t.either([t.string(), t.integer()]),
                "body": t.string().optional(),
                "assignee": t.string().optional(),
                "milestone": t.either([t.string(), t.integer()]).optional(),
                "labels": t.array(
                    t.either(
                        [
                            t.string(),
                            t.struct(
                                {
                                    "id": t.integer().optional(),
                                    "name": t.string().optional(),
                                    "description": t.string().optional(),
                                    "color": t.string().optional(),
                                }
                            ),
                        ]
                    )
                ).optional(),
                "assignees": t.array(t.string()).optional(),
            }
        ),
        t.proxy(renames["issue"]).optional(),
        content_type="application/json",
        body_fields=("title", "body", "assignee", "milestone", "labels", "assignees"),
    )
    functions["issues_list_comments_for_repo"] = ghes.get(
        "/repos/{owner}/{repo}/issues/comments",
        t.struct(
            {
                "owner": t.string(),
                "repo": t.string(),
                "sort": t.string(),
                "direction": t.string(),
                "since": t.string(),
                "per_page": t.integer(),
                "page": t.integer(),
            }
        ),
        t.array(t.proxy(renames["issue_comment"])).optional(),
    )
    functions["issues_get_comment"] = ghes.get(
        "/repos/{owner}/{repo}/issues/comments/{comment_id}",
        t.struct({"owner": t.string(), "repo": t.string(), "comment_id": t.integer()}),
        t.proxy(renames["issue_comment"]).optional(),
    )
    functions["issues_update_comment"] = ghes.patch(
        "/repos/{owner}/{repo}/issues/comments/{comment_id}",
        t.struct(
            {
                "owner": t.string(),
                "repo": t.string(),
                "comment_id": t.integer(),
                "body": t.string(),
            }
        ),
        t.proxy(renames["issue_comment"]),
        content_type="application/json",
        body_fields=("body",),
    )
    functions["issues_delete_comment"] = ghes.delete(
        "/repos/{owner}/{repo}/issues/comments/{comment_id}",
        t.struct({"owner": t.string(), "repo": t.string(), "comment_id": t.integer()}),
        t.boolean(),
    )
    functions["reactions_list_for_issue_comment"] = ghes.get(
        "/repos/{owner}/{repo}/issues/comments/{comment_id}/reactions",
        t.struct(
            {
                "owner": t.string(),
                "repo": t.string(),
                "comment_id": t.integer(),
                "content": t.string(),
                "per_page": t.integer(),
                "page": t.integer(),
            }
        ),
        t.array(t.proxy(renames["reaction"])).optional(),
    )
    functions["reactions_create_for_issue_comment"] = ghes.post(
        "/repos/{owner}/{repo}/issues/comments/{comment_id}/reactions",
        t.struct(
            {
                "owner": t.string(),
                "repo": t.string(),
                "comment_id": t.integer(),
                "content": t.string(),
            }
        ),
        t.proxy(renames["reaction"]),
        content_type="application/json",
        body_fields=("content",),
    )
    functions["reactions_delete_for_issue_comment"] = ghes.delete(
        "/repos/{owner}/{repo}/issues/comments/{comment_id}/reactions/{reaction_id}",
        t.struct(
            {
                "owner": t.string(),
                "repo": t.string(),
                "comment_id": t.integer(),
                "reaction_id": t.integer(),
            }
        ),
        t.boolean(),
    )
    functions["issues_list_events_for_repo"] = ghes.get(
        "/repos/{owner}/{repo}/issues/events",
        t.struct(
            {
                "owner": t.string(),
                "repo": t.string(),
                "per_page": t.integer(),
                "page": t.integer(),
            }
        ),
        t.array(t.proxy(renames["issue_event"])),
    )
    functions["issues_get_event"] = ghes.get(
        "/repos/{owner}/{repo}/issues/events/{event_id}",
        t.struct({"owner": t.string(), "repo": t.string(), "event_id": t.integer()}),
        t.proxy(renames["issue_event"]).optional(),
    )
    functions["issues_get"] = ghes.get(
        "/repos/{owner}/{repo}/issues/{issue_number}",
        t.struct(
            {"owner": t.string(), "repo": t.string(), "issue_number": t.integer()}
        ),
        t.proxy(renames["issue"]).optional(),
    )
    functions["issues_update"] = ghes.patch(
        "/repos/{owner}/{repo}/issues/{issue_number}",
        t.struct(
            {
                "owner": t.string(),
                "repo": t.string(),
                "issue_number": t.integer(),
                "title": t.either([t.string(), t.integer()]).optional(),
                "body": t.string().optional(),
                "assignee": t.string().optional(),
                "state": t.string().optional(),
                "milestone": t.either([t.string(), t.integer()]).optional(),
                "labels": t.array(
                    t.either(
                        [
                            t.string(),
                            t.struct(
                                {
                                    "id": t.integer().optional(),
                                    "name": t.string().optional(),
                                    "description": t.string().optional(),
                                    "color": t.string().optional(),
                                }
                            ),
                        ]
                    )
                ).optional(),
                "assignees": t.array(t.string()).optional(),
            }
        ),
        t.proxy(renames["issue"]).optional(),
        content_type="application/json",
        body_fields=(
            "title",
            "body",
            "assignee",
            "state",
            "milestone",
            "labels",
            "assignees",
        ),
    )
    functions["issues_add_assignees"] = ghes.post(
        "/repos/{owner}/{repo}/issues/{issue_number}/assignees",
        t.struct(
            {
                "owner": t.string(),
                "repo": t.string(),
                "issue_number": t.integer(),
                "assignees": t.array(t.string()).optional(),
            }
        ),
        t.proxy(renames["issue"]),
        content_type="application/json",
        body_fields=("assignees",),
    )
    functions["issues_remove_assignees"] = ghes.delete(
        "/repos/{owner}/{repo}/issues/{issue_number}/assignees",
        t.struct(
            {
                "owner": t.string(),
                "repo": t.string(),
                "issue_number": t.integer(),
                "assignees": t.array(t.string()).optional(),
            }
        ),
        t.proxy(renames["issue"]),
        content_type="application/json",
        body_fields=("assignees",),
    )
    functions["issues_list_comments"] = ghes.get(
        "/repos/{owner}/{repo}/issues/{issue_number}/comments",
        t.struct(
            {
                "owner": t.string(),
                "repo": t.string(),
                "issue_number": t.integer(),
                "since": t.string(),
                "per_page": t.integer(),
                "page": t.integer(),
            }
        ),
        t.array(t.proxy(renames["issue_comment"])).optional(),
    )
    functions["issues_create_comment"] = ghes.post(
        "/repos/{owner}/{repo}/issues/{issue_number}/comments",
        t.struct(
            {
                "owner": t.string(),
                "repo": t.string(),
                "issue_number": t.integer(),
                "body": t.string(),
            }
        ),
        t.proxy(renames["issue_comment"]).optional(),
        content_type="application/json",
        body_fields=("body",),
    )
    functions["issues_list_events"] = ghes.get(
        "/repos/{owner}/{repo}/issues/{issue_number}/events",
        t.struct(
            {
                "owner": t.string(),
                "repo": t.string(),
                "issue_number": t.integer(),
                "per_page": t.integer(),
                "page": t.integer(),
            }
        ),
        t.array(t.proxy(renames["issue_event_for_issue"])),
    )
    functions["issues_list_labels_on_issue"] = ghes.get(
        "/repos/{owner}/{repo}/issues/{issue_number}/labels",
        t.struct(
            {
                "owner": t.string(),
                "repo": t.string(),
                "issue_number": t.integer(),
                "per_page": t.integer(),
                "page": t.integer(),
            }
        ),
        t.array(t.proxy(renames["label"])),
    )
    functions["issues_remove_all_labels"] = ghes.delete(
        "/repos/{owner}/{repo}/issues/{issue_number}/labels",
        t.struct(
            {"owner": t.string(), "repo": t.string(), "issue_number": t.integer()}
        ),
        t.boolean(),
    )
    functions["issues_remove_label"] = ghes.delete(
        "/repos/{owner}/{repo}/issues/{issue_number}/labels/{name}",
        t.struct(
            {
                "owner": t.string(),
                "repo": t.string(),
                "issue_number": t.integer(),
                "name": t.string(),
            }
        ),
        t.array(t.proxy(renames["label"])).optional(),
    )
    functions["issues_lock"] = ghes.put(
        "/repos/{owner}/{repo}/issues/{issue_number}/lock",
        t.struct(
            {
                "owner": t.string(),
                "repo": t.string(),
                "issue_number": t.integer(),
                "lock_reason": t.string().optional(),
            }
        ),
        t.boolean().optional(),
        content_type="application/json",
        body_fields=("lock_reason",),
    )
    functions["issues_unlock"] = ghes.delete(
        "/repos/{owner}/{repo}/issues/{issue_number}/lock",
        t.struct(
            {"owner": t.string(), "repo": t.string(), "issue_number": t.integer()}
        ),
        t.boolean().optional(),
    )
    functions["reactions_list_for_issue"] = ghes.get(
        "/repos/{owner}/{repo}/issues/{issue_number}/reactions",
        t.struct(
            {
                "owner": t.string(),
                "repo": t.string(),
                "issue_number": t.integer(),
                "content": t.string(),
                "per_page": t.integer(),
                "page": t.integer(),
            }
        ),
        t.array(t.proxy(renames["reaction"])).optional(),
    )
    functions["reactions_create_for_issue"] = ghes.post(
        "/repos/{owner}/{repo}/issues/{issue_number}/reactions",
        t.struct(
            {
                "owner": t.string(),
                "repo": t.string(),
                "issue_number": t.integer(),
                "content": t.string(),
            }
        ),
        t.proxy(renames["reaction"]),
        content_type="application/json",
        body_fields=("content",),
    )
    functions["reactions_delete_for_issue"] = ghes.delete(
        "/repos/{owner}/{repo}/issues/{issue_number}/reactions/{reaction_id}",
        t.struct(
            {
                "owner": t.string(),
                "repo": t.string(),
                "issue_number": t.integer(),
                "reaction_id": t.integer(),
            }
        ),
        t.boolean(),
    )
    functions["issues_list_events_for_timeline"] = ghes.get(
        "/repos/{owner}/{repo}/issues/{issue_number}/timeline",
        t.struct(
            {
                "owner": t.string(),
                "repo": t.string(),
                "issue_number": t.integer(),
                "per_page": t.integer(),
                "page": t.integer(),
            }
        ),
        t.array(t.proxy(renames["timeline_issue_events"])).optional(),
    )
    functions["repos_list_deploy_keys"] = ghes.get(
        "/repos/{owner}/{repo}/keys",
        t.struct(
            {
                "owner": t.string(),
                "repo": t.string(),
                "per_page": t.integer(),
                "page": t.integer(),
            }
        ),
        t.array(t.proxy(renames["deploy_key"])),
    )
    functions["repos_create_deploy_key"] = ghes.post(
        "/repos/{owner}/{repo}/keys",
        t.struct(
            {
                "owner": t.string(),
                "repo": t.string(),
                "title": t.string().optional(),
                "key": t.string(),
                "read_only": t.boolean().optional(),
            }
        ),
        t.proxy(renames["deploy_key"]),
        content_type="application/json",
        body_fields=("title", "key", "read_only"),
    )
    functions["repos_get_deploy_key"] = ghes.get(
        "/repos/{owner}/{repo}/keys/{key_id}",
        t.struct({"owner": t.string(), "repo": t.string(), "key_id": t.integer()}),
        t.proxy(renames["deploy_key"]).optional(),
    )
    functions["repos_delete_deploy_key"] = ghes.delete(
        "/repos/{owner}/{repo}/keys/{key_id}",
        t.struct({"owner": t.string(), "repo": t.string(), "key_id": t.integer()}),
        t.boolean(),
    )
    functions["issues_list_labels_for_repo"] = ghes.get(
        "/repos/{owner}/{repo}/labels",
        t.struct(
            {
                "owner": t.string(),
                "repo": t.string(),
                "per_page": t.integer(),
                "page": t.integer(),
            }
        ),
        t.array(t.proxy(renames["label"])).optional(),
    )
    functions["issues_create_label"] = ghes.post(
        "/repos/{owner}/{repo}/labels",
        t.struct(
            {
                "owner": t.string(),
                "repo": t.string(),
                "name": t.string(),
                "color": t.string().optional(),
                "description": t.string().optional(),
            }
        ),
        t.proxy(renames["label"]).optional(),
        content_type="application/json",
        body_fields=("name", "color", "description"),
    )
    functions["issues_get_label"] = ghes.get(
        "/repos/{owner}/{repo}/labels/{name}",
        t.struct({"owner": t.string(), "repo": t.string(), "name": t.string()}),
        t.proxy(renames["label"]).optional(),
    )
    functions["issues_update_label"] = ghes.patch(
        "/repos/{owner}/{repo}/labels/{name}",
        t.struct(
            {
                "owner": t.string(),
                "repo": t.string(),
                "name": t.string(),
                "new_name": t.string().optional(),
                "color": t.string().optional(),
                "description": t.string().optional(),
            }
        ),
        t.proxy(renames["label"]),
        content_type="application/json",
        body_fields=("new_name", "color", "description"),
    )
    functions["issues_delete_label"] = ghes.delete(
        "/repos/{owner}/{repo}/labels/{name}",
        t.struct({"owner": t.string(), "repo": t.string(), "name": t.string()}),
        t.boolean(),
    )
    functions["repos_list_languages"] = ghes.get(
        "/repos/{owner}/{repo}/languages",
        t.struct({"owner": t.string(), "repo": t.string()}),
        t.proxy(renames["language"]),
    )
    functions["licenses_get_for_repo"] = ghes.get(
        "/repos/{owner}/{repo}/license",
        t.struct({"owner": t.string(), "repo": t.string()}),
        t.proxy(renames["license_content"]),
    )
    functions["repos_merge"] = ghes.post(
        "/repos/{owner}/{repo}/merges",
        t.struct(
            {
                "owner": t.string(),
                "repo": t.string(),
                "base": t.string(),
                "head": t.string(),
                "commit_message": t.string().optional(),
            }
        ),
        t.proxy(renames["commit"]).optional(),
        content_type="application/json",
        body_fields=("base", "head", "commit_message"),
    )
    functions["issues_list_milestones"] = ghes.get(
        "/repos/{owner}/{repo}/milestones",
        t.struct(
            {
                "owner": t.string(),
                "repo": t.string(),
                "state": t.string(),
                "sort": t.string(),
                "direction": t.string(),
                "per_page": t.integer(),
                "page": t.integer(),
            }
        ),
        t.array(t.proxy(renames["milestone"])).optional(),
    )
    functions["issues_create_milestone"] = ghes.post(
        "/repos/{owner}/{repo}/milestones",
        t.struct(
            {
                "owner": t.string(),
                "repo": t.string(),
                "title": t.string(),
                "state": t.string().optional(),
                "description": t.string().optional(),
                "due_on": t.string().optional(),
            }
        ),
        t.proxy(renames["milestone"]).optional(),
        content_type="application/json",
        body_fields=("title", "state", "description", "due_on"),
    )
    functions["issues_get_milestone"] = ghes.get(
        "/repos/{owner}/{repo}/milestones/{milestone_number}",
        t.struct(
            {"owner": t.string(), "repo": t.string(), "milestone_number": t.integer()}
        ),
        t.proxy(renames["milestone"]).optional(),
    )
    functions["issues_update_milestone"] = ghes.patch(
        "/repos/{owner}/{repo}/milestones/{milestone_number}",
        t.struct(
            {
                "owner": t.string(),
                "repo": t.string(),
                "milestone_number": t.integer(),
                "title": t.string().optional(),
                "state": t.string().optional(),
                "description": t.string().optional(),
                "due_on": t.string().optional(),
            }
        ),
        t.proxy(renames["milestone"]),
        content_type="application/json",
        body_fields=("title", "state", "description", "due_on"),
    )
    functions["issues_delete_milestone"] = ghes.delete(
        "/repos/{owner}/{repo}/milestones/{milestone_number}",
        t.struct(
            {"owner": t.string(), "repo": t.string(), "milestone_number": t.integer()}
        ),
        t.boolean().optional(),
    )
    functions["issues_list_labels_for_milestone"] = ghes.get(
        "/repos/{owner}/{repo}/milestones/{milestone_number}/labels",
        t.struct(
            {
                "owner": t.string(),
                "repo": t.string(),
                "milestone_number": t.integer(),
                "per_page": t.integer(),
                "page": t.integer(),
            }
        ),
        t.array(t.proxy(renames["label"])),
    )
    functions["activity_list_repo_notifications_for_authenticated_user"] = ghes.get(
        "/repos/{owner}/{repo}/notifications",
        t.struct(
            {
                "owner": t.string(),
                "repo": t.string(),
                "all": t.boolean(),
                "participating": t.boolean(),
                "since": t.string(),
                "before": t.string(),
                "per_page": t.integer(),
                "page": t.integer(),
            }
        ),
        t.array(t.proxy(renames["thread"])),
    )
    functions["activity_mark_repo_notifications_as_read"] = ghes.put(
        "/repos/{owner}/{repo}/notifications",
        t.struct(
            {
                "owner": t.string(),
                "repo": t.string(),
                "last_read_at": t.string().optional(),
            }
        ),
        t.struct({"message": t.string().optional(), "url": t.string().optional()}),
        content_type="application/json",
        body_fields=("last_read_at",),
    )
    functions["repos_get_pages"] = ghes.get(
        "/repos/{owner}/{repo}/pages",
        t.struct({"owner": t.string(), "repo": t.string()}),
        t.proxy(renames["page"]).optional(),
    )
    functions["repos_create_pages_site"] = ghes.post(
        "/repos/{owner}/{repo}/pages",
        t.struct(
            {
                "owner": t.string(),
                "repo": t.string(),
                "source": t.struct(
                    {"branch": t.string(), "path": t.string().optional()}
                ),
            }
        ),
        t.proxy(renames["page"]),
        content_type="application/json",
        body_fields=("source",),
    )
    functions["repos_delete_pages_site"] = ghes.delete(
        "/repos/{owner}/{repo}/pages",
        t.struct({"owner": t.string(), "repo": t.string()}),
        t.boolean().optional(),
    )
    functions["repos_list_pages_builds"] = ghes.get(
        "/repos/{owner}/{repo}/pages/builds",
        t.struct(
            {
                "owner": t.string(),
                "repo": t.string(),
                "per_page": t.integer(),
                "page": t.integer(),
            }
        ),
        t.array(t.proxy(renames["page_build"])),
    )
    functions["repos_request_pages_build"] = ghes.post(
        "/repos/{owner}/{repo}/pages/builds",
        t.struct({"owner": t.string(), "repo": t.string()}),
        t.proxy(renames["page_build_status"]),
    )
    functions["repos_get_latest_pages_build"] = ghes.get(
        "/repos/{owner}/{repo}/pages/builds/latest",
        t.struct({"owner": t.string(), "repo": t.string()}),
        t.proxy(renames["page_build"]),
    )
    functions["repos_get_pages_build"] = ghes.get(
        "/repos/{owner}/{repo}/pages/builds/{build_id}",
        t.struct({"owner": t.string(), "repo": t.string(), "build_id": t.integer()}),
        t.proxy(renames["page_build"]),
    )
    functions["enterprise_admin_list_pre_receive_hooks_for_repo"] = ghes.get(
        "/repos/{owner}/{repo}/pre-receive-hooks",
        t.struct(
            {
                "owner": t.string(),
                "repo": t.string(),
                "per_page": t.integer(),
                "page": t.integer(),
                "direction": t.string(),
                "sort": t.string(),
            }
        ),
        t.array(t.proxy(renames["repository_pre_receive_hook"])),
    )
    functions["enterprise_admin_get_pre_receive_hook_for_repo"] = ghes.get(
        "/repos/{owner}/{repo}/pre-receive-hooks/{pre_receive_hook_id}",
        t.struct(
            {
                "owner": t.string(),
                "repo": t.string(),
                "pre_receive_hook_id": t.integer(),
            }
        ),
        t.proxy(renames["repository_pre_receive_hook"]),
    )
    functions[
        "enterprise_admin_update_pre_receive_hook_enforcement_for_repo"
    ] = ghes.patch(
        "/repos/{owner}/{repo}/pre-receive-hooks/{pre_receive_hook_id}",
        t.struct(
            {
                "owner": t.string(),
                "repo": t.string(),
                "pre_receive_hook_id": t.integer(),
                "enforcement": t.string().optional(),
            }
        ),
        t.proxy(renames["repository_pre_receive_hook"]),
        content_type="application/json",
        body_fields=("enforcement",),
    )
    functions[
        "enterprise_admin_remove_pre_receive_hook_enforcement_for_repo"
    ] = ghes.delete(
        "/repos/{owner}/{repo}/pre-receive-hooks/{pre_receive_hook_id}",
        t.struct(
            {
                "owner": t.string(),
                "repo": t.string(),
                "pre_receive_hook_id": t.integer(),
            }
        ),
        t.proxy(renames["repository_pre_receive_hook"]),
    )
    functions["projects_list_for_repo"] = ghes.get(
        "/repos/{owner}/{repo}/projects",
        t.struct(
            {
                "owner": t.string(),
                "repo": t.string(),
                "state": t.string(),
                "per_page": t.integer(),
                "page": t.integer(),
            }
        ),
        t.array(t.proxy(renames["project"])).optional(),
    )
    functions["projects_create_for_repo"] = ghes.post(
        "/repos/{owner}/{repo}/projects",
        t.struct(
            {
                "owner": t.string(),
                "repo": t.string(),
                "name": t.string(),
                "body": t.string().optional(),
            }
        ),
        t.proxy(renames["project"]).optional(),
        content_type="application/json",
        body_fields=("name", "body"),
    )
    functions["pulls_list"] = ghes.get(
        "/repos/{owner}/{repo}/pulls",
        t.struct(
            {
                "owner": t.string(),
                "repo": t.string(),
                "state": t.string(),
                "head": t.string(),
                "base": t.string(),
                "sort": t.string(),
                "direction": t.string(),
                "per_page": t.integer(),
                "page": t.integer(),
            }
        ),
        t.array(t.proxy(renames["pull_request_simple"])),
    )
    functions["pulls_create"] = ghes.post(
        "/repos/{owner}/{repo}/pulls",
        t.struct(
            {
                "owner": t.string(),
                "repo": t.string(),
                "title": t.string().optional(),
                "head": t.string(),
                "base": t.string(),
                "body": t.string().optional(),
                "maintainer_can_modify": t.boolean().optional(),
                "draft": t.boolean().optional(),
                "issue": t.integer().optional(),
            }
        ),
        t.proxy(renames["pull_request"]),
        content_type="application/json",
        body_fields=(
            "title",
            "head",
            "base",
            "body",
            "maintainer_can_modify",
            "draft",
            "issue",
        ),
    )
    functions["pulls_list_review_comments_for_repo"] = ghes.get(
        "/repos/{owner}/{repo}/pulls/comments",
        t.struct(
            {
                "owner": t.string(),
                "repo": t.string(),
                "sort": t.string(),
                "direction": t.string(),
                "since": t.string(),
                "per_page": t.integer(),
                "page": t.integer(),
            }
        ),
        t.array(t.proxy(renames["pull_request_review_comment"])),
    )
    functions["pulls_get_review_comment"] = ghes.get(
        "/repos/{owner}/{repo}/pulls/comments/{comment_id}",
        t.struct({"owner": t.string(), "repo": t.string(), "comment_id": t.integer()}),
        t.proxy(renames["pull_request_review_comment"]).optional(),
    )
    functions["pulls_update_review_comment"] = ghes.patch(
        "/repos/{owner}/{repo}/pulls/comments/{comment_id}",
        t.struct(
            {
                "owner": t.string(),
                "repo": t.string(),
                "comment_id": t.integer(),
                "body": t.string(),
            }
        ),
        t.proxy(renames["pull_request_review_comment"]),
        content_type="application/json",
        body_fields=("body",),
    )
    functions["pulls_delete_review_comment"] = ghes.delete(
        "/repos/{owner}/{repo}/pulls/comments/{comment_id}",
        t.struct({"owner": t.string(), "repo": t.string(), "comment_id": t.integer()}),
        t.boolean().optional(),
    )
    functions["reactions_list_for_pull_request_review_comment"] = ghes.get(
        "/repos/{owner}/{repo}/pulls/comments/{comment_id}/reactions",
        t.struct(
            {
                "owner": t.string(),
                "repo": t.string(),
                "comment_id": t.integer(),
                "content": t.string(),
                "per_page": t.integer(),
                "page": t.integer(),
            }
        ),
        t.array(t.proxy(renames["reaction"])).optional(),
    )
    functions["reactions_create_for_pull_request_review_comment"] = ghes.post(
        "/repos/{owner}/{repo}/pulls/comments/{comment_id}/reactions",
        t.struct(
            {
                "owner": t.string(),
                "repo": t.string(),
                "comment_id": t.integer(),
                "content": t.string(),
            }
        ),
        t.proxy(renames["reaction"]),
        content_type="application/json",
        body_fields=("content",),
    )
    functions["reactions_delete_for_pull_request_comment"] = ghes.delete(
        "/repos/{owner}/{repo}/pulls/comments/{comment_id}/reactions/{reaction_id}",
        t.struct(
            {
                "owner": t.string(),
                "repo": t.string(),
                "comment_id": t.integer(),
                "reaction_id": t.integer(),
            }
        ),
        t.boolean(),
    )
    functions["pulls_get"] = ghes.get(
        "/repos/{owner}/{repo}/pulls/{pull_number}",
        t.struct({"owner": t.string(), "repo": t.string(), "pull_number": t.integer()}),
        t.proxy(renames["pull_request"]).optional(),
    )
    functions["pulls_update"] = ghes.patch(
        "/repos/{owner}/{repo}/pulls/{pull_number}",
        t.struct(
            {
                "owner": t.string(),
                "repo": t.string(),
                "pull_number": t.integer(),
                "title": t.string().optional(),
                "body": t.string().optional(),
                "state": t.string().optional(),
                "base": t.string().optional(),
                "maintainer_can_modify": t.boolean().optional(),
            }
        ),
        t.proxy(renames["pull_request"]),
        content_type="application/json",
        body_fields=("title", "body", "state", "base", "maintainer_can_modify"),
    )
    functions["pulls_list_review_comments"] = ghes.get(
        "/repos/{owner}/{repo}/pulls/{pull_number}/comments",
        t.struct(
            {
                "owner": t.string(),
                "repo": t.string(),
                "pull_number": t.integer(),
                "sort": t.string(),
                "direction": t.string(),
                "since": t.string(),
                "per_page": t.integer(),
                "page": t.integer(),
            }
        ),
        t.array(t.proxy(renames["pull_request_review_comment"])),
    )
    functions["pulls_create_review_comment"] = ghes.post(
        "/repos/{owner}/{repo}/pulls/{pull_number}/comments",
        t.struct(
            {
                "owner": t.string(),
                "repo": t.string(),
                "pull_number": t.integer(),
                "body": t.string(),
                "commit_id": t.string().optional(),
                "path": t.string().optional(),
                "position": t.integer().optional(),
                "side": t.string().optional(),
                "line": t.integer().optional(),
                "start_line": t.integer().optional(),
                "start_side": t.string().optional(),
                "in_reply_to": t.integer().optional(),
            }
        ),
        t.proxy(renames["pull_request_review_comment"]),
        content_type="application/json",
        body_fields=(
            "body",
            "commit_id",
            "path",
            "position",
            "side",
            "line",
            "start_line",
            "start_side",
            "in_reply_to",
        ),
    )
    functions["pulls_create_reply_for_review_comment"] = ghes.post(
        "/repos/{owner}/{repo}/pulls/{pull_number}/comments/{comment_id}/replies",
        t.struct(
            {
                "owner": t.string(),
                "repo": t.string(),
                "pull_number": t.integer(),
                "comment_id": t.integer(),
                "body": t.string(),
            }
        ),
        t.proxy(renames["pull_request_review_comment"]).optional(),
        content_type="application/json",
        body_fields=("body",),
    )
    functions["pulls_list_commits"] = ghes.get(
        "/repos/{owner}/{repo}/pulls/{pull_number}/commits",
        t.struct(
            {
                "owner": t.string(),
                "repo": t.string(),
                "pull_number": t.integer(),
                "per_page": t.integer(),
                "page": t.integer(),
            }
        ),
        t.array(t.proxy(renames["commit"])),
    )
    functions["pulls_list_files"] = ghes.get(
        "/repos/{owner}/{repo}/pulls/{pull_number}/files",
        t.struct(
            {
                "owner": t.string(),
                "repo": t.string(),
                "pull_number": t.integer(),
                "per_page": t.integer(),
                "page": t.integer(),
            }
        ),
        t.array(t.proxy(renames["diff_entry"])),
    )
    functions["pulls_check_if_merged"] = ghes.get(
        "/repos/{owner}/{repo}/pulls/{pull_number}/merge",
        t.struct({"owner": t.string(), "repo": t.string(), "pull_number": t.integer()}),
        t.boolean().optional(),
    )
    functions["pulls_merge"] = ghes.put(
        "/repos/{owner}/{repo}/pulls/{pull_number}/merge",
        t.struct(
            {
                "owner": t.string(),
                "repo": t.string(),
                "pull_number": t.integer(),
                "commit_title": t.string().optional(),
                "commit_message": t.string().optional(),
                "sha": t.string().optional(),
                "merge_method": t.string().optional(),
            }
        ),
        t.proxy(renames["pull_request_merge_result"]).optional(),
        content_type="application/json",
        body_fields=("commit_title", "commit_message", "sha", "merge_method"),
    )
    functions["pulls_list_requested_reviewers"] = ghes.get(
        "/repos/{owner}/{repo}/pulls/{pull_number}/requested_reviewers",
        t.struct(
            {
                "owner": t.string(),
                "repo": t.string(),
                "pull_number": t.integer(),
                "per_page": t.integer(),
                "page": t.integer(),
            }
        ),
        t.proxy(renames["pull_request_review_request"]),
    )
    functions["pulls_remove_requested_reviewers"] = ghes.delete(
        "/repos/{owner}/{repo}/pulls/{pull_number}/requested_reviewers",
        t.struct(
            {
                "owner": t.string(),
                "repo": t.string(),
                "pull_number": t.integer(),
                "reviewers": t.array(t.string()),
                "team_reviewers": t.array(t.string()).optional(),
            }
        ),
        t.proxy(renames["pull_request_simple"]),
        content_type="application/json",
        body_fields=("reviewers", "team_reviewers"),
    )
    functions["pulls_list_reviews"] = ghes.get(
        "/repos/{owner}/{repo}/pulls/{pull_number}/reviews",
        t.struct(
            {
                "owner": t.string(),
                "repo": t.string(),
                "pull_number": t.integer(),
                "per_page": t.integer(),
                "page": t.integer(),
            }
        ),
        t.array(t.proxy(renames["pull_request_review"])),
    )
    functions["pulls_create_review"] = ghes.post(
        "/repos/{owner}/{repo}/pulls/{pull_number}/reviews",
        t.struct(
            {
                "owner": t.string(),
                "repo": t.string(),
                "pull_number": t.integer(),
                "commit_id": t.string().optional(),
                "body": t.string().optional(),
                "event": t.string().optional(),
                "comments": t.array(
                    t.struct(
                        {
                            "path": t.string(),
                            "position": t.integer().optional(),
                            "body": t.string(),
                            "line": t.integer().optional(),
                            "side": t.string().optional(),
                            "start_line": t.integer().optional(),
                            "start_side": t.string().optional(),
                        }
                    )
                ).optional(),
            }
        ),
        t.proxy(renames["pull_request_review"]),
        content_type="application/json",
        body_fields=("commit_id", "body", "event", "comments"),
    )
    functions["pulls_get_review"] = ghes.get(
        "/repos/{owner}/{repo}/pulls/{pull_number}/reviews/{review_id}",
        t.struct(
            {
                "owner": t.string(),
                "repo": t.string(),
                "pull_number": t.integer(),
                "review_id": t.integer(),
            }
        ),
        t.proxy(renames["pull_request_review"]).optional(),
    )
    functions["pulls_update_review"] = ghes.put(
        "/repos/{owner}/{repo}/pulls/{pull_number}/reviews/{review_id}",
        t.struct(
            {
                "owner": t.string(),
                "repo": t.string(),
                "pull_number": t.integer(),
                "review_id": t.integer(),
                "body": t.string(),
            }
        ),
        t.proxy(renames["pull_request_review"]),
        content_type="application/json",
        body_fields=("body",),
    )
    functions["pulls_delete_pending_review"] = ghes.delete(
        "/repos/{owner}/{repo}/pulls/{pull_number}/reviews/{review_id}",
        t.struct(
            {
                "owner": t.string(),
                "repo": t.string(),
                "pull_number": t.integer(),
                "review_id": t.integer(),
            }
        ),
        t.proxy(renames["pull_request_review"]).optional(),
    )
    functions["pulls_list_comments_for_review"] = ghes.get(
        "/repos/{owner}/{repo}/pulls/{pull_number}/reviews/{review_id}/comments",
        t.struct(
            {
                "owner": t.string(),
                "repo": t.string(),
                "pull_number": t.integer(),
                "review_id": t.integer(),
                "per_page": t.integer(),
                "page": t.integer(),
            }
        ),
        t.array(t.proxy(renames["review_comment"])).optional(),
    )
    functions["pulls_dismiss_review"] = ghes.put(
        "/repos/{owner}/{repo}/pulls/{pull_number}/reviews/{review_id}/dismissals",
        t.struct(
            {
                "owner": t.string(),
                "repo": t.string(),
                "pull_number": t.integer(),
                "review_id": t.integer(),
                "message": t.string(),
                "event": t.string().optional(),
            }
        ),
        t.proxy(renames["pull_request_review"]).optional(),
        content_type="application/json",
        body_fields=("message", "event"),
    )
    functions["pulls_submit_review"] = ghes.post(
        "/repos/{owner}/{repo}/pulls/{pull_number}/reviews/{review_id}/events",
        t.struct(
            {
                "owner": t.string(),
                "repo": t.string(),
                "pull_number": t.integer(),
                "review_id": t.integer(),
                "body": t.string().optional(),
                "event": t.string(),
            }
        ),
        t.proxy(renames["pull_request_review"]).optional(),
        content_type="application/json",
        body_fields=("body", "event"),
    )
    functions["pulls_update_branch"] = ghes.put(
        "/repos/{owner}/{repo}/pulls/{pull_number}/update-branch",
        t.struct(
            {
                "owner": t.string(),
                "repo": t.string(),
                "pull_number": t.integer(),
                "expected_head_sha": t.string().optional(),
            }
        ),
        t.struct({"message": t.string().optional(), "url": t.string().optional()}),
        content_type="application/json",
        body_fields=("expected_head_sha",),
    )
    functions["repos_get_readme"] = ghes.get(
        "/repos/{owner}/{repo}/readme",
        t.struct({"owner": t.string(), "repo": t.string(), "ref": t.string()}),
        t.proxy(renames["content_file"]).optional(),
    )
    functions["repos_get_readme_in_directory"] = ghes.get(
        "/repos/{owner}/{repo}/readme/{dir}",
        t.struct(
            {
                "owner": t.string(),
                "repo": t.string(),
                "dir": t.string(),
                "ref": t.string(),
            }
        ),
        t.proxy(renames["content_file"]).optional(),
    )
    functions["repos_list_releases"] = ghes.get(
        "/repos/{owner}/{repo}/releases",
        t.struct(
            {
                "owner": t.string(),
                "repo": t.string(),
                "per_page": t.integer(),
                "page": t.integer(),
            }
        ),
        t.array(t.proxy(renames["release"])).optional(),
    )
    functions["repos_create_release"] = ghes.post(
        "/repos/{owner}/{repo}/releases",
        t.struct(
            {
                "owner": t.string(),
                "repo": t.string(),
                "tag_name": t.string(),
                "target_commitish": t.string().optional(),
                "name": t.string().optional(),
                "body": t.string().optional(),
                "draft": t.boolean().optional(),
                "prerelease": t.boolean().optional(),
            }
        ),
        t.proxy(renames["release"]),
        content_type="application/json",
        body_fields=(
            "tag_name",
            "target_commitish",
            "name",
            "body",
            "draft",
            "prerelease",
        ),
    )
    functions["repos_get_release_asset"] = ghes.get(
        "/repos/{owner}/{repo}/releases/assets/{asset_id}",
        t.struct({"owner": t.string(), "repo": t.string(), "asset_id": t.integer()}),
        t.proxy(renames["release_asset"]).optional(),
    )
    functions["repos_update_release_asset"] = ghes.patch(
        "/repos/{owner}/{repo}/releases/assets/{asset_id}",
        t.struct(
            {
                "owner": t.string(),
                "repo": t.string(),
                "asset_id": t.integer(),
                "name": t.string().optional(),
                "label": t.string().optional(),
                "state": t.string().optional(),
            }
        ),
        t.proxy(renames["release_asset"]),
        content_type="application/json",
        body_fields=("name", "label", "state"),
    )
    functions["repos_delete_release_asset"] = ghes.delete(
        "/repos/{owner}/{repo}/releases/assets/{asset_id}",
        t.struct({"owner": t.string(), "repo": t.string(), "asset_id": t.integer()}),
        t.boolean(),
    )
    functions["repos_get_latest_release"] = ghes.get(
        "/repos/{owner}/{repo}/releases/latest",
        t.struct({"owner": t.string(), "repo": t.string()}),
        t.proxy(renames["release"]),
    )
    functions["repos_get_release_by_tag"] = ghes.get(
        "/repos/{owner}/{repo}/releases/tags/{tag}",
        t.struct({"owner": t.string(), "repo": t.string(), "tag": t.string()}),
        t.proxy(renames["release"]).optional(),
    )
    functions["repos_get_release"] = ghes.get(
        "/repos/{owner}/{repo}/releases/{release_id}",
        t.struct({"owner": t.string(), "repo": t.string(), "release_id": t.integer()}),
        t.proxy(renames["release"]).optional(),
    )
    functions["repos_update_release"] = ghes.patch(
        "/repos/{owner}/{repo}/releases/{release_id}",
        t.struct(
            {
                "owner": t.string(),
                "repo": t.string(),
                "release_id": t.integer(),
                "tag_name": t.string().optional(),
                "target_commitish": t.string().optional(),
                "name": t.string().optional(),
                "body": t.string().optional(),
                "draft": t.boolean().optional(),
                "prerelease": t.boolean().optional(),
            }
        ),
        t.proxy(renames["release"]),
        content_type="application/json",
        body_fields=(
            "tag_name",
            "target_commitish",
            "name",
            "body",
            "draft",
            "prerelease",
        ),
    )
    functions["repos_delete_release"] = ghes.delete(
        "/repos/{owner}/{repo}/releases/{release_id}",
        t.struct({"owner": t.string(), "repo": t.string(), "release_id": t.integer()}),
        t.boolean(),
    )
    functions["repos_list_release_assets"] = ghes.get(
        "/repos/{owner}/{repo}/releases/{release_id}/assets",
        t.struct(
            {
                "owner": t.string(),
                "repo": t.string(),
                "release_id": t.integer(),
                "per_page": t.integer(),
                "page": t.integer(),
            }
        ),
        t.array(t.proxy(renames["release_asset"])),
    )
    functions["activity_list_stargazers_for_repo"] = ghes.get(
        "/repos/{owner}/{repo}/stargazers",
        t.struct(
            {
                "owner": t.string(),
                "repo": t.string(),
                "per_page": t.integer(),
                "page": t.integer(),
            }
        ),
        t.union(
            [
                t.array(t.proxy(renames["simple_user"])),
                t.array(t.proxy(renames["stargazer"])),
            ]
        ),
    )
    functions["repos_get_code_frequency_stats"] = ghes.get(
        "/repos/{owner}/{repo}/stats/code_frequency",
        t.struct({"owner": t.string(), "repo": t.string()}),
        t.array(t.proxy(renames["code_frequency_stat"])),
    )
    functions["repos_get_commit_activity_stats"] = ghes.get(
        "/repos/{owner}/{repo}/stats/commit_activity",
        t.struct({"owner": t.string(), "repo": t.string()}),
        t.array(t.proxy(renames["commit_activity"])),
    )
    functions["repos_get_contributors_stats"] = ghes.get(
        "/repos/{owner}/{repo}/stats/contributors",
        t.struct({"owner": t.string(), "repo": t.string()}),
        t.array(t.proxy(renames["contributor_activity"])),
    )
    functions["repos_get_participation_stats"] = ghes.get(
        "/repos/{owner}/{repo}/stats/participation",
        t.struct({"owner": t.string(), "repo": t.string()}),
        t.proxy(renames["participation_stats"]).optional(),
    )
    functions["repos_get_punch_card_stats"] = ghes.get(
        "/repos/{owner}/{repo}/stats/punch_card",
        t.struct({"owner": t.string(), "repo": t.string()}),
        t.array(t.proxy(renames["code_frequency_stat"])),
    )
    functions["repos_create_commit_status"] = ghes.post(
        "/repos/{owner}/{repo}/statuses/{sha}",
        t.struct(
            {
                "owner": t.string(),
                "repo": t.string(),
                "sha": t.string(),
                "state": t.string(),
                "target_url": t.string().optional(),
                "description": t.string().optional(),
                "context": t.string().optional(),
            }
        ),
        t.proxy(renames["status"]),
        content_type="application/json",
        body_fields=("state", "target_url", "description", "context"),
    )
    functions["activity_list_watchers_for_repo"] = ghes.get(
        "/repos/{owner}/{repo}/subscribers",
        t.struct(
            {
                "owner": t.string(),
                "repo": t.string(),
                "per_page": t.integer(),
                "page": t.integer(),
            }
        ),
        t.array(t.proxy(renames["simple_user"])),
    )
    functions["activity_get_repo_subscription"] = ghes.get(
        "/repos/{owner}/{repo}/subscription",
        t.struct({"owner": t.string(), "repo": t.string()}),
        t.proxy(renames["repository_subscription"]).optional(),
    )
    functions["activity_set_repo_subscription"] = ghes.put(
        "/repos/{owner}/{repo}/subscription",
        t.struct(
            {
                "owner": t.string(),
                "repo": t.string(),
                "subscribed": t.boolean().optional(),
                "ignored": t.boolean().optional(),
            }
        ),
        t.proxy(renames["repository_subscription"]),
        content_type="application/json",
        body_fields=("subscribed", "ignored"),
    )
    functions["activity_delete_repo_subscription"] = ghes.delete(
        "/repos/{owner}/{repo}/subscription",
        t.struct({"owner": t.string(), "repo": t.string()}),
        t.boolean(),
    )
    functions["repos_list_tags"] = ghes.get(
        "/repos/{owner}/{repo}/tags",
        t.struct(
            {
                "owner": t.string(),
                "repo": t.string(),
                "per_page": t.integer(),
                "page": t.integer(),
            }
        ),
        t.array(t.proxy(renames["tag"])),
    )
    functions["repos_download_tarball_archive"] = ghes.get(
        "/repos/{owner}/{repo}/tarball/{ref}",
        t.struct({"owner": t.string(), "repo": t.string(), "ref": t.string()}),
        t.struct({}),
    )
    functions["repos_list_teams"] = ghes.get(
        "/repos/{owner}/{repo}/teams",
        t.struct(
            {
                "owner": t.string(),
                "repo": t.string(),
                "per_page": t.integer(),
                "page": t.integer(),
            }
        ),
        t.array(t.proxy(renames["team"])),
    )
    functions["repos_get_all_topics"] = ghes.get(
        "/repos/{owner}/{repo}/topics",
        t.struct(
            {
                "owner": t.string(),
                "repo": t.string(),
                "page": t.integer(),
                "per_page": t.integer(),
            }
        ),
        t.proxy(renames["topic"]).optional(),
    )
    functions["repos_replace_all_topics"] = ghes.put(
        "/repos/{owner}/{repo}/topics",
        t.struct(
            {"owner": t.string(), "repo": t.string(), "names": t.array(t.string())}
        ),
        t.proxy(renames["topic"]).optional(),
        content_type="application/json",
        body_fields=("names",),
    )
    functions["repos_transfer"] = ghes.post(
        "/repos/{owner}/{repo}/transfer",
        t.struct(
            {
                "owner": t.string(),
                "repo": t.string(),
                "new_owner": t.string(),
                "team_ids": t.array(t.integer()).optional(),
            }
        ),
        t.proxy(renames["minimal_repository"]),
        content_type="application/json",
        body_fields=("new_owner", "team_ids"),
    )
    functions["repos_download_zipball_archive"] = ghes.get(
        "/repos/{owner}/{repo}/zipball/{ref}",
        t.struct({"owner": t.string(), "repo": t.string(), "ref": t.string()}),
        t.struct({}),
    )
    functions["repos_create_using_template"] = ghes.post(
        "/repos/{template_owner}/{template_repo}/generate",
        t.struct(
            {
                "template_owner": t.string(),
                "template_repo": t.string(),
                "owner": t.string().optional(),
                "name": t.string(),
                "description": t.string().optional(),
                "include_all_branches": t.boolean().optional(),
                "private": t.boolean().optional(),
            }
        ),
        t.proxy(renames["repository"]),
        content_type="application/json",
        body_fields=("owner", "name", "description", "include_all_branches", "private"),
    )
    functions["repos_list_public"] = ghes.get(
        "/repositories",
        t.struct({"since": t.integer(), "visibility": t.string()}),
        t.array(t.proxy(renames["minimal_repository"])),
    )
    functions["search_code"] = ghes.get(
        "/search/code",
        t.struct(
            {
                "q": t.string(),
                "sort": t.string(),
                "order": t.string(),
                "per_page": t.integer(),
                "page": t.integer(),
            }
        ),
        t.struct(
            {
                "total_count": t.integer(),
                "incomplete_results": t.boolean(),
                "items": t.array(t.proxy(renames["code_search_result_item"])),
            }
        ),
    )
    functions["search_commits"] = ghes.get(
        "/search/commits",
        t.struct(
            {
                "q": t.string(),
                "sort": t.string(),
                "order": t.string(),
                "per_page": t.integer(),
                "page": t.integer(),
            }
        ),
        t.struct(
            {
                "total_count": t.integer(),
                "incomplete_results": t.boolean(),
                "items": t.array(t.proxy(renames["commit_search_result_item"])),
            }
        ),
    )
    functions["search_issues_and_pull_requests"] = ghes.get(
        "/search/issues",
        t.struct(
            {
                "q": t.string(),
                "sort": t.string(),
                "order": t.string(),
                "per_page": t.integer(),
                "page": t.integer(),
            }
        ),
        t.struct(
            {
                "total_count": t.integer(),
                "incomplete_results": t.boolean(),
                "items": t.array(t.proxy(renames["issue_search_result_item"])),
            }
        ),
    )
    functions["search_labels"] = ghes.get(
        "/search/labels",
        t.struct(
            {
                "repository_id": t.integer(),
                "q": t.string(),
                "sort": t.string(),
                "order": t.string(),
                "per_page": t.integer(),
                "page": t.integer(),
            }
        ),
        t.struct(
            {
                "total_count": t.integer(),
                "incomplete_results": t.boolean(),
                "items": t.array(t.proxy(renames["label_search_result_item"])),
            }
        ).optional(),
    )
    functions["search_repos"] = ghes.get(
        "/search/repositories",
        t.struct(
            {
                "q": t.string(),
                "sort": t.string(),
                "order": t.string(),
                "per_page": t.integer(),
                "page": t.integer(),
            }
        ),
        t.struct(
            {
                "total_count": t.integer(),
                "incomplete_results": t.boolean(),
                "items": t.array(t.proxy(renames["repo_search_result_item"])),
            }
        ),
    )
    functions["search_topics"] = ghes.get(
        "/search/topics",
        t.struct({"q": t.string(), "per_page": t.integer(), "page": t.integer()}),
        t.struct(
            {
                "total_count": t.integer(),
                "incomplete_results": t.boolean(),
                "items": t.array(t.proxy(renames["topic_search_result_item"])),
            }
        ),
    )
    functions["search_users"] = ghes.get(
        "/search/users",
        t.struct(
            {
                "q": t.string(),
                "sort": t.string(),
                "order": t.string(),
                "per_page": t.integer(),
                "page": t.integer(),
            }
        ),
        t.struct(
            {
                "total_count": t.integer(),
                "incomplete_results": t.boolean(),
                "items": t.array(t.proxy(renames["user_search_result_item"])),
            }
        ),
    )
    functions["enterprise_admin_get_configuration_status"] = ghes.get(
        "/setup/api/configcheck",
        t.struct({}),
        t.proxy(renames["configuration_status"]),
    )
    functions["enterprise_admin_start_configuration_process"] = ghes.post(
        "/setup/api/configure",
        t.struct({}),
        t.struct({}),
    )
    functions["enterprise_admin_get_maintenance_status"] = ghes.get(
        "/setup/api/maintenance",
        t.struct({}),
        t.proxy(renames["maintenance_status"]),
    )
    functions["enterprise_admin_enable_or_disable_maintenance_mode"] = ghes.post(
        "/setup/api/maintenance",
        t.struct({"maintenance": t.string()}),
        t.proxy(renames["maintenance_status"]),
        content_type="application/x-www-form-urlencoded",
        body_fields=("maintenance",),
    )
    functions["enterprise_admin_get_settings"] = ghes.get(
        "/setup/api/settings",
        t.struct({}),
        t.proxy(renames["enterprise_settings"]),
    )
    functions["enterprise_admin_set_settings"] = ghes.put(
        "/setup/api/settings",
        t.struct({"settings": t.string()}),
        t.boolean(),
        content_type="application/x-www-form-urlencoded",
        body_fields=("settings",),
    )
    functions["enterprise_admin_get_all_authorized_ssh_keys"] = ghes.get(
        "/setup/api/settings/authorized-keys",
        t.struct({}),
        t.array(t.proxy(renames["ssh_key"])),
    )
    functions["enterprise_admin_add_authorized_ssh_key"] = ghes.post(
        "/setup/api/settings/authorized-keys",
        t.struct({"authorized_key": t.string()}),
        t.array(t.proxy(renames["ssh_key"])),
        content_type="application/x-www-form-urlencoded",
        body_fields=("authorized_key",),
    )
    functions["enterprise_admin_remove_authorized_ssh_key"] = ghes.delete(
        "/setup/api/settings/authorized-keys",
        t.struct({"authorized_key": t.string()}),
        t.array(t.proxy(renames["ssh_key"])),
        content_type="application/x-www-form-urlencoded",
        body_fields=("authorized_key",),
    )
    functions["enterprise_admin_create_enterprise_server_license"] = ghes.post(
        "/setup/api/start",
        t.struct(
            {
                "license": t.string(),
                "password": t.string().optional(),
                "settings": t.string().optional(),
            }
        ),
        t.struct({}),
        content_type="application/x-www-form-urlencoded",
        body_fields=("license", "password", "settings"),
    )
    functions["enterprise_admin_upgrade_license"] = ghes.post(
        "/setup/api/upgrade",
        t.struct({"license": t.string().optional()}),
        t.struct({}),
        content_type="application/x-www-form-urlencoded",
        body_fields=("license",),
    )
    functions["teams_get_legacy"] = ghes.get(
        "/teams/{team_id}",
        t.struct({"team_id": t.integer()}),
        t.proxy(renames["team_full"]).optional(),
    )
    functions["teams_update_legacy"] = ghes.patch(
        "/teams/{team_id}",
        t.struct(
            {
                "team_id": t.integer(),
                "name": t.string(),
                "description": t.string().optional(),
                "privacy": t.string().optional(),
                "permission": t.string().optional(),
                "parent_team_id": t.integer().optional(),
            }
        ),
        t.proxy(renames["team_full"]).optional(),
        content_type="application/json",
        body_fields=("name", "description", "privacy", "permission", "parent_team_id"),
    )
    functions["teams_delete_legacy"] = ghes.delete(
        "/teams/{team_id}",
        t.struct({"team_id": t.integer()}),
        t.boolean().optional(),
    )
    functions["teams_list_discussions_legacy"] = ghes.get(
        "/teams/{team_id}/discussions",
        t.struct(
            {
                "team_id": t.integer(),
                "direction": t.string(),
                "per_page": t.integer(),
                "page": t.integer(),
            }
        ),
        t.array(t.proxy(renames["team_discussion"])),
    )
    functions["teams_create_discussion_legacy"] = ghes.post(
        "/teams/{team_id}/discussions",
        t.struct(
            {
                "team_id": t.integer(),
                "title": t.string(),
                "body": t.string(),
                "private": t.boolean().optional(),
            }
        ),
        t.proxy(renames["team_discussion"]),
        content_type="application/json",
        body_fields=("title", "body", "private"),
    )
    functions["teams_get_discussion_legacy"] = ghes.get(
        "/teams/{team_id}/discussions/{discussion_number}",
        t.struct({"team_id": t.integer(), "discussion_number": t.integer()}),
        t.proxy(renames["team_discussion"]),
    )
    functions["teams_update_discussion_legacy"] = ghes.patch(
        "/teams/{team_id}/discussions/{discussion_number}",
        t.struct(
            {
                "team_id": t.integer(),
                "discussion_number": t.integer(),
                "title": t.string().optional(),
                "body": t.string().optional(),
            }
        ),
        t.proxy(renames["team_discussion"]),
        content_type="application/json",
        body_fields=("title", "body"),
    )
    functions["teams_delete_discussion_legacy"] = ghes.delete(
        "/teams/{team_id}/discussions/{discussion_number}",
        t.struct({"team_id": t.integer(), "discussion_number": t.integer()}),
        t.boolean(),
    )
    functions["teams_list_discussion_comments_legacy"] = ghes.get(
        "/teams/{team_id}/discussions/{discussion_number}/comments",
        t.struct(
            {
                "team_id": t.integer(),
                "discussion_number": t.integer(),
                "direction": t.string(),
                "per_page": t.integer(),
                "page": t.integer(),
            }
        ),
        t.array(t.proxy(renames["team_discussion_comment"])),
    )
    functions["teams_create_discussion_comment_legacy"] = ghes.post(
        "/teams/{team_id}/discussions/{discussion_number}/comments",
        t.struct(
            {
                "team_id": t.integer(),
                "discussion_number": t.integer(),
                "body": t.string(),
            }
        ),
        t.proxy(renames["team_discussion_comment"]),
        content_type="application/json",
        body_fields=("body",),
    )
    functions["teams_get_discussion_comment_legacy"] = ghes.get(
        "/teams/{team_id}/discussions/{discussion_number}/comments/{comment_number}",
        t.struct(
            {
                "team_id": t.integer(),
                "discussion_number": t.integer(),
                "comment_number": t.integer(),
            }
        ),
        t.proxy(renames["team_discussion_comment"]),
    )
    functions["teams_update_discussion_comment_legacy"] = ghes.patch(
        "/teams/{team_id}/discussions/{discussion_number}/comments/{comment_number}",
        t.struct(
            {
                "team_id": t.integer(),
                "discussion_number": t.integer(),
                "comment_number": t.integer(),
                "body": t.string(),
            }
        ),
        t.proxy(renames["team_discussion_comment"]),
        content_type="application/json",
        body_fields=("body",),
    )
    functions["teams_delete_discussion_comment_legacy"] = ghes.delete(
        "/teams/{team_id}/discussions/{discussion_number}/comments/{comment_number}",
        t.struct(
            {
                "team_id": t.integer(),
                "discussion_number": t.integer(),
                "comment_number": t.integer(),
            }
        ),
        t.boolean(),
    )
    functions["reactions_list_for_team_discussion_comment_legacy"] = ghes.get(
        "/teams/{team_id}/discussions/{discussion_number}/comments/{comment_number}/reactions",
        t.struct(
            {
                "team_id": t.integer(),
                "discussion_number": t.integer(),
                "comment_number": t.integer(),
                "content": t.string(),
                "per_page": t.integer(),
                "page": t.integer(),
            }
        ),
        t.array(t.proxy(renames["reaction"])),
    )
    functions["reactions_create_for_team_discussion_comment_legacy"] = ghes.post(
        "/teams/{team_id}/discussions/{discussion_number}/comments/{comment_number}/reactions",
        t.struct(
            {
                "team_id": t.integer(),
                "discussion_number": t.integer(),
                "comment_number": t.integer(),
                "content": t.string(),
            }
        ),
        t.proxy(renames["reaction"]),
        content_type="application/json",
        body_fields=("content",),
    )
    functions["reactions_list_for_team_discussion_legacy"] = ghes.get(
        "/teams/{team_id}/discussions/{discussion_number}/reactions",
        t.struct(
            {
                "team_id": t.integer(),
                "discussion_number": t.integer(),
                "content": t.string(),
                "per_page": t.integer(),
                "page": t.integer(),
            }
        ),
        t.array(t.proxy(renames["reaction"])),
    )
    functions["reactions_create_for_team_discussion_legacy"] = ghes.post(
        "/teams/{team_id}/discussions/{discussion_number}/reactions",
        t.struct(
            {
                "team_id": t.integer(),
                "discussion_number": t.integer(),
                "content": t.string(),
            }
        ),
        t.proxy(renames["reaction"]),
        content_type="application/json",
        body_fields=("content",),
    )
    functions["teams_list_members_legacy"] = ghes.get(
        "/teams/{team_id}/members",
        t.struct(
            {
                "team_id": t.integer(),
                "role": t.string(),
                "per_page": t.integer(),
                "page": t.integer(),
            }
        ),
        t.array(t.proxy(renames["simple_user"])).optional(),
    )
    functions["teams_get_member_legacy"] = ghes.get(
        "/teams/{team_id}/members/{username}",
        t.struct({"team_id": t.integer(), "username": t.string()}),
        t.boolean().optional(),
    )
    functions["teams_add_member_legacy"] = ghes.put(
        "/teams/{team_id}/members/{username}",
        t.struct({"team_id": t.integer(), "username": t.string()}),
        t.boolean().optional(),
    )
    functions["teams_remove_member_legacy"] = ghes.delete(
        "/teams/{team_id}/members/{username}",
        t.struct({"team_id": t.integer(), "username": t.string()}),
        t.boolean().optional(),
    )
    functions["teams_get_membership_for_user_legacy"] = ghes.get(
        "/teams/{team_id}/memberships/{username}",
        t.struct({"team_id": t.integer(), "username": t.string()}),
        t.proxy(renames["team_membership"]).optional(),
    )
    functions["teams_add_or_update_membership_for_user_legacy"] = ghes.put(
        "/teams/{team_id}/memberships/{username}",
        t.struct(
            {
                "team_id": t.integer(),
                "username": t.string(),
                "role": t.string().optional(),
            }
        ),
        t.proxy(renames["team_membership"]).optional(),
        content_type="application/json",
        body_fields=("role",),
    )
    functions["teams_remove_membership_for_user_legacy"] = ghes.delete(
        "/teams/{team_id}/memberships/{username}",
        t.struct({"team_id": t.integer(), "username": t.string()}),
        t.boolean(),
    )
    functions["teams_list_projects_legacy"] = ghes.get(
        "/teams/{team_id}/projects",
        t.struct(
            {"team_id": t.integer(), "per_page": t.integer(), "page": t.integer()}
        ),
        t.array(t.proxy(renames["team_project"])).optional(),
    )
    functions["teams_check_permissions_for_project_legacy"] = ghes.get(
        "/teams/{team_id}/projects/{project_id}",
        t.struct({"team_id": t.integer(), "project_id": t.integer()}),
        t.proxy(renames["team_project"]).optional(),
    )
    functions["teams_add_or_update_project_permissions_legacy"] = ghes.put(
        "/teams/{team_id}/projects/{project_id}",
        t.struct(
            {
                "team_id": t.integer(),
                "project_id": t.integer(),
                "permission": t.string().optional(),
            }
        ),
        t.boolean().optional(),
        content_type="application/json",
        body_fields=("permission",),
    )
    functions["teams_remove_project_legacy"] = ghes.delete(
        "/teams/{team_id}/projects/{project_id}",
        t.struct({"team_id": t.integer(), "project_id": t.integer()}),
        t.boolean().optional(),
    )
    functions["teams_list_repos_legacy"] = ghes.get(
        "/teams/{team_id}/repos",
        t.struct(
            {"team_id": t.integer(), "per_page": t.integer(), "page": t.integer()}
        ),
        t.array(t.proxy(renames["minimal_repository"])).optional(),
    )
    functions["teams_check_permissions_for_repo_legacy"] = ghes.get(
        "/teams/{team_id}/repos/{owner}/{repo}",
        t.struct({"team_id": t.integer(), "owner": t.string(), "repo": t.string()}),
        t.proxy(renames["team_repository"]).optional(),
    )
    functions["teams_add_or_update_repo_permissions_legacy"] = ghes.put(
        "/teams/{team_id}/repos/{owner}/{repo}",
        t.struct(
            {
                "team_id": t.integer(),
                "owner": t.string(),
                "repo": t.string(),
                "permission": t.string().optional(),
            }
        ),
        t.boolean(),
        content_type="application/json",
        body_fields=("permission",),
    )
    functions["teams_remove_repo_legacy"] = ghes.delete(
        "/teams/{team_id}/repos/{owner}/{repo}",
        t.struct({"team_id": t.integer(), "owner": t.string(), "repo": t.string()}),
        t.boolean(),
    )
    functions["teams_list_child_legacy"] = ghes.get(
        "/teams/{team_id}/teams",
        t.struct(
            {"team_id": t.integer(), "per_page": t.integer(), "page": t.integer()}
        ),
        t.array(t.proxy(renames["team"])).optional(),
    )
    functions["users_get_authenticated"] = ghes.get(
        "/user",
        t.struct({}),
        t.either([t.proxy(renames["private_user"]), t.proxy(renames["public_user"])]),
    )
    functions["users_update_authenticated"] = ghes.patch(
        "/user",
        t.struct(
            {
                "name": t.string().optional(),
                "email": t.string().optional(),
                "blog": t.string().optional(),
                "twitter_username": t.string().optional(),
                "company": t.string().optional(),
                "location": t.string().optional(),
                "hireable": t.boolean().optional(),
                "bio": t.string().optional(),
            }
        ),
        t.proxy(renames["private_user"]).optional(),
        content_type="application/json",
        body_fields=(
            "name",
            "email",
            "blog",
            "twitter_username",
            "company",
            "location",
            "hireable",
            "bio",
        ),
    )
    functions["users_list_emails_for_authenticated_user"] = ghes.get(
        "/user/emails",
        t.struct({"per_page": t.integer(), "page": t.integer()}),
        t.array(t.proxy(renames["email"])).optional(),
    )
    functions["users_list_followers_for_authenticated_user"] = ghes.get(
        "/user/followers",
        t.struct({"per_page": t.integer(), "page": t.integer()}),
        t.array(t.proxy(renames["simple_user"])),
    )
    functions["users_list_followed_by_authenticated_user"] = ghes.get(
        "/user/following",
        t.struct({"per_page": t.integer(), "page": t.integer()}),
        t.array(t.proxy(renames["simple_user"])),
    )
    functions["users_check_person_is_followed_by_authenticated"] = ghes.get(
        "/user/following/{username}",
        t.struct({"username": t.string()}),
        t.boolean().optional(),
    )
    functions["users_follow"] = ghes.put(
        "/user/following/{username}",
        t.struct({"username": t.string()}),
        t.boolean().optional(),
    )
    functions["users_unfollow"] = ghes.delete(
        "/user/following/{username}",
        t.struct({"username": t.string()}),
        t.boolean().optional(),
    )
    functions["users_list_gpg_keys_for_authenticated_user"] = ghes.get(
        "/user/gpg_keys",
        t.struct({"per_page": t.integer(), "page": t.integer()}),
        t.array(t.proxy(renames["gpg_key"])).optional(),
    )
    functions["users_create_gpg_key_for_authenticated_user"] = ghes.post(
        "/user/gpg_keys",
        t.struct({"armored_public_key": t.string()}),
        t.proxy(renames["gpg_key"]).optional(),
        content_type="application/json",
        body_fields=("armored_public_key",),
    )
    functions["users_get_gpg_key_for_authenticated_user"] = ghes.get(
        "/user/gpg_keys/{gpg_key_id}",
        t.struct({"gpg_key_id": t.integer()}),
        t.proxy(renames["gpg_key"]).optional(),
    )
    functions["users_delete_gpg_key_for_authenticated_user"] = ghes.delete(
        "/user/gpg_keys/{gpg_key_id}",
        t.struct({"gpg_key_id": t.integer()}),
        t.boolean().optional(),
    )
    functions["apps_list_installations_for_authenticated_user"] = ghes.get(
        "/user/installations",
        t.struct({"per_page": t.integer(), "page": t.integer()}),
        t.struct(
            {
                "total_count": t.integer(),
                "installations": t.array(t.proxy(renames["installation"])),
            }
        ),
    )
    functions["apps_list_installation_repos_for_authenticated_user"] = ghes.get(
        "/user/installations/{installation_id}/repositories",
        t.struct(
            {
                "installation_id": t.integer(),
                "per_page": t.integer(),
                "page": t.integer(),
            }
        ),
        t.struct(
            {
                "total_count": t.integer(),
                "repository_selection": t.string().optional(),
                "repositories": t.array(t.proxy(renames["repository"])),
            }
        ).optional(),
    )
    functions["apps_add_repo_to_installation_for_authenticated_user"] = ghes.put(
        "/user/installations/{installation_id}/repositories/{repository_id}",
        t.struct({"installation_id": t.integer(), "repository_id": t.integer()}),
        t.boolean().optional(),
    )
    functions[
        "apps_remove_repo_from_installation_for_authenticated_user"
    ] = ghes.delete(
        "/user/installations/{installation_id}/repositories/{repository_id}",
        t.struct({"installation_id": t.integer(), "repository_id": t.integer()}),
        t.boolean().optional(),
    )
    functions["issues_list_for_authenticated_user"] = ghes.get(
        "/user/issues",
        t.struct(
            {
                "filter": t.string(),
                "state": t.string(),
                "labels": t.string(),
                "sort": t.string(),
                "direction": t.string(),
                "since": t.string(),
                "per_page": t.integer(),
                "page": t.integer(),
            }
        ),
        t.array(t.proxy(renames["issue"])).optional(),
    )
    functions["users_list_public_ssh_keys_for_authenticated_user"] = ghes.get(
        "/user/keys",
        t.struct({"per_page": t.integer(), "page": t.integer()}),
        t.array(t.proxy(renames["key"])).optional(),
    )
    functions["users_create_public_ssh_key_for_authenticated_user"] = ghes.post(
        "/user/keys",
        t.struct({"title": t.string().optional(), "key": t.string()}),
        t.proxy(renames["key"]).optional(),
        content_type="application/json",
        body_fields=("title", "key"),
    )
    functions["users_get_public_ssh_key_for_authenticated_user"] = ghes.get(
        "/user/keys/{key_id}",
        t.struct({"key_id": t.integer()}),
        t.proxy(renames["key"]).optional(),
    )
    functions["users_delete_public_ssh_key_for_authenticated_user"] = ghes.delete(
        "/user/keys/{key_id}",
        t.struct({"key_id": t.integer()}),
        t.boolean().optional(),
    )
    functions["orgs_list_memberships_for_authenticated_user"] = ghes.get(
        "/user/memberships/orgs",
        t.struct({"state": t.string(), "per_page": t.integer(), "page": t.integer()}),
        t.array(t.proxy(renames["org_membership"])),
    )
    functions["orgs_get_membership_for_authenticated_user"] = ghes.get(
        "/user/memberships/orgs/{org}",
        t.struct({"org": t.string()}),
        t.proxy(renames["org_membership"]).optional(),
    )
    functions["orgs_update_membership_for_authenticated_user"] = ghes.patch(
        "/user/memberships/orgs/{org}",
        t.struct({"org": t.string(), "state": t.string()}),
        t.proxy(renames["org_membership"]).optional(),
        content_type="application/json",
        body_fields=("state",),
    )
    functions["orgs_list_for_authenticated_user"] = ghes.get(
        "/user/orgs",
        t.struct({"per_page": t.integer(), "page": t.integer()}),
        t.array(t.proxy(renames["organization_simple"])),
    )
    functions["projects_create_for_authenticated_user"] = ghes.post(
        "/user/projects",
        t.struct({"name": t.string(), "body": t.string().optional()}),
        t.proxy(renames["project"]),
        content_type="application/json",
        body_fields=("name", "body"),
    )
    functions["users_list_public_emails_for_authenticated_user"] = ghes.get(
        "/user/public_emails",
        t.struct({"per_page": t.integer(), "page": t.integer()}),
        t.array(t.proxy(renames["email"])).optional(),
    )
    functions["repos_list_for_authenticated_user"] = ghes.get(
        "/user/repos",
        t.struct(
            {
                "visibility": t.string(),
                "affiliation": t.string(),
                "type": t.string(),
                "sort": t.string(),
                "direction": t.string(),
                "per_page": t.integer(),
                "page": t.integer(),
                "since": t.string(),
                "before": t.string(),
            }
        ),
        t.array(t.proxy(renames["repository"])),
    )
    functions["repos_create_for_authenticated_user"] = ghes.post(
        "/user/repos",
        t.struct(
            {
                "name": t.string(),
                "description": t.string().optional(),
                "homepage": t.string().optional(),
                "private": t.boolean().optional(),
                "has_issues": t.boolean().optional(),
                "has_projects": t.boolean().optional(),
                "has_wiki": t.boolean().optional(),
                "team_id": t.integer().optional(),
                "auto_init": t.boolean().optional(),
                "gitignore_template": t.string().optional(),
                "license_template": t.string().optional(),
                "allow_squash_merge": t.boolean().optional(),
                "allow_merge_commit": t.boolean().optional(),
                "allow_rebase_merge": t.boolean().optional(),
                "delete_branch_on_merge": t.boolean().optional(),
                "has_downloads": t.boolean().optional(),
                "is_template": t.boolean().optional(),
            }
        ),
        t.proxy(renames["repository"]).optional(),
        content_type="application/json",
        body_fields=(
            "name",
            "description",
            "homepage",
            "private",
            "has_issues",
            "has_projects",
            "has_wiki",
            "team_id",
            "auto_init",
            "gitignore_template",
            "license_template",
            "allow_squash_merge",
            "allow_merge_commit",
            "allow_rebase_merge",
            "delete_branch_on_merge",
            "has_downloads",
            "is_template",
        ),
    )
    functions["repos_list_invitations_for_authenticated_user"] = ghes.get(
        "/user/repository_invitations",
        t.struct({"per_page": t.integer(), "page": t.integer()}),
        t.array(t.proxy(renames["repository_invitation"])).optional(),
    )
    functions["repos_accept_invitation_for_authenticated_user"] = ghes.patch(
        "/user/repository_invitations/{invitation_id}",
        t.struct({"invitation_id": t.integer()}),
        t.boolean().optional(),
    )
    functions["repos_decline_invitation_for_authenticated_user"] = ghes.delete(
        "/user/repository_invitations/{invitation_id}",
        t.struct({"invitation_id": t.integer()}),
        t.boolean().optional(),
    )
    functions["activity_list_repos_starred_by_authenticated_user"] = ghes.get(
        "/user/starred",
        t.struct(
            {
                "sort": t.string(),
                "direction": t.string(),
                "per_page": t.integer(),
                "page": t.integer(),
            }
        ),
        t.array(t.proxy(renames["repository"])),
    )
    functions["activity_check_repo_is_starred_by_authenticated_user"] = ghes.get(
        "/user/starred/{owner}/{repo}",
        t.struct({"owner": t.string(), "repo": t.string()}),
        t.boolean().optional(),
    )
    functions["activity_star_repo_for_authenticated_user"] = ghes.put(
        "/user/starred/{owner}/{repo}",
        t.struct({"owner": t.string(), "repo": t.string()}),
        t.boolean().optional(),
    )
    functions["activity_unstar_repo_for_authenticated_user"] = ghes.delete(
        "/user/starred/{owner}/{repo}",
        t.struct({"owner": t.string(), "repo": t.string()}),
        t.boolean().optional(),
    )
    functions["activity_list_watched_repos_for_authenticated_user"] = ghes.get(
        "/user/subscriptions",
        t.struct({"per_page": t.integer(), "page": t.integer()}),
        t.array(t.proxy(renames["minimal_repository"])),
    )
    functions["teams_list_for_authenticated_user"] = ghes.get(
        "/user/teams",
        t.struct({"per_page": t.integer(), "page": t.integer()}),
        t.array(t.proxy(renames["team_full"])).optional(),
    )
    functions["users_list"] = ghes.get(
        "/users",
        t.struct({"since": t.integer(), "per_page": t.integer()}),
        t.array(t.proxy(renames["simple_user"])),
    )
    functions["users_get_by_username"] = ghes.get(
        "/users/{username}",
        t.struct({"username": t.string()}),
        t.either(
            [t.proxy(renames["private_user"]), t.proxy(renames["public_user"])]
        ).optional(),
    )
    functions["activity_list_events_for_authenticated_user"] = ghes.get(
        "/users/{username}/events",
        t.struct(
            {"username": t.string(), "per_page": t.integer(), "page": t.integer()}
        ),
        t.array(t.proxy(renames["event"])),
    )
    functions["activity_list_org_events_for_authenticated_user"] = ghes.get(
        "/users/{username}/events/orgs/{org}",
        t.struct(
            {
                "username": t.string(),
                "org": t.string(),
                "per_page": t.integer(),
                "page": t.integer(),
            }
        ),
        t.array(t.proxy(renames["event"])),
    )
    functions["activity_list_public_events_for_user"] = ghes.get(
        "/users/{username}/events/public",
        t.struct(
            {"username": t.string(), "per_page": t.integer(), "page": t.integer()}
        ),
        t.array(t.proxy(renames["event"])),
    )
    functions["users_list_followers_for_user"] = ghes.get(
        "/users/{username}/followers",
        t.struct(
            {"username": t.string(), "per_page": t.integer(), "page": t.integer()}
        ),
        t.array(t.proxy(renames["simple_user"])),
    )
    functions["users_list_following_for_user"] = ghes.get(
        "/users/{username}/following",
        t.struct(
            {"username": t.string(), "per_page": t.integer(), "page": t.integer()}
        ),
        t.array(t.proxy(renames["simple_user"])),
    )
    functions["users_check_following_for_user"] = ghes.get(
        "/users/{username}/following/{target_user}",
        t.struct({"username": t.string(), "target_user": t.string()}),
        t.boolean().optional(),
    )
    functions["gists_list_for_user"] = ghes.get(
        "/users/{username}/gists",
        t.struct(
            {
                "username": t.string(),
                "since": t.string(),
                "per_page": t.integer(),
                "page": t.integer(),
            }
        ),
        t.array(t.proxy(renames["base_gist"])),
    )
    functions["users_list_gpg_keys_for_user"] = ghes.get(
        "/users/{username}/gpg_keys",
        t.struct(
            {"username": t.string(), "per_page": t.integer(), "page": t.integer()}
        ),
        t.array(t.proxy(renames["gpg_key"])),
    )
    functions["users_get_context_for_user"] = ghes.get(
        "/users/{username}/hovercard",
        t.struct(
            {
                "username": t.string(),
                "subject_type": t.string(),
                "subject_id": t.string(),
            }
        ),
        t.proxy(renames["hovercard"]).optional(),
    )
    functions["apps_get_user_installation"] = ghes.get(
        "/users/{username}/installation",
        t.struct({"username": t.string()}),
        t.proxy(renames["installation"]),
    )
    functions["users_list_public_keys_for_user"] = ghes.get(
        "/users/{username}/keys",
        t.struct(
            {"username": t.string(), "per_page": t.integer(), "page": t.integer()}
        ),
        t.array(t.proxy(renames["key_simple"])),
    )
    functions["orgs_list_for_user"] = ghes.get(
        "/users/{username}/orgs",
        t.struct(
            {"username": t.string(), "per_page": t.integer(), "page": t.integer()}
        ),
        t.array(t.proxy(renames["organization_simple"])),
    )
    functions["projects_list_for_user"] = ghes.get(
        "/users/{username}/projects",
        t.struct(
            {
                "username": t.string(),
                "state": t.string(),
                "per_page": t.integer(),
                "page": t.integer(),
            }
        ),
        t.array(t.proxy(renames["project"])),
    )
    functions["activity_list_received_events_for_user"] = ghes.get(
        "/users/{username}/received_events",
        t.struct(
            {"username": t.string(), "per_page": t.integer(), "page": t.integer()}
        ),
        t.array(t.proxy(renames["event"])),
    )
    functions["activity_list_received_public_events_for_user"] = ghes.get(
        "/users/{username}/received_events/public",
        t.struct(
            {"username": t.string(), "per_page": t.integer(), "page": t.integer()}
        ),
        t.array(t.proxy(renames["event"])),
    )
    functions["repos_list_for_user"] = ghes.get(
        "/users/{username}/repos",
        t.struct(
            {
                "username": t.string(),
                "type": t.string(),
                "sort": t.string(),
                "direction": t.string(),
                "per_page": t.integer(),
                "page": t.integer(),
            }
        ),
        t.array(t.proxy(renames["minimal_repository"])),
    )
    functions["enterprise_admin_promote_user_to_be_site_administrator"] = ghes.put(
        "/users/{username}/site_admin",
        t.struct({"username": t.string()}),
        t.boolean(),
    )
    functions["enterprise_admin_demote_site_administrator"] = ghes.delete(
        "/users/{username}/site_admin",
        t.struct({"username": t.string()}),
        t.boolean(),
    )
    functions["activity_list_repos_starred_by_user"] = ghes.get(
        "/users/{username}/starred",
        t.struct(
            {
                "username": t.string(),
                "sort": t.string(),
                "direction": t.string(),
                "per_page": t.integer(),
                "page": t.integer(),
            }
        ),
        t.union(
            [
                t.array(t.proxy(renames["starred_repository"])),
                t.array(t.proxy(renames["repository"])),
            ]
        ),
    )
    functions["activity_list_repos_watched_by_user"] = ghes.get(
        "/users/{username}/subscriptions",
        t.struct(
            {"username": t.string(), "per_page": t.integer(), "page": t.integer()}
        ),
        t.array(t.proxy(renames["minimal_repository"])),
    )
    functions["enterprise_admin_suspend_user"] = ghes.put(
        "/users/{username}/suspended",
        t.struct({"username": t.string(), "reason": t.string().optional()}),
        t.boolean(),
        content_type="application/json",
        body_fields=("reason",),
    )
    functions["enterprise_admin_unsuspend_user"] = ghes.delete(
        "/users/{username}/suspended",
        t.struct({"username": t.string(), "reason": t.string().optional()}),
        t.boolean(),
        content_type="application/json",
        body_fields=("reason",),
    )

    return Import(
        importer="ghes", renames=renames, types=Box(types), functions=Box(functions)
    )
