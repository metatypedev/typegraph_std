from typegraph.importers.base.importer import Import
from typegraph import t
from typegraph.utils.sanitizers import inject_params
from typegraph.runtimes.http import HTTPRuntime
from box import Box


def import_github(params=None):
    target_url = inject_params("{protocol}://{hostname}/api/v3", params)
    github = HTTPRuntime(target_url)

    renames = {
        "global-hook": "_github_1_global-hook",
        "global-hook-2": "_github_2_global-hook-2",
        "public-key-full": "_github_3_public-key-full",
        "ldap-mapping-team": "_github_4_ldap-mapping-team",
        "ldap-mapping-user": "_github_5_ldap-mapping-user",
        "organization-simple": "_github_6_organization-simple",
        "pre-receive-environment": "_github_7_pre-receive-environment",
        "pre-receive-environment-download-status": "_github_8_pre-receive-environment-download-status",
        "pre-receive-hook": "_github_9_pre-receive-hook",
        "nullable-simple-user": "_github_10_nullable-simple-user",
        "app-permissions": "_github_11_app-permissions",
        "simple-user": "_github_12_simple-user",
        "nullable-scoped-installation": "_github_13_nullable-scoped-installation",
        "authorization": "_github_14_authorization",
        "integration": "_github_15_integration",
        "basic-error": "_github_16_basic-error",
        "validation-error-simple": "_github_17_validation-error-simple",
        "webhook-config-url": "_github_18_webhook-config-url",
        "webhook-config-content-type": "_github_19_webhook-config-content-type",
        "webhook-config-secret": "_github_20_webhook-config-secret",
        "webhook-config-insecure-ssl": "_github_21_webhook-config-insecure-ssl",
        "webhook-config": "_github_22_webhook-config",
        "enterprise": "_github_23_enterprise",
        "installation": "_github_24_installation",
        "nullable-license-simple": "_github_25_nullable-license-simple",
        "repository": "_github_26_repository",
        "installation-token": "_github_27_installation-token",
        "validation-error": "_github_28_validation-error",
        "application-grant": "_github_29_application-grant",
        "nullable-authorization": "_github_30_nullable-authorization",
        "code-of-conduct": "_github_31_code-of-conduct",
        "announcement-message": "_github_32_announcement-message",
        "announcement-expiration": "_github_33_announcement-expiration",
        "announcement": "_github_34_announcement",
        "license-info": "_github_35_license-info",
        "enterprise-repository-overview": "_github_36_enterprise-repository-overview",
        "enterprise-hook-overview": "_github_37_enterprise-hook-overview",
        "enterprise-page-overview": "_github_38_enterprise-page-overview",
        "enterprise-organization-overview": "_github_39_enterprise-organization-overview",
        "enterprise-user-overview": "_github_40_enterprise-user-overview",
        "enterprise-pull-request-overview": "_github_41_enterprise-pull-request-overview",
        "enterprise-issue-overview": "_github_42_enterprise-issue-overview",
        "enterprise-milestone-overview": "_github_43_enterprise-milestone-overview",
        "enterprise-gist-overview": "_github_44_enterprise-gist-overview",
        "enterprise-comment-overview": "_github_45_enterprise-comment-overview",
        "enterprise-overview": "_github_46_enterprise-overview",
        "enabled-organizations": "_github_47_enabled-organizations",
        "allowed-actions": "_github_48_allowed-actions",
        "selected-actions-url": "_github_49_selected-actions-url",
        "actions-enterprise-permissions": "_github_50_actions-enterprise-permissions",
        "selected-actions": "_github_51_selected-actions",
        "runner-groups-enterprise": "_github_52_runner-groups-enterprise",
        "runner-label": "_github_53_runner-label",
        "runner": "_github_54_runner",
        "runner-application": "_github_55_runner-application",
        "authentication-token": "_github_56_authentication-token",
        "actor": "_github_57_actor",
        "nullable-milestone": "_github_58_nullable-milestone",
        "nullable-integration": "_github_59_nullable-integration",
        "author_association": "_github_60_author_association",
        "reaction-rollup": "_github_61_reaction-rollup",
        "issue": "_github_62_issue",
        "issue-comment": "_github_63_issue-comment",
        "event": "_github_64_event",
        "link-with-type": "_github_65_link-with-type",
        "feed": "_github_66_feed",
        "base-gist": "_github_67_base-gist",
        "public-user": "_github_68_public-user",
        "gist-history": "_github_69_gist-history",
        "gist-simple": "_github_70_gist-simple",
        "gist-comment": "_github_71_gist-comment",
        "gist-commit": "_github_72_gist-commit",
        "gitignore-template": "_github_73_gitignore-template",
        "license-simple": "_github_74_license-simple",
        "license": "_github_75_license",
        "api-overview": "_github_76_api-overview",
        "nullable-repository": "_github_77_nullable-repository",
        "minimal-repository": "_github_78_minimal-repository",
        "thread": "_github_79_thread",
        "thread-subscription": "_github_80_thread-subscription",
        "organization-full": "_github_81_organization-full",
        "enabled-repositories": "_github_82_enabled-repositories",
        "actions-organization-permissions": "_github_83_actions-organization-permissions",
        "runner-groups-org": "_github_84_runner-groups-org",
        "organization-actions-secret": "_github_85_organization-actions-secret",
        "actions-public-key": "_github_86_actions-public-key",
        "empty-object": "_github_87_empty-object",
        "org-hook": "_github_88_org-hook",
        "org-membership": "_github_89_org-membership",
        "org-pre-receive-hook": "_github_90_org-pre-receive-hook",
        "project": "_github_91_project",
        "nullable-team-simple": "_github_92_nullable-team-simple",
        "team": "_github_93_team",
        "team-full": "_github_94_team-full",
        "team-discussion": "_github_95_team-discussion",
        "team-discussion-comment": "_github_96_team-discussion-comment",
        "reaction": "_github_97_reaction",
        "team-membership": "_github_98_team-membership",
        "team-project": "_github_99_team-project",
        "team-repository": "_github_100_team-repository",
        "project-card": "_github_101_project-card",
        "project-column": "_github_102_project-column",
        "project-collaborator-permission": "_github_103_project-collaborator-permission",
        "rate-limit": "_github_104_rate-limit",
        "rate-limit-overview": "_github_105_rate-limit-overview",
        "code-of-conduct-simple": "_github_106_code-of-conduct-simple",
        "full-repository": "_github_107_full-repository",
        "artifact": "_github_108_artifact",
        "job": "_github_109_job",
        "actions-enabled": "_github_110_actions-enabled",
        "actions-repository-permissions": "_github_111_actions-repository-permissions",
        "pull-request-minimal": "_github_112_pull-request-minimal",
        "nullable-simple-commit": "_github_113_nullable-simple-commit",
        "workflow-run": "_github_114_workflow-run",
        "actions-secret": "_github_115_actions-secret",
        "workflow": "_github_116_workflow",
        "protected-branch-required-status-check": "_github_117_protected-branch-required-status-check",
        "protected-branch-admin-enforced": "_github_118_protected-branch-admin-enforced",
        "protected-branch-pull-request-review": "_github_119_protected-branch-pull-request-review",
        "branch-restriction-policy": "_github_120_branch-restriction-policy",
        "branch-protection": "_github_121_branch-protection",
        "short-branch": "_github_122_short-branch",
        "nullable-git-user": "_github_123_nullable-git-user",
        "verification": "_github_124_verification",
        "diff-entry": "_github_125_diff-entry",
        "commit": "_github_126_commit",
        "branch-with-protection": "_github_127_branch-with-protection",
        "status-check-policy": "_github_128_status-check-policy",
        "protected-branch": "_github_129_protected-branch",
        "deployment-simple": "_github_130_deployment-simple",
        "check-run": "_github_131_check-run",
        "check-annotation": "_github_132_check-annotation",
        "simple-commit": "_github_133_simple-commit",
        "check-suite": "_github_134_check-suite",
        "check-suite-preference": "_github_135_check-suite-preference",
        "code-scanning-analysis-tool-name": "_github_136_code-scanning-analysis-tool-name",
        "code-scanning-analysis-tool-guid": "_github_137_code-scanning-analysis-tool-guid",
        "code-scanning-ref": "_github_138_code-scanning-ref",
        "code-scanning-alert-state": "_github_139_code-scanning-alert-state",
        "alert-number": "_github_140_alert-number",
        "alert-created-at": "_github_141_alert-created-at",
        "alert-url": "_github_142_alert-url",
        "alert-html-url": "_github_143_alert-html-url",
        "alert-instances-url": "_github_144_alert-instances-url",
        "code-scanning-alert-dismissed-at": "_github_145_code-scanning-alert-dismissed-at",
        "code-scanning-alert-dismissed-reason": "_github_146_code-scanning-alert-dismissed-reason",
        "code-scanning-alert-rule-summary": "_github_147_code-scanning-alert-rule-summary",
        "code-scanning-analysis-tool-version": "_github_148_code-scanning-analysis-tool-version",
        "code-scanning-analysis-tool": "_github_149_code-scanning-analysis-tool",
        "code-scanning-analysis-analysis-key": "_github_150_code-scanning-analysis-analysis-key",
        "code-scanning-alert-environment": "_github_151_code-scanning-alert-environment",
        "code-scanning-analysis-category": "_github_152_code-scanning-analysis-category",
        "code-scanning-alert-location": "_github_153_code-scanning-alert-location",
        "code-scanning-alert-classification": "_github_154_code-scanning-alert-classification",
        "code-scanning-alert-instance": "_github_155_code-scanning-alert-instance",
        "code-scanning-alert-items": "_github_156_code-scanning-alert-items",
        "code-scanning-alert-rule": "_github_157_code-scanning-alert-rule",
        "code-scanning-alert": "_github_158_code-scanning-alert",
        "code-scanning-alert-set-state": "_github_159_code-scanning-alert-set-state",
        "code-scanning-analysis-sarif-id": "_github_160_code-scanning-analysis-sarif-id",
        "code-scanning-analysis-commit-sha": "_github_161_code-scanning-analysis-commit-sha",
        "code-scanning-analysis-environment": "_github_162_code-scanning-analysis-environment",
        "code-scanning-analysis-created-at": "_github_163_code-scanning-analysis-created-at",
        "code-scanning-analysis-url": "_github_164_code-scanning-analysis-url",
        "code-scanning-analysis": "_github_165_code-scanning-analysis",
        "code-scanning-analysis-sarif-file": "_github_166_code-scanning-analysis-sarif-file",
        "code-scanning-sarifs-receipt": "_github_167_code-scanning-sarifs-receipt",
        "collaborator": "_github_168_collaborator",
        "repository-invitation": "_github_169_repository-invitation",
        "nullable-collaborator": "_github_170_nullable-collaborator",
        "repository-collaborator-permission": "_github_171_repository-collaborator-permission",
        "commit-comment": "_github_172_commit-comment",
        "scim-error": "_github_173_scim-error",
        "branch-short": "_github_174_branch-short",
        "link": "_github_175_link",
        "pull-request-simple": "_github_176_pull-request-simple",
        "simple-commit-status": "_github_177_simple-commit-status",
        "combined-commit-status": "_github_178_combined-commit-status",
        "status": "_github_179_status",
        "commit-comparison": "_github_180_commit-comparison",
        "content-reference-attachment": "_github_181_content-reference-attachment",
        "content-tree": "_github_182_content-tree",
        "content-directory": "_github_183_content-directory",
        "content-file": "_github_184_content-file",
        "content-symlink": "_github_185_content-symlink",
        "content-submodule": "_github_186_content-submodule",
        "file-commit": "_github_187_file-commit",
        "contributor": "_github_188_contributor",
        "deployment": "_github_189_deployment",
        "deployment-status": "_github_190_deployment-status",
        "short-blob": "_github_191_short-blob",
        "blob": "_github_192_blob",
        "git-commit": "_github_193_git-commit",
        "git-ref": "_github_194_git-ref",
        "git-tag": "_github_195_git-tag",
        "git-tree": "_github_196_git-tree",
        "hook-response": "_github_197_hook-response",
        "hook": "_github_198_hook",
        "nullable-issue": "_github_199_nullable-issue",
        "issue-event-label": "_github_200_issue-event-label",
        "issue-event-dismissed-review": "_github_201_issue-event-dismissed-review",
        "issue-event-milestone": "_github_202_issue-event-milestone",
        "issue-event-project-card": "_github_203_issue-event-project-card",
        "issue-event-rename": "_github_204_issue-event-rename",
        "issue-event": "_github_205_issue-event",
        "labeled-issue-event": "_github_206_labeled-issue-event",
        "unlabeled-issue-event": "_github_207_unlabeled-issue-event",
        "assigned-issue-event": "_github_208_assigned-issue-event",
        "unassigned-issue-event": "_github_209_unassigned-issue-event",
        "milestoned-issue-event": "_github_210_milestoned-issue-event",
        "demilestoned-issue-event": "_github_211_demilestoned-issue-event",
        "renamed-issue-event": "_github_212_renamed-issue-event",
        "review-requested-issue-event": "_github_213_review-requested-issue-event",
        "review-request-removed-issue-event": "_github_214_review-request-removed-issue-event",
        "review-dismissed-issue-event": "_github_215_review-dismissed-issue-event",
        "locked-issue-event": "_github_216_locked-issue-event",
        "added-to-project-issue-event": "_github_217_added-to-project-issue-event",
        "moved-column-in-project-issue-event": "_github_218_moved-column-in-project-issue-event",
        "removed-from-project-issue-event": "_github_219_removed-from-project-issue-event",
        "converted-note-to-issue-issue-event": "_github_220_converted-note-to-issue-issue-event",
        "issue-event-for-issue": "_github_221_issue-event-for-issue",
        "label": "_github_222_label",
        "timeline-comment-event": "_github_223_timeline-comment-event",
        "timeline-cross-referenced-event": "_github_224_timeline-cross-referenced-event",
        "timeline-committed-event": "_github_225_timeline-committed-event",
        "timeline-reviewed-event": "_github_226_timeline-reviewed-event",
        "pull-request-review-comment": "_github_227_pull-request-review-comment",
        "timeline-line-commented-event": "_github_228_timeline-line-commented-event",
        "timeline-commit-commented-event": "_github_229_timeline-commit-commented-event",
        "timeline-assigned-issue-event": "_github_230_timeline-assigned-issue-event",
        "timeline-unassigned-issue-event": "_github_231_timeline-unassigned-issue-event",
        "state-change-issue-event": "_github_232_state-change-issue-event",
        "timeline-issue-events": "_github_233_timeline-issue-events",
        "deploy-key": "_github_234_deploy-key",
        "language": "_github_235_language",
        "license-content": "_github_236_license-content",
        "milestone": "_github_237_milestone",
        "pages-source-hash": "_github_238_pages-source-hash",
        "pages-https-certificate": "_github_239_pages-https-certificate",
        "page": "_github_240_page",
        "page-build": "_github_241_page-build",
        "page-build-status": "_github_242_page-build-status",
        "repository-pre-receive-hook": "_github_243_repository-pre-receive-hook",
        "team-simple": "_github_244_team-simple",
        "pull-request": "_github_245_pull-request",
        "pull-request-merge-result": "_github_246_pull-request-merge-result",
        "pull-request-review-request": "_github_247_pull-request-review-request",
        "pull-request-review": "_github_248_pull-request-review",
        "review-comment": "_github_249_review-comment",
        "release-asset": "_github_250_release-asset",
        "release": "_github_251_release",
        "stargazer": "_github_252_stargazer",
        "code-frequency-stat": "_github_253_code-frequency-stat",
        "commit-activity": "_github_254_commit-activity",
        "contributor-activity": "_github_255_contributor-activity",
        "participation-stats": "_github_256_participation-stats",
        "repository-subscription": "_github_257_repository-subscription",
        "tag": "_github_258_tag",
        "topic": "_github_259_topic",
        "search-result-text-matches": "_github_260_search-result-text-matches",
        "code-search-result-item": "_github_261_code-search-result-item",
        "commit-search-result-item": "_github_262_commit-search-result-item",
        "issue-search-result-item": "_github_263_issue-search-result-item",
        "label-search-result-item": "_github_264_label-search-result-item",
        "repo-search-result-item": "_github_265_repo-search-result-item",
        "topic-search-result-item": "_github_266_topic-search-result-item",
        "user-search-result-item": "_github_267_user-search-result-item",
        "configuration-status": "_github_268_configuration-status",
        "maintenance-status": "_github_269_maintenance-status",
        "enterprise-settings": "_github_270_enterprise-settings",
        "ssh-key": "_github_271_ssh-key",
        "private-user": "_github_272_private-user",
        "email": "_github_273_email",
        "gpg-key": "_github_274_gpg-key",
        "key": "_github_275_key",
        "starred-repository": "_github_276_starred-repository",
        "hovercard": "_github_277_hovercard",
        "key-simple": "_github_278_key-simple",
    }

    types = {}
    types["global-hook"] = t.struct(
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
    ).named(renames["global-hook"])
    types["global-hook-2"] = t.struct(
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
    ).named(renames["global-hook-2"])
    types["public-key-full"] = t.struct(
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
    ).named(renames["public-key-full"])
    types["ldap-mapping-team"] = t.struct(
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
    ).named(renames["ldap-mapping-team"])
    types["ldap-mapping-user"] = t.struct(
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
    ).named(renames["ldap-mapping-user"])
    types["organization-simple"] = t.struct(
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
    ).named(renames["organization-simple"])
    types["pre-receive-environment"] = t.struct(
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
    ).named(renames["pre-receive-environment"])
    types["pre-receive-environment-download-status"] = t.struct(
        {
            "url": t.string().optional(),
            "state": t.string().optional(),
            "downloaded_at": t.string().optional(),
            "message": t.string().optional(),
        }
    ).named(renames["pre-receive-environment-download-status"])
    types["pre-receive-hook"] = t.struct(
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
    ).named(renames["pre-receive-hook"])
    types["nullable-simple-user"] = (
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
        .named(renames["nullable-simple-user"])
    )
    types["app-permissions"] = t.struct(
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
    ).named(renames["app-permissions"])
    types["simple-user"] = t.struct(
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
    ).named(renames["simple-user"])
    types["nullable-scoped-installation"] = (
        t.struct(
            {
                "permissions": t.proxy(renames["app-permissions"]),
                "repository_selection": t.string(),
                "single_file_name": t.string().optional(),
                "has_multiple_single_files": t.boolean().optional(),
                "single_file_paths": t.array(t.string()).optional(),
                "repositories_url": t.string(),
                "account": t.proxy(renames["simple-user"]),
            }
        )
        .optional()
        .named(renames["nullable-scoped-installation"])
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
            "user": t.proxy(renames["nullable-simple-user"]).optional(),
            "installation": t.proxy(renames["nullable-scoped-installation"]).optional(),
        }
    ).named(renames["authorization"])
    types["integration"] = t.struct(
        {
            "id": t.integer(),
            "slug": t.string().optional(),
            "node_id": t.string(),
            "owner": t.proxy(renames["nullable-simple-user"]),
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
    types["basic-error"] = t.struct(
        {
            "message": t.string().optional(),
            "documentation_url": t.string().optional(),
            "url": t.string().optional(),
            "status": t.string().optional(),
        }
    ).named(renames["basic-error"])
    types["validation-error-simple"] = t.struct(
        {
            "message": t.string(),
            "documentation_url": t.string(),
            "errors": t.array(t.string()).optional(),
        }
    ).named(renames["validation-error-simple"])
    types["webhook-config-url"] = t.string().named(renames["webhook-config-url"])
    types["webhook-config-content-type"] = t.string().named(
        renames["webhook-config-content-type"]
    )
    types["webhook-config-secret"] = t.string().named(renames["webhook-config-secret"])
    types["webhook-config-insecure-ssl"] = t.either([t.string(), t.number()]).named(
        renames["webhook-config-insecure-ssl"]
    )
    types["webhook-config"] = t.struct(
        {
            "url": t.proxy(renames["webhook-config-url"]).optional(),
            "content_type": t.proxy(renames["webhook-config-content-type"]).optional(),
            "secret": t.proxy(renames["webhook-config-secret"]).optional(),
            "insecure_ssl": t.proxy(renames["webhook-config-insecure-ssl"]).optional(),
        }
    ).named(renames["webhook-config"])
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
                [t.proxy(renames["simple-user"]), t.proxy(renames["enterprise"])]
            ).optional(),
            "repository_selection": t.string(),
            "access_tokens_url": t.string(),
            "repositories_url": t.string(),
            "html_url": t.string(),
            "app_id": t.integer(),
            "target_id": t.integer(),
            "target_type": t.string(),
            "permissions": t.proxy(renames["app-permissions"]),
            "events": t.array(t.string()),
            "created_at": t.string(),
            "updated_at": t.string(),
            "single_file_name": t.string().optional(),
            "has_multiple_single_files": t.boolean().optional(),
            "single_file_paths": t.array(t.string()).optional(),
            "app_slug": t.string(),
            "suspended_by": t.proxy(renames["nullable-simple-user"]),
            "suspended_at": t.string().optional(),
            "contact_email": t.string().optional(),
        }
    ).named(renames["installation"])
    types["nullable-license-simple"] = (
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
        .named(renames["nullable-license-simple"])
    )
    types["repository"] = t.struct(
        {
            "id": t.integer(),
            "node_id": t.string(),
            "name": t.string(),
            "full_name": t.string(),
            "license": t.proxy(renames["nullable-license-simple"]),
            "organization": t.proxy(renames["nullable-simple-user"]).optional(),
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
            "owner": t.proxy(renames["simple-user"]),
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
    types["installation-token"] = t.struct(
        {
            "token": t.string(),
            "expires_at": t.string(),
            "permissions": t.proxy(renames["app-permissions"]).optional(),
            "repository_selection": t.string().optional(),
            "repositories": t.array(t.proxy(renames["repository"])).optional(),
            "single_file": t.string().optional(),
            "has_multiple_single_files": t.boolean().optional(),
            "single_file_paths": t.array(t.string()).optional(),
        }
    ).named(renames["installation-token"])
    types["validation-error"] = t.struct(
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
    ).named(renames["validation-error"])
    types["application-grant"] = t.struct(
        {
            "id": t.integer(),
            "url": t.string(),
            "app": t.struct(
                {"client_id": t.string(), "name": t.string(), "url": t.string()}
            ),
            "created_at": t.string(),
            "updated_at": t.string(),
            "scopes": t.array(t.string()),
            "user": t.proxy(renames["nullable-simple-user"]).optional(),
        }
    ).named(renames["application-grant"])
    types["nullable-authorization"] = (
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
                "user": t.proxy(renames["nullable-simple-user"]).optional(),
                "installation": t.proxy(
                    renames["nullable-scoped-installation"]
                ).optional(),
            }
        )
        .optional()
        .named(renames["nullable-authorization"])
    )
    types["code-of-conduct"] = t.struct(
        {
            "key": t.string(),
            "name": t.string(),
            "url": t.string(),
            "body": t.string().optional(),
            "html_url": t.string().optional(),
        }
    ).named(renames["code-of-conduct"])
    types["announcement-message"] = t.string().named(renames["announcement-message"])
    types["announcement-expiration"] = (
        t.string().optional().named(renames["announcement-expiration"])
    )
    types["announcement"] = t.struct(
        {
            "announcement": t.proxy(renames["announcement-message"]),
            "expires_at": t.proxy(renames["announcement-expiration"]).optional(),
        }
    ).named(renames["announcement"])
    types["license-info"] = t.struct(
        {
            "seats": t.either([t.string(), t.integer()]).optional(),
            "seats_used": t.integer().optional(),
            "seats_available": t.either([t.string(), t.integer()]).optional(),
            "kind": t.string().optional(),
            "days_until_expiration": t.integer().optional(),
            "expire_at": t.string().optional(),
        }
    ).named(renames["license-info"])
    types["enterprise-repository-overview"] = t.struct(
        {
            "total_repos": t.integer(),
            "root_repos": t.integer(),
            "fork_repos": t.integer(),
            "org_repos": t.integer(),
            "total_pushes": t.integer(),
            "total_wikis": t.integer(),
        }
    ).named(renames["enterprise-repository-overview"])
    types["enterprise-hook-overview"] = t.struct(
        {
            "total_hooks": t.integer(),
            "active_hooks": t.integer(),
            "inactive_hooks": t.integer(),
        }
    ).named(renames["enterprise-hook-overview"])
    types["enterprise-page-overview"] = t.struct({"total_pages": t.integer()}).named(
        renames["enterprise-page-overview"]
    )
    types["enterprise-organization-overview"] = t.struct(
        {
            "total_orgs": t.integer(),
            "disabled_orgs": t.integer(),
            "total_teams": t.integer(),
            "total_team_members": t.integer(),
        }
    ).named(renames["enterprise-organization-overview"])
    types["enterprise-user-overview"] = t.struct(
        {
            "total_users": t.integer(),
            "admin_users": t.integer(),
            "suspended_users": t.integer(),
        }
    ).named(renames["enterprise-user-overview"])
    types["enterprise-pull-request-overview"] = t.struct(
        {
            "total_pulls": t.integer(),
            "merged_pulls": t.integer(),
            "mergeable_pulls": t.integer(),
            "unmergeable_pulls": t.integer(),
        }
    ).named(renames["enterprise-pull-request-overview"])
    types["enterprise-issue-overview"] = t.struct(
        {
            "total_issues": t.integer(),
            "open_issues": t.integer(),
            "closed_issues": t.integer(),
        }
    ).named(renames["enterprise-issue-overview"])
    types["enterprise-milestone-overview"] = t.struct(
        {
            "total_milestones": t.integer(),
            "open_milestones": t.integer(),
            "closed_milestones": t.integer(),
        }
    ).named(renames["enterprise-milestone-overview"])
    types["enterprise-gist-overview"] = t.struct(
        {
            "total_gists": t.integer(),
            "private_gists": t.integer(),
            "public_gists": t.integer(),
        }
    ).named(renames["enterprise-gist-overview"])
    types["enterprise-comment-overview"] = t.struct(
        {
            "total_commit_comments": t.integer(),
            "total_gist_comments": t.integer(),
            "total_issue_comments": t.integer(),
            "total_pull_request_comments": t.integer(),
        }
    ).named(renames["enterprise-comment-overview"])
    types["enterprise-overview"] = t.struct(
        {
            "repos": t.proxy(renames["enterprise-repository-overview"]).optional(),
            "hooks": t.proxy(renames["enterprise-hook-overview"]).optional(),
            "pages": t.proxy(renames["enterprise-page-overview"]).optional(),
            "orgs": t.proxy(renames["enterprise-organization-overview"]).optional(),
            "users": t.proxy(renames["enterprise-user-overview"]).optional(),
            "pulls": t.proxy(renames["enterprise-pull-request-overview"]).optional(),
            "issues": t.proxy(renames["enterprise-issue-overview"]).optional(),
            "milestones": t.proxy(renames["enterprise-milestone-overview"]).optional(),
            "gists": t.proxy(renames["enterprise-gist-overview"]).optional(),
            "comments": t.proxy(renames["enterprise-comment-overview"]).optional(),
        }
    ).named(renames["enterprise-overview"])
    types["enabled-organizations"] = t.string().named(renames["enabled-organizations"])
    types["allowed-actions"] = t.string().named(renames["allowed-actions"])
    types["selected-actions-url"] = t.string().named(renames["selected-actions-url"])
    types["actions-enterprise-permissions"] = t.struct(
        {
            "enabled_organizations": t.proxy(renames["enabled-organizations"]),
            "selected_organizations_url": t.string().optional(),
            "allowed_actions": t.proxy(renames["allowed-actions"]).optional(),
            "selected_actions_url": t.proxy(renames["selected-actions-url"]).optional(),
        }
    ).named(renames["actions-enterprise-permissions"])
    types["selected-actions"] = t.struct(
        {"github_owned_allowed": t.boolean(), "patterns_allowed": t.array(t.string())}
    ).named(renames["selected-actions"])
    types["runner-groups-enterprise"] = t.struct(
        {
            "id": t.number(),
            "name": t.string(),
            "visibility": t.string(),
            "default": t.boolean(),
            "selected_organizations_url": t.string().optional(),
            "runners_url": t.string(),
            "allows_public_repositories": t.boolean(),
        }
    ).named(renames["runner-groups-enterprise"])
    types["runner-label"] = t.struct(
        {
            "id": t.integer().optional(),
            "name": t.string(),
            "type": t.string().optional(),
        }
    ).named(renames["runner-label"])
    types["runner"] = t.struct(
        {
            "id": t.integer(),
            "name": t.string(),
            "os": t.string(),
            "status": t.string(),
            "busy": t.boolean(),
            "labels": t.array(t.proxy(renames["runner-label"])),
        }
    ).named(renames["runner"])
    types["runner-application"] = t.struct(
        {
            "os": t.string(),
            "architecture": t.string(),
            "download_url": t.string(),
            "filename": t.string(),
            "temp_download_token": t.string().optional(),
            "sha256_checksum": t.string().optional(),
        }
    ).named(renames["runner-application"])
    types["authentication-token"] = t.struct(
        {
            "token": t.string(),
            "expires_at": t.string(),
            "permissions": t.struct({}).optional(),
            "repositories": t.array(t.proxy(renames["repository"])).optional(),
            "single_file": t.string().optional(),
            "repository_selection": t.string().optional(),
        }
    ).named(renames["authentication-token"])
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
    types["nullable-milestone"] = (
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
                "creator": t.proxy(renames["nullable-simple-user"]),
                "open_issues": t.integer(),
                "closed_issues": t.integer(),
                "created_at": t.string(),
                "updated_at": t.string(),
                "closed_at": t.string().optional(),
                "due_on": t.string().optional(),
            }
        )
        .optional()
        .named(renames["nullable-milestone"])
    )
    types["nullable-integration"] = (
        t.struct(
            {
                "id": t.integer(),
                "slug": t.string().optional(),
                "node_id": t.string(),
                "owner": t.proxy(renames["nullable-simple-user"]),
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
        .named(renames["nullable-integration"])
    )
    types["author_association"] = t.string().named(renames["author_association"])
    types["reaction-rollup"] = t.struct(
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
    ).named(renames["reaction-rollup"])
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
            "user": t.proxy(renames["nullable-simple-user"]),
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
            "assignee": t.proxy(renames["nullable-simple-user"]),
            "assignees": t.array(t.proxy(renames["simple-user"])).optional(),
            "milestone": t.proxy(renames["nullable-milestone"]),
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
            "closed_by": t.proxy(renames["nullable-simple-user"]).optional(),
            "body_html": t.string().optional(),
            "body_text": t.string().optional(),
            "timeline_url": t.string().optional(),
            "repository": t.proxy(renames["repository"]).optional(),
            "performed_via_github_app": t.proxy(
                renames["nullable-integration"]
            ).optional(),
            "author_association": t.proxy(renames["author_association"]),
            "reactions": t.proxy(renames["reaction-rollup"]).optional(),
        }
    ).named(renames["issue"])
    types["issue-comment"] = t.struct(
        {
            "id": t.integer(),
            "node_id": t.string(),
            "url": t.string(),
            "body": t.string().optional(),
            "body_text": t.string().optional(),
            "body_html": t.string().optional(),
            "html_url": t.string(),
            "user": t.proxy(renames["nullable-simple-user"]),
            "created_at": t.string(),
            "updated_at": t.string(),
            "issue_url": t.string(),
            "author_association": t.proxy(renames["author_association"]),
            "performed_via_github_app": t.proxy(
                renames["nullable-integration"]
            ).optional(),
            "reactions": t.proxy(renames["reaction-rollup"]).optional(),
        }
    ).named(renames["issue-comment"])
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
                    "comment": t.proxy(renames["issue-comment"]).optional(),
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
    types["link-with-type"] = t.struct({"href": t.string(), "type": t.string()}).named(
        renames["link-with-type"]
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
                    "timeline": t.proxy(renames["link-with-type"]),
                    "user": t.proxy(renames["link-with-type"]),
                    "security_advisories": t.proxy(
                        renames["link-with-type"]
                    ).optional(),
                    "current_user": t.proxy(renames["link-with-type"]).optional(),
                    "current_user_public": t.proxy(
                        renames["link-with-type"]
                    ).optional(),
                    "current_user_actor": t.proxy(renames["link-with-type"]).optional(),
                    "current_user_organization": t.proxy(
                        renames["link-with-type"]
                    ).optional(),
                    "current_user_organizations": t.array(
                        t.proxy(renames["link-with-type"])
                    ).optional(),
                }
            ),
        }
    ).named(renames["feed"])
    types["base-gist"] = t.struct(
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
            "user": t.proxy(renames["nullable-simple-user"]),
            "comments_url": t.string(),
            "owner": t.proxy(renames["simple-user"]).optional(),
            "truncated": t.boolean().optional(),
            "forks": t.array(t.struct({"_": t.string().optional()})).optional(),
            "history": t.array(t.struct({"_": t.string().optional()})).optional(),
        }
    ).named(renames["base-gist"])
    types["public-user"] = t.struct(
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
    ).named(renames["public-user"])
    types["gist-history"] = t.struct(
        {
            "user": t.proxy(renames["nullable-simple-user"]).optional(),
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
    ).named(renames["gist-history"])
    types["gist-simple"] = t.struct(
        {
            "forks": t.array(
                t.struct(
                    {
                        "id": t.string().optional(),
                        "url": t.string().optional(),
                        "user": t.proxy(renames["public-user"]).optional(),
                        "created_at": t.string().optional(),
                        "updated_at": t.string().optional(),
                    }
                )
            ).optional(),
            "history": t.array(t.proxy(renames["gist-history"])).optional(),
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
                    "user": t.proxy(renames["nullable-simple-user"]),
                    "comments_url": t.string(),
                    "owner": t.proxy(renames["nullable-simple-user"]).optional(),
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
            "owner": t.proxy(renames["simple-user"]).optional(),
            "truncated": t.boolean().optional(),
        }
    ).named(renames["gist-simple"])
    types["gist-comment"] = t.struct(
        {
            "id": t.integer(),
            "node_id": t.string(),
            "url": t.string(),
            "body": t.string(),
            "user": t.proxy(renames["nullable-simple-user"]),
            "created_at": t.string(),
            "updated_at": t.string(),
            "author_association": t.proxy(renames["author_association"]),
        }
    ).named(renames["gist-comment"])
    types["gist-commit"] = t.struct(
        {
            "url": t.string(),
            "version": t.string(),
            "user": t.proxy(renames["nullable-simple-user"]),
            "change_status": t.struct(
                {
                    "total": t.integer().optional(),
                    "additions": t.integer().optional(),
                    "deletions": t.integer().optional(),
                }
            ),
            "committed_at": t.string(),
        }
    ).named(renames["gist-commit"])
    types["gitignore-template"] = t.struct(
        {"name": t.string(), "source": t.string()}
    ).named(renames["gitignore-template"])
    types["license-simple"] = t.struct(
        {
            "key": t.string(),
            "name": t.string(),
            "url": t.string().optional(),
            "spdx_id": t.string().optional(),
            "node_id": t.string(),
            "html_url": t.string().optional(),
        }
    ).named(renames["license-simple"])
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
    types["api-overview"] = t.struct(
        {
            "verifiable_password_authentication": t.boolean(),
            "packages": t.array(t.string()).optional(),
            "dependabot": t.array(t.string()).optional(),
            "installed_version": t.string().optional(),
        }
    ).named(renames["api-overview"])
    types["nullable-repository"] = (
        t.struct(
            {
                "id": t.integer(),
                "node_id": t.string(),
                "name": t.string(),
                "full_name": t.string(),
                "license": t.proxy(renames["nullable-license-simple"]),
                "organization": t.proxy(renames["nullable-simple-user"]).optional(),
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
                "owner": t.proxy(renames["simple-user"]),
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
        .named(renames["nullable-repository"])
    )
    types["minimal-repository"] = t.struct(
        {
            "id": t.integer(),
            "node_id": t.string(),
            "name": t.string(),
            "full_name": t.string(),
            "owner": t.proxy(renames["simple-user"]),
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
            "template_repository": t.proxy(renames["nullable-repository"]).optional(),
            "temp_clone_token": t.string().optional(),
            "delete_branch_on_merge": t.boolean().optional(),
            "subscribers_count": t.integer().optional(),
            "network_count": t.integer().optional(),
            "code_of_conduct": t.proxy(renames["code-of-conduct"]).optional(),
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
    ).named(renames["minimal-repository"])
    types["thread"] = t.struct(
        {
            "id": t.string(),
            "repository": t.proxy(renames["minimal-repository"]),
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
    types["thread-subscription"] = t.struct(
        {
            "subscribed": t.boolean(),
            "ignored": t.boolean(),
            "reason": t.string().optional(),
            "created_at": t.string().optional(),
            "url": t.string(),
            "thread_url": t.string().optional(),
            "repository_url": t.string().optional(),
        }
    ).named(renames["thread-subscription"])
    types["organization-full"] = t.struct(
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
    ).named(renames["organization-full"])
    types["enabled-repositories"] = t.string().named(renames["enabled-repositories"])
    types["actions-organization-permissions"] = t.struct(
        {
            "enabled_repositories": t.proxy(renames["enabled-repositories"]),
            "selected_repositories_url": t.string().optional(),
            "allowed_actions": t.proxy(renames["allowed-actions"]).optional(),
            "selected_actions_url": t.proxy(renames["selected-actions-url"]).optional(),
        }
    ).named(renames["actions-organization-permissions"])
    types["runner-groups-org"] = t.struct(
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
    ).named(renames["runner-groups-org"])
    types["organization-actions-secret"] = t.struct(
        {
            "name": t.string(),
            "created_at": t.string(),
            "updated_at": t.string(),
            "visibility": t.string(),
            "selected_repositories_url": t.string().optional(),
        }
    ).named(renames["organization-actions-secret"])
    types["actions-public-key"] = t.struct(
        {
            "key_id": t.string(),
            "key": t.string(),
            "id": t.integer().optional(),
            "url": t.string().optional(),
            "title": t.string().optional(),
            "created_at": t.string().optional(),
        }
    ).named(renames["actions-public-key"])
    types["empty-object"] = t.struct({}).named(renames["empty-object"])
    types["org-hook"] = t.struct(
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
    ).named(renames["org-hook"])
    types["org-membership"] = t.struct(
        {
            "url": t.string(),
            "state": t.string(),
            "role": t.string(),
            "organization_url": t.string(),
            "organization": t.proxy(renames["organization-simple"]),
            "user": t.proxy(renames["nullable-simple-user"]),
            "permissions": t.struct({"can_create_repository": t.boolean()}).optional(),
        }
    ).named(renames["org-membership"])
    types["org-pre-receive-hook"] = t.struct(
        {
            "id": t.integer().optional(),
            "name": t.string().optional(),
            "enforcement": t.string().optional(),
            "configuration_url": t.string().optional(),
            "allow_downstream_configuration": t.boolean().optional(),
        }
    ).named(renames["org-pre-receive-hook"])
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
            "creator": t.proxy(renames["nullable-simple-user"]),
            "created_at": t.string(),
            "updated_at": t.string(),
            "organization_permission": t.string().optional(),
            "private": t.boolean().optional(),
        }
    ).named(renames["project"])
    types["nullable-team-simple"] = (
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
        .named(renames["nullable-team-simple"])
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
            "parent": t.proxy(renames["nullable-team-simple"]),
        }
    ).named(renames["team"])
    types["team-full"] = t.struct(
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
            "parent": t.proxy(renames["nullable-team-simple"]).optional(),
            "members_count": t.integer(),
            "repos_count": t.integer(),
            "created_at": t.string(),
            "updated_at": t.string(),
            "organization": t.proxy(renames["organization-full"]),
            "ldap_dn": t.string().optional(),
        }
    ).named(renames["team-full"])
    types["team-discussion"] = t.struct(
        {
            "author": t.proxy(renames["nullable-simple-user"]),
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
            "reactions": t.proxy(renames["reaction-rollup"]).optional(),
        }
    ).named(renames["team-discussion"])
    types["team-discussion-comment"] = t.struct(
        {
            "author": t.proxy(renames["nullable-simple-user"]),
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
            "reactions": t.proxy(renames["reaction-rollup"]).optional(),
        }
    ).named(renames["team-discussion-comment"])
    types["reaction"] = t.struct(
        {
            "id": t.integer(),
            "node_id": t.string(),
            "user": t.proxy(renames["nullable-simple-user"]),
            "content": t.string(),
            "created_at": t.string(),
        }
    ).named(renames["reaction"])
    types["team-membership"] = t.struct(
        {"url": t.string(), "role": t.string(), "state": t.string()}
    ).named(renames["team-membership"])
    types["team-project"] = t.struct(
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
            "creator": t.proxy(renames["simple-user"]),
            "created_at": t.string(),
            "updated_at": t.string(),
            "organization_permission": t.string().optional(),
            "private": t.boolean().optional(),
            "permissions": t.struct(
                {"read": t.boolean(), "write": t.boolean(), "admin": t.boolean()}
            ),
        }
    ).named(renames["team-project"])
    types["team-repository"] = t.struct(
        {
            "id": t.integer(),
            "node_id": t.string(),
            "name": t.string(),
            "full_name": t.string(),
            "license": t.proxy(renames["nullable-license-simple"]),
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
            "owner": t.proxy(renames["nullable-simple-user"]),
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
            "template_repository": t.proxy(renames["nullable-repository"]).optional(),
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
    ).named(renames["team-repository"])
    types["project-card"] = t.struct(
        {
            "url": t.string(),
            "id": t.integer(),
            "node_id": t.string(),
            "note": t.string().optional(),
            "creator": t.proxy(renames["nullable-simple-user"]),
            "created_at": t.string(),
            "updated_at": t.string(),
            "archived": t.boolean().optional(),
            "column_name": t.string().optional(),
            "project_id": t.string().optional(),
            "column_url": t.string(),
            "content_url": t.string().optional(),
            "project_url": t.string(),
        }
    ).named(renames["project-card"])
    types["project-column"] = t.struct(
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
    ).named(renames["project-column"])
    types["project-collaborator-permission"] = t.struct(
        {"permission": t.string(), "user": t.proxy(renames["nullable-simple-user"])}
    ).named(renames["project-collaborator-permission"])
    types["rate-limit"] = t.struct(
        {
            "limit": t.integer(),
            "remaining": t.integer(),
            "reset": t.integer(),
            "used": t.integer(),
        }
    ).named(renames["rate-limit"])
    types["rate-limit-overview"] = t.struct(
        {
            "resources": t.struct(
                {
                    "core": t.proxy(renames["rate-limit"]),
                    "graphql": t.proxy(renames["rate-limit"]).optional(),
                    "search": t.proxy(renames["rate-limit"]),
                    "source_import": t.proxy(renames["rate-limit"]).optional(),
                    "integration_manifest": t.proxy(renames["rate-limit"]).optional(),
                    "code_scanning_upload": t.proxy(renames["rate-limit"]).optional(),
                    "actions_runner_registration": t.proxy(
                        renames["rate-limit"]
                    ).optional(),
                    "scim": t.proxy(renames["rate-limit"]).optional(),
                }
            ),
            "rate": t.proxy(renames["rate-limit"]),
        }
    ).named(renames["rate-limit-overview"])
    types["code-of-conduct-simple"] = t.struct(
        {
            "url": t.string(),
            "key": t.string(),
            "name": t.string(),
            "html_url": t.string().optional(),
        }
    ).named(renames["code-of-conduct-simple"])
    types["full-repository"] = t.struct(
        {
            "id": t.integer(),
            "node_id": t.string(),
            "name": t.string(),
            "full_name": t.string(),
            "owner": t.proxy(renames["simple-user"]),
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
            "template_repository": t.proxy(renames["nullable-repository"]).optional(),
            "temp_clone_token": t.string().optional(),
            "allow_squash_merge": t.boolean().optional(),
            "delete_branch_on_merge": t.boolean().optional(),
            "allow_merge_commit": t.boolean().optional(),
            "allow_forking": t.boolean().optional(),
            "subscribers_count": t.integer(),
            "network_count": t.integer(),
            "license": t.proxy(renames["nullable-license-simple"]),
            "organization": t.proxy(renames["nullable-simple-user"]).optional(),
            "parent": t.proxy(renames["repository"]).optional(),
            "source": t.proxy(renames["repository"]).optional(),
            "forks": t.integer(),
            "master_branch": t.string().optional(),
            "open_issues": t.integer(),
            "watchers": t.integer(),
            "anonymous_access_enabled": t.boolean().optional(),
            "code_of_conduct": t.proxy(renames["code-of-conduct-simple"]).optional(),
        }
    ).named(renames["full-repository"])
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
    types["actions-enabled"] = t.boolean().named(renames["actions-enabled"])
    types["actions-repository-permissions"] = t.struct(
        {
            "enabled": t.proxy(renames["actions-enabled"]),
            "allowed_actions": t.proxy(renames["allowed-actions"]).optional(),
            "selected_actions_url": t.proxy(renames["selected-actions-url"]).optional(),
        }
    ).named(renames["actions-repository-permissions"])
    types["pull-request-minimal"] = t.struct(
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
    ).named(renames["pull-request-minimal"])
    types["nullable-simple-commit"] = (
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
        .named(renames["nullable-simple-commit"])
    )
    types["workflow-run"] = t.struct(
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
                t.proxy(renames["pull-request-minimal"])
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
            "head_commit": t.proxy(renames["nullable-simple-commit"]),
            "repository": t.proxy(renames["minimal-repository"]),
            "head_repository": t.proxy(renames["minimal-repository"]),
            "head_repository_id": t.integer().optional(),
        }
    ).named(renames["workflow-run"])
    types["actions-secret"] = t.struct(
        {"name": t.string(), "created_at": t.string(), "updated_at": t.string()}
    ).named(renames["actions-secret"])
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
    types["protected-branch-required-status-check"] = t.struct(
        {
            "url": t.string().optional(),
            "enforcement_level": t.string().optional(),
            "contexts": t.array(t.string()),
            "contexts_url": t.string().optional(),
            "strict": t.boolean().optional(),
        }
    ).named(renames["protected-branch-required-status-check"])
    types["protected-branch-admin-enforced"] = t.struct(
        {"url": t.string(), "enabled": t.boolean()}
    ).named(renames["protected-branch-admin-enforced"])
    types["protected-branch-pull-request-review"] = t.struct(
        {
            "url": t.string().optional(),
            "dismissal_restrictions": t.struct(
                {
                    "users": t.array(t.proxy(renames["simple-user"])).optional(),
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
    ).named(renames["protected-branch-pull-request-review"])
    types["branch-restriction-policy"] = t.struct(
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
    ).named(renames["branch-restriction-policy"])
    types["branch-protection"] = t.struct(
        {
            "url": t.string().optional(),
            "enabled": t.boolean().optional(),
            "required_status_checks": t.proxy(
                renames["protected-branch-required-status-check"]
            ).optional(),
            "enforce_admins": t.proxy(
                renames["protected-branch-admin-enforced"]
            ).optional(),
            "required_pull_request_reviews": t.proxy(
                renames["protected-branch-pull-request-review"]
            ).optional(),
            "restrictions": t.proxy(renames["branch-restriction-policy"]).optional(),
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
    ).named(renames["branch-protection"])
    types["short-branch"] = t.struct(
        {
            "name": t.string(),
            "commit": t.struct({"sha": t.string(), "url": t.string()}),
            "protected": t.boolean(),
            "protection": t.proxy(renames["branch-protection"]).optional(),
            "protection_url": t.string().optional(),
        }
    ).named(renames["short-branch"])
    types["nullable-git-user"] = (
        t.struct(
            {
                "name": t.string().optional(),
                "email": t.string().optional(),
                "date": t.string().optional(),
            }
        )
        .optional()
        .named(renames["nullable-git-user"])
    )
    types["verification"] = t.struct(
        {
            "verified": t.boolean(),
            "reason": t.string(),
            "payload": t.string().optional(),
            "signature": t.string().optional(),
        }
    ).named(renames["verification"])
    types["diff-entry"] = t.struct(
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
    ).named(renames["diff-entry"])
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
                    "author": t.proxy(renames["nullable-git-user"]),
                    "committer": t.proxy(renames["nullable-git-user"]),
                    "message": t.string(),
                    "comment_count": t.integer(),
                    "tree": t.struct({"sha": t.string(), "url": t.string()}),
                    "verification": t.proxy(renames["verification"]).optional(),
                }
            ),
            "author": t.proxy(renames["nullable-simple-user"]),
            "committer": t.proxy(renames["nullable-simple-user"]),
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
            "files": t.array(t.proxy(renames["diff-entry"])).optional(),
        }
    ).named(renames["commit"])
    types["branch-with-protection"] = t.struct(
        {
            "name": t.string(),
            "commit": t.proxy(renames["commit"]),
            "_links": t.struct({"html": t.string(), "self": t.string()}),
            "protected": t.boolean(),
            "protection": t.proxy(renames["branch-protection"]),
            "protection_url": t.string(),
            "pattern": t.string().optional(),
            "required_approving_review_count": t.integer().optional(),
        }
    ).named(renames["branch-with-protection"])
    types["status-check-policy"] = t.struct(
        {
            "url": t.string(),
            "strict": t.boolean(),
            "contexts": t.array(t.string()),
            "contexts_url": t.string(),
        }
    ).named(renames["status-check-policy"])
    types["protected-branch"] = t.struct(
        {
            "url": t.string(),
            "required_status_checks": t.proxy(
                renames["status-check-policy"]
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
                            "users": t.array(t.proxy(renames["simple-user"])),
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
            "restrictions": t.proxy(renames["branch-restriction-policy"]).optional(),
            "required_conversation_resolution": t.struct(
                {"enabled": t.boolean().optional()}
            ).optional(),
        }
    ).named(renames["protected-branch"])
    types["deployment-simple"] = t.struct(
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
                renames["nullable-integration"]
            ).optional(),
        }
    ).named(renames["deployment-simple"])
    types["check-run"] = t.struct(
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
            "app": t.proxy(renames["nullable-integration"]),
            "pull_requests": t.array(t.proxy(renames["pull-request-minimal"])),
            "deployment": t.proxy(renames["deployment-simple"]).optional(),
        }
    ).named(renames["check-run"])
    types["check-annotation"] = t.struct(
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
    ).named(renames["check-annotation"])
    types["simple-commit"] = t.struct(
        {
            "id": t.string(),
            "tree_id": t.string(),
            "message": t.string(),
            "timestamp": t.string(),
            "author": t.struct({"name": t.string(), "email": t.string()}).optional(),
            "committer": t.struct({"name": t.string(), "email": t.string()}).optional(),
        }
    ).named(renames["simple-commit"])
    types["check-suite"] = t.struct(
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
                t.proxy(renames["pull-request-minimal"])
            ).optional(),
            "app": t.proxy(renames["nullable-integration"]),
            "repository": t.proxy(renames["minimal-repository"]),
            "created_at": t.string().optional(),
            "updated_at": t.string().optional(),
            "head_commit": t.proxy(renames["simple-commit"]),
            "latest_check_runs_count": t.integer(),
            "check_runs_url": t.string(),
            "rerequestable": t.boolean().optional(),
            "runs_rerequestable": t.boolean().optional(),
        }
    ).named(renames["check-suite"])
    types["check-suite-preference"] = t.struct(
        {
            "preferences": t.struct(
                {
                    "auto_trigger_checks": t.array(
                        t.struct({"app_id": t.integer(), "setting": t.boolean()})
                    ).optional()
                }
            ),
            "repository": t.proxy(renames["minimal-repository"]),
        }
    ).named(renames["check-suite-preference"])
    types["code-scanning-analysis-tool-name"] = t.string().named(
        renames["code-scanning-analysis-tool-name"]
    )
    types["code-scanning-analysis-tool-guid"] = (
        t.string().optional().named(renames["code-scanning-analysis-tool-guid"])
    )
    types["code-scanning-ref"] = t.string().named(renames["code-scanning-ref"])
    types["code-scanning-alert-state"] = t.string().named(
        renames["code-scanning-alert-state"]
    )
    types["alert-number"] = t.integer().named(renames["alert-number"])
    types["alert-created-at"] = t.string().named(renames["alert-created-at"])
    types["alert-url"] = t.string().named(renames["alert-url"])
    types["alert-html-url"] = t.string().named(renames["alert-html-url"])
    types["alert-instances-url"] = t.string().named(renames["alert-instances-url"])
    types["code-scanning-alert-dismissed-at"] = (
        t.string().optional().named(renames["code-scanning-alert-dismissed-at"])
    )
    types["code-scanning-alert-dismissed-reason"] = (
        t.string().optional().named(renames["code-scanning-alert-dismissed-reason"])
    )
    types["code-scanning-alert-rule-summary"] = t.struct(
        {
            "id": t.string().optional(),
            "name": t.string().optional(),
            "severity": t.string().optional(),
            "description": t.string().optional(),
        }
    ).named(renames["code-scanning-alert-rule-summary"])
    types["code-scanning-analysis-tool-version"] = (
        t.string().optional().named(renames["code-scanning-analysis-tool-version"])
    )
    types["code-scanning-analysis-tool"] = t.struct(
        {
            "name": t.proxy(renames["code-scanning-analysis-tool-name"]).optional(),
            "version": t.proxy(
                renames["code-scanning-analysis-tool-version"]
            ).optional(),
            "guid": t.proxy(renames["code-scanning-analysis-tool-guid"]).optional(),
        }
    ).named(renames["code-scanning-analysis-tool"])
    types["code-scanning-analysis-analysis-key"] = t.string().named(
        renames["code-scanning-analysis-analysis-key"]
    )
    types["code-scanning-alert-environment"] = t.string().named(
        renames["code-scanning-alert-environment"]
    )
    types["code-scanning-analysis-category"] = t.string().named(
        renames["code-scanning-analysis-category"]
    )
    types["code-scanning-alert-location"] = t.struct(
        {
            "path": t.string().optional(),
            "start_line": t.integer().optional(),
            "end_line": t.integer().optional(),
            "start_column": t.integer().optional(),
            "end_column": t.integer().optional(),
        }
    ).named(renames["code-scanning-alert-location"])
    types["code-scanning-alert-classification"] = (
        t.string().optional().named(renames["code-scanning-alert-classification"])
    )
    types["code-scanning-alert-instance"] = t.struct(
        {
            "ref": t.proxy(renames["code-scanning-ref"]).optional(),
            "analysis_key": t.proxy(
                renames["code-scanning-analysis-analysis-key"]
            ).optional(),
            "environment": t.proxy(
                renames["code-scanning-alert-environment"]
            ).optional(),
            "category": t.proxy(renames["code-scanning-analysis-category"]).optional(),
            "state": t.proxy(renames["code-scanning-alert-state"]).optional(),
            "commit_sha": t.string().optional(),
            "message": t.struct({"text": t.string().optional()}).optional(),
            "location": t.proxy(renames["code-scanning-alert-location"]).optional(),
            "html_url": t.string().optional(),
            "classifications": t.array(
                t.proxy(renames["code-scanning-alert-classification"])
            ).optional(),
        }
    ).named(renames["code-scanning-alert-instance"])
    types["code-scanning-alert-items"] = t.struct(
        {
            "number": t.proxy(renames["alert-number"]),
            "created_at": t.proxy(renames["alert-created-at"]),
            "url": t.proxy(renames["alert-url"]),
            "html_url": t.proxy(renames["alert-html-url"]),
            "instances_url": t.proxy(renames["alert-instances-url"]),
            "state": t.proxy(renames["code-scanning-alert-state"]),
            "dismissed_by": t.proxy(renames["nullable-simple-user"]),
            "dismissed_at": t.proxy(renames["code-scanning-alert-dismissed-at"]),
            "dismissed_reason": t.proxy(
                renames["code-scanning-alert-dismissed-reason"]
            ),
            "rule": t.proxy(renames["code-scanning-alert-rule-summary"]),
            "tool": t.proxy(renames["code-scanning-analysis-tool"]),
            "most_recent_instance": t.proxy(renames["code-scanning-alert-instance"]),
        }
    ).named(renames["code-scanning-alert-items"])
    types["code-scanning-alert-rule"] = t.struct(
        {
            "id": t.string().optional(),
            "name": t.string().optional(),
            "severity": t.string().optional(),
            "description": t.string().optional(),
            "full_description": t.string().optional(),
            "tags": t.array(t.string()).optional(),
            "help": t.string().optional(),
        }
    ).named(renames["code-scanning-alert-rule"])
    types["code-scanning-alert"] = t.struct(
        {
            "number": t.proxy(renames["alert-number"]),
            "created_at": t.proxy(renames["alert-created-at"]),
            "url": t.proxy(renames["alert-url"]),
            "html_url": t.proxy(renames["alert-html-url"]),
            "instances_url": t.proxy(renames["alert-instances-url"]),
            "state": t.proxy(renames["code-scanning-alert-state"]),
            "dismissed_by": t.proxy(renames["nullable-simple-user"]),
            "dismissed_at": t.proxy(renames["code-scanning-alert-dismissed-at"]),
            "dismissed_reason": t.proxy(
                renames["code-scanning-alert-dismissed-reason"]
            ),
            "rule": t.proxy(renames["code-scanning-alert-rule"]),
            "tool": t.proxy(renames["code-scanning-analysis-tool"]),
            "most_recent_instance": t.proxy(renames["code-scanning-alert-instance"]),
            "instances": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["code-scanning-alert"])
    types["code-scanning-alert-set-state"] = t.string().named(
        renames["code-scanning-alert-set-state"]
    )
    types["code-scanning-analysis-sarif-id"] = t.string().named(
        renames["code-scanning-analysis-sarif-id"]
    )
    types["code-scanning-analysis-commit-sha"] = t.string().named(
        renames["code-scanning-analysis-commit-sha"]
    )
    types["code-scanning-analysis-environment"] = t.string().named(
        renames["code-scanning-analysis-environment"]
    )
    types["code-scanning-analysis-created-at"] = t.string().named(
        renames["code-scanning-analysis-created-at"]
    )
    types["code-scanning-analysis-url"] = t.string().named(
        renames["code-scanning-analysis-url"]
    )
    types["code-scanning-analysis"] = t.struct(
        {
            "ref": t.proxy(renames["code-scanning-ref"]),
            "commit_sha": t.proxy(renames["code-scanning-analysis-commit-sha"]),
            "analysis_key": t.proxy(renames["code-scanning-analysis-analysis-key"]),
            "environment": t.proxy(renames["code-scanning-analysis-environment"]),
            "category": t.proxy(renames["code-scanning-analysis-category"]).optional(),
            "error": t.string(),
            "created_at": t.proxy(renames["code-scanning-analysis-created-at"]),
            "results_count": t.integer(),
            "rules_count": t.integer(),
            "id": t.integer(),
            "url": t.proxy(renames["code-scanning-analysis-url"]),
            "sarif_id": t.proxy(renames["code-scanning-analysis-sarif-id"]),
            "tool": t.proxy(renames["code-scanning-analysis-tool"]),
            "deletable": t.boolean(),
            "warning": t.string(),
            "tool_name": t.string().optional(),
        }
    ).named(renames["code-scanning-analysis"])
    types["code-scanning-analysis-sarif-file"] = t.string().named(
        renames["code-scanning-analysis-sarif-file"]
    )
    types["code-scanning-sarifs-receipt"] = t.struct(
        {
            "id": t.proxy(renames["code-scanning-analysis-sarif-id"]).optional(),
            "url": t.string().optional(),
        }
    ).named(renames["code-scanning-sarifs-receipt"])
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
    types["repository-invitation"] = t.struct(
        {
            "id": t.integer(),
            "repository": t.proxy(renames["minimal-repository"]),
            "invitee": t.proxy(renames["nullable-simple-user"]),
            "inviter": t.proxy(renames["nullable-simple-user"]),
            "permissions": t.string(),
            "created_at": t.string(),
            "expired": t.boolean().optional(),
            "url": t.string(),
            "html_url": t.string(),
            "node_id": t.string(),
        }
    ).named(renames["repository-invitation"])
    types["nullable-collaborator"] = (
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
        .named(renames["nullable-collaborator"])
    )
    types["repository-collaborator-permission"] = t.struct(
        {"permission": t.string(), "user": t.proxy(renames["nullable-collaborator"])}
    ).named(renames["repository-collaborator-permission"])
    types["commit-comment"] = t.struct(
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
            "user": t.proxy(renames["nullable-simple-user"]),
            "created_at": t.string(),
            "updated_at": t.string(),
            "author_association": t.proxy(renames["author_association"]),
            "reactions": t.proxy(renames["reaction-rollup"]).optional(),
        }
    ).named(renames["commit-comment"])
    types["scim-error"] = t.struct(
        {
            "message": t.string().optional(),
            "documentation_url": t.string().optional(),
            "detail": t.string().optional(),
            "status": t.integer().optional(),
            "scimType": t.string().optional(),
            "schemas": t.array(t.string()).optional(),
        }
    ).named(renames["scim-error"])
    types["branch-short"] = t.struct(
        {
            "name": t.string(),
            "commit": t.struct({"sha": t.string(), "url": t.string()}),
            "protected": t.boolean(),
        }
    ).named(renames["branch-short"])
    types["link"] = t.struct({"href": t.string()}).named(renames["link"])
    types["pull-request-simple"] = t.struct(
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
            "user": t.proxy(renames["nullable-simple-user"]),
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
            "milestone": t.proxy(renames["nullable-milestone"]),
            "active_lock_reason": t.string().optional(),
            "created_at": t.string(),
            "updated_at": t.string(),
            "closed_at": t.string().optional(),
            "merged_at": t.string().optional(),
            "merge_commit_sha": t.string().optional(),
            "assignee": t.proxy(renames["nullable-simple-user"]),
            "assignees": t.array(t.proxy(renames["simple-user"])).optional(),
            "requested_reviewers": t.array(t.proxy(renames["simple-user"])).optional(),
            "requested_teams": t.array(t.proxy(renames["team"])).optional(),
            "head": t.struct(
                {
                    "label": t.string(),
                    "ref": t.string(),
                    "repo": t.proxy(renames["repository"]),
                    "sha": t.string(),
                    "user": t.proxy(renames["nullable-simple-user"]),
                }
            ),
            "base": t.struct(
                {
                    "label": t.string(),
                    "ref": t.string(),
                    "repo": t.proxy(renames["repository"]),
                    "sha": t.string(),
                    "user": t.proxy(renames["nullable-simple-user"]),
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
    ).named(renames["pull-request-simple"])
    types["simple-commit-status"] = t.struct(
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
    ).named(renames["simple-commit-status"])
    types["combined-commit-status"] = t.struct(
        {
            "state": t.string(),
            "statuses": t.array(t.proxy(renames["simple-commit-status"])),
            "sha": t.string(),
            "total_count": t.integer(),
            "repository": t.proxy(renames["minimal-repository"]),
            "commit_url": t.string(),
            "url": t.string(),
        }
    ).named(renames["combined-commit-status"])
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
            "creator": t.proxy(renames["nullable-simple-user"]),
        }
    ).named(renames["status"])
    types["commit-comparison"] = t.struct(
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
            "files": t.array(t.proxy(renames["diff-entry"])).optional(),
        }
    ).named(renames["commit-comparison"])
    types["content-reference-attachment"] = t.struct(
        {
            "id": t.integer(),
            "title": t.string(),
            "body": t.string(),
            "node_id": t.string().optional(),
        }
    ).named(renames["content-reference-attachment"])
    types["content-tree"] = t.struct(
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
    ).named(renames["content-tree"])
    types["content-directory"] = t.array(
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
    ).named(renames["content-directory"])
    types["content-file"] = t.struct(
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
    ).named(renames["content-file"])
    types["content-symlink"] = t.struct(
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
    ).named(renames["content-symlink"])
    types["content-submodule"] = t.struct(
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
    ).named(renames["content-submodule"])
    types["file-commit"] = t.struct(
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
    ).named(renames["file-commit"])
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
            "creator": t.proxy(renames["nullable-simple-user"]),
            "created_at": t.string(),
            "updated_at": t.string(),
            "statuses_url": t.string(),
            "repository_url": t.string(),
            "transient_environment": t.boolean().optional(),
            "production_environment": t.boolean().optional(),
            "performed_via_github_app": t.proxy(
                renames["nullable-integration"]
            ).optional(),
        }
    ).named(renames["deployment"])
    types["deployment-status"] = t.struct(
        {
            "url": t.string(),
            "id": t.integer(),
            "node_id": t.string(),
            "state": t.string(),
            "creator": t.proxy(renames["nullable-simple-user"]),
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
                renames["nullable-integration"]
            ).optional(),
        }
    ).named(renames["deployment-status"])
    types["short-blob"] = t.struct({"url": t.string(), "sha": t.string()}).named(
        renames["short-blob"]
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
    types["git-commit"] = t.struct(
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
    ).named(renames["git-commit"])
    types["git-ref"] = t.struct(
        {
            "ref": t.string(),
            "node_id": t.string(),
            "url": t.string(),
            "object": t.struct(
                {"type": t.string(), "sha": t.string(), "url": t.string()}
            ),
        }
    ).named(renames["git-ref"])
    types["git-tag"] = t.struct(
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
    ).named(renames["git-tag"])
    types["git-tree"] = t.struct(
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
    ).named(renames["git-tree"])
    types["hook-response"] = t.struct(
        {
            "code": t.integer().optional(),
            "status": t.string().optional(),
            "message": t.string().optional(),
        }
    ).named(renames["hook-response"])
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
                    "url": t.proxy(renames["webhook-config-url"]).optional(),
                    "insecure_ssl": t.proxy(
                        renames["webhook-config-insecure-ssl"]
                    ).optional(),
                    "content_type": t.proxy(
                        renames["webhook-config-content-type"]
                    ).optional(),
                    "digest": t.string().optional(),
                    "secret": t.proxy(renames["webhook-config-secret"]).optional(),
                    "token": t.string().optional(),
                }
            ),
            "updated_at": t.string(),
            "created_at": t.string(),
            "url": t.string(),
            "test_url": t.string(),
            "ping_url": t.string(),
            "last_response": t.proxy(renames["hook-response"]),
        }
    ).named(renames["hook"])
    types["nullable-issue"] = (
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
                "user": t.proxy(renames["nullable-simple-user"]),
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
                "assignee": t.proxy(renames["nullable-simple-user"]),
                "assignees": t.array(t.proxy(renames["simple-user"])).optional(),
                "milestone": t.proxy(renames["nullable-milestone"]),
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
                "closed_by": t.proxy(renames["nullable-simple-user"]).optional(),
                "body_html": t.string().optional(),
                "body_text": t.string().optional(),
                "timeline_url": t.string().optional(),
                "repository": t.proxy(renames["repository"]).optional(),
                "performed_via_github_app": t.proxy(
                    renames["nullable-integration"]
                ).optional(),
                "author_association": t.proxy(renames["author_association"]),
                "reactions": t.proxy(renames["reaction-rollup"]).optional(),
            }
        )
        .optional()
        .named(renames["nullable-issue"])
    )
    types["issue-event-label"] = t.struct(
        {"name": t.string().optional(), "color": t.string().optional()}
    ).named(renames["issue-event-label"])
    types["issue-event-dismissed-review"] = t.struct(
        {
            "state": t.string(),
            "review_id": t.integer(),
            "dismissal_message": t.string().optional(),
            "dismissal_commit_id": t.string().optional(),
        }
    ).named(renames["issue-event-dismissed-review"])
    types["issue-event-milestone"] = t.struct({"title": t.string()}).named(
        renames["issue-event-milestone"]
    )
    types["issue-event-project-card"] = t.struct(
        {
            "url": t.string(),
            "id": t.integer(),
            "project_url": t.string(),
            "project_id": t.integer(),
            "column_name": t.string(),
            "previous_column_name": t.string().optional(),
        }
    ).named(renames["issue-event-project-card"])
    types["issue-event-rename"] = t.struct(
        {"from": t.string(), "to": t.string()}
    ).named(renames["issue-event-rename"])
    types["issue-event"] = t.struct(
        {
            "id": t.integer(),
            "node_id": t.string(),
            "url": t.string(),
            "actor": t.proxy(renames["nullable-simple-user"]),
            "event": t.string(),
            "commit_id": t.string().optional(),
            "commit_url": t.string().optional(),
            "created_at": t.string(),
            "issue": t.proxy(renames["nullable-issue"]).optional(),
            "label": t.proxy(renames["issue-event-label"]).optional(),
            "assignee": t.proxy(renames["nullable-simple-user"]).optional(),
            "assigner": t.proxy(renames["nullable-simple-user"]).optional(),
            "review_requester": t.proxy(renames["nullable-simple-user"]).optional(),
            "requested_reviewer": t.proxy(renames["nullable-simple-user"]).optional(),
            "requested_team": t.proxy(renames["team"]).optional(),
            "dismissed_review": t.proxy(
                renames["issue-event-dismissed-review"]
            ).optional(),
            "milestone": t.proxy(renames["issue-event-milestone"]).optional(),
            "project_card": t.proxy(renames["issue-event-project-card"]).optional(),
            "rename": t.proxy(renames["issue-event-rename"]).optional(),
            "author_association": t.proxy(renames["author_association"]).optional(),
            "lock_reason": t.string().optional(),
            "performed_via_github_app": t.proxy(
                renames["nullable-integration"]
            ).optional(),
        }
    ).named(renames["issue-event"])
    types["labeled-issue-event"] = t.struct(
        {
            "id": t.integer(),
            "node_id": t.string(),
            "url": t.string(),
            "actor": t.proxy(renames["simple-user"]),
            "event": t.string(),
            "commit_id": t.string().optional(),
            "commit_url": t.string().optional(),
            "created_at": t.string(),
            "performed_via_github_app": t.proxy(renames["nullable-integration"]),
            "label": t.struct({"name": t.string(), "color": t.string()}),
        }
    ).named(renames["labeled-issue-event"])
    types["unlabeled-issue-event"] = t.struct(
        {
            "id": t.integer(),
            "node_id": t.string(),
            "url": t.string(),
            "actor": t.proxy(renames["simple-user"]),
            "event": t.string(),
            "commit_id": t.string().optional(),
            "commit_url": t.string().optional(),
            "created_at": t.string(),
            "performed_via_github_app": t.proxy(renames["nullable-integration"]),
            "label": t.struct({"name": t.string(), "color": t.string()}),
        }
    ).named(renames["unlabeled-issue-event"])
    types["assigned-issue-event"] = t.struct(
        {
            "id": t.integer(),
            "node_id": t.string(),
            "url": t.string(),
            "actor": t.proxy(renames["simple-user"]),
            "event": t.string(),
            "commit_id": t.string().optional(),
            "commit_url": t.string().optional(),
            "created_at": t.string(),
            "performed_via_github_app": t.proxy(renames["integration"]),
            "assignee": t.proxy(renames["simple-user"]),
            "assigner": t.proxy(renames["simple-user"]),
        }
    ).named(renames["assigned-issue-event"])
    types["unassigned-issue-event"] = t.struct(
        {
            "id": t.integer(),
            "node_id": t.string(),
            "url": t.string(),
            "actor": t.proxy(renames["simple-user"]),
            "event": t.string(),
            "commit_id": t.string().optional(),
            "commit_url": t.string().optional(),
            "created_at": t.string(),
            "performed_via_github_app": t.proxy(renames["nullable-integration"]),
            "assignee": t.proxy(renames["simple-user"]),
            "assigner": t.proxy(renames["simple-user"]),
        }
    ).named(renames["unassigned-issue-event"])
    types["milestoned-issue-event"] = t.struct(
        {
            "id": t.integer(),
            "node_id": t.string(),
            "url": t.string(),
            "actor": t.proxy(renames["simple-user"]),
            "event": t.string(),
            "commit_id": t.string().optional(),
            "commit_url": t.string().optional(),
            "created_at": t.string(),
            "performed_via_github_app": t.proxy(renames["nullable-integration"]),
            "milestone": t.struct({"title": t.string()}),
        }
    ).named(renames["milestoned-issue-event"])
    types["demilestoned-issue-event"] = t.struct(
        {
            "id": t.integer(),
            "node_id": t.string(),
            "url": t.string(),
            "actor": t.proxy(renames["simple-user"]),
            "event": t.string(),
            "commit_id": t.string().optional(),
            "commit_url": t.string().optional(),
            "created_at": t.string(),
            "performed_via_github_app": t.proxy(renames["nullable-integration"]),
            "milestone": t.struct({"title": t.string()}),
        }
    ).named(renames["demilestoned-issue-event"])
    types["renamed-issue-event"] = t.struct(
        {
            "id": t.integer(),
            "node_id": t.string(),
            "url": t.string(),
            "actor": t.proxy(renames["simple-user"]),
            "event": t.string(),
            "commit_id": t.string().optional(),
            "commit_url": t.string().optional(),
            "created_at": t.string(),
            "performed_via_github_app": t.proxy(renames["nullable-integration"]),
            "rename": t.struct({"from": t.string(), "to": t.string()}),
        }
    ).named(renames["renamed-issue-event"])
    types["review-requested-issue-event"] = t.struct(
        {
            "id": t.integer(),
            "node_id": t.string(),
            "url": t.string(),
            "actor": t.proxy(renames["simple-user"]),
            "event": t.string(),
            "commit_id": t.string().optional(),
            "commit_url": t.string().optional(),
            "created_at": t.string(),
            "performed_via_github_app": t.proxy(renames["nullable-integration"]),
            "review_requester": t.proxy(renames["simple-user"]),
            "requested_team": t.proxy(renames["team"]).optional(),
            "requested_reviewer": t.proxy(renames["simple-user"]).optional(),
        }
    ).named(renames["review-requested-issue-event"])
    types["review-request-removed-issue-event"] = t.struct(
        {
            "id": t.integer(),
            "node_id": t.string(),
            "url": t.string(),
            "actor": t.proxy(renames["simple-user"]),
            "event": t.string(),
            "commit_id": t.string().optional(),
            "commit_url": t.string().optional(),
            "created_at": t.string(),
            "performed_via_github_app": t.proxy(renames["nullable-integration"]),
            "review_requester": t.proxy(renames["simple-user"]),
            "requested_team": t.proxy(renames["team"]).optional(),
            "requested_reviewer": t.proxy(renames["simple-user"]).optional(),
        }
    ).named(renames["review-request-removed-issue-event"])
    types["review-dismissed-issue-event"] = t.struct(
        {
            "id": t.integer(),
            "node_id": t.string(),
            "url": t.string(),
            "actor": t.proxy(renames["simple-user"]),
            "event": t.string(),
            "commit_id": t.string().optional(),
            "commit_url": t.string().optional(),
            "created_at": t.string(),
            "performed_via_github_app": t.proxy(renames["nullable-integration"]),
            "dismissed_review": t.struct(
                {
                    "state": t.string(),
                    "review_id": t.integer(),
                    "dismissal_message": t.string().optional(),
                    "dismissal_commit_id": t.string().optional(),
                }
            ),
        }
    ).named(renames["review-dismissed-issue-event"])
    types["locked-issue-event"] = t.struct(
        {
            "id": t.integer(),
            "node_id": t.string(),
            "url": t.string(),
            "actor": t.proxy(renames["simple-user"]),
            "event": t.string(),
            "commit_id": t.string().optional(),
            "commit_url": t.string().optional(),
            "created_at": t.string(),
            "performed_via_github_app": t.proxy(renames["nullable-integration"]),
            "lock_reason": t.string().optional(),
        }
    ).named(renames["locked-issue-event"])
    types["added-to-project-issue-event"] = t.struct(
        {
            "id": t.integer(),
            "node_id": t.string(),
            "url": t.string(),
            "actor": t.proxy(renames["simple-user"]),
            "event": t.string(),
            "commit_id": t.string().optional(),
            "commit_url": t.string().optional(),
            "created_at": t.string(),
            "performed_via_github_app": t.proxy(renames["nullable-integration"]),
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
    ).named(renames["added-to-project-issue-event"])
    types["moved-column-in-project-issue-event"] = t.struct(
        {
            "id": t.integer(),
            "node_id": t.string(),
            "url": t.string(),
            "actor": t.proxy(renames["simple-user"]),
            "event": t.string(),
            "commit_id": t.string().optional(),
            "commit_url": t.string().optional(),
            "created_at": t.string(),
            "performed_via_github_app": t.proxy(renames["nullable-integration"]),
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
    ).named(renames["moved-column-in-project-issue-event"])
    types["removed-from-project-issue-event"] = t.struct(
        {
            "id": t.integer(),
            "node_id": t.string(),
            "url": t.string(),
            "actor": t.proxy(renames["simple-user"]),
            "event": t.string(),
            "commit_id": t.string().optional(),
            "commit_url": t.string().optional(),
            "created_at": t.string(),
            "performed_via_github_app": t.proxy(renames["nullable-integration"]),
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
    ).named(renames["removed-from-project-issue-event"])
    types["converted-note-to-issue-issue-event"] = t.struct(
        {
            "id": t.integer(),
            "node_id": t.string(),
            "url": t.string(),
            "actor": t.proxy(renames["simple-user"]),
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
    ).named(renames["converted-note-to-issue-issue-event"])
    types["issue-event-for-issue"] = t.union(
        [
            t.proxy(renames["labeled-issue-event"]),
            t.proxy(renames["unlabeled-issue-event"]),
            t.proxy(renames["assigned-issue-event"]),
            t.proxy(renames["unassigned-issue-event"]),
            t.proxy(renames["milestoned-issue-event"]),
            t.proxy(renames["demilestoned-issue-event"]),
            t.proxy(renames["renamed-issue-event"]),
            t.proxy(renames["review-requested-issue-event"]),
            t.proxy(renames["review-request-removed-issue-event"]),
            t.proxy(renames["review-dismissed-issue-event"]),
            t.proxy(renames["locked-issue-event"]),
            t.proxy(renames["added-to-project-issue-event"]),
            t.proxy(renames["moved-column-in-project-issue-event"]),
            t.proxy(renames["removed-from-project-issue-event"]),
            t.proxy(renames["converted-note-to-issue-issue-event"]),
        ]
    ).named(renames["issue-event-for-issue"])
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
    types["timeline-comment-event"] = t.struct(
        {
            "event": t.string(),
            "actor": t.proxy(renames["simple-user"]),
            "id": t.integer(),
            "node_id": t.string(),
            "url": t.string(),
            "body": t.string().optional(),
            "body_text": t.string().optional(),
            "body_html": t.string().optional(),
            "html_url": t.string(),
            "user": t.proxy(renames["simple-user"]),
            "created_at": t.string(),
            "updated_at": t.string(),
            "issue_url": t.string(),
            "author_association": t.proxy(renames["author_association"]),
            "performed_via_github_app": t.proxy(
                renames["nullable-integration"]
            ).optional(),
            "reactions": t.proxy(renames["reaction-rollup"]).optional(),
        }
    ).named(renames["timeline-comment-event"])
    types["timeline-cross-referenced-event"] = t.struct(
        {
            "event": t.string(),
            "actor": t.proxy(renames["simple-user"]).optional(),
            "created_at": t.string(),
            "updated_at": t.string(),
            "source": t.struct(
                {
                    "type": t.string().optional(),
                    "issue": t.proxy(renames["issue"]).optional(),
                }
            ),
        }
    ).named(renames["timeline-cross-referenced-event"])
    types["timeline-committed-event"] = t.struct(
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
    ).named(renames["timeline-committed-event"])
    types["timeline-reviewed-event"] = t.struct(
        {
            "event": t.string(),
            "id": t.integer(),
            "node_id": t.string(),
            "user": t.proxy(renames["simple-user"]),
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
    ).named(renames["timeline-reviewed-event"])
    types["pull-request-review-comment"] = t.struct(
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
            "user": t.proxy(renames["simple-user"]),
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
            "reactions": t.proxy(renames["reaction-rollup"]).optional(),
            "body_html": t.string().optional(),
            "body_text": t.string().optional(),
        }
    ).named(renames["pull-request-review-comment"])
    types["timeline-line-commented-event"] = t.struct(
        {
            "event": t.string().optional(),
            "node_id": t.string().optional(),
            "comments": t.array(
                t.proxy(renames["pull-request-review-comment"])
            ).optional(),
        }
    ).named(renames["timeline-line-commented-event"])
    types["timeline-commit-commented-event"] = t.struct(
        {
            "event": t.string().optional(),
            "node_id": t.string().optional(),
            "commit_id": t.string().optional(),
            "comments": t.array(t.proxy(renames["commit-comment"])).optional(),
        }
    ).named(renames["timeline-commit-commented-event"])
    types["timeline-assigned-issue-event"] = t.struct(
        {
            "id": t.integer(),
            "node_id": t.string(),
            "url": t.string(),
            "actor": t.proxy(renames["simple-user"]),
            "event": t.string(),
            "commit_id": t.string().optional(),
            "commit_url": t.string().optional(),
            "created_at": t.string(),
            "performed_via_github_app": t.proxy(renames["nullable-integration"]),
            "assignee": t.proxy(renames["simple-user"]),
        }
    ).named(renames["timeline-assigned-issue-event"])
    types["timeline-unassigned-issue-event"] = t.struct(
        {
            "id": t.integer(),
            "node_id": t.string(),
            "url": t.string(),
            "actor": t.proxy(renames["simple-user"]),
            "event": t.string(),
            "commit_id": t.string().optional(),
            "commit_url": t.string().optional(),
            "created_at": t.string(),
            "performed_via_github_app": t.proxy(renames["nullable-integration"]),
            "assignee": t.proxy(renames["simple-user"]),
        }
    ).named(renames["timeline-unassigned-issue-event"])
    types["state-change-issue-event"] = t.struct(
        {
            "id": t.integer(),
            "node_id": t.string(),
            "url": t.string(),
            "actor": t.proxy(renames["simple-user"]),
            "event": t.string(),
            "commit_id": t.string().optional(),
            "commit_url": t.string().optional(),
            "created_at": t.string(),
            "performed_via_github_app": t.proxy(renames["nullable-integration"]),
        }
    ).named(renames["state-change-issue-event"])
    types["timeline-issue-events"] = t.union(
        [
            t.proxy(renames["labeled-issue-event"]),
            t.proxy(renames["unlabeled-issue-event"]),
            t.proxy(renames["milestoned-issue-event"]),
            t.proxy(renames["demilestoned-issue-event"]),
            t.proxy(renames["renamed-issue-event"]),
            t.proxy(renames["review-requested-issue-event"]),
            t.proxy(renames["review-request-removed-issue-event"]),
            t.proxy(renames["review-dismissed-issue-event"]),
            t.proxy(renames["locked-issue-event"]),
            t.proxy(renames["added-to-project-issue-event"]),
            t.proxy(renames["moved-column-in-project-issue-event"]),
            t.proxy(renames["removed-from-project-issue-event"]),
            t.proxy(renames["converted-note-to-issue-issue-event"]),
            t.proxy(renames["timeline-comment-event"]),
            t.proxy(renames["timeline-cross-referenced-event"]),
            t.proxy(renames["timeline-committed-event"]),
            t.proxy(renames["timeline-reviewed-event"]),
            t.proxy(renames["timeline-line-commented-event"]),
            t.proxy(renames["timeline-commit-commented-event"]),
            t.proxy(renames["timeline-assigned-issue-event"]),
            t.proxy(renames["timeline-unassigned-issue-event"]),
            t.proxy(renames["state-change-issue-event"]),
        ]
    ).named(renames["timeline-issue-events"])
    types["deploy-key"] = t.struct(
        {
            "id": t.integer(),
            "key": t.string(),
            "url": t.string(),
            "title": t.string(),
            "verified": t.boolean(),
            "created_at": t.string(),
            "read_only": t.boolean(),
        }
    ).named(renames["deploy-key"])
    types["language"] = t.struct({}).named(renames["language"])
    types["license-content"] = t.struct(
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
            "license": t.proxy(renames["nullable-license-simple"]),
        }
    ).named(renames["license-content"])
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
            "creator": t.proxy(renames["nullable-simple-user"]),
            "open_issues": t.integer(),
            "closed_issues": t.integer(),
            "created_at": t.string(),
            "updated_at": t.string(),
            "closed_at": t.string().optional(),
            "due_on": t.string().optional(),
        }
    ).named(renames["milestone"])
    types["pages-source-hash"] = t.struct(
        {"branch": t.string(), "path": t.string()}
    ).named(renames["pages-source-hash"])
    types["pages-https-certificate"] = t.struct(
        {
            "state": t.string(),
            "description": t.string(),
            "domains": t.array(t.string()),
            "expires_at": t.string().optional(),
        }
    ).named(renames["pages-https-certificate"])
    types["page"] = t.struct(
        {
            "url": t.string(),
            "status": t.string().optional(),
            "cname": t.string().optional(),
            "protected_domain_state": t.string().optional(),
            "pending_domain_unverified_at": t.string().optional(),
            "custom_404": t.boolean(),
            "html_url": t.string().optional(),
            "source": t.proxy(renames["pages-source-hash"]).optional(),
            "public": t.boolean(),
            "https_certificate": t.proxy(renames["pages-https-certificate"]).optional(),
            "https_enforced": t.boolean().optional(),
        }
    ).named(renames["page"])
    types["page-build"] = t.struct(
        {
            "url": t.string(),
            "status": t.string(),
            "error": t.struct({"message": t.string().optional()}),
            "pusher": t.proxy(renames["nullable-simple-user"]),
            "commit": t.string(),
            "duration": t.integer(),
            "created_at": t.string(),
            "updated_at": t.string(),
        }
    ).named(renames["page-build"])
    types["page-build-status"] = t.struct(
        {"url": t.string(), "status": t.string()}
    ).named(renames["page-build-status"])
    types["repository-pre-receive-hook"] = t.struct(
        {
            "id": t.integer().optional(),
            "name": t.string().optional(),
            "enforcement": t.string().optional(),
            "configuration_url": t.string().optional(),
        }
    ).named(renames["repository-pre-receive-hook"])
    types["team-simple"] = t.struct(
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
    ).named(renames["team-simple"])
    types["pull-request"] = t.struct(
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
            "user": t.proxy(renames["nullable-simple-user"]),
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
            "milestone": t.proxy(renames["nullable-milestone"]),
            "active_lock_reason": t.string().optional(),
            "created_at": t.string(),
            "updated_at": t.string(),
            "closed_at": t.string().optional(),
            "merged_at": t.string().optional(),
            "merge_commit_sha": t.string().optional(),
            "assignee": t.proxy(renames["nullable-simple-user"]),
            "assignees": t.array(t.proxy(renames["simple-user"])).optional(),
            "requested_reviewers": t.array(t.proxy(renames["simple-user"])).optional(),
            "requested_teams": t.array(t.proxy(renames["team-simple"])).optional(),
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
                            "license": t.proxy(renames["nullable-license-simple"]),
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
            "merged_by": t.proxy(renames["nullable-simple-user"]),
            "comments": t.integer(),
            "review_comments": t.integer(),
            "maintainer_can_modify": t.boolean(),
            "commits": t.integer(),
            "additions": t.integer(),
            "deletions": t.integer(),
            "changed_files": t.integer(),
        }
    ).named(renames["pull-request"])
    types["pull-request-merge-result"] = t.struct(
        {"sha": t.string(), "merged": t.boolean(), "message": t.string()}
    ).named(renames["pull-request-merge-result"])
    types["pull-request-review-request"] = t.struct(
        {
            "users": t.array(t.proxy(renames["simple-user"])),
            "teams": t.array(t.proxy(renames["team"])),
        }
    ).named(renames["pull-request-review-request"])
    types["pull-request-review"] = t.struct(
        {
            "id": t.integer(),
            "node_id": t.string(),
            "user": t.proxy(renames["nullable-simple-user"]),
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
    ).named(renames["pull-request-review"])
    types["review-comment"] = t.struct(
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
            "user": t.proxy(renames["nullable-simple-user"]),
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
            "reactions": t.proxy(renames["reaction-rollup"]).optional(),
            "side": t.string().optional(),
            "start_side": t.string().optional(),
            "line": t.integer().optional(),
            "original_line": t.integer().optional(),
            "start_line": t.integer().optional(),
            "original_start_line": t.integer().optional(),
        }
    ).named(renames["review-comment"])
    types["release-asset"] = t.struct(
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
            "uploader": t.proxy(renames["nullable-simple-user"]),
        }
    ).named(renames["release-asset"])
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
            "author": t.proxy(renames["simple-user"]),
            "assets": t.array(t.proxy(renames["release-asset"])),
            "body_html": t.string().optional(),
            "body_text": t.string().optional(),
            "reactions": t.proxy(renames["reaction-rollup"]).optional(),
        }
    ).named(renames["release"])
    types["stargazer"] = t.struct(
        {"starred_at": t.string(), "user": t.proxy(renames["nullable-simple-user"])}
    ).named(renames["stargazer"])
    types["code-frequency-stat"] = t.array(t.integer()).named(
        renames["code-frequency-stat"]
    )
    types["commit-activity"] = t.struct(
        {"days": t.array(t.integer()), "total": t.integer(), "week": t.integer()}
    ).named(renames["commit-activity"])
    types["contributor-activity"] = t.struct(
        {
            "author": t.proxy(renames["nullable-simple-user"]),
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
    ).named(renames["contributor-activity"])
    types["participation-stats"] = t.struct(
        {"all": t.array(t.integer()), "owner": t.array(t.integer())}
    ).named(renames["participation-stats"])
    types["repository-subscription"] = t.struct(
        {
            "subscribed": t.boolean(),
            "ignored": t.boolean(),
            "reason": t.string().optional(),
            "created_at": t.string(),
            "url": t.string(),
            "repository_url": t.string(),
        }
    ).named(renames["repository-subscription"])
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
    types["search-result-text-matches"] = t.array(
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
    ).named(renames["search-result-text-matches"])
    types["code-search-result-item"] = t.struct(
        {
            "name": t.string(),
            "path": t.string(),
            "sha": t.string(),
            "url": t.string(),
            "git_url": t.string(),
            "html_url": t.string(),
            "repository": t.proxy(renames["minimal-repository"]),
            "score": t.number(),
            "file_size": t.integer().optional(),
            "language": t.string().optional(),
            "last_modified_at": t.string().optional(),
            "line_numbers": t.array(t.string()).optional(),
            "text_matches": t.proxy(renames["search-result-text-matches"]).optional(),
        }
    ).named(renames["code-search-result-item"])
    types["commit-search-result-item"] = t.struct(
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
                    "committer": t.proxy(renames["nullable-git-user"]),
                    "comment_count": t.integer(),
                    "message": t.string(),
                    "tree": t.struct({"sha": t.string(), "url": t.string()}),
                    "url": t.string(),
                    "verification": t.proxy(renames["verification"]).optional(),
                }
            ),
            "author": t.proxy(renames["nullable-simple-user"]),
            "committer": t.proxy(renames["nullable-git-user"]),
            "parents": t.array(
                t.struct(
                    {
                        "url": t.string().optional(),
                        "html_url": t.string().optional(),
                        "sha": t.string().optional(),
                    }
                )
            ),
            "repository": t.proxy(renames["minimal-repository"]),
            "score": t.number(),
            "node_id": t.string(),
            "text_matches": t.proxy(renames["search-result-text-matches"]).optional(),
        }
    ).named(renames["commit-search-result-item"])
    types["issue-search-result-item"] = t.struct(
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
            "assignees": t.array(t.proxy(renames["simple-user"])).optional(),
            "user": t.proxy(renames["nullable-simple-user"]),
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
            "assignee": t.proxy(renames["nullable-simple-user"]),
            "milestone": t.proxy(renames["nullable-milestone"]),
            "comments": t.integer(),
            "created_at": t.string(),
            "updated_at": t.string(),
            "closed_at": t.string().optional(),
            "text_matches": t.proxy(renames["search-result-text-matches"]).optional(),
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
                renames["nullable-integration"]
            ).optional(),
            "reactions": t.proxy(renames["reaction-rollup"]).optional(),
        }
    ).named(renames["issue-search-result-item"])
    types["label-search-result-item"] = t.struct(
        {
            "id": t.integer(),
            "node_id": t.string(),
            "url": t.string(),
            "name": t.string(),
            "color": t.string(),
            "default": t.boolean(),
            "description": t.string().optional(),
            "score": t.number(),
            "text_matches": t.proxy(renames["search-result-text-matches"]).optional(),
        }
    ).named(renames["label-search-result-item"])
    types["repo-search-result-item"] = t.struct(
        {
            "id": t.integer(),
            "node_id": t.string(),
            "name": t.string(),
            "full_name": t.string(),
            "owner": t.proxy(renames["nullable-simple-user"]),
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
            "license": t.proxy(renames["nullable-license-simple"]),
            "permissions": t.struct(
                {
                    "admin": t.boolean(),
                    "maintain": t.boolean().optional(),
                    "push": t.boolean(),
                    "triage": t.boolean().optional(),
                    "pull": t.boolean(),
                }
            ).optional(),
            "text_matches": t.proxy(renames["search-result-text-matches"]).optional(),
            "temp_clone_token": t.string().optional(),
            "allow_merge_commit": t.boolean().optional(),
            "allow_squash_merge": t.boolean().optional(),
            "allow_rebase_merge": t.boolean().optional(),
            "delete_branch_on_merge": t.boolean().optional(),
            "allow_forking": t.boolean().optional(),
            "is_template": t.boolean().optional(),
        }
    ).named(renames["repo-search-result-item"])
    types["topic-search-result-item"] = t.struct(
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
            "text_matches": t.proxy(renames["search-result-text-matches"]).optional(),
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
    ).named(renames["topic-search-result-item"])
    types["user-search-result-item"] = t.struct(
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
            "text_matches": t.proxy(renames["search-result-text-matches"]).optional(),
            "blog": t.string().optional(),
            "company": t.string().optional(),
            "suspended_at": t.string().optional(),
        }
    ).named(renames["user-search-result-item"])
    types["configuration-status"] = t.struct(
        {
            "status": t.string().optional(),
            "progress": t.array(
                t.struct({"status": t.string(), "key": t.string()})
            ).optional(),
        }
    ).named(renames["configuration-status"])
    types["maintenance-status"] = t.struct(
        {
            "status": t.string().optional(),
            "scheduled_time": t.string().optional(),
            "connection_services": t.array(
                t.struct({"name": t.string(), "number": t.integer()})
            ).optional(),
        }
    ).named(renames["maintenance-status"])
    types["enterprise-settings"] = t.struct(
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
    ).named(renames["enterprise-settings"])
    types["ssh-key"] = t.struct(
        {"key": t.string().optional(), "pretty-print": t.string().optional()}
    ).named(renames["ssh-key"])
    types["private-user"] = t.struct(
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
    ).named(renames["private-user"])
    types["email"] = t.struct(
        {
            "email": t.string(),
            "primary": t.boolean(),
            "verified": t.boolean(),
            "visibility": t.string().optional(),
        }
    ).named(renames["email"])
    types["gpg-key"] = t.struct(
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
    ).named(renames["gpg-key"])
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
    types["starred-repository"] = t.struct(
        {"starred_at": t.string(), "repo": t.proxy(renames["repository"])}
    ).named(renames["starred-repository"])
    types["hovercard"] = t.struct(
        {"contexts": t.array(t.struct({"message": t.string(), "octicon": t.string()}))}
    ).named(renames["hovercard"])
    types["key-simple"] = t.struct({"id": t.integer(), "key": t.string()}).named(
        renames["key-simple"]
    )

    functions = {}
    functions["meta/root"] = github.get(
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
    functions["enterprise-admin/list-global-webhooks"] = github.get(
        "/admin/hooks",
        t.struct({"accept": t.string(), "per_page": t.integer(), "page": t.integer()}),
        t.array(t.proxy(renames["global-hook"])),
    )
    functions["enterprise-admin/create-global-webhook"] = github.post(
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
        t.proxy(renames["global-hook"]),
        content_type="application/json",
        body_fields=("name", "config", "events", "active"),
    )
    functions["enterprise-admin/get-global-webhook"] = github.get(
        "/admin/hooks/{hook_id}",
        t.struct({"accept": t.string(), "hook_id": t.integer()}),
        t.proxy(renames["global-hook"]),
    )
    functions["enterprise-admin/update-global-webhook"] = github.patch(
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
        t.proxy(renames["global-hook-2"]),
        content_type="application/json",
        body_fields=("config", "events", "active"),
    )
    functions["enterprise-admin/delete-global-webhook"] = github.delete(
        "/admin/hooks/{hook_id}",
        t.struct({"accept": t.string(), "hook_id": t.integer()}),
        t.boolean(),
    )
    functions["enterprise-admin/ping-global-webhook"] = github.post(
        "/admin/hooks/{hook_id}/pings",
        t.struct({"accept": t.string(), "hook_id": t.integer()}),
        t.boolean(),
    )
    functions["enterprise-admin/list-public-keys"] = github.get(
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
        t.array(t.proxy(renames["public-key-full"])),
    )
    functions["enterprise-admin/delete-public-key"] = github.delete(
        "/admin/keys/{key_ids}",
        t.struct({"key_ids": t.string()}),
        t.boolean(),
    )
    functions["enterprise-admin/update-ldap-mapping-for-team"] = github.patch(
        "/admin/ldap/teams/{team_id}/mapping",
        t.struct({"team_id": t.integer(), "ldap_dn": t.string()}),
        t.proxy(renames["ldap-mapping-team"]),
        content_type="application/json",
        body_fields=("ldap_dn",),
    )
    functions["enterprise-admin/sync-ldap-mapping-for-team"] = github.post(
        "/admin/ldap/teams/{team_id}/sync",
        t.struct({"team_id": t.integer()}),
        t.struct({"status": t.string().optional()}),
    )
    functions["enterprise-admin/update-ldap-mapping-for-user"] = github.patch(
        "/admin/ldap/users/{username}/mapping",
        t.struct({"username": t.string(), "ldap_dn": t.string()}),
        t.proxy(renames["ldap-mapping-user"]),
        content_type="application/json",
        body_fields=("ldap_dn",),
    )
    functions["enterprise-admin/sync-ldap-mapping-for-user"] = github.post(
        "/admin/ldap/users/{username}/sync",
        t.struct({"username": t.string()}),
        t.struct({"status": t.string().optional()}),
    )
    functions["enterprise-admin/create-org"] = github.post(
        "/admin/organizations",
        t.struct(
            {
                "login": t.string(),
                "admin": t.string(),
                "profile_name": t.string().optional(),
            }
        ),
        t.proxy(renames["organization-simple"]),
        content_type="application/json",
        body_fields=("login", "admin", "profile_name"),
    )
    functions["enterprise-admin/update-org-name"] = github.patch(
        "/admin/organizations/{org}",
        t.struct({"org": t.string(), "login": t.string()}),
        t.struct({"message": t.string().optional(), "url": t.string().optional()}),
        content_type="application/json",
        body_fields=("login",),
    )
    functions["enterprise-admin/list-pre-receive-environments"] = github.get(
        "/admin/pre-receive-environments",
        t.struct(
            {
                "per_page": t.integer(),
                "page": t.integer(),
                "direction": t.string(),
                "sort": t.string(),
            }
        ),
        t.array(t.proxy(renames["pre-receive-environment"])),
    )
    functions["enterprise-admin/create-pre-receive-environment"] = github.post(
        "/admin/pre-receive-environments",
        t.struct({"name": t.string(), "image_url": t.string()}),
        t.proxy(renames["pre-receive-environment"]),
        content_type="application/json",
        body_fields=("name", "image_url"),
    )
    functions["enterprise-admin/get-pre-receive-environment"] = github.get(
        "/admin/pre-receive-environments/{pre_receive_environment_id}",
        t.struct({"pre_receive_environment_id": t.integer()}),
        t.proxy(renames["pre-receive-environment"]),
    )
    functions["enterprise-admin/update-pre-receive-environment"] = github.patch(
        "/admin/pre-receive-environments/{pre_receive_environment_id}",
        t.struct(
            {
                "pre_receive_environment_id": t.integer(),
                "name": t.string().optional(),
                "image_url": t.string().optional(),
            }
        ),
        t.proxy(renames["pre-receive-environment"]),
        content_type="application/json",
        body_fields=("name", "image_url"),
    )
    functions["enterprise-admin/delete-pre-receive-environment"] = github.delete(
        "/admin/pre-receive-environments/{pre_receive_environment_id}",
        t.struct({"pre_receive_environment_id": t.integer()}),
        t.boolean(),
    )
    functions["enterprise-admin/start-pre-receive-environment-download"] = github.post(
        "/admin/pre-receive-environments/{pre_receive_environment_id}/downloads",
        t.struct({"pre_receive_environment_id": t.integer()}),
        t.proxy(renames["pre-receive-environment-download-status"]),
    )
    functions[
        "enterprise-admin/get-download-status-for-pre-receive-environment"
    ] = github.get(
        "/admin/pre-receive-environments/{pre_receive_environment_id}/downloads/latest",
        t.struct({"pre_receive_environment_id": t.integer()}),
        t.proxy(renames["pre-receive-environment-download-status"]),
    )
    functions["enterprise-admin/list-pre-receive-hooks"] = github.get(
        "/admin/pre-receive-hooks",
        t.struct(
            {
                "per_page": t.integer(),
                "page": t.integer(),
                "direction": t.string(),
                "sort": t.string(),
            }
        ),
        t.array(t.proxy(renames["pre-receive-hook"])),
    )
    functions["enterprise-admin/create-pre-receive-hook"] = github.post(
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
        t.proxy(renames["pre-receive-hook"]),
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
    functions["enterprise-admin/get-pre-receive-hook"] = github.get(
        "/admin/pre-receive-hooks/{pre_receive_hook_id}",
        t.struct({"pre_receive_hook_id": t.integer()}),
        t.proxy(renames["pre-receive-hook"]),
    )
    functions["enterprise-admin/update-pre-receive-hook"] = github.patch(
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
        t.proxy(renames["pre-receive-hook"]),
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
    functions["enterprise-admin/delete-pre-receive-hook"] = github.delete(
        "/admin/pre-receive-hooks/{pre_receive_hook_id}",
        t.struct({"pre_receive_hook_id": t.integer()}),
        t.boolean(),
    )
    functions["enterprise-admin/list-personal-access-tokens"] = github.get(
        "/admin/tokens",
        t.struct({"per_page": t.integer(), "page": t.integer()}),
        t.array(t.proxy(renames["authorization"])),
    )
    functions["enterprise-admin/delete-personal-access-token"] = github.delete(
        "/admin/tokens/{token_id}",
        t.struct({"token_id": t.integer()}),
        t.boolean(),
    )
    functions["enterprise-admin/create-user"] = github.post(
        "/admin/users",
        t.struct({"login": t.string(), "email": t.string().optional()}),
        t.proxy(renames["simple-user"]),
        content_type="application/json",
        body_fields=("login", "email"),
    )
    functions["enterprise-admin/update-username-for-user"] = github.patch(
        "/admin/users/{username}",
        t.struct({"username": t.string(), "login": t.string()}),
        t.struct({"message": t.string().optional(), "url": t.string().optional()}),
        content_type="application/json",
        body_fields=("login",),
    )
    functions["enterprise-admin/delete-user"] = github.delete(
        "/admin/users/{username}",
        t.struct({"username": t.string()}),
        t.boolean(),
    )
    functions["enterprise-admin/create-impersonation-o-auth-token"] = github.post(
        "/admin/users/{username}/authorizations",
        t.struct({"username": t.string(), "scopes": t.array(t.string()).optional()}),
        t.proxy(renames["authorization"]),
        content_type="application/json",
        body_fields=("scopes",),
    )
    functions["enterprise-admin/delete-impersonation-o-auth-token"] = github.delete(
        "/admin/users/{username}/authorizations",
        t.struct({"username": t.string()}),
        t.boolean(),
    )
    functions["apps/get-authenticated"] = github.get(
        "/app",
        t.struct({}),
        t.proxy(renames["integration"]),
    )
    functions["apps/get-webhook-config-for-app"] = github.get(
        "/app/hook/config",
        t.struct({}),
        t.proxy(renames["webhook-config"]),
    )
    functions["apps/update-webhook-config-for-app"] = github.patch(
        "/app/hook/config",
        t.struct(
            {
                "url": t.proxy(renames["webhook-config-url"]).optional(),
                "content_type": t.proxy(
                    renames["webhook-config-content-type"]
                ).optional(),
                "secret": t.proxy(renames["webhook-config-secret"]).optional(),
                "insecure_ssl": t.proxy(
                    renames["webhook-config-insecure-ssl"]
                ).optional(),
            }
        ),
        t.proxy(renames["webhook-config"]),
        content_type="application/json",
        body_fields=("url", "content_type", "secret", "insecure_ssl"),
    )
    functions["apps/list-installations"] = github.get(
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
    functions["apps/get-installation"] = github.get(
        "/app/installations/{installation_id}",
        t.struct({"installation_id": t.integer()}),
        t.proxy(renames["installation"]).optional(),
    )
    functions["apps/delete-installation"] = github.delete(
        "/app/installations/{installation_id}",
        t.struct({"installation_id": t.integer()}),
        t.boolean().optional(),
    )
    functions["apps/create-installation-access-token"] = github.post(
        "/app/installations/{installation_id}/access_tokens",
        t.struct(
            {
                "installation_id": t.integer(),
                "repositories": t.array(t.string()).optional(),
                "repository_ids": t.array(t.integer()).optional(),
                "permissions": t.proxy(renames["app-permissions"]).optional(),
            }
        ),
        t.proxy(renames["installation-token"]).optional(),
        content_type="application/json",
        body_fields=("repositories", "repository_ids", "permissions"),
    )
    functions["apps/suspend-installation"] = github.put(
        "/app/installations/{installation_id}/suspended",
        t.struct({"installation_id": t.integer()}),
        t.boolean().optional(),
    )
    functions["apps/unsuspend-installation"] = github.delete(
        "/app/installations/{installation_id}/suspended",
        t.struct({"installation_id": t.integer()}),
        t.boolean().optional(),
    )
    functions["oauth-authorizations/list-grants"] = github.get(
        "/applications/grants",
        t.struct(
            {"per_page": t.integer(), "page": t.integer(), "client_id": t.string()}
        ),
        t.array(t.proxy(renames["application-grant"])).optional(),
    )
    functions["oauth-authorizations/get-grant"] = github.get(
        "/applications/grants/{grant_id}",
        t.struct({"grant_id": t.integer()}),
        t.proxy(renames["application-grant"]),
    )
    functions["oauth-authorizations/delete-grant"] = github.delete(
        "/applications/grants/{grant_id}",
        t.struct({"grant_id": t.integer()}),
        t.boolean(),
    )
    functions["apps/delete-authorization"] = github.delete(
        "/applications/{client_id}/grant",
        t.struct({"client_id": t.string(), "access_token": t.string()}),
        t.boolean(),
        content_type="application/json",
        body_fields=("access_token",),
    )
    functions["apps/revoke-grant-for-application"] = github.delete(
        "/applications/{client_id}/grants/{access_token}",
        t.struct({"client_id": t.string(), "access_token": t.string()}),
        t.boolean(),
    )
    functions["apps/check-token"] = github.post(
        "/applications/{client_id}/token",
        t.struct({"client_id": t.string(), "access_token": t.string()}),
        t.proxy(renames["authorization"]).optional(),
        content_type="application/json",
        body_fields=("access_token",),
    )
    functions["apps/reset-token"] = github.patch(
        "/applications/{client_id}/token",
        t.struct({"client_id": t.string(), "access_token": t.string()}),
        t.proxy(renames["authorization"]),
        content_type="application/json",
        body_fields=("access_token",),
    )
    functions["apps/delete-token"] = github.delete(
        "/applications/{client_id}/token",
        t.struct({"client_id": t.string(), "access_token": t.string()}),
        t.boolean(),
        content_type="application/json",
        body_fields=("access_token",),
    )
    functions["apps/scope-token"] = github.post(
        "/applications/{client_id}/token/scoped",
        t.struct(
            {
                "client_id": t.string(),
                "access_token": t.string(),
                "target": t.string().optional(),
                "target_id": t.integer().optional(),
                "repositories": t.array(t.string()).optional(),
                "repository_ids": t.array(t.integer()).optional(),
                "permissions": t.proxy(renames["app-permissions"]).optional(),
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
    functions["apps/check-authorization"] = github.get(
        "/applications/{client_id}/tokens/{access_token}",
        t.struct({"client_id": t.string(), "access_token": t.string()}),
        t.proxy(renames["nullable-authorization"]).optional(),
    )
    functions["apps/reset-authorization"] = github.post(
        "/applications/{client_id}/tokens/{access_token}",
        t.struct({"client_id": t.string(), "access_token": t.string()}),
        t.proxy(renames["authorization"]),
    )
    functions["apps/revoke-authorization-for-application"] = github.delete(
        "/applications/{client_id}/tokens/{access_token}",
        t.struct({"client_id": t.string(), "access_token": t.string()}),
        t.boolean(),
    )
    functions["apps/get-by-slug"] = github.get(
        "/apps/{app_slug}",
        t.struct({"app_slug": t.string()}),
        t.proxy(renames["integration"]).optional(),
    )
    functions["oauth-authorizations/list-authorizations"] = github.get(
        "/authorizations",
        t.struct(
            {"per_page": t.integer(), "page": t.integer(), "client_id": t.string()}
        ),
        t.array(t.proxy(renames["authorization"])).optional(),
    )
    functions["oauth-authorizations/create-authorization"] = github.post(
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
    functions["oauth-authorizations/get-or-create-authorization-for-app"] = github.put(
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
        "oauth-authorizations/get-or-create-authorization-for-app-and-fingerprint"
    ] = github.put(
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
    functions["oauth-authorizations/get-authorization"] = github.get(
        "/authorizations/{authorization_id}",
        t.struct({"authorization_id": t.integer()}),
        t.proxy(renames["authorization"]),
    )
    functions["oauth-authorizations/update-authorization"] = github.patch(
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
    functions["oauth-authorizations/delete-authorization"] = github.delete(
        "/authorizations/{authorization_id}",
        t.struct({"authorization_id": t.integer()}),
        t.boolean(),
    )
    functions["codes-of-conduct/get-all-codes-of-conduct"] = github.get(
        "/codes_of_conduct",
        t.struct({}),
        t.array(t.proxy(renames["code-of-conduct"])),
    )
    functions["codes-of-conduct/get-conduct-code"] = github.get(
        "/codes_of_conduct/{key}",
        t.struct({"key": t.string()}),
        t.proxy(renames["code-of-conduct"]).optional(),
    )
    functions["emojis/get"] = github.get(
        "/emojis",
        t.struct({}),
        t.struct({}),
    )
    functions["enterprise-admin/get-announcement"] = github.get(
        "/enterprise/announcement",
        t.struct({}),
        t.proxy(renames["announcement"]),
    )
    functions["enterprise-admin/set-announcement"] = github.patch(
        "/enterprise/announcement",
        t.struct(
            {
                "announcement": t.proxy(renames["announcement-message"]),
                "expires_at": t.proxy(renames["announcement-expiration"]).optional(),
            }
        ),
        t.proxy(renames["announcement"]),
        content_type="application/json",
        body_fields=("announcement", "expires_at"),
    )
    functions["enterprise-admin/remove-announcement"] = github.delete(
        "/enterprise/announcement",
        t.struct({}),
        t.boolean(),
    )
    functions["enterprise-admin/get-license-information"] = github.get(
        "/enterprise/settings/license",
        t.struct({}),
        t.proxy(renames["license-info"]),
    )
    functions["enterprise-admin/get-all-stats"] = github.get(
        "/enterprise/stats/all",
        t.struct({}),
        t.proxy(renames["enterprise-overview"]),
    )
    functions["enterprise-admin/get-comment-stats"] = github.get(
        "/enterprise/stats/comments",
        t.struct({}),
        t.proxy(renames["enterprise-comment-overview"]),
    )
    functions["enterprise-admin/get-gist-stats"] = github.get(
        "/enterprise/stats/gists",
        t.struct({}),
        t.proxy(renames["enterprise-gist-overview"]),
    )
    functions["enterprise-admin/get-hooks-stats"] = github.get(
        "/enterprise/stats/hooks",
        t.struct({}),
        t.proxy(renames["enterprise-hook-overview"]),
    )
    functions["enterprise-admin/get-issue-stats"] = github.get(
        "/enterprise/stats/issues",
        t.struct({}),
        t.proxy(renames["enterprise-issue-overview"]),
    )
    functions["enterprise-admin/get-milestone-stats"] = github.get(
        "/enterprise/stats/milestones",
        t.struct({}),
        t.proxy(renames["enterprise-milestone-overview"]),
    )
    functions["enterprise-admin/get-org-stats"] = github.get(
        "/enterprise/stats/orgs",
        t.struct({}),
        t.proxy(renames["enterprise-organization-overview"]),
    )
    functions["enterprise-admin/get-pages-stats"] = github.get(
        "/enterprise/stats/pages",
        t.struct({}),
        t.proxy(renames["enterprise-page-overview"]),
    )
    functions["enterprise-admin/get-pull-request-stats"] = github.get(
        "/enterprise/stats/pulls",
        t.struct({}),
        t.proxy(renames["enterprise-pull-request-overview"]),
    )
    functions["enterprise-admin/get-repo-stats"] = github.get(
        "/enterprise/stats/repos",
        t.struct({}),
        t.proxy(renames["enterprise-repository-overview"]),
    )
    functions["enterprise-admin/get-user-stats"] = github.get(
        "/enterprise/stats/users",
        t.struct({}),
        t.proxy(renames["enterprise-user-overview"]),
    )
    functions[
        "enterprise-admin/get-github-actions-permissions-enterprise"
    ] = github.get(
        "/enterprises/{enterprise}/actions/permissions",
        t.struct({"enterprise": t.string()}),
        t.proxy(renames["actions-enterprise-permissions"]),
    )
    functions[
        "enterprise-admin/set-github-actions-permissions-enterprise"
    ] = github.put(
        "/enterprises/{enterprise}/actions/permissions",
        t.struct(
            {
                "enterprise": t.string(),
                "enabled_organizations": t.proxy(renames["enabled-organizations"]),
                "allowed_actions": t.proxy(renames["allowed-actions"]).optional(),
            }
        ),
        t.boolean(),
        content_type="application/json",
        body_fields=("enabled_organizations", "allowed_actions"),
    )
    functions[
        "enterprise-admin/list-selected-organizations-enabled-github-actions-enterprise"
    ] = github.get(
        "/enterprises/{enterprise}/actions/permissions/organizations",
        t.struct(
            {"enterprise": t.string(), "per_page": t.integer(), "page": t.integer()}
        ),
        t.struct(
            {
                "total_count": t.number(),
                "organizations": t.array(t.proxy(renames["organization-simple"])),
            }
        ),
    )
    functions[
        "enterprise-admin/set-selected-organizations-enabled-github-actions-enterprise"
    ] = github.put(
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
        "enterprise-admin/enable-selected-organization-github-actions-enterprise"
    ] = github.put(
        "/enterprises/{enterprise}/actions/permissions/organizations/{org_id}",
        t.struct({"enterprise": t.string(), "org_id": t.integer()}),
        t.boolean(),
    )
    functions[
        "enterprise-admin/disable-selected-organization-github-actions-enterprise"
    ] = github.delete(
        "/enterprises/{enterprise}/actions/permissions/organizations/{org_id}",
        t.struct({"enterprise": t.string(), "org_id": t.integer()}),
        t.boolean(),
    )
    functions["enterprise-admin/get-allowed-actions-enterprise"] = github.get(
        "/enterprises/{enterprise}/actions/permissions/selected-actions",
        t.struct({"enterprise": t.string()}),
        t.proxy(renames["selected-actions"]),
    )
    functions["enterprise-admin/set-allowed-actions-enterprise"] = github.put(
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
        "enterprise-admin/list-self-hosted-runner-groups-for-enterprise"
    ] = github.get(
        "/enterprises/{enterprise}/actions/runner-groups",
        t.struct(
            {"enterprise": t.string(), "per_page": t.integer(), "page": t.integer()}
        ),
        t.struct(
            {
                "total_count": t.number(),
                "runner_groups": t.array(t.proxy(renames["runner-groups-enterprise"])),
            }
        ),
    )
    functions[
        "enterprise-admin/create-self-hosted-runner-group-for-enterprise"
    ] = github.post(
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
        t.proxy(renames["runner-groups-enterprise"]),
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
        "enterprise-admin/get-self-hosted-runner-group-for-enterprise"
    ] = github.get(
        "/enterprises/{enterprise}/actions/runner-groups/{runner_group_id}",
        t.struct({"enterprise": t.string(), "runner_group_id": t.integer()}),
        t.proxy(renames["runner-groups-enterprise"]),
    )
    functions[
        "enterprise-admin/update-self-hosted-runner-group-for-enterprise"
    ] = github.patch(
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
        t.proxy(renames["runner-groups-enterprise"]),
        content_type="application/json",
        body_fields=("name", "visibility", "allows_public_repositories"),
    )
    functions[
        "enterprise-admin/delete-self-hosted-runner-group-from-enterprise"
    ] = github.delete(
        "/enterprises/{enterprise}/actions/runner-groups/{runner_group_id}",
        t.struct({"enterprise": t.string(), "runner_group_id": t.integer()}),
        t.boolean(),
    )
    functions[
        "enterprise-admin/list-org-access-to-self-hosted-runner-group-in-enterprise"
    ] = github.get(
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
                "organizations": t.array(t.proxy(renames["organization-simple"])),
            }
        ),
    )
    functions[
        "enterprise-admin/set-org-access-to-self-hosted-runner-group-in-enterprise"
    ] = github.put(
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
        "enterprise-admin/add-org-access-to-self-hosted-runner-group-in-enterprise"
    ] = github.put(
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
        "enterprise-admin/remove-org-access-to-self-hosted-runner-group-in-enterprise"
    ] = github.delete(
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
        "enterprise-admin/list-self-hosted-runners-in-group-for-enterprise"
    ] = github.get(
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
        "enterprise-admin/set-self-hosted-runners-in-group-for-enterprise"
    ] = github.put(
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
        "enterprise-admin/add-self-hosted-runner-to-group-for-enterprise"
    ] = github.put(
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
        "enterprise-admin/remove-self-hosted-runner-from-group-for-enterprise"
    ] = github.delete(
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
    functions["enterprise-admin/list-self-hosted-runners-for-enterprise"] = github.get(
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
    functions["enterprise-admin/list-runner-applications-for-enterprise"] = github.get(
        "/enterprises/{enterprise}/actions/runners/downloads",
        t.struct({"enterprise": t.string()}),
        t.array(t.proxy(renames["runner-application"])),
    )
    functions[
        "enterprise-admin/create-registration-token-for-enterprise"
    ] = github.post(
        "/enterprises/{enterprise}/actions/runners/registration-token",
        t.struct({"enterprise": t.string()}),
        t.proxy(renames["authentication-token"]),
    )
    functions["enterprise-admin/create-remove-token-for-enterprise"] = github.post(
        "/enterprises/{enterprise}/actions/runners/remove-token",
        t.struct({"enterprise": t.string()}),
        t.proxy(renames["authentication-token"]),
    )
    functions["enterprise-admin/get-self-hosted-runner-for-enterprise"] = github.get(
        "/enterprises/{enterprise}/actions/runners/{runner_id}",
        t.struct({"enterprise": t.string(), "runner_id": t.integer()}),
        t.proxy(renames["runner"]),
    )
    functions[
        "enterprise-admin/delete-self-hosted-runner-from-enterprise"
    ] = github.delete(
        "/enterprises/{enterprise}/actions/runners/{runner_id}",
        t.struct({"enterprise": t.string(), "runner_id": t.integer()}),
        t.boolean(),
    )
    functions["activity/list-public-events"] = github.get(
        "/events",
        t.struct({"per_page": t.integer(), "page": t.integer()}),
        t.array(t.proxy(renames["event"])),
    )
    functions["activity/get-feeds"] = github.get(
        "/feeds",
        t.struct({}),
        t.proxy(renames["feed"]),
    )
    functions["gists/list"] = github.get(
        "/gists",
        t.struct({"since": t.string(), "per_page": t.integer(), "page": t.integer()}),
        t.array(t.proxy(renames["base-gist"])),
    )
    functions["gists/create"] = github.post(
        "/gists",
        t.struct(
            {
                "description": t.string().optional(),
                "files": t.struct({}),
                "public": t.either([t.boolean(), t.string()]).optional(),
            }
        ),
        t.proxy(renames["gist-simple"]).optional(),
        content_type="application/json",
        body_fields=("description", "files", "public"),
    )
    functions["gists/list-public"] = github.get(
        "/gists/public",
        t.struct({"since": t.string(), "per_page": t.integer(), "page": t.integer()}),
        t.array(t.proxy(renames["base-gist"])),
    )
    functions["gists/list-starred"] = github.get(
        "/gists/starred",
        t.struct({"since": t.string(), "per_page": t.integer(), "page": t.integer()}),
        t.array(t.proxy(renames["base-gist"])),
    )
    functions["gists/get"] = github.get(
        "/gists/{gist_id}",
        t.struct({"gist_id": t.string()}),
        t.proxy(renames["gist-simple"]).optional(),
    )
    functions["gists/delete"] = github.delete(
        "/gists/{gist_id}",
        t.struct({"gist_id": t.string()}),
        t.boolean().optional(),
    )
    functions["gists/list-comments"] = github.get(
        "/gists/{gist_id}/comments",
        t.struct({"gist_id": t.string(), "per_page": t.integer(), "page": t.integer()}),
        t.array(t.proxy(renames["gist-comment"])).optional(),
    )
    functions["gists/create-comment"] = github.post(
        "/gists/{gist_id}/comments",
        t.struct({"gist_id": t.string(), "body": t.string()}),
        t.proxy(renames["gist-comment"]).optional(),
        content_type="application/json",
        body_fields=("body",),
    )
    functions["gists/get-comment"] = github.get(
        "/gists/{gist_id}/comments/{comment_id}",
        t.struct({"gist_id": t.string(), "comment_id": t.integer()}),
        t.proxy(renames["gist-comment"]).optional(),
    )
    functions["gists/update-comment"] = github.patch(
        "/gists/{gist_id}/comments/{comment_id}",
        t.struct(
            {"gist_id": t.string(), "comment_id": t.integer(), "body": t.string()}
        ),
        t.proxy(renames["gist-comment"]).optional(),
        content_type="application/json",
        body_fields=("body",),
    )
    functions["gists/delete-comment"] = github.delete(
        "/gists/{gist_id}/comments/{comment_id}",
        t.struct({"gist_id": t.string(), "comment_id": t.integer()}),
        t.boolean().optional(),
    )
    functions["gists/list-commits"] = github.get(
        "/gists/{gist_id}/commits",
        t.struct({"gist_id": t.string(), "per_page": t.integer(), "page": t.integer()}),
        t.array(t.proxy(renames["gist-commit"])).optional(),
    )
    functions["gists/list-forks"] = github.get(
        "/gists/{gist_id}/forks",
        t.struct({"gist_id": t.string(), "per_page": t.integer(), "page": t.integer()}),
        t.array(t.proxy(renames["gist-simple"])).optional(),
    )
    functions["gists/fork"] = github.post(
        "/gists/{gist_id}/forks",
        t.struct({"gist_id": t.string()}),
        t.proxy(renames["base-gist"]).optional(),
    )
    functions["gists/check-is-starred"] = github.get(
        "/gists/{gist_id}/star",
        t.struct({"gist_id": t.string()}),
        t.boolean().optional(),
    )
    functions["gists/star"] = github.put(
        "/gists/{gist_id}/star",
        t.struct({"gist_id": t.string()}),
        t.boolean().optional(),
    )
    functions["gists/unstar"] = github.delete(
        "/gists/{gist_id}/star",
        t.struct({"gist_id": t.string()}),
        t.boolean().optional(),
    )
    functions["gists/get-revision"] = github.get(
        "/gists/{gist_id}/{sha}",
        t.struct({"gist_id": t.string(), "sha": t.string()}),
        t.proxy(renames["gist-simple"]).optional(),
    )
    functions["gitignore/get-all-templates"] = github.get(
        "/gitignore/templates",
        t.struct({}),
        t.array(t.string()),
    )
    functions["gitignore/get-template"] = github.get(
        "/gitignore/templates/{name}",
        t.struct({"name": t.string()}),
        t.proxy(renames["gitignore-template"]),
    )
    functions["apps/list-repos-accessible-to-installation"] = github.get(
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
    functions["apps/revoke-installation-access-token"] = github.delete(
        "/installation/token",
        t.struct({}),
        t.boolean(),
    )
    functions["issues/list"] = github.get(
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
    functions["licenses/get-all-commonly-used"] = github.get(
        "/licenses",
        t.struct(
            {"featured": t.boolean(), "per_page": t.integer(), "page": t.integer()}
        ),
        t.array(t.proxy(renames["license-simple"])),
    )
    functions["licenses/get"] = github.get(
        "/licenses/{license}",
        t.struct({"license": t.string()}),
        t.proxy(renames["license"]).optional(),
    )
    functions["meta/get"] = github.get(
        "/meta",
        t.struct({}),
        t.proxy(renames["api-overview"]),
    )
    functions["activity/list-public-events-for-repo-network"] = github.get(
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
    functions["activity/list-notifications-for-authenticated-user"] = github.get(
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
    functions["activity/mark-notifications-as-read"] = github.put(
        "/notifications",
        t.struct(
            {"last_read_at": t.string().optional(), "read": t.boolean().optional()}
        ),
        t.struct({"message": t.string().optional()}),
        content_type="application/json",
        body_fields=("last_read_at", "read"),
    )
    functions["activity/get-thread"] = github.get(
        "/notifications/threads/{thread_id}",
        t.struct({"thread_id": t.integer()}),
        t.proxy(renames["thread"]),
    )
    functions["activity/mark-thread-as-read"] = github.patch(
        "/notifications/threads/{thread_id}",
        t.struct({"thread_id": t.integer()}),
        t.struct({}),
    )
    functions["activity/get-thread-subscription-for-authenticated-user"] = github.get(
        "/notifications/threads/{thread_id}/subscription",
        t.struct({"thread_id": t.integer()}),
        t.proxy(renames["thread-subscription"]),
    )
    functions["activity/set-thread-subscription"] = github.put(
        "/notifications/threads/{thread_id}/subscription",
        t.struct({"thread_id": t.integer(), "ignored": t.boolean().optional()}),
        t.proxy(renames["thread-subscription"]),
        content_type="application/json",
        body_fields=("ignored",),
    )
    functions["activity/delete-thread-subscription"] = github.delete(
        "/notifications/threads/{thread_id}/subscription",
        t.struct({"thread_id": t.integer()}),
        t.boolean(),
    )
    functions["orgs/list"] = github.get(
        "/organizations",
        t.struct({"since": t.integer(), "per_page": t.integer()}),
        t.array(t.proxy(renames["organization-simple"])),
    )
    functions["orgs/get"] = github.get(
        "/orgs/{org}",
        t.struct({"org": t.string()}),
        t.proxy(renames["organization-full"]).optional(),
    )
    functions["orgs/update"] = github.patch(
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
        t.proxy(renames["organization-full"]),
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
    functions["actions/get-github-actions-permissions-organization"] = github.get(
        "/orgs/{org}/actions/permissions",
        t.struct({"org": t.string()}),
        t.proxy(renames["actions-organization-permissions"]),
    )
    functions["actions/set-github-actions-permissions-organization"] = github.put(
        "/orgs/{org}/actions/permissions",
        t.struct(
            {
                "org": t.string(),
                "enabled_repositories": t.proxy(renames["enabled-repositories"]),
                "allowed_actions": t.proxy(renames["allowed-actions"]).optional(),
            }
        ),
        t.boolean(),
        content_type="application/json",
        body_fields=("enabled_repositories", "allowed_actions"),
    )
    functions[
        "actions/list-selected-repositories-enabled-github-actions-organization"
    ] = github.get(
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
        "actions/set-selected-repositories-enabled-github-actions-organization"
    ] = github.put(
        "/orgs/{org}/actions/permissions/repositories",
        t.struct({"org": t.string(), "selected_repository_ids": t.array(t.integer())}),
        t.boolean(),
        content_type="application/json",
        body_fields=("selected_repository_ids",),
    )
    functions[
        "actions/enable-selected-repository-github-actions-organization"
    ] = github.put(
        "/orgs/{org}/actions/permissions/repositories/{repository_id}",
        t.struct({"org": t.string(), "repository_id": t.integer()}),
        t.boolean(),
    )
    functions[
        "actions/disable-selected-repository-github-actions-organization"
    ] = github.delete(
        "/orgs/{org}/actions/permissions/repositories/{repository_id}",
        t.struct({"org": t.string(), "repository_id": t.integer()}),
        t.boolean(),
    )
    functions["actions/get-allowed-actions-organization"] = github.get(
        "/orgs/{org}/actions/permissions/selected-actions",
        t.struct({"org": t.string()}),
        t.proxy(renames["selected-actions"]),
    )
    functions["actions/set-allowed-actions-organization"] = github.put(
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
    functions["actions/list-self-hosted-runner-groups-for-org"] = github.get(
        "/orgs/{org}/actions/runner-groups",
        t.struct({"org": t.string(), "per_page": t.integer(), "page": t.integer()}),
        t.struct(
            {
                "total_count": t.number(),
                "runner_groups": t.array(t.proxy(renames["runner-groups-org"])),
            }
        ),
    )
    functions["actions/create-self-hosted-runner-group-for-org"] = github.post(
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
        t.proxy(renames["runner-groups-org"]),
        content_type="application/json",
        body_fields=(
            "name",
            "visibility",
            "selected_repository_ids",
            "runners",
            "allows_public_repositories",
        ),
    )
    functions["actions/get-self-hosted-runner-group-for-org"] = github.get(
        "/orgs/{org}/actions/runner-groups/{runner_group_id}",
        t.struct({"org": t.string(), "runner_group_id": t.integer()}),
        t.proxy(renames["runner-groups-org"]),
    )
    functions["actions/update-self-hosted-runner-group-for-org"] = github.patch(
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
        t.proxy(renames["runner-groups-org"]),
        content_type="application/json",
        body_fields=("name", "visibility", "allows_public_repositories"),
    )
    functions["actions/delete-self-hosted-runner-group-from-org"] = github.delete(
        "/orgs/{org}/actions/runner-groups/{runner_group_id}",
        t.struct({"org": t.string(), "runner_group_id": t.integer()}),
        t.boolean(),
    )
    functions[
        "actions/list-repo-access-to-self-hosted-runner-group-in-org"
    ] = github.get(
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
                "repositories": t.array(t.proxy(renames["minimal-repository"])),
            }
        ),
    )
    functions[
        "actions/set-repo-access-to-self-hosted-runner-group-in-org"
    ] = github.put(
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
    functions[
        "actions/add-repo-access-to-self-hosted-runner-group-in-org"
    ] = github.put(
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
        "actions/remove-repo-access-to-self-hosted-runner-group-in-org"
    ] = github.delete(
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
    functions["actions/list-self-hosted-runners-in-group-for-org"] = github.get(
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
    functions["actions/set-self-hosted-runners-in-group-for-org"] = github.put(
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
    functions["actions/add-self-hosted-runner-to-group-for-org"] = github.put(
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
    functions["actions/remove-self-hosted-runner-from-group-for-org"] = github.delete(
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
    functions["actions/list-self-hosted-runners-for-org"] = github.get(
        "/orgs/{org}/actions/runners",
        t.struct({"org": t.string(), "per_page": t.integer(), "page": t.integer()}),
        t.struct(
            {"total_count": t.integer(), "runners": t.array(t.proxy(renames["runner"]))}
        ),
    )
    functions["actions/list-runner-applications-for-org"] = github.get(
        "/orgs/{org}/actions/runners/downloads",
        t.struct({"org": t.string()}),
        t.array(t.proxy(renames["runner-application"])),
    )
    functions["actions/create-registration-token-for-org"] = github.post(
        "/orgs/{org}/actions/runners/registration-token",
        t.struct({"org": t.string()}),
        t.proxy(renames["authentication-token"]),
    )
    functions["actions/create-remove-token-for-org"] = github.post(
        "/orgs/{org}/actions/runners/remove-token",
        t.struct({"org": t.string()}),
        t.proxy(renames["authentication-token"]),
    )
    functions["actions/get-self-hosted-runner-for-org"] = github.get(
        "/orgs/{org}/actions/runners/{runner_id}",
        t.struct({"org": t.string(), "runner_id": t.integer()}),
        t.proxy(renames["runner"]),
    )
    functions["actions/delete-self-hosted-runner-from-org"] = github.delete(
        "/orgs/{org}/actions/runners/{runner_id}",
        t.struct({"org": t.string(), "runner_id": t.integer()}),
        t.boolean(),
    )
    functions["actions/list-org-secrets"] = github.get(
        "/orgs/{org}/actions/secrets",
        t.struct({"org": t.string(), "per_page": t.integer(), "page": t.integer()}),
        t.struct(
            {
                "total_count": t.integer(),
                "secrets": t.array(t.proxy(renames["organization-actions-secret"])),
            }
        ),
    )
    functions["actions/get-org-public-key"] = github.get(
        "/orgs/{org}/actions/secrets/public-key",
        t.struct({"org": t.string()}),
        t.proxy(renames["actions-public-key"]),
    )
    functions["actions/get-org-secret"] = github.get(
        "/orgs/{org}/actions/secrets/{secret_name}",
        t.struct({"org": t.string(), "secret_name": t.string()}),
        t.proxy(renames["organization-actions-secret"]),
    )
    functions["actions/create-or-update-org-secret"] = github.put(
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
        t.proxy(renames["empty-object"]),
        content_type="application/json",
        body_fields=(
            "encrypted_value",
            "key_id",
            "visibility",
            "selected_repository_ids",
        ),
    )
    functions["actions/delete-org-secret"] = github.delete(
        "/orgs/{org}/actions/secrets/{secret_name}",
        t.struct({"org": t.string(), "secret_name": t.string()}),
        t.boolean(),
    )
    functions["actions/list-selected-repos-for-org-secret"] = github.get(
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
                "repositories": t.array(t.proxy(renames["minimal-repository"])),
            }
        ),
    )
    functions["actions/set-selected-repos-for-org-secret"] = github.put(
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
    functions["actions/add-selected-repo-to-org-secret"] = github.put(
        "/orgs/{org}/actions/secrets/{secret_name}/repositories/{repository_id}",
        t.struct(
            {"org": t.string(), "secret_name": t.string(), "repository_id": t.integer()}
        ),
        t.boolean(),
    )
    functions["actions/remove-selected-repo-from-org-secret"] = github.delete(
        "/orgs/{org}/actions/secrets/{secret_name}/repositories/{repository_id}",
        t.struct(
            {"org": t.string(), "secret_name": t.string(), "repository_id": t.integer()}
        ),
        t.boolean(),
    )
    functions["activity/list-public-org-events"] = github.get(
        "/orgs/{org}/events",
        t.struct({"org": t.string(), "per_page": t.integer(), "page": t.integer()}),
        t.array(t.proxy(renames["event"])),
    )
    functions["orgs/list-webhooks"] = github.get(
        "/orgs/{org}/hooks",
        t.struct({"org": t.string(), "per_page": t.integer(), "page": t.integer()}),
        t.array(t.proxy(renames["org-hook"])).optional(),
    )
    functions["orgs/create-webhook"] = github.post(
        "/orgs/{org}/hooks",
        t.struct(
            {
                "org": t.string(),
                "name": t.string(),
                "config": t.struct(
                    {
                        "url": t.proxy(renames["webhook-config-url"]),
                        "content_type": t.proxy(
                            renames["webhook-config-content-type"]
                        ).optional(),
                        "secret": t.proxy(renames["webhook-config-secret"]).optional(),
                        "insecure_ssl": t.proxy(
                            renames["webhook-config-insecure-ssl"]
                        ).optional(),
                        "username": t.string().optional(),
                        "password": t.string().optional(),
                    }
                ),
                "events": t.array(t.string()).optional(),
                "active": t.boolean().optional(),
            }
        ),
        t.proxy(renames["org-hook"]).optional(),
        content_type="application/json",
        body_fields=("name", "config", "events", "active"),
    )
    functions["orgs/get-webhook"] = github.get(
        "/orgs/{org}/hooks/{hook_id}",
        t.struct({"org": t.string(), "hook_id": t.integer()}),
        t.proxy(renames["org-hook"]).optional(),
    )
    functions["orgs/update-webhook"] = github.patch(
        "/orgs/{org}/hooks/{hook_id}",
        t.struct(
            {
                "org": t.string(),
                "hook_id": t.integer(),
                "config": t.struct(
                    {
                        "url": t.proxy(renames["webhook-config-url"]),
                        "content_type": t.proxy(
                            renames["webhook-config-content-type"]
                        ).optional(),
                        "secret": t.proxy(renames["webhook-config-secret"]).optional(),
                        "insecure_ssl": t.proxy(
                            renames["webhook-config-insecure-ssl"]
                        ).optional(),
                    }
                ).optional(),
                "events": t.array(t.string()).optional(),
                "active": t.boolean().optional(),
                "name": t.string().optional(),
            }
        ),
        t.proxy(renames["org-hook"]).optional(),
        content_type="application/json",
        body_fields=("config", "events", "active", "name"),
    )
    functions["orgs/delete-webhook"] = github.delete(
        "/orgs/{org}/hooks/{hook_id}",
        t.struct({"org": t.string(), "hook_id": t.integer()}),
        t.boolean().optional(),
    )
    functions["orgs/get-webhook-config-for-org"] = github.get(
        "/orgs/{org}/hooks/{hook_id}/config",
        t.struct({"org": t.string(), "hook_id": t.integer()}),
        t.proxy(renames["webhook-config"]),
    )
    functions["orgs/update-webhook-config-for-org"] = github.patch(
        "/orgs/{org}/hooks/{hook_id}/config",
        t.struct(
            {
                "org": t.string(),
                "hook_id": t.integer(),
                "url": t.proxy(renames["webhook-config-url"]).optional(),
                "content_type": t.proxy(
                    renames["webhook-config-content-type"]
                ).optional(),
                "secret": t.proxy(renames["webhook-config-secret"]).optional(),
                "insecure_ssl": t.proxy(
                    renames["webhook-config-insecure-ssl"]
                ).optional(),
            }
        ),
        t.proxy(renames["webhook-config"]),
        content_type="application/json",
        body_fields=("url", "content_type", "secret", "insecure_ssl"),
    )
    functions["orgs/ping-webhook"] = github.post(
        "/orgs/{org}/hooks/{hook_id}/pings",
        t.struct({"org": t.string(), "hook_id": t.integer()}),
        t.boolean().optional(),
    )
    functions["apps/get-org-installation"] = github.get(
        "/orgs/{org}/installation",
        t.struct({"org": t.string()}),
        t.proxy(renames["installation"]),
    )
    functions["orgs/list-app-installations"] = github.get(
        "/orgs/{org}/installations",
        t.struct({"org": t.string(), "per_page": t.integer(), "page": t.integer()}),
        t.struct(
            {
                "total_count": t.integer(),
                "installations": t.array(t.proxy(renames["installation"])),
            }
        ),
    )
    functions["issues/list-for-org"] = github.get(
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
    functions["orgs/list-members"] = github.get(
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
        t.array(t.proxy(renames["simple-user"])),
    )
    functions["orgs/check-membership-for-user"] = github.get(
        "/orgs/{org}/members/{username}",
        t.struct({"org": t.string(), "username": t.string()}),
        t.boolean().optional(),
    )
    functions["orgs/remove-member"] = github.delete(
        "/orgs/{org}/members/{username}",
        t.struct({"org": t.string(), "username": t.string()}),
        t.boolean(),
    )
    functions["orgs/get-membership-for-user"] = github.get(
        "/orgs/{org}/memberships/{username}",
        t.struct({"org": t.string(), "username": t.string()}),
        t.proxy(renames["org-membership"]).optional(),
    )
    functions["orgs/set-membership-for-user"] = github.put(
        "/orgs/{org}/memberships/{username}",
        t.struct(
            {"org": t.string(), "username": t.string(), "role": t.string().optional()}
        ),
        t.proxy(renames["org-membership"]),
        content_type="application/json",
        body_fields=("role",),
    )
    functions["orgs/remove-membership-for-user"] = github.delete(
        "/orgs/{org}/memberships/{username}",
        t.struct({"org": t.string(), "username": t.string()}),
        t.boolean().optional(),
    )
    functions["orgs/list-outside-collaborators"] = github.get(
        "/orgs/{org}/outside_collaborators",
        t.struct(
            {
                "org": t.string(),
                "filter": t.string(),
                "per_page": t.integer(),
                "page": t.integer(),
            }
        ),
        t.array(t.proxy(renames["simple-user"])),
    )
    functions["orgs/convert-member-to-outside-collaborator"] = github.put(
        "/orgs/{org}/outside_collaborators/{username}",
        t.struct({"org": t.string(), "username": t.string()}),
        t.struct({}).optional(),
    )
    functions["orgs/remove-outside-collaborator"] = github.delete(
        "/orgs/{org}/outside_collaborators/{username}",
        t.struct({"org": t.string(), "username": t.string()}),
        t.boolean(),
    )
    functions["enterprise-admin/list-pre-receive-hooks-for-org"] = github.get(
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
        t.array(t.proxy(renames["org-pre-receive-hook"])),
    )
    functions["enterprise-admin/get-pre-receive-hook-for-org"] = github.get(
        "/orgs/{org}/pre-receive-hooks/{pre_receive_hook_id}",
        t.struct({"org": t.string(), "pre_receive_hook_id": t.integer()}),
        t.proxy(renames["org-pre-receive-hook"]),
    )
    functions[
        "enterprise-admin/update-pre-receive-hook-enforcement-for-org"
    ] = github.patch(
        "/orgs/{org}/pre-receive-hooks/{pre_receive_hook_id}",
        t.struct(
            {
                "org": t.string(),
                "pre_receive_hook_id": t.integer(),
                "enforcement": t.string().optional(),
                "allow_downstream_configuration": t.boolean().optional(),
            }
        ),
        t.proxy(renames["org-pre-receive-hook"]),
        content_type="application/json",
        body_fields=("enforcement", "allow_downstream_configuration"),
    )
    functions[
        "enterprise-admin/remove-pre-receive-hook-enforcement-for-org"
    ] = github.delete(
        "/orgs/{org}/pre-receive-hooks/{pre_receive_hook_id}",
        t.struct({"org": t.string(), "pre_receive_hook_id": t.integer()}),
        t.proxy(renames["org-pre-receive-hook"]),
    )
    functions["projects/list-for-org"] = github.get(
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
    functions["projects/create-for-org"] = github.post(
        "/orgs/{org}/projects",
        t.struct(
            {"org": t.string(), "name": t.string(), "body": t.string().optional()}
        ),
        t.proxy(renames["project"]).optional(),
        content_type="application/json",
        body_fields=("name", "body"),
    )
    functions["orgs/list-public-members"] = github.get(
        "/orgs/{org}/public_members",
        t.struct({"org": t.string(), "per_page": t.integer(), "page": t.integer()}),
        t.array(t.proxy(renames["simple-user"])),
    )
    functions["orgs/check-public-membership-for-user"] = github.get(
        "/orgs/{org}/public_members/{username}",
        t.struct({"org": t.string(), "username": t.string()}),
        t.boolean().optional(),
    )
    functions["orgs/set-public-membership-for-authenticated-user"] = github.put(
        "/orgs/{org}/public_members/{username}",
        t.struct({"org": t.string(), "username": t.string()}),
        t.boolean(),
    )
    functions["orgs/remove-public-membership-for-authenticated-user"] = github.delete(
        "/orgs/{org}/public_members/{username}",
        t.struct({"org": t.string(), "username": t.string()}),
        t.boolean(),
    )
    functions["repos/list-for-org"] = github.get(
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
        t.array(t.proxy(renames["minimal-repository"])),
    )
    functions["repos/create-in-org"] = github.post(
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
    functions["teams/list"] = github.get(
        "/orgs/{org}/teams",
        t.struct({"org": t.string(), "per_page": t.integer(), "page": t.integer()}),
        t.array(t.proxy(renames["team"])),
    )
    functions["teams/create"] = github.post(
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
        t.proxy(renames["team-full"]),
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
    functions["teams/get-by-name"] = github.get(
        "/orgs/{org}/teams/{team_slug}",
        t.struct({"org": t.string(), "team_slug": t.string()}),
        t.proxy(renames["team-full"]).optional(),
    )
    functions["teams/update-in-org"] = github.patch(
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
        t.proxy(renames["team-full"]),
        content_type="application/json",
        body_fields=("name", "description", "privacy", "permission", "parent_team_id"),
    )
    functions["teams/delete-in-org"] = github.delete(
        "/orgs/{org}/teams/{team_slug}",
        t.struct({"org": t.string(), "team_slug": t.string()}),
        t.boolean(),
    )
    functions["teams/list-discussions-in-org"] = github.get(
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
        t.array(t.proxy(renames["team-discussion"])),
    )
    functions["teams/create-discussion-in-org"] = github.post(
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
        t.proxy(renames["team-discussion"]),
        content_type="application/json",
        body_fields=("title", "body", "private"),
    )
    functions["teams/get-discussion-in-org"] = github.get(
        "/orgs/{org}/teams/{team_slug}/discussions/{discussion_number}",
        t.struct(
            {
                "org": t.string(),
                "team_slug": t.string(),
                "discussion_number": t.integer(),
            }
        ),
        t.proxy(renames["team-discussion"]),
    )
    functions["teams/update-discussion-in-org"] = github.patch(
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
        t.proxy(renames["team-discussion"]),
        content_type="application/json",
        body_fields=("title", "body"),
    )
    functions["teams/delete-discussion-in-org"] = github.delete(
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
    functions["teams/list-discussion-comments-in-org"] = github.get(
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
        t.array(t.proxy(renames["team-discussion-comment"])),
    )
    functions["teams/create-discussion-comment-in-org"] = github.post(
        "/orgs/{org}/teams/{team_slug}/discussions/{discussion_number}/comments",
        t.struct(
            {
                "org": t.string(),
                "team_slug": t.string(),
                "discussion_number": t.integer(),
                "body": t.string(),
            }
        ),
        t.proxy(renames["team-discussion-comment"]),
        content_type="application/json",
        body_fields=("body",),
    )
    functions["teams/get-discussion-comment-in-org"] = github.get(
        "/orgs/{org}/teams/{team_slug}/discussions/{discussion_number}/comments/{comment_number}",
        t.struct(
            {
                "org": t.string(),
                "team_slug": t.string(),
                "discussion_number": t.integer(),
                "comment_number": t.integer(),
            }
        ),
        t.proxy(renames["team-discussion-comment"]),
    )
    functions["teams/update-discussion-comment-in-org"] = github.patch(
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
        t.proxy(renames["team-discussion-comment"]),
        content_type="application/json",
        body_fields=("body",),
    )
    functions["teams/delete-discussion-comment-in-org"] = github.delete(
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
    functions["reactions/list-for-team-discussion-comment-in-org"] = github.get(
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
    functions["reactions/create-for-team-discussion-comment-in-org"] = github.post(
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
    functions["reactions/delete-for-team-discussion-comment"] = github.delete(
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
    functions["reactions/list-for-team-discussion-in-org"] = github.get(
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
    functions["reactions/create-for-team-discussion-in-org"] = github.post(
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
    functions["reactions/delete-for-team-discussion"] = github.delete(
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
    functions["teams/list-members-in-org"] = github.get(
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
        t.array(t.proxy(renames["simple-user"])),
    )
    functions["teams/get-membership-for-user-in-org"] = github.get(
        "/orgs/{org}/teams/{team_slug}/memberships/{username}",
        t.struct({"org": t.string(), "team_slug": t.string(), "username": t.string()}),
        t.proxy(renames["team-membership"]).optional(),
    )
    functions["teams/add-or-update-membership-for-user-in-org"] = github.put(
        "/orgs/{org}/teams/{team_slug}/memberships/{username}",
        t.struct(
            {
                "org": t.string(),
                "team_slug": t.string(),
                "username": t.string(),
                "role": t.string().optional(),
            }
        ),
        t.proxy(renames["team-membership"]),
        content_type="application/json",
        body_fields=("role",),
    )
    functions["teams/remove-membership-for-user-in-org"] = github.delete(
        "/orgs/{org}/teams/{team_slug}/memberships/{username}",
        t.struct({"org": t.string(), "team_slug": t.string(), "username": t.string()}),
        t.boolean(),
    )
    functions["teams/list-projects-in-org"] = github.get(
        "/orgs/{org}/teams/{team_slug}/projects",
        t.struct(
            {
                "org": t.string(),
                "team_slug": t.string(),
                "per_page": t.integer(),
                "page": t.integer(),
            }
        ),
        t.array(t.proxy(renames["team-project"])),
    )
    functions["teams/check-permissions-for-project-in-org"] = github.get(
        "/orgs/{org}/teams/{team_slug}/projects/{project_id}",
        t.struct(
            {"org": t.string(), "team_slug": t.string(), "project_id": t.integer()}
        ),
        t.proxy(renames["team-project"]).optional(),
    )
    functions["teams/add-or-update-project-permissions-in-org"] = github.put(
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
    functions["teams/remove-project-in-org"] = github.delete(
        "/orgs/{org}/teams/{team_slug}/projects/{project_id}",
        t.struct(
            {"org": t.string(), "team_slug": t.string(), "project_id": t.integer()}
        ),
        t.boolean(),
    )
    functions["teams/list-repos-in-org"] = github.get(
        "/orgs/{org}/teams/{team_slug}/repos",
        t.struct(
            {
                "org": t.string(),
                "team_slug": t.string(),
                "per_page": t.integer(),
                "page": t.integer(),
            }
        ),
        t.array(t.proxy(renames["minimal-repository"])),
    )
    functions["teams/check-permissions-for-repo-in-org"] = github.get(
        "/orgs/{org}/teams/{team_slug}/repos/{owner}/{repo}",
        t.struct(
            {
                "org": t.string(),
                "team_slug": t.string(),
                "owner": t.string(),
                "repo": t.string(),
            }
        ),
        t.proxy(renames["team-repository"]).optional(),
    )
    functions["teams/add-or-update-repo-permissions-in-org"] = github.put(
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
    functions["teams/remove-repo-in-org"] = github.delete(
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
    functions["teams/list-child-in-org"] = github.get(
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
    functions["projects/get-card"] = github.get(
        "/projects/columns/cards/{card_id}",
        t.struct({"card_id": t.integer()}),
        t.proxy(renames["project-card"]).optional(),
    )
    functions["projects/update-card"] = github.patch(
        "/projects/columns/cards/{card_id}",
        t.struct(
            {
                "card_id": t.integer(),
                "note": t.string().optional(),
                "archived": t.boolean().optional(),
            }
        ),
        t.proxy(renames["project-card"]).optional(),
        content_type="application/json",
        body_fields=("note", "archived"),
    )
    functions["projects/delete-card"] = github.delete(
        "/projects/columns/cards/{card_id}",
        t.struct({"card_id": t.integer()}),
        t.boolean().optional(),
    )
    functions["projects/move-card"] = github.post(
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
    functions["projects/get-column"] = github.get(
        "/projects/columns/{column_id}",
        t.struct({"column_id": t.integer()}),
        t.proxy(renames["project-column"]).optional(),
    )
    functions["projects/update-column"] = github.patch(
        "/projects/columns/{column_id}",
        t.struct({"column_id": t.integer(), "name": t.string()}),
        t.proxy(renames["project-column"]),
        content_type="application/json",
        body_fields=("name",),
    )
    functions["projects/delete-column"] = github.delete(
        "/projects/columns/{column_id}",
        t.struct({"column_id": t.integer()}),
        t.boolean(),
    )
    functions["projects/list-cards"] = github.get(
        "/projects/columns/{column_id}/cards",
        t.struct(
            {
                "column_id": t.integer(),
                "archived_state": t.string(),
                "per_page": t.integer(),
                "page": t.integer(),
            }
        ),
        t.array(t.proxy(renames["project-card"])),
    )
    functions["projects/move-column"] = github.post(
        "/projects/columns/{column_id}/moves",
        t.struct({"column_id": t.integer(), "position": t.string()}),
        t.struct({}),
        content_type="application/json",
        body_fields=("position",),
    )
    functions["projects/get"] = github.get(
        "/projects/{project_id}",
        t.struct({"project_id": t.integer()}),
        t.proxy(renames["project"]),
    )
    functions["projects/update"] = github.patch(
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
    functions["projects/delete"] = github.delete(
        "/projects/{project_id}",
        t.struct({"project_id": t.integer()}),
        t.boolean().optional(),
    )
    functions["projects/list-collaborators"] = github.get(
        "/projects/{project_id}/collaborators",
        t.struct(
            {
                "project_id": t.integer(),
                "affiliation": t.string(),
                "per_page": t.integer(),
                "page": t.integer(),
            }
        ),
        t.array(t.proxy(renames["simple-user"])).optional(),
    )
    functions["projects/add-collaborator"] = github.put(
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
    functions["projects/remove-collaborator"] = github.delete(
        "/projects/{project_id}/collaborators/{username}",
        t.struct({"project_id": t.integer(), "username": t.string()}),
        t.boolean().optional(),
    )
    functions["projects/get-permission-for-user"] = github.get(
        "/projects/{project_id}/collaborators/{username}/permission",
        t.struct({"project_id": t.integer(), "username": t.string()}),
        t.proxy(renames["project-collaborator-permission"]).optional(),
    )
    functions["projects/list-columns"] = github.get(
        "/projects/{project_id}/columns",
        t.struct(
            {"project_id": t.integer(), "per_page": t.integer(), "page": t.integer()}
        ),
        t.array(t.proxy(renames["project-column"])),
    )
    functions["projects/create-column"] = github.post(
        "/projects/{project_id}/columns",
        t.struct({"project_id": t.integer(), "name": t.string()}),
        t.proxy(renames["project-column"]),
        content_type="application/json",
        body_fields=("name",),
    )
    functions["rate-limit/get"] = github.get(
        "/rate_limit",
        t.struct({}),
        t.proxy(renames["rate-limit-overview"]).optional(),
    )
    functions["reactions/delete-legacy"] = github.delete(
        "/reactions/{reaction_id}",
        t.struct({"reaction_id": t.integer()}),
        t.boolean(),
    )
    functions["repos/get"] = github.get(
        "/repos/{owner}/{repo}",
        t.struct({"owner": t.string(), "repo": t.string()}),
        t.proxy(renames["full-repository"]).optional(),
    )
    functions["repos/update"] = github.patch(
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
        t.proxy(renames["full-repository"]).optional(),
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
    functions["repos/delete"] = github.delete(
        "/repos/{owner}/{repo}",
        t.struct({"owner": t.string(), "repo": t.string()}),
        t.boolean().optional(),
    )
    functions["actions/list-artifacts-for-repo"] = github.get(
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
    functions["actions/get-artifact"] = github.get(
        "/repos/{owner}/{repo}/actions/artifacts/{artifact_id}",
        t.struct({"owner": t.string(), "repo": t.string(), "artifact_id": t.integer()}),
        t.proxy(renames["artifact"]),
    )
    functions["actions/delete-artifact"] = github.delete(
        "/repos/{owner}/{repo}/actions/artifacts/{artifact_id}",
        t.struct({"owner": t.string(), "repo": t.string(), "artifact_id": t.integer()}),
        t.boolean(),
    )
    functions["actions/download-artifact"] = github.get(
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
    functions["actions/get-job-for-workflow-run"] = github.get(
        "/repos/{owner}/{repo}/actions/jobs/{job_id}",
        t.struct({"owner": t.string(), "repo": t.string(), "job_id": t.integer()}),
        t.proxy(renames["job"]),
    )
    functions["actions/download-job-logs-for-workflow-run"] = github.get(
        "/repos/{owner}/{repo}/actions/jobs/{job_id}/logs",
        t.struct({"owner": t.string(), "repo": t.string(), "job_id": t.integer()}),
        t.struct({}),
    )
    functions["actions/get-github-actions-permissions-repository"] = github.get(
        "/repos/{owner}/{repo}/actions/permissions",
        t.struct({"owner": t.string(), "repo": t.string()}),
        t.proxy(renames["actions-repository-permissions"]),
    )
    functions["actions/set-github-actions-permissions-repository"] = github.put(
        "/repos/{owner}/{repo}/actions/permissions",
        t.struct(
            {
                "owner": t.string(),
                "repo": t.string(),
                "enabled": t.proxy(renames["actions-enabled"]),
                "allowed_actions": t.proxy(renames["allowed-actions"]).optional(),
            }
        ),
        t.boolean(),
        content_type="application/json",
        body_fields=("enabled", "allowed_actions"),
    )
    functions["actions/get-allowed-actions-repository"] = github.get(
        "/repos/{owner}/{repo}/actions/permissions/selected-actions",
        t.struct({"owner": t.string(), "repo": t.string()}),
        t.proxy(renames["selected-actions"]),
    )
    functions["actions/set-allowed-actions-repository"] = github.put(
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
    functions["actions/list-self-hosted-runners-for-repo"] = github.get(
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
    functions["actions/list-runner-applications-for-repo"] = github.get(
        "/repos/{owner}/{repo}/actions/runners/downloads",
        t.struct({"owner": t.string(), "repo": t.string()}),
        t.array(t.proxy(renames["runner-application"])),
    )
    functions["actions/create-registration-token-for-repo"] = github.post(
        "/repos/{owner}/{repo}/actions/runners/registration-token",
        t.struct({"owner": t.string(), "repo": t.string()}),
        t.proxy(renames["authentication-token"]),
    )
    functions["actions/create-remove-token-for-repo"] = github.post(
        "/repos/{owner}/{repo}/actions/runners/remove-token",
        t.struct({"owner": t.string(), "repo": t.string()}),
        t.proxy(renames["authentication-token"]),
    )
    functions["actions/get-self-hosted-runner-for-repo"] = github.get(
        "/repos/{owner}/{repo}/actions/runners/{runner_id}",
        t.struct({"owner": t.string(), "repo": t.string(), "runner_id": t.integer()}),
        t.proxy(renames["runner"]),
    )
    functions["actions/delete-self-hosted-runner-from-repo"] = github.delete(
        "/repos/{owner}/{repo}/actions/runners/{runner_id}",
        t.struct({"owner": t.string(), "repo": t.string(), "runner_id": t.integer()}),
        t.boolean(),
    )
    functions["actions/list-workflow-runs-for-repo"] = github.get(
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
                "workflow_runs": t.array(t.proxy(renames["workflow-run"])),
            }
        ),
    )
    functions["actions/get-workflow-run"] = github.get(
        "/repos/{owner}/{repo}/actions/runs/{run_id}",
        t.struct(
            {
                "owner": t.string(),
                "repo": t.string(),
                "run_id": t.integer(),
                "exclude_pull_requests": t.boolean(),
            }
        ),
        t.proxy(renames["workflow-run"]),
    )
    functions["actions/delete-workflow-run"] = github.delete(
        "/repos/{owner}/{repo}/actions/runs/{run_id}",
        t.struct({"owner": t.string(), "repo": t.string(), "run_id": t.integer()}),
        t.boolean(),
    )
    functions["actions/list-workflow-run-artifacts"] = github.get(
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
    functions["actions/cancel-workflow-run"] = github.post(
        "/repos/{owner}/{repo}/actions/runs/{run_id}/cancel",
        t.struct({"owner": t.string(), "repo": t.string(), "run_id": t.integer()}),
        t.struct({}),
    )
    functions["actions/list-jobs-for-workflow-run"] = github.get(
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
    functions["actions/download-workflow-run-logs"] = github.get(
        "/repos/{owner}/{repo}/actions/runs/{run_id}/logs",
        t.struct({"owner": t.string(), "repo": t.string(), "run_id": t.integer()}),
        t.struct({}),
    )
    functions["actions/delete-workflow-run-logs"] = github.delete(
        "/repos/{owner}/{repo}/actions/runs/{run_id}/logs",
        t.struct({"owner": t.string(), "repo": t.string(), "run_id": t.integer()}),
        t.boolean(),
    )
    functions["actions/re-run-workflow"] = github.post(
        "/repos/{owner}/{repo}/actions/runs/{run_id}/rerun",
        t.struct({"owner": t.string(), "repo": t.string(), "run_id": t.integer()}),
        t.struct({}),
    )
    functions["actions/list-repo-secrets"] = github.get(
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
                "secrets": t.array(t.proxy(renames["actions-secret"])),
            }
        ),
    )
    functions["actions/get-repo-public-key"] = github.get(
        "/repos/{owner}/{repo}/actions/secrets/public-key",
        t.struct({"owner": t.string(), "repo": t.string()}),
        t.proxy(renames["actions-public-key"]),
    )
    functions["actions/get-repo-secret"] = github.get(
        "/repos/{owner}/{repo}/actions/secrets/{secret_name}",
        t.struct({"owner": t.string(), "repo": t.string(), "secret_name": t.string()}),
        t.proxy(renames["actions-secret"]),
    )
    functions["actions/create-or-update-repo-secret"] = github.put(
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
    functions["actions/delete-repo-secret"] = github.delete(
        "/repos/{owner}/{repo}/actions/secrets/{secret_name}",
        t.struct({"owner": t.string(), "repo": t.string(), "secret_name": t.string()}),
        t.boolean(),
    )
    functions["actions/list-repo-workflows"] = github.get(
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
    functions["actions/get-workflow"] = github.get(
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
    functions["actions/disable-workflow"] = github.put(
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
    functions["actions/create-workflow-dispatch"] = github.post(
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
    functions["actions/enable-workflow"] = github.put(
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
    functions["actions/list-workflow-runs"] = github.get(
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
                "workflow_runs": t.array(t.proxy(renames["workflow-run"])),
            }
        ),
    )
    functions["issues/list-assignees"] = github.get(
        "/repos/{owner}/{repo}/assignees",
        t.struct(
            {
                "owner": t.string(),
                "repo": t.string(),
                "per_page": t.integer(),
                "page": t.integer(),
            }
        ),
        t.array(t.proxy(renames["simple-user"])).optional(),
    )
    functions["issues/check-user-can-be-assigned"] = github.get(
        "/repos/{owner}/{repo}/assignees/{assignee}",
        t.struct({"owner": t.string(), "repo": t.string(), "assignee": t.string()}),
        t.boolean().optional(),
    )
    functions["repos/list-branches"] = github.get(
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
        t.array(t.proxy(renames["short-branch"])).optional(),
    )
    functions["repos/get-branch"] = github.get(
        "/repos/{owner}/{repo}/branches/{branch}",
        t.struct({"owner": t.string(), "repo": t.string(), "branch": t.string()}),
        t.proxy(renames["branch-with-protection"]).optional(),
    )
    functions["repos/get-branch-protection"] = github.get(
        "/repos/{owner}/{repo}/branches/{branch}/protection",
        t.struct({"owner": t.string(), "repo": t.string(), "branch": t.string()}),
        t.proxy(renames["branch-protection"]).optional(),
    )
    functions["repos/update-branch-protection"] = github.put(
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
        t.proxy(renames["protected-branch"]).optional(),
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
    functions["repos/delete-branch-protection"] = github.delete(
        "/repos/{owner}/{repo}/branches/{branch}/protection",
        t.struct({"owner": t.string(), "repo": t.string(), "branch": t.string()}),
        t.boolean(),
    )
    functions["repos/get-admin-branch-protection"] = github.get(
        "/repos/{owner}/{repo}/branches/{branch}/protection/enforce_admins",
        t.struct({"owner": t.string(), "repo": t.string(), "branch": t.string()}),
        t.proxy(renames["protected-branch-admin-enforced"]),
    )
    functions["repos/set-admin-branch-protection"] = github.post(
        "/repos/{owner}/{repo}/branches/{branch}/protection/enforce_admins",
        t.struct({"owner": t.string(), "repo": t.string(), "branch": t.string()}),
        t.proxy(renames["protected-branch-admin-enforced"]),
    )
    functions["repos/delete-admin-branch-protection"] = github.delete(
        "/repos/{owner}/{repo}/branches/{branch}/protection/enforce_admins",
        t.struct({"owner": t.string(), "repo": t.string(), "branch": t.string()}),
        t.boolean().optional(),
    )
    functions["repos/get-pull-request-review-protection"] = github.get(
        "/repos/{owner}/{repo}/branches/{branch}/protection/required_pull_request_reviews",
        t.struct({"owner": t.string(), "repo": t.string(), "branch": t.string()}),
        t.proxy(renames["protected-branch-pull-request-review"]),
    )
    functions["repos/update-pull-request-review-protection"] = github.patch(
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
        t.proxy(renames["protected-branch-pull-request-review"]),
        content_type="application/json",
        body_fields=(
            "dismissal_restrictions",
            "dismiss_stale_reviews",
            "require_code_owner_reviews",
            "required_approving_review_count",
        ),
    )
    functions["repos/delete-pull-request-review-protection"] = github.delete(
        "/repos/{owner}/{repo}/branches/{branch}/protection/required_pull_request_reviews",
        t.struct({"owner": t.string(), "repo": t.string(), "branch": t.string()}),
        t.boolean().optional(),
    )
    functions["repos/get-commit-signature-protection"] = github.get(
        "/repos/{owner}/{repo}/branches/{branch}/protection/required_signatures",
        t.struct({"owner": t.string(), "repo": t.string(), "branch": t.string()}),
        t.proxy(renames["protected-branch-admin-enforced"]).optional(),
    )
    functions["repos/create-commit-signature-protection"] = github.post(
        "/repos/{owner}/{repo}/branches/{branch}/protection/required_signatures",
        t.struct({"owner": t.string(), "repo": t.string(), "branch": t.string()}),
        t.proxy(renames["protected-branch-admin-enforced"]).optional(),
    )
    functions["repos/delete-commit-signature-protection"] = github.delete(
        "/repos/{owner}/{repo}/branches/{branch}/protection/required_signatures",
        t.struct({"owner": t.string(), "repo": t.string(), "branch": t.string()}),
        t.boolean().optional(),
    )
    functions["repos/get-status-checks-protection"] = github.get(
        "/repos/{owner}/{repo}/branches/{branch}/protection/required_status_checks",
        t.struct({"owner": t.string(), "repo": t.string(), "branch": t.string()}),
        t.proxy(renames["status-check-policy"]).optional(),
    )
    functions["repos/update-status-check-protection"] = github.patch(
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
        t.proxy(renames["status-check-policy"]).optional(),
        content_type="application/json",
        body_fields=("strict", "contexts"),
    )
    functions["repos/remove-status-check-protection"] = github.delete(
        "/repos/{owner}/{repo}/branches/{branch}/protection/required_status_checks",
        t.struct({"owner": t.string(), "repo": t.string(), "branch": t.string()}),
        t.boolean(),
    )
    functions["repos/get-all-status-check-contexts"] = github.get(
        "/repos/{owner}/{repo}/branches/{branch}/protection/required_status_checks/contexts",
        t.struct({"owner": t.string(), "repo": t.string(), "branch": t.string()}),
        t.array(t.string()).optional(),
    )
    functions["repos/get-access-restrictions"] = github.get(
        "/repos/{owner}/{repo}/branches/{branch}/protection/restrictions",
        t.struct({"owner": t.string(), "repo": t.string(), "branch": t.string()}),
        t.proxy(renames["branch-restriction-policy"]).optional(),
    )
    functions["repos/delete-access-restrictions"] = github.delete(
        "/repos/{owner}/{repo}/branches/{branch}/protection/restrictions",
        t.struct({"owner": t.string(), "repo": t.string(), "branch": t.string()}),
        t.boolean(),
    )
    functions["repos/get-apps-with-access-to-protected-branch"] = github.get(
        "/repos/{owner}/{repo}/branches/{branch}/protection/restrictions/apps",
        t.struct({"owner": t.string(), "repo": t.string(), "branch": t.string()}),
        t.array(t.proxy(renames["integration"])).optional(),
    )
    functions["repos/get-teams-with-access-to-protected-branch"] = github.get(
        "/repos/{owner}/{repo}/branches/{branch}/protection/restrictions/teams",
        t.struct({"owner": t.string(), "repo": t.string(), "branch": t.string()}),
        t.array(t.proxy(renames["team"])).optional(),
    )
    functions["repos/get-users-with-access-to-protected-branch"] = github.get(
        "/repos/{owner}/{repo}/branches/{branch}/protection/restrictions/users",
        t.struct({"owner": t.string(), "repo": t.string(), "branch": t.string()}),
        t.array(t.proxy(renames["simple-user"])).optional(),
    )
    functions["checks/get"] = github.get(
        "/repos/{owner}/{repo}/check-runs/{check_run_id}",
        t.struct(
            {"owner": t.string(), "repo": t.string(), "check_run_id": t.integer()}
        ),
        t.proxy(renames["check-run"]),
    )
    functions["checks/list-annotations"] = github.get(
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
        t.array(t.proxy(renames["check-annotation"])),
    )
    functions["checks/create-suite"] = github.post(
        "/repos/{owner}/{repo}/check-suites",
        t.struct({"owner": t.string(), "repo": t.string(), "head_sha": t.string()}),
        t.proxy(renames["check-suite"]),
        content_type="application/json",
        body_fields=("head_sha",),
    )
    functions["checks/set-suites-preferences"] = github.patch(
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
        t.proxy(renames["check-suite-preference"]),
        content_type="application/json",
        body_fields=("auto_trigger_checks",),
    )
    functions["checks/get-suite"] = github.get(
        "/repos/{owner}/{repo}/check-suites/{check_suite_id}",
        t.struct(
            {"owner": t.string(), "repo": t.string(), "check_suite_id": t.integer()}
        ),
        t.proxy(renames["check-suite"]),
    )
    functions["checks/list-for-suite"] = github.get(
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
                "check_runs": t.array(t.proxy(renames["check-run"])),
            }
        ),
    )
    functions["checks/rerequest-suite"] = github.post(
        "/repos/{owner}/{repo}/check-suites/{check_suite_id}/rerequest",
        t.struct(
            {"owner": t.string(), "repo": t.string(), "check_suite_id": t.integer()}
        ),
        t.struct({}),
    )
    functions["code-scanning/list-alerts-for-repo"] = github.get(
        "/repos/{owner}/{repo}/code-scanning/alerts",
        t.struct(
            {
                "owner": t.string(),
                "repo": t.string(),
                "tool_name": t.proxy(renames["code-scanning-analysis-tool-name"]),
                "tool_guid": t.proxy(renames["code-scanning-analysis-tool-guid"]),
                "page": t.integer(),
                "per_page": t.integer(),
                "ref": t.proxy(renames["code-scanning-ref"]),
                "state": t.proxy(renames["code-scanning-alert-state"]),
            }
        ),
        t.array(t.proxy(renames["code-scanning-alert-items"])).optional(),
    )
    functions["code-scanning/get-alert"] = github.get(
        "/repos/{owner}/{repo}/code-scanning/alerts/{alert_number}",
        t.struct(
            {
                "owner": t.string(),
                "repo": t.string(),
                "alert_number": t.proxy(renames["alert-number"]),
            }
        ),
        t.proxy(renames["code-scanning-alert"]).optional(),
    )
    functions["code-scanning/update-alert"] = github.patch(
        "/repos/{owner}/{repo}/code-scanning/alerts/{alert_number}",
        t.struct(
            {
                "owner": t.string(),
                "repo": t.string(),
                "alert_number": t.proxy(renames["alert-number"]),
                "state": t.proxy(renames["code-scanning-alert-set-state"]),
                "dismissed_reason": t.proxy(
                    renames["code-scanning-alert-dismissed-reason"]
                ).optional(),
            }
        ),
        t.proxy(renames["code-scanning-alert"]).optional(),
        content_type="application/json",
        body_fields=("state", "dismissed_reason"),
    )
    functions["code-scanning/list-recent-analyses"] = github.get(
        "/repos/{owner}/{repo}/code-scanning/analyses",
        t.struct(
            {
                "owner": t.string(),
                "repo": t.string(),
                "tool_name": t.proxy(renames["code-scanning-analysis-tool-name"]),
                "tool_guid": t.proxy(renames["code-scanning-analysis-tool-guid"]),
                "page": t.integer(),
                "per_page": t.integer(),
                "ref": t.proxy(renames["code-scanning-ref"]),
                "sarif_id": t.proxy(renames["code-scanning-analysis-sarif-id"]),
            }
        ),
        t.array(t.proxy(renames["code-scanning-analysis"])).optional(),
    )
    functions["code-scanning/upload-sarif"] = github.post(
        "/repos/{owner}/{repo}/code-scanning/sarifs",
        t.struct(
            {
                "owner": t.string(),
                "repo": t.string(),
                "commit_sha": t.proxy(renames["code-scanning-analysis-commit-sha"]),
                "ref": t.proxy(renames["code-scanning-ref"]),
                "sarif": t.proxy(renames["code-scanning-analysis-sarif-file"]),
                "checkout_uri": t.string().optional(),
                "started_at": t.string().optional(),
                "tool_name": t.string().optional(),
            }
        ),
        t.proxy(renames["code-scanning-sarifs-receipt"]).optional(),
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
    functions["repos/list-collaborators"] = github.get(
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
    functions["repos/check-collaborator"] = github.get(
        "/repos/{owner}/{repo}/collaborators/{username}",
        t.struct({"owner": t.string(), "repo": t.string(), "username": t.string()}),
        t.boolean().optional(),
    )
    functions["repos/add-collaborator"] = github.put(
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
        t.proxy(renames["repository-invitation"]),
        content_type="application/json",
        body_fields=("permission", "permissions"),
    )
    functions["repos/remove-collaborator"] = github.delete(
        "/repos/{owner}/{repo}/collaborators/{username}",
        t.struct({"owner": t.string(), "repo": t.string(), "username": t.string()}),
        t.boolean(),
    )
    functions["repos/get-collaborator-permission-level"] = github.get(
        "/repos/{owner}/{repo}/collaborators/{username}/permission",
        t.struct({"owner": t.string(), "repo": t.string(), "username": t.string()}),
        t.proxy(renames["repository-collaborator-permission"]).optional(),
    )
    functions["repos/list-commit-comments-for-repo"] = github.get(
        "/repos/{owner}/{repo}/comments",
        t.struct(
            {
                "owner": t.string(),
                "repo": t.string(),
                "per_page": t.integer(),
                "page": t.integer(),
            }
        ),
        t.array(t.proxy(renames["commit-comment"])),
    )
    functions["repos/get-commit-comment"] = github.get(
        "/repos/{owner}/{repo}/comments/{comment_id}",
        t.struct({"owner": t.string(), "repo": t.string(), "comment_id": t.integer()}),
        t.proxy(renames["commit-comment"]).optional(),
    )
    functions["repos/update-commit-comment"] = github.patch(
        "/repos/{owner}/{repo}/comments/{comment_id}",
        t.struct(
            {
                "owner": t.string(),
                "repo": t.string(),
                "comment_id": t.integer(),
                "body": t.string(),
            }
        ),
        t.proxy(renames["commit-comment"]).optional(),
        content_type="application/json",
        body_fields=("body",),
    )
    functions["repos/delete-commit-comment"] = github.delete(
        "/repos/{owner}/{repo}/comments/{comment_id}",
        t.struct({"owner": t.string(), "repo": t.string(), "comment_id": t.integer()}),
        t.boolean().optional(),
    )
    functions["reactions/list-for-commit-comment"] = github.get(
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
    functions["reactions/create-for-commit-comment"] = github.post(
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
    functions["reactions/delete-for-commit-comment"] = github.delete(
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
    functions["repos/list-commits"] = github.get(
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
    functions["repos/list-branches-for-head-commit"] = github.get(
        "/repos/{owner}/{repo}/commits/{commit_sha}/branches-where-head",
        t.struct({"owner": t.string(), "repo": t.string(), "commit_sha": t.string()}),
        t.array(t.proxy(renames["branch-short"])),
    )
    functions["repos/list-comments-for-commit"] = github.get(
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
        t.array(t.proxy(renames["commit-comment"])),
    )
    functions["repos/create-commit-comment"] = github.post(
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
        t.proxy(renames["commit-comment"]),
        content_type="application/json",
        body_fields=("body", "path", "position", "line"),
    )
    functions["repos/list-pull-requests-associated-with-commit"] = github.get(
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
        t.array(t.proxy(renames["pull-request-simple"])),
    )
    functions["repos/get-commit"] = github.get(
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
    functions["checks/list-for-ref"] = github.get(
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
                "check_runs": t.array(t.proxy(renames["check-run"])),
            }
        ),
    )
    functions["checks/list-suites-for-ref"] = github.get(
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
                "check_suites": t.array(t.proxy(renames["check-suite"])),
            }
        ),
    )
    functions["repos/get-combined-status-for-ref"] = github.get(
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
        t.proxy(renames["combined-commit-status"]).optional(),
    )
    functions["repos/list-commit-statuses-for-ref"] = github.get(
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
    functions["repos/compare-commits"] = github.get(
        "/repos/{owner}/{repo}/compare/{basehead}",
        t.struct({"owner": t.string(), "repo": t.string(), "basehead": t.string()}),
        t.proxy(renames["commit-comparison"]).optional(),
    )
    functions["apps/create-content-attachment"] = github.post(
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
        t.proxy(renames["content-reference-attachment"]).optional(),
        content_type="application/json",
        body_fields=("title", "body"),
    )
    functions["repos/get-content"] = github.get(
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
                t.proxy(renames["content-directory"]),
                t.proxy(renames["content-file"]),
                t.proxy(renames["content-symlink"]),
                t.proxy(renames["content-submodule"]),
            ]
        ).optional(),
    )
    functions["repos/create-or-update-file-contents"] = github.put(
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
        t.proxy(renames["file-commit"]).optional(),
        content_type="application/json",
        body_fields=("message", "content", "sha", "branch", "committer", "author"),
    )
    functions["repos/delete-file"] = github.delete(
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
        t.proxy(renames["file-commit"]).optional(),
        content_type="application/json",
        body_fields=("message", "sha", "branch", "committer", "author"),
    )
    functions["repos/list-contributors"] = github.get(
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
    functions["repos/list-deployments"] = github.get(
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
    functions["repos/create-deployment"] = github.post(
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
    functions["repos/get-deployment"] = github.get(
        "/repos/{owner}/{repo}/deployments/{deployment_id}",
        t.struct(
            {"owner": t.string(), "repo": t.string(), "deployment_id": t.integer()}
        ),
        t.proxy(renames["deployment"]).optional(),
    )
    functions["repos/delete-deployment"] = github.delete(
        "/repos/{owner}/{repo}/deployments/{deployment_id}",
        t.struct(
            {"owner": t.string(), "repo": t.string(), "deployment_id": t.integer()}
        ),
        t.boolean().optional(),
    )
    functions["repos/list-deployment-statuses"] = github.get(
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
        t.array(t.proxy(renames["deployment-status"])).optional(),
    )
    functions["repos/create-deployment-status"] = github.post(
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
        t.proxy(renames["deployment-status"]),
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
    functions["repos/get-deployment-status"] = github.get(
        "/repos/{owner}/{repo}/deployments/{deployment_id}/statuses/{status_id}",
        t.struct(
            {
                "owner": t.string(),
                "repo": t.string(),
                "deployment_id": t.integer(),
                "status_id": t.integer(),
            }
        ),
        t.proxy(renames["deployment-status"]).optional(),
    )
    functions["repos/create-dispatch-event"] = github.post(
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
    functions["activity/list-repo-events"] = github.get(
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
    functions["repos/list-forks"] = github.get(
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
        t.array(t.proxy(renames["minimal-repository"])),
    )
    functions["repos/create-fork"] = github.post(
        "/repos/{owner}/{repo}/forks",
        t.struct(
            {
                "owner": t.string(),
                "repo": t.string(),
                "organization": t.string().optional(),
            }
        ),
        t.proxy(renames["full-repository"]).optional(),
        content_type="application/json",
        body_fields=("organization",),
    )
    functions["git/create-blob"] = github.post(
        "/repos/{owner}/{repo}/git/blobs",
        t.struct(
            {
                "owner": t.string(),
                "repo": t.string(),
                "content": t.string(),
                "encoding": t.string().optional(),
            }
        ),
        t.proxy(renames["short-blob"]).optional(),
        content_type="application/json",
        body_fields=("content", "encoding"),
    )
    functions["git/get-blob"] = github.get(
        "/repos/{owner}/{repo}/git/blobs/{file_sha}",
        t.struct({"owner": t.string(), "repo": t.string(), "file_sha": t.string()}),
        t.proxy(renames["blob"]).optional(),
    )
    functions["git/create-commit"] = github.post(
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
        t.proxy(renames["git-commit"]).optional(),
        content_type="application/json",
        body_fields=("message", "tree", "parents", "author", "committer", "signature"),
    )
    functions["git/get-commit"] = github.get(
        "/repos/{owner}/{repo}/git/commits/{commit_sha}",
        t.struct({"owner": t.string(), "repo": t.string(), "commit_sha": t.string()}),
        t.proxy(renames["git-commit"]).optional(),
    )
    functions["git/list-matching-refs"] = github.get(
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
        t.array(t.proxy(renames["git-ref"])),
    )
    functions["git/get-ref"] = github.get(
        "/repos/{owner}/{repo}/git/ref/{ref}",
        t.struct({"owner": t.string(), "repo": t.string(), "ref": t.string()}),
        t.proxy(renames["git-ref"]).optional(),
    )
    functions["git/create-ref"] = github.post(
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
        t.proxy(renames["git-ref"]),
        content_type="application/json",
        body_fields=("ref", "sha", "key"),
    )
    functions["git/update-ref"] = github.patch(
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
        t.proxy(renames["git-ref"]),
        content_type="application/json",
        body_fields=("sha", "force"),
    )
    functions["git/delete-ref"] = github.delete(
        "/repos/{owner}/{repo}/git/refs/{ref}",
        t.struct({"owner": t.string(), "repo": t.string(), "ref": t.string()}),
        t.boolean(),
    )
    functions["git/create-tag"] = github.post(
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
        t.proxy(renames["git-tag"]),
        content_type="application/json",
        body_fields=("tag", "message", "object", "type", "tagger"),
    )
    functions["git/get-tag"] = github.get(
        "/repos/{owner}/{repo}/git/tags/{tag_sha}",
        t.struct({"owner": t.string(), "repo": t.string(), "tag_sha": t.string()}),
        t.proxy(renames["git-tag"]).optional(),
    )
    functions["git/create-tree"] = github.post(
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
        t.proxy(renames["git-tree"]).optional(),
        content_type="application/json",
        body_fields=("tree", "base_tree"),
    )
    functions["git/get-tree"] = github.get(
        "/repos/{owner}/{repo}/git/trees/{tree_sha}",
        t.struct(
            {
                "owner": t.string(),
                "repo": t.string(),
                "tree_sha": t.string(),
                "recursive": t.string(),
            }
        ),
        t.proxy(renames["git-tree"]).optional(),
    )
    functions["repos/list-webhooks"] = github.get(
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
    functions["repos/create-webhook"] = github.post(
        "/repos/{owner}/{repo}/hooks",
        t.struct(
            {
                "owner": t.string(),
                "repo": t.string(),
                "name": t.string().optional(),
                "config": t.struct(
                    {
                        "url": t.proxy(renames["webhook-config-url"]).optional(),
                        "content_type": t.proxy(
                            renames["webhook-config-content-type"]
                        ).optional(),
                        "secret": t.proxy(renames["webhook-config-secret"]).optional(),
                        "insecure_ssl": t.proxy(
                            renames["webhook-config-insecure-ssl"]
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
    functions["repos/get-webhook"] = github.get(
        "/repos/{owner}/{repo}/hooks/{hook_id}",
        t.struct({"owner": t.string(), "repo": t.string(), "hook_id": t.integer()}),
        t.proxy(renames["hook"]).optional(),
    )
    functions["repos/update-webhook"] = github.patch(
        "/repos/{owner}/{repo}/hooks/{hook_id}",
        t.struct(
            {
                "owner": t.string(),
                "repo": t.string(),
                "hook_id": t.integer(),
                "config": t.struct(
                    {
                        "url": t.proxy(renames["webhook-config-url"]),
                        "content_type": t.proxy(
                            renames["webhook-config-content-type"]
                        ).optional(),
                        "secret": t.proxy(renames["webhook-config-secret"]).optional(),
                        "insecure_ssl": t.proxy(
                            renames["webhook-config-insecure-ssl"]
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
    functions["repos/delete-webhook"] = github.delete(
        "/repos/{owner}/{repo}/hooks/{hook_id}",
        t.struct({"owner": t.string(), "repo": t.string(), "hook_id": t.integer()}),
        t.boolean().optional(),
    )
    functions["repos/get-webhook-config-for-repo"] = github.get(
        "/repos/{owner}/{repo}/hooks/{hook_id}/config",
        t.struct({"owner": t.string(), "repo": t.string(), "hook_id": t.integer()}),
        t.proxy(renames["webhook-config"]),
    )
    functions["repos/update-webhook-config-for-repo"] = github.patch(
        "/repos/{owner}/{repo}/hooks/{hook_id}/config",
        t.struct(
            {
                "owner": t.string(),
                "repo": t.string(),
                "hook_id": t.integer(),
                "url": t.proxy(renames["webhook-config-url"]).optional(),
                "content_type": t.proxy(
                    renames["webhook-config-content-type"]
                ).optional(),
                "secret": t.proxy(renames["webhook-config-secret"]).optional(),
                "insecure_ssl": t.proxy(
                    renames["webhook-config-insecure-ssl"]
                ).optional(),
            }
        ),
        t.proxy(renames["webhook-config"]),
        content_type="application/json",
        body_fields=("url", "content_type", "secret", "insecure_ssl"),
    )
    functions["repos/ping-webhook"] = github.post(
        "/repos/{owner}/{repo}/hooks/{hook_id}/pings",
        t.struct({"owner": t.string(), "repo": t.string(), "hook_id": t.integer()}),
        t.boolean().optional(),
    )
    functions["repos/test-push-webhook"] = github.post(
        "/repos/{owner}/{repo}/hooks/{hook_id}/tests",
        t.struct({"owner": t.string(), "repo": t.string(), "hook_id": t.integer()}),
        t.boolean().optional(),
    )
    functions["apps/get-repo-installation"] = github.get(
        "/repos/{owner}/{repo}/installation",
        t.struct({"owner": t.string(), "repo": t.string()}),
        t.proxy(renames["installation"]).optional(),
    )
    functions["repos/list-invitations"] = github.get(
        "/repos/{owner}/{repo}/invitations",
        t.struct(
            {
                "owner": t.string(),
                "repo": t.string(),
                "per_page": t.integer(),
                "page": t.integer(),
            }
        ),
        t.array(t.proxy(renames["repository-invitation"])),
    )
    functions["repos/update-invitation"] = github.patch(
        "/repos/{owner}/{repo}/invitations/{invitation_id}",
        t.struct(
            {
                "owner": t.string(),
                "repo": t.string(),
                "invitation_id": t.integer(),
                "permissions": t.string().optional(),
            }
        ),
        t.proxy(renames["repository-invitation"]),
        content_type="application/json",
        body_fields=("permissions",),
    )
    functions["repos/delete-invitation"] = github.delete(
        "/repos/{owner}/{repo}/invitations/{invitation_id}",
        t.struct(
            {"owner": t.string(), "repo": t.string(), "invitation_id": t.integer()}
        ),
        t.boolean(),
    )
    functions["issues/list-for-repo"] = github.get(
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
    functions["issues/create"] = github.post(
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
    functions["issues/list-comments-for-repo"] = github.get(
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
        t.array(t.proxy(renames["issue-comment"])).optional(),
    )
    functions["issues/get-comment"] = github.get(
        "/repos/{owner}/{repo}/issues/comments/{comment_id}",
        t.struct({"owner": t.string(), "repo": t.string(), "comment_id": t.integer()}),
        t.proxy(renames["issue-comment"]).optional(),
    )
    functions["issues/update-comment"] = github.patch(
        "/repos/{owner}/{repo}/issues/comments/{comment_id}",
        t.struct(
            {
                "owner": t.string(),
                "repo": t.string(),
                "comment_id": t.integer(),
                "body": t.string(),
            }
        ),
        t.proxy(renames["issue-comment"]),
        content_type="application/json",
        body_fields=("body",),
    )
    functions["issues/delete-comment"] = github.delete(
        "/repos/{owner}/{repo}/issues/comments/{comment_id}",
        t.struct({"owner": t.string(), "repo": t.string(), "comment_id": t.integer()}),
        t.boolean(),
    )
    functions["reactions/list-for-issue-comment"] = github.get(
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
    functions["reactions/create-for-issue-comment"] = github.post(
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
    functions["reactions/delete-for-issue-comment"] = github.delete(
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
    functions["issues/list-events-for-repo"] = github.get(
        "/repos/{owner}/{repo}/issues/events",
        t.struct(
            {
                "owner": t.string(),
                "repo": t.string(),
                "per_page": t.integer(),
                "page": t.integer(),
            }
        ),
        t.array(t.proxy(renames["issue-event"])),
    )
    functions["issues/get-event"] = github.get(
        "/repos/{owner}/{repo}/issues/events/{event_id}",
        t.struct({"owner": t.string(), "repo": t.string(), "event_id": t.integer()}),
        t.proxy(renames["issue-event"]).optional(),
    )
    functions["issues/get"] = github.get(
        "/repos/{owner}/{repo}/issues/{issue_number}",
        t.struct(
            {"owner": t.string(), "repo": t.string(), "issue_number": t.integer()}
        ),
        t.proxy(renames["issue"]).optional(),
    )
    functions["issues/update"] = github.patch(
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
    functions["issues/add-assignees"] = github.post(
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
    functions["issues/remove-assignees"] = github.delete(
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
    functions["issues/list-comments"] = github.get(
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
        t.array(t.proxy(renames["issue-comment"])).optional(),
    )
    functions["issues/create-comment"] = github.post(
        "/repos/{owner}/{repo}/issues/{issue_number}/comments",
        t.struct(
            {
                "owner": t.string(),
                "repo": t.string(),
                "issue_number": t.integer(),
                "body": t.string(),
            }
        ),
        t.proxy(renames["issue-comment"]).optional(),
        content_type="application/json",
        body_fields=("body",),
    )
    functions["issues/list-events"] = github.get(
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
        t.array(t.proxy(renames["issue-event-for-issue"])),
    )
    functions["issues/list-labels-on-issue"] = github.get(
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
    functions["issues/remove-all-labels"] = github.delete(
        "/repos/{owner}/{repo}/issues/{issue_number}/labels",
        t.struct(
            {"owner": t.string(), "repo": t.string(), "issue_number": t.integer()}
        ),
        t.boolean(),
    )
    functions["issues/remove-label"] = github.delete(
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
    functions["issues/lock"] = github.put(
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
    functions["issues/unlock"] = github.delete(
        "/repos/{owner}/{repo}/issues/{issue_number}/lock",
        t.struct(
            {"owner": t.string(), "repo": t.string(), "issue_number": t.integer()}
        ),
        t.boolean().optional(),
    )
    functions["reactions/list-for-issue"] = github.get(
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
    functions["reactions/create-for-issue"] = github.post(
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
    functions["reactions/delete-for-issue"] = github.delete(
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
    functions["issues/list-events-for-timeline"] = github.get(
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
        t.array(t.proxy(renames["timeline-issue-events"])).optional(),
    )
    functions["repos/list-deploy-keys"] = github.get(
        "/repos/{owner}/{repo}/keys",
        t.struct(
            {
                "owner": t.string(),
                "repo": t.string(),
                "per_page": t.integer(),
                "page": t.integer(),
            }
        ),
        t.array(t.proxy(renames["deploy-key"])),
    )
    functions["repos/create-deploy-key"] = github.post(
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
        t.proxy(renames["deploy-key"]),
        content_type="application/json",
        body_fields=("title", "key", "read_only"),
    )
    functions["repos/get-deploy-key"] = github.get(
        "/repos/{owner}/{repo}/keys/{key_id}",
        t.struct({"owner": t.string(), "repo": t.string(), "key_id": t.integer()}),
        t.proxy(renames["deploy-key"]).optional(),
    )
    functions["repos/delete-deploy-key"] = github.delete(
        "/repos/{owner}/{repo}/keys/{key_id}",
        t.struct({"owner": t.string(), "repo": t.string(), "key_id": t.integer()}),
        t.boolean(),
    )
    functions["issues/list-labels-for-repo"] = github.get(
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
    functions["issues/create-label"] = github.post(
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
    functions["issues/get-label"] = github.get(
        "/repos/{owner}/{repo}/labels/{name}",
        t.struct({"owner": t.string(), "repo": t.string(), "name": t.string()}),
        t.proxy(renames["label"]).optional(),
    )
    functions["issues/update-label"] = github.patch(
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
    functions["issues/delete-label"] = github.delete(
        "/repos/{owner}/{repo}/labels/{name}",
        t.struct({"owner": t.string(), "repo": t.string(), "name": t.string()}),
        t.boolean(),
    )
    functions["repos/list-languages"] = github.get(
        "/repos/{owner}/{repo}/languages",
        t.struct({"owner": t.string(), "repo": t.string()}),
        t.proxy(renames["language"]),
    )
    functions["licenses/get-for-repo"] = github.get(
        "/repos/{owner}/{repo}/license",
        t.struct({"owner": t.string(), "repo": t.string()}),
        t.proxy(renames["license-content"]),
    )
    functions["repos/merge"] = github.post(
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
    functions["issues/list-milestones"] = github.get(
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
    functions["issues/create-milestone"] = github.post(
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
    functions["issues/get-milestone"] = github.get(
        "/repos/{owner}/{repo}/milestones/{milestone_number}",
        t.struct(
            {"owner": t.string(), "repo": t.string(), "milestone_number": t.integer()}
        ),
        t.proxy(renames["milestone"]).optional(),
    )
    functions["issues/update-milestone"] = github.patch(
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
    functions["issues/delete-milestone"] = github.delete(
        "/repos/{owner}/{repo}/milestones/{milestone_number}",
        t.struct(
            {"owner": t.string(), "repo": t.string(), "milestone_number": t.integer()}
        ),
        t.boolean().optional(),
    )
    functions["issues/list-labels-for-milestone"] = github.get(
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
    functions["activity/list-repo-notifications-for-authenticated-user"] = github.get(
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
    functions["activity/mark-repo-notifications-as-read"] = github.put(
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
    functions["repos/get-pages"] = github.get(
        "/repos/{owner}/{repo}/pages",
        t.struct({"owner": t.string(), "repo": t.string()}),
        t.proxy(renames["page"]).optional(),
    )
    functions["repos/create-pages-site"] = github.post(
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
    functions["repos/delete-pages-site"] = github.delete(
        "/repos/{owner}/{repo}/pages",
        t.struct({"owner": t.string(), "repo": t.string()}),
        t.boolean().optional(),
    )
    functions["repos/list-pages-builds"] = github.get(
        "/repos/{owner}/{repo}/pages/builds",
        t.struct(
            {
                "owner": t.string(),
                "repo": t.string(),
                "per_page": t.integer(),
                "page": t.integer(),
            }
        ),
        t.array(t.proxy(renames["page-build"])),
    )
    functions["repos/request-pages-build"] = github.post(
        "/repos/{owner}/{repo}/pages/builds",
        t.struct({"owner": t.string(), "repo": t.string()}),
        t.proxy(renames["page-build-status"]),
    )
    functions["repos/get-latest-pages-build"] = github.get(
        "/repos/{owner}/{repo}/pages/builds/latest",
        t.struct({"owner": t.string(), "repo": t.string()}),
        t.proxy(renames["page-build"]),
    )
    functions["repos/get-pages-build"] = github.get(
        "/repos/{owner}/{repo}/pages/builds/{build_id}",
        t.struct({"owner": t.string(), "repo": t.string(), "build_id": t.integer()}),
        t.proxy(renames["page-build"]),
    )
    functions["enterprise-admin/list-pre-receive-hooks-for-repo"] = github.get(
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
        t.array(t.proxy(renames["repository-pre-receive-hook"])),
    )
    functions["enterprise-admin/get-pre-receive-hook-for-repo"] = github.get(
        "/repos/{owner}/{repo}/pre-receive-hooks/{pre_receive_hook_id}",
        t.struct(
            {
                "owner": t.string(),
                "repo": t.string(),
                "pre_receive_hook_id": t.integer(),
            }
        ),
        t.proxy(renames["repository-pre-receive-hook"]),
    )
    functions[
        "enterprise-admin/update-pre-receive-hook-enforcement-for-repo"
    ] = github.patch(
        "/repos/{owner}/{repo}/pre-receive-hooks/{pre_receive_hook_id}",
        t.struct(
            {
                "owner": t.string(),
                "repo": t.string(),
                "pre_receive_hook_id": t.integer(),
                "enforcement": t.string().optional(),
            }
        ),
        t.proxy(renames["repository-pre-receive-hook"]),
        content_type="application/json",
        body_fields=("enforcement",),
    )
    functions[
        "enterprise-admin/remove-pre-receive-hook-enforcement-for-repo"
    ] = github.delete(
        "/repos/{owner}/{repo}/pre-receive-hooks/{pre_receive_hook_id}",
        t.struct(
            {
                "owner": t.string(),
                "repo": t.string(),
                "pre_receive_hook_id": t.integer(),
            }
        ),
        t.proxy(renames["repository-pre-receive-hook"]),
    )
    functions["projects/list-for-repo"] = github.get(
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
    functions["projects/create-for-repo"] = github.post(
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
    functions["pulls/list"] = github.get(
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
        t.array(t.proxy(renames["pull-request-simple"])),
    )
    functions["pulls/create"] = github.post(
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
        t.proxy(renames["pull-request"]),
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
    functions["pulls/list-review-comments-for-repo"] = github.get(
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
        t.array(t.proxy(renames["pull-request-review-comment"])),
    )
    functions["pulls/get-review-comment"] = github.get(
        "/repos/{owner}/{repo}/pulls/comments/{comment_id}",
        t.struct({"owner": t.string(), "repo": t.string(), "comment_id": t.integer()}),
        t.proxy(renames["pull-request-review-comment"]).optional(),
    )
    functions["pulls/update-review-comment"] = github.patch(
        "/repos/{owner}/{repo}/pulls/comments/{comment_id}",
        t.struct(
            {
                "owner": t.string(),
                "repo": t.string(),
                "comment_id": t.integer(),
                "body": t.string(),
            }
        ),
        t.proxy(renames["pull-request-review-comment"]),
        content_type="application/json",
        body_fields=("body",),
    )
    functions["pulls/delete-review-comment"] = github.delete(
        "/repos/{owner}/{repo}/pulls/comments/{comment_id}",
        t.struct({"owner": t.string(), "repo": t.string(), "comment_id": t.integer()}),
        t.boolean().optional(),
    )
    functions["reactions/list-for-pull-request-review-comment"] = github.get(
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
    functions["reactions/create-for-pull-request-review-comment"] = github.post(
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
    functions["reactions/delete-for-pull-request-comment"] = github.delete(
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
    functions["pulls/get"] = github.get(
        "/repos/{owner}/{repo}/pulls/{pull_number}",
        t.struct({"owner": t.string(), "repo": t.string(), "pull_number": t.integer()}),
        t.proxy(renames["pull-request"]).optional(),
    )
    functions["pulls/update"] = github.patch(
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
        t.proxy(renames["pull-request"]),
        content_type="application/json",
        body_fields=("title", "body", "state", "base", "maintainer_can_modify"),
    )
    functions["pulls/list-review-comments"] = github.get(
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
        t.array(t.proxy(renames["pull-request-review-comment"])),
    )
    functions["pulls/create-review-comment"] = github.post(
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
        t.proxy(renames["pull-request-review-comment"]),
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
    functions["pulls/create-reply-for-review-comment"] = github.post(
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
        t.proxy(renames["pull-request-review-comment"]).optional(),
        content_type="application/json",
        body_fields=("body",),
    )
    functions["pulls/list-commits"] = github.get(
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
    functions["pulls/list-files"] = github.get(
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
        t.array(t.proxy(renames["diff-entry"])),
    )
    functions["pulls/check-if-merged"] = github.get(
        "/repos/{owner}/{repo}/pulls/{pull_number}/merge",
        t.struct({"owner": t.string(), "repo": t.string(), "pull_number": t.integer()}),
        t.boolean().optional(),
    )
    functions["pulls/merge"] = github.put(
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
        t.proxy(renames["pull-request-merge-result"]).optional(),
        content_type="application/json",
        body_fields=("commit_title", "commit_message", "sha", "merge_method"),
    )
    functions["pulls/list-requested-reviewers"] = github.get(
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
        t.proxy(renames["pull-request-review-request"]),
    )
    functions["pulls/remove-requested-reviewers"] = github.delete(
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
        t.proxy(renames["pull-request-simple"]),
        content_type="application/json",
        body_fields=("reviewers", "team_reviewers"),
    )
    functions["pulls/list-reviews"] = github.get(
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
        t.array(t.proxy(renames["pull-request-review"])),
    )
    functions["pulls/create-review"] = github.post(
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
        t.proxy(renames["pull-request-review"]),
        content_type="application/json",
        body_fields=("commit_id", "body", "event", "comments"),
    )
    functions["pulls/get-review"] = github.get(
        "/repos/{owner}/{repo}/pulls/{pull_number}/reviews/{review_id}",
        t.struct(
            {
                "owner": t.string(),
                "repo": t.string(),
                "pull_number": t.integer(),
                "review_id": t.integer(),
            }
        ),
        t.proxy(renames["pull-request-review"]).optional(),
    )
    functions["pulls/update-review"] = github.put(
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
        t.proxy(renames["pull-request-review"]),
        content_type="application/json",
        body_fields=("body",),
    )
    functions["pulls/delete-pending-review"] = github.delete(
        "/repos/{owner}/{repo}/pulls/{pull_number}/reviews/{review_id}",
        t.struct(
            {
                "owner": t.string(),
                "repo": t.string(),
                "pull_number": t.integer(),
                "review_id": t.integer(),
            }
        ),
        t.proxy(renames["pull-request-review"]).optional(),
    )
    functions["pulls/list-comments-for-review"] = github.get(
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
        t.array(t.proxy(renames["review-comment"])).optional(),
    )
    functions["pulls/dismiss-review"] = github.put(
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
        t.proxy(renames["pull-request-review"]).optional(),
        content_type="application/json",
        body_fields=("message", "event"),
    )
    functions["pulls/submit-review"] = github.post(
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
        t.proxy(renames["pull-request-review"]).optional(),
        content_type="application/json",
        body_fields=("body", "event"),
    )
    functions["pulls/update-branch"] = github.put(
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
    functions["repos/get-readme"] = github.get(
        "/repos/{owner}/{repo}/readme",
        t.struct({"owner": t.string(), "repo": t.string(), "ref": t.string()}),
        t.proxy(renames["content-file"]).optional(),
    )
    functions["repos/get-readme-in-directory"] = github.get(
        "/repos/{owner}/{repo}/readme/{dir}",
        t.struct(
            {
                "owner": t.string(),
                "repo": t.string(),
                "dir": t.string(),
                "ref": t.string(),
            }
        ),
        t.proxy(renames["content-file"]).optional(),
    )
    functions["repos/list-releases"] = github.get(
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
    functions["repos/create-release"] = github.post(
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
    functions["repos/get-release-asset"] = github.get(
        "/repos/{owner}/{repo}/releases/assets/{asset_id}",
        t.struct({"owner": t.string(), "repo": t.string(), "asset_id": t.integer()}),
        t.proxy(renames["release-asset"]).optional(),
    )
    functions["repos/update-release-asset"] = github.patch(
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
        t.proxy(renames["release-asset"]),
        content_type="application/json",
        body_fields=("name", "label", "state"),
    )
    functions["repos/delete-release-asset"] = github.delete(
        "/repos/{owner}/{repo}/releases/assets/{asset_id}",
        t.struct({"owner": t.string(), "repo": t.string(), "asset_id": t.integer()}),
        t.boolean(),
    )
    functions["repos/get-latest-release"] = github.get(
        "/repos/{owner}/{repo}/releases/latest",
        t.struct({"owner": t.string(), "repo": t.string()}),
        t.proxy(renames["release"]),
    )
    functions["repos/get-release-by-tag"] = github.get(
        "/repos/{owner}/{repo}/releases/tags/{tag}",
        t.struct({"owner": t.string(), "repo": t.string(), "tag": t.string()}),
        t.proxy(renames["release"]).optional(),
    )
    functions["repos/get-release"] = github.get(
        "/repos/{owner}/{repo}/releases/{release_id}",
        t.struct({"owner": t.string(), "repo": t.string(), "release_id": t.integer()}),
        t.proxy(renames["release"]).optional(),
    )
    functions["repos/update-release"] = github.patch(
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
    functions["repos/delete-release"] = github.delete(
        "/repos/{owner}/{repo}/releases/{release_id}",
        t.struct({"owner": t.string(), "repo": t.string(), "release_id": t.integer()}),
        t.boolean(),
    )
    functions["repos/list-release-assets"] = github.get(
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
        t.array(t.proxy(renames["release-asset"])),
    )
    functions["activity/list-stargazers-for-repo"] = github.get(
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
                t.array(t.proxy(renames["simple-user"])),
                t.array(t.proxy(renames["stargazer"])),
            ]
        ),
    )
    functions["repos/get-code-frequency-stats"] = github.get(
        "/repos/{owner}/{repo}/stats/code_frequency",
        t.struct({"owner": t.string(), "repo": t.string()}),
        t.array(t.proxy(renames["code-frequency-stat"])),
    )
    functions["repos/get-commit-activity-stats"] = github.get(
        "/repos/{owner}/{repo}/stats/commit_activity",
        t.struct({"owner": t.string(), "repo": t.string()}),
        t.array(t.proxy(renames["commit-activity"])),
    )
    functions["repos/get-contributors-stats"] = github.get(
        "/repos/{owner}/{repo}/stats/contributors",
        t.struct({"owner": t.string(), "repo": t.string()}),
        t.array(t.proxy(renames["contributor-activity"])),
    )
    functions["repos/get-participation-stats"] = github.get(
        "/repos/{owner}/{repo}/stats/participation",
        t.struct({"owner": t.string(), "repo": t.string()}),
        t.proxy(renames["participation-stats"]).optional(),
    )
    functions["repos/get-punch-card-stats"] = github.get(
        "/repos/{owner}/{repo}/stats/punch_card",
        t.struct({"owner": t.string(), "repo": t.string()}),
        t.array(t.proxy(renames["code-frequency-stat"])),
    )
    functions["repos/create-commit-status"] = github.post(
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
    functions["activity/list-watchers-for-repo"] = github.get(
        "/repos/{owner}/{repo}/subscribers",
        t.struct(
            {
                "owner": t.string(),
                "repo": t.string(),
                "per_page": t.integer(),
                "page": t.integer(),
            }
        ),
        t.array(t.proxy(renames["simple-user"])),
    )
    functions["activity/get-repo-subscription"] = github.get(
        "/repos/{owner}/{repo}/subscription",
        t.struct({"owner": t.string(), "repo": t.string()}),
        t.proxy(renames["repository-subscription"]).optional(),
    )
    functions["activity/set-repo-subscription"] = github.put(
        "/repos/{owner}/{repo}/subscription",
        t.struct(
            {
                "owner": t.string(),
                "repo": t.string(),
                "subscribed": t.boolean().optional(),
                "ignored": t.boolean().optional(),
            }
        ),
        t.proxy(renames["repository-subscription"]),
        content_type="application/json",
        body_fields=("subscribed", "ignored"),
    )
    functions["activity/delete-repo-subscription"] = github.delete(
        "/repos/{owner}/{repo}/subscription",
        t.struct({"owner": t.string(), "repo": t.string()}),
        t.boolean(),
    )
    functions["repos/list-tags"] = github.get(
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
    functions["repos/download-tarball-archive"] = github.get(
        "/repos/{owner}/{repo}/tarball/{ref}",
        t.struct({"owner": t.string(), "repo": t.string(), "ref": t.string()}),
        t.struct({}),
    )
    functions["repos/list-teams"] = github.get(
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
    functions["repos/get-all-topics"] = github.get(
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
    functions["repos/replace-all-topics"] = github.put(
        "/repos/{owner}/{repo}/topics",
        t.struct(
            {"owner": t.string(), "repo": t.string(), "names": t.array(t.string())}
        ),
        t.proxy(renames["topic"]).optional(),
        content_type="application/json",
        body_fields=("names",),
    )
    functions["repos/transfer"] = github.post(
        "/repos/{owner}/{repo}/transfer",
        t.struct(
            {
                "owner": t.string(),
                "repo": t.string(),
                "new_owner": t.string(),
                "team_ids": t.array(t.integer()).optional(),
            }
        ),
        t.proxy(renames["minimal-repository"]),
        content_type="application/json",
        body_fields=("new_owner", "team_ids"),
    )
    functions["repos/download-zipball-archive"] = github.get(
        "/repos/{owner}/{repo}/zipball/{ref}",
        t.struct({"owner": t.string(), "repo": t.string(), "ref": t.string()}),
        t.struct({}),
    )
    functions["repos/create-using-template"] = github.post(
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
    functions["repos/list-public"] = github.get(
        "/repositories",
        t.struct({"since": t.integer(), "visibility": t.string()}),
        t.array(t.proxy(renames["minimal-repository"])),
    )
    functions["search/code"] = github.get(
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
                "items": t.array(t.proxy(renames["code-search-result-item"])),
            }
        ),
    )
    functions["search/commits"] = github.get(
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
                "items": t.array(t.proxy(renames["commit-search-result-item"])),
            }
        ),
    )
    functions["search/issues-and-pull-requests"] = github.get(
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
                "items": t.array(t.proxy(renames["issue-search-result-item"])),
            }
        ),
    )
    functions["search/labels"] = github.get(
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
                "items": t.array(t.proxy(renames["label-search-result-item"])),
            }
        ).optional(),
    )
    functions["search/repos"] = github.get(
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
                "items": t.array(t.proxy(renames["repo-search-result-item"])),
            }
        ),
    )
    functions["search/topics"] = github.get(
        "/search/topics",
        t.struct({"q": t.string(), "per_page": t.integer(), "page": t.integer()}),
        t.struct(
            {
                "total_count": t.integer(),
                "incomplete_results": t.boolean(),
                "items": t.array(t.proxy(renames["topic-search-result-item"])),
            }
        ),
    )
    functions["search/users"] = github.get(
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
                "items": t.array(t.proxy(renames["user-search-result-item"])),
            }
        ),
    )
    functions["enterprise-admin/get-configuration-status"] = github.get(
        "/setup/api/configcheck",
        t.struct({}),
        t.proxy(renames["configuration-status"]),
    )
    functions["enterprise-admin/start-configuration-process"] = github.post(
        "/setup/api/configure",
        t.struct({}),
        t.struct({}),
    )
    functions["enterprise-admin/get-maintenance-status"] = github.get(
        "/setup/api/maintenance",
        t.struct({}),
        t.proxy(renames["maintenance-status"]),
    )
    functions["enterprise-admin/enable-or-disable-maintenance-mode"] = github.post(
        "/setup/api/maintenance",
        t.struct({"maintenance": t.string()}),
        t.proxy(renames["maintenance-status"]),
        content_type="application/x-www-form-urlencoded",
        body_fields=("maintenance",),
    )
    functions["enterprise-admin/get-settings"] = github.get(
        "/setup/api/settings",
        t.struct({}),
        t.proxy(renames["enterprise-settings"]),
    )
    functions["enterprise-admin/set-settings"] = github.put(
        "/setup/api/settings",
        t.struct({"settings": t.string()}),
        t.boolean(),
        content_type="application/x-www-form-urlencoded",
        body_fields=("settings",),
    )
    functions["enterprise-admin/get-all-authorized-ssh-keys"] = github.get(
        "/setup/api/settings/authorized-keys",
        t.struct({}),
        t.array(t.proxy(renames["ssh-key"])),
    )
    functions["enterprise-admin/add-authorized-ssh-key"] = github.post(
        "/setup/api/settings/authorized-keys",
        t.struct({"authorized_key": t.string()}),
        t.array(t.proxy(renames["ssh-key"])),
        content_type="application/x-www-form-urlencoded",
        body_fields=("authorized_key",),
    )
    functions["enterprise-admin/remove-authorized-ssh-key"] = github.delete(
        "/setup/api/settings/authorized-keys",
        t.struct({"authorized_key": t.string()}),
        t.array(t.proxy(renames["ssh-key"])),
        content_type="application/x-www-form-urlencoded",
        body_fields=("authorized_key",),
    )
    functions["enterprise-admin/create-enterprise-server-license"] = github.post(
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
    functions["enterprise-admin/upgrade-license"] = github.post(
        "/setup/api/upgrade",
        t.struct({"license": t.string().optional()}),
        t.struct({}),
        content_type="application/x-www-form-urlencoded",
        body_fields=("license",),
    )
    functions["teams/get-legacy"] = github.get(
        "/teams/{team_id}",
        t.struct({"team_id": t.integer()}),
        t.proxy(renames["team-full"]).optional(),
    )
    functions["teams/update-legacy"] = github.patch(
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
        t.proxy(renames["team-full"]).optional(),
        content_type="application/json",
        body_fields=("name", "description", "privacy", "permission", "parent_team_id"),
    )
    functions["teams/delete-legacy"] = github.delete(
        "/teams/{team_id}",
        t.struct({"team_id": t.integer()}),
        t.boolean().optional(),
    )
    functions["teams/list-discussions-legacy"] = github.get(
        "/teams/{team_id}/discussions",
        t.struct(
            {
                "team_id": t.integer(),
                "direction": t.string(),
                "per_page": t.integer(),
                "page": t.integer(),
            }
        ),
        t.array(t.proxy(renames["team-discussion"])),
    )
    functions["teams/create-discussion-legacy"] = github.post(
        "/teams/{team_id}/discussions",
        t.struct(
            {
                "team_id": t.integer(),
                "title": t.string(),
                "body": t.string(),
                "private": t.boolean().optional(),
            }
        ),
        t.proxy(renames["team-discussion"]),
        content_type="application/json",
        body_fields=("title", "body", "private"),
    )
    functions["teams/get-discussion-legacy"] = github.get(
        "/teams/{team_id}/discussions/{discussion_number}",
        t.struct({"team_id": t.integer(), "discussion_number": t.integer()}),
        t.proxy(renames["team-discussion"]),
    )
    functions["teams/update-discussion-legacy"] = github.patch(
        "/teams/{team_id}/discussions/{discussion_number}",
        t.struct(
            {
                "team_id": t.integer(),
                "discussion_number": t.integer(),
                "title": t.string().optional(),
                "body": t.string().optional(),
            }
        ),
        t.proxy(renames["team-discussion"]),
        content_type="application/json",
        body_fields=("title", "body"),
    )
    functions["teams/delete-discussion-legacy"] = github.delete(
        "/teams/{team_id}/discussions/{discussion_number}",
        t.struct({"team_id": t.integer(), "discussion_number": t.integer()}),
        t.boolean(),
    )
    functions["teams/list-discussion-comments-legacy"] = github.get(
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
        t.array(t.proxy(renames["team-discussion-comment"])),
    )
    functions["teams/create-discussion-comment-legacy"] = github.post(
        "/teams/{team_id}/discussions/{discussion_number}/comments",
        t.struct(
            {
                "team_id": t.integer(),
                "discussion_number": t.integer(),
                "body": t.string(),
            }
        ),
        t.proxy(renames["team-discussion-comment"]),
        content_type="application/json",
        body_fields=("body",),
    )
    functions["teams/get-discussion-comment-legacy"] = github.get(
        "/teams/{team_id}/discussions/{discussion_number}/comments/{comment_number}",
        t.struct(
            {
                "team_id": t.integer(),
                "discussion_number": t.integer(),
                "comment_number": t.integer(),
            }
        ),
        t.proxy(renames["team-discussion-comment"]),
    )
    functions["teams/update-discussion-comment-legacy"] = github.patch(
        "/teams/{team_id}/discussions/{discussion_number}/comments/{comment_number}",
        t.struct(
            {
                "team_id": t.integer(),
                "discussion_number": t.integer(),
                "comment_number": t.integer(),
                "body": t.string(),
            }
        ),
        t.proxy(renames["team-discussion-comment"]),
        content_type="application/json",
        body_fields=("body",),
    )
    functions["teams/delete-discussion-comment-legacy"] = github.delete(
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
    functions["reactions/list-for-team-discussion-comment-legacy"] = github.get(
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
    functions["reactions/create-for-team-discussion-comment-legacy"] = github.post(
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
    functions["reactions/list-for-team-discussion-legacy"] = github.get(
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
    functions["reactions/create-for-team-discussion-legacy"] = github.post(
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
    functions["teams/list-members-legacy"] = github.get(
        "/teams/{team_id}/members",
        t.struct(
            {
                "team_id": t.integer(),
                "role": t.string(),
                "per_page": t.integer(),
                "page": t.integer(),
            }
        ),
        t.array(t.proxy(renames["simple-user"])).optional(),
    )
    functions["teams/get-member-legacy"] = github.get(
        "/teams/{team_id}/members/{username}",
        t.struct({"team_id": t.integer(), "username": t.string()}),
        t.boolean().optional(),
    )
    functions["teams/add-member-legacy"] = github.put(
        "/teams/{team_id}/members/{username}",
        t.struct({"team_id": t.integer(), "username": t.string()}),
        t.boolean().optional(),
    )
    functions["teams/remove-member-legacy"] = github.delete(
        "/teams/{team_id}/members/{username}",
        t.struct({"team_id": t.integer(), "username": t.string()}),
        t.boolean().optional(),
    )
    functions["teams/get-membership-for-user-legacy"] = github.get(
        "/teams/{team_id}/memberships/{username}",
        t.struct({"team_id": t.integer(), "username": t.string()}),
        t.proxy(renames["team-membership"]).optional(),
    )
    functions["teams/add-or-update-membership-for-user-legacy"] = github.put(
        "/teams/{team_id}/memberships/{username}",
        t.struct(
            {
                "team_id": t.integer(),
                "username": t.string(),
                "role": t.string().optional(),
            }
        ),
        t.proxy(renames["team-membership"]).optional(),
        content_type="application/json",
        body_fields=("role",),
    )
    functions["teams/remove-membership-for-user-legacy"] = github.delete(
        "/teams/{team_id}/memberships/{username}",
        t.struct({"team_id": t.integer(), "username": t.string()}),
        t.boolean(),
    )
    functions["teams/list-projects-legacy"] = github.get(
        "/teams/{team_id}/projects",
        t.struct(
            {"team_id": t.integer(), "per_page": t.integer(), "page": t.integer()}
        ),
        t.array(t.proxy(renames["team-project"])).optional(),
    )
    functions["teams/check-permissions-for-project-legacy"] = github.get(
        "/teams/{team_id}/projects/{project_id}",
        t.struct({"team_id": t.integer(), "project_id": t.integer()}),
        t.proxy(renames["team-project"]).optional(),
    )
    functions["teams/add-or-update-project-permissions-legacy"] = github.put(
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
    functions["teams/remove-project-legacy"] = github.delete(
        "/teams/{team_id}/projects/{project_id}",
        t.struct({"team_id": t.integer(), "project_id": t.integer()}),
        t.boolean().optional(),
    )
    functions["teams/list-repos-legacy"] = github.get(
        "/teams/{team_id}/repos",
        t.struct(
            {"team_id": t.integer(), "per_page": t.integer(), "page": t.integer()}
        ),
        t.array(t.proxy(renames["minimal-repository"])).optional(),
    )
    functions["teams/check-permissions-for-repo-legacy"] = github.get(
        "/teams/{team_id}/repos/{owner}/{repo}",
        t.struct({"team_id": t.integer(), "owner": t.string(), "repo": t.string()}),
        t.proxy(renames["team-repository"]).optional(),
    )
    functions["teams/add-or-update-repo-permissions-legacy"] = github.put(
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
    functions["teams/remove-repo-legacy"] = github.delete(
        "/teams/{team_id}/repos/{owner}/{repo}",
        t.struct({"team_id": t.integer(), "owner": t.string(), "repo": t.string()}),
        t.boolean(),
    )
    functions["teams/list-child-legacy"] = github.get(
        "/teams/{team_id}/teams",
        t.struct(
            {"team_id": t.integer(), "per_page": t.integer(), "page": t.integer()}
        ),
        t.array(t.proxy(renames["team"])).optional(),
    )
    functions["users/get-authenticated"] = github.get(
        "/user",
        t.struct({}),
        t.either([t.proxy(renames["private-user"]), t.proxy(renames["public-user"])]),
    )
    functions["users/update-authenticated"] = github.patch(
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
        t.proxy(renames["private-user"]).optional(),
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
    functions["users/list-emails-for-authenticated-user"] = github.get(
        "/user/emails",
        t.struct({"per_page": t.integer(), "page": t.integer()}),
        t.array(t.proxy(renames["email"])).optional(),
    )
    functions["users/list-followers-for-authenticated-user"] = github.get(
        "/user/followers",
        t.struct({"per_page": t.integer(), "page": t.integer()}),
        t.array(t.proxy(renames["simple-user"])),
    )
    functions["users/list-followed-by-authenticated-user"] = github.get(
        "/user/following",
        t.struct({"per_page": t.integer(), "page": t.integer()}),
        t.array(t.proxy(renames["simple-user"])),
    )
    functions["users/check-person-is-followed-by-authenticated"] = github.get(
        "/user/following/{username}",
        t.struct({"username": t.string()}),
        t.boolean().optional(),
    )
    functions["users/follow"] = github.put(
        "/user/following/{username}",
        t.struct({"username": t.string()}),
        t.boolean().optional(),
    )
    functions["users/unfollow"] = github.delete(
        "/user/following/{username}",
        t.struct({"username": t.string()}),
        t.boolean().optional(),
    )
    functions["users/list-gpg-keys-for-authenticated-user"] = github.get(
        "/user/gpg_keys",
        t.struct({"per_page": t.integer(), "page": t.integer()}),
        t.array(t.proxy(renames["gpg-key"])).optional(),
    )
    functions["users/create-gpg-key-for-authenticated-user"] = github.post(
        "/user/gpg_keys",
        t.struct({"armored_public_key": t.string()}),
        t.proxy(renames["gpg-key"]).optional(),
        content_type="application/json",
        body_fields=("armored_public_key",),
    )
    functions["users/get-gpg-key-for-authenticated-user"] = github.get(
        "/user/gpg_keys/{gpg_key_id}",
        t.struct({"gpg_key_id": t.integer()}),
        t.proxy(renames["gpg-key"]).optional(),
    )
    functions["users/delete-gpg-key-for-authenticated-user"] = github.delete(
        "/user/gpg_keys/{gpg_key_id}",
        t.struct({"gpg_key_id": t.integer()}),
        t.boolean().optional(),
    )
    functions["apps/list-installations-for-authenticated-user"] = github.get(
        "/user/installations",
        t.struct({"per_page": t.integer(), "page": t.integer()}),
        t.struct(
            {
                "total_count": t.integer(),
                "installations": t.array(t.proxy(renames["installation"])),
            }
        ),
    )
    functions["apps/list-installation-repos-for-authenticated-user"] = github.get(
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
    functions["apps/add-repo-to-installation-for-authenticated-user"] = github.put(
        "/user/installations/{installation_id}/repositories/{repository_id}",
        t.struct({"installation_id": t.integer(), "repository_id": t.integer()}),
        t.boolean().optional(),
    )
    functions[
        "apps/remove-repo-from-installation-for-authenticated-user"
    ] = github.delete(
        "/user/installations/{installation_id}/repositories/{repository_id}",
        t.struct({"installation_id": t.integer(), "repository_id": t.integer()}),
        t.boolean().optional(),
    )
    functions["issues/list-for-authenticated-user"] = github.get(
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
    functions["users/list-public-ssh-keys-for-authenticated-user"] = github.get(
        "/user/keys",
        t.struct({"per_page": t.integer(), "page": t.integer()}),
        t.array(t.proxy(renames["key"])).optional(),
    )
    functions["users/create-public-ssh-key-for-authenticated-user"] = github.post(
        "/user/keys",
        t.struct({"title": t.string().optional(), "key": t.string()}),
        t.proxy(renames["key"]).optional(),
        content_type="application/json",
        body_fields=("title", "key"),
    )
    functions["users/get-public-ssh-key-for-authenticated-user"] = github.get(
        "/user/keys/{key_id}",
        t.struct({"key_id": t.integer()}),
        t.proxy(renames["key"]).optional(),
    )
    functions["users/delete-public-ssh-key-for-authenticated-user"] = github.delete(
        "/user/keys/{key_id}",
        t.struct({"key_id": t.integer()}),
        t.boolean().optional(),
    )
    functions["orgs/list-memberships-for-authenticated-user"] = github.get(
        "/user/memberships/orgs",
        t.struct({"state": t.string(), "per_page": t.integer(), "page": t.integer()}),
        t.array(t.proxy(renames["org-membership"])),
    )
    functions["orgs/get-membership-for-authenticated-user"] = github.get(
        "/user/memberships/orgs/{org}",
        t.struct({"org": t.string()}),
        t.proxy(renames["org-membership"]).optional(),
    )
    functions["orgs/update-membership-for-authenticated-user"] = github.patch(
        "/user/memberships/orgs/{org}",
        t.struct({"org": t.string(), "state": t.string()}),
        t.proxy(renames["org-membership"]).optional(),
        content_type="application/json",
        body_fields=("state",),
    )
    functions["orgs/list-for-authenticated-user"] = github.get(
        "/user/orgs",
        t.struct({"per_page": t.integer(), "page": t.integer()}),
        t.array(t.proxy(renames["organization-simple"])),
    )
    functions["projects/create-for-authenticated-user"] = github.post(
        "/user/projects",
        t.struct({"name": t.string(), "body": t.string().optional()}),
        t.proxy(renames["project"]),
        content_type="application/json",
        body_fields=("name", "body"),
    )
    functions["users/list-public-emails-for-authenticated-user"] = github.get(
        "/user/public_emails",
        t.struct({"per_page": t.integer(), "page": t.integer()}),
        t.array(t.proxy(renames["email"])).optional(),
    )
    functions["repos/list-for-authenticated-user"] = github.get(
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
    functions["repos/create-for-authenticated-user"] = github.post(
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
    functions["repos/list-invitations-for-authenticated-user"] = github.get(
        "/user/repository_invitations",
        t.struct({"per_page": t.integer(), "page": t.integer()}),
        t.array(t.proxy(renames["repository-invitation"])).optional(),
    )
    functions["repos/accept-invitation-for-authenticated-user"] = github.patch(
        "/user/repository_invitations/{invitation_id}",
        t.struct({"invitation_id": t.integer()}),
        t.boolean().optional(),
    )
    functions["repos/decline-invitation-for-authenticated-user"] = github.delete(
        "/user/repository_invitations/{invitation_id}",
        t.struct({"invitation_id": t.integer()}),
        t.boolean().optional(),
    )
    functions["activity/list-repos-starred-by-authenticated-user"] = github.get(
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
    functions["activity/check-repo-is-starred-by-authenticated-user"] = github.get(
        "/user/starred/{owner}/{repo}",
        t.struct({"owner": t.string(), "repo": t.string()}),
        t.boolean().optional(),
    )
    functions["activity/star-repo-for-authenticated-user"] = github.put(
        "/user/starred/{owner}/{repo}",
        t.struct({"owner": t.string(), "repo": t.string()}),
        t.boolean().optional(),
    )
    functions["activity/unstar-repo-for-authenticated-user"] = github.delete(
        "/user/starred/{owner}/{repo}",
        t.struct({"owner": t.string(), "repo": t.string()}),
        t.boolean().optional(),
    )
    functions["activity/list-watched-repos-for-authenticated-user"] = github.get(
        "/user/subscriptions",
        t.struct({"per_page": t.integer(), "page": t.integer()}),
        t.array(t.proxy(renames["minimal-repository"])),
    )
    functions["teams/list-for-authenticated-user"] = github.get(
        "/user/teams",
        t.struct({"per_page": t.integer(), "page": t.integer()}),
        t.array(t.proxy(renames["team-full"])).optional(),
    )
    functions["users/list"] = github.get(
        "/users",
        t.struct({"since": t.integer(), "per_page": t.integer()}),
        t.array(t.proxy(renames["simple-user"])),
    )
    functions["users/get-by-username"] = github.get(
        "/users/{username}",
        t.struct({"username": t.string()}),
        t.either(
            [t.proxy(renames["private-user"]), t.proxy(renames["public-user"])]
        ).optional(),
    )
    functions["activity/list-events-for-authenticated-user"] = github.get(
        "/users/{username}/events",
        t.struct(
            {"username": t.string(), "per_page": t.integer(), "page": t.integer()}
        ),
        t.array(t.proxy(renames["event"])),
    )
    functions["activity/list-org-events-for-authenticated-user"] = github.get(
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
    functions["activity/list-public-events-for-user"] = github.get(
        "/users/{username}/events/public",
        t.struct(
            {"username": t.string(), "per_page": t.integer(), "page": t.integer()}
        ),
        t.array(t.proxy(renames["event"])),
    )
    functions["users/list-followers-for-user"] = github.get(
        "/users/{username}/followers",
        t.struct(
            {"username": t.string(), "per_page": t.integer(), "page": t.integer()}
        ),
        t.array(t.proxy(renames["simple-user"])),
    )
    functions["users/list-following-for-user"] = github.get(
        "/users/{username}/following",
        t.struct(
            {"username": t.string(), "per_page": t.integer(), "page": t.integer()}
        ),
        t.array(t.proxy(renames["simple-user"])),
    )
    functions["users/check-following-for-user"] = github.get(
        "/users/{username}/following/{target_user}",
        t.struct({"username": t.string(), "target_user": t.string()}),
        t.boolean().optional(),
    )
    functions["gists/list-for-user"] = github.get(
        "/users/{username}/gists",
        t.struct(
            {
                "username": t.string(),
                "since": t.string(),
                "per_page": t.integer(),
                "page": t.integer(),
            }
        ),
        t.array(t.proxy(renames["base-gist"])),
    )
    functions["users/list-gpg-keys-for-user"] = github.get(
        "/users/{username}/gpg_keys",
        t.struct(
            {"username": t.string(), "per_page": t.integer(), "page": t.integer()}
        ),
        t.array(t.proxy(renames["gpg-key"])),
    )
    functions["users/get-context-for-user"] = github.get(
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
    functions["apps/get-user-installation"] = github.get(
        "/users/{username}/installation",
        t.struct({"username": t.string()}),
        t.proxy(renames["installation"]),
    )
    functions["users/list-public-keys-for-user"] = github.get(
        "/users/{username}/keys",
        t.struct(
            {"username": t.string(), "per_page": t.integer(), "page": t.integer()}
        ),
        t.array(t.proxy(renames["key-simple"])),
    )
    functions["orgs/list-for-user"] = github.get(
        "/users/{username}/orgs",
        t.struct(
            {"username": t.string(), "per_page": t.integer(), "page": t.integer()}
        ),
        t.array(t.proxy(renames["organization-simple"])),
    )
    functions["projects/list-for-user"] = github.get(
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
    functions["activity/list-received-events-for-user"] = github.get(
        "/users/{username}/received_events",
        t.struct(
            {"username": t.string(), "per_page": t.integer(), "page": t.integer()}
        ),
        t.array(t.proxy(renames["event"])),
    )
    functions["activity/list-received-public-events-for-user"] = github.get(
        "/users/{username}/received_events/public",
        t.struct(
            {"username": t.string(), "per_page": t.integer(), "page": t.integer()}
        ),
        t.array(t.proxy(renames["event"])),
    )
    functions["repos/list-for-user"] = github.get(
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
        t.array(t.proxy(renames["minimal-repository"])),
    )
    functions["enterprise-admin/promote-user-to-be-site-administrator"] = github.put(
        "/users/{username}/site_admin",
        t.struct({"username": t.string()}),
        t.boolean(),
    )
    functions["enterprise-admin/demote-site-administrator"] = github.delete(
        "/users/{username}/site_admin",
        t.struct({"username": t.string()}),
        t.boolean(),
    )
    functions["activity/list-repos-starred-by-user"] = github.get(
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
                t.array(t.proxy(renames["starred-repository"])),
                t.array(t.proxy(renames["repository"])),
            ]
        ),
    )
    functions["activity/list-repos-watched-by-user"] = github.get(
        "/users/{username}/subscriptions",
        t.struct(
            {"username": t.string(), "per_page": t.integer(), "page": t.integer()}
        ),
        t.array(t.proxy(renames["minimal-repository"])),
    )
    functions["enterprise-admin/suspend-user"] = github.put(
        "/users/{username}/suspended",
        t.struct({"username": t.string(), "reason": t.string().optional()}),
        t.boolean(),
        content_type="application/json",
        body_fields=("reason",),
    )
    functions["enterprise-admin/unsuspend-user"] = github.delete(
        "/users/{username}/suspended",
        t.struct({"username": t.string(), "reason": t.string().optional()}),
        t.boolean(),
        content_type="application/json",
        body_fields=("reason",),
    )

    return Import(
        importer="github", renames=renames, types=Box(types), functions=Box(functions)
    )
