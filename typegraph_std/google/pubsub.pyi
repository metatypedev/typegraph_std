from typegraph import t

class TypeList:
    ErrorResponse: t.typedef = ...
    ExprIn: t.typedef = ...
    ExprOut: t.typedef = ...
    BindingIn: t.typedef = ...
    BindingOut: t.typedef = ...
    ListSchemaRevisionsResponseIn: t.typedef = ...
    ListSchemaRevisionsResponseOut: t.typedef = ...
    PullResponseIn: t.typedef = ...
    PullResponseOut: t.typedef = ...
    PolicyIn: t.typedef = ...
    PolicyOut: t.typedef = ...
    PushConfigIn: t.typedef = ...
    PushConfigOut: t.typedef = ...
    SeekResponseIn: t.typedef = ...
    SeekResponseOut: t.typedef = ...
    CommitSchemaRequestIn: t.typedef = ...
    CommitSchemaRequestOut: t.typedef = ...
    PublishRequestIn: t.typedef = ...
    PublishRequestOut: t.typedef = ...
    TestIamPermissionsResponseIn: t.typedef = ...
    TestIamPermissionsResponseOut: t.typedef = ...
    TopicIn: t.typedef = ...
    TopicOut: t.typedef = ...
    SchemaSettingsIn: t.typedef = ...
    SchemaSettingsOut: t.typedef = ...
    PullRequestIn: t.typedef = ...
    PullRequestOut: t.typedef = ...
    DeadLetterPolicyIn: t.typedef = ...
    DeadLetterPolicyOut: t.typedef = ...
    ListSchemasResponseIn: t.typedef = ...
    ListSchemasResponseOut: t.typedef = ...
    TextConfigIn: t.typedef = ...
    TextConfigOut: t.typedef = ...
    UpdateSubscriptionRequestIn: t.typedef = ...
    UpdateSubscriptionRequestOut: t.typedef = ...
    ListTopicSnapshotsResponseIn: t.typedef = ...
    ListTopicSnapshotsResponseOut: t.typedef = ...
    SnapshotIn: t.typedef = ...
    SnapshotOut: t.typedef = ...
    ExpirationPolicyIn: t.typedef = ...
    ExpirationPolicyOut: t.typedef = ...
    ModifyAckDeadlineRequestIn: t.typedef = ...
    ModifyAckDeadlineRequestOut: t.typedef = ...
    CreateSnapshotRequestIn: t.typedef = ...
    CreateSnapshotRequestOut: t.typedef = ...
    ModifyPushConfigRequestIn: t.typedef = ...
    ModifyPushConfigRequestOut: t.typedef = ...
    CloudStorageConfigIn: t.typedef = ...
    CloudStorageConfigOut: t.typedef = ...
    BigQueryConfigIn: t.typedef = ...
    BigQueryConfigOut: t.typedef = ...
    DetachSubscriptionResponseIn: t.typedef = ...
    DetachSubscriptionResponseOut: t.typedef = ...
    OidcTokenIn: t.typedef = ...
    OidcTokenOut: t.typedef = ...
    TestIamPermissionsRequestIn: t.typedef = ...
    TestIamPermissionsRequestOut: t.typedef = ...
    ListSubscriptionsResponseIn: t.typedef = ...
    ListSubscriptionsResponseOut: t.typedef = ...
    PubsubMessageIn: t.typedef = ...
    PubsubMessageOut: t.typedef = ...
    SeekRequestIn: t.typedef = ...
    SeekRequestOut: t.typedef = ...
    RetryPolicyIn: t.typedef = ...
    RetryPolicyOut: t.typedef = ...
    ValidateMessageResponseIn: t.typedef = ...
    ValidateMessageResponseOut: t.typedef = ...
    AvroConfigIn: t.typedef = ...
    AvroConfigOut: t.typedef = ...
    ValidateSchemaResponseIn: t.typedef = ...
    ValidateSchemaResponseOut: t.typedef = ...
    MessageStoragePolicyIn: t.typedef = ...
    MessageStoragePolicyOut: t.typedef = ...
    ListSnapshotsResponseIn: t.typedef = ...
    ListSnapshotsResponseOut: t.typedef = ...
    ListTopicSubscriptionsResponseIn: t.typedef = ...
    ListTopicSubscriptionsResponseOut: t.typedef = ...
    RollbackSchemaRequestIn: t.typedef = ...
    RollbackSchemaRequestOut: t.typedef = ...
    SetIamPolicyRequestIn: t.typedef = ...
    SetIamPolicyRequestOut: t.typedef = ...
    UpdateTopicRequestIn: t.typedef = ...
    UpdateTopicRequestOut: t.typedef = ...
    UpdateSnapshotRequestIn: t.typedef = ...
    UpdateSnapshotRequestOut: t.typedef = ...
    ReceivedMessageIn: t.typedef = ...
    ReceivedMessageOut: t.typedef = ...
    SchemaIn: t.typedef = ...
    SchemaOut: t.typedef = ...
    EmptyIn: t.typedef = ...
    EmptyOut: t.typedef = ...
    ValidateMessageRequestIn: t.typedef = ...
    ValidateMessageRequestOut: t.typedef = ...
    ValidateSchemaRequestIn: t.typedef = ...
    ValidateSchemaRequestOut: t.typedef = ...
    AcknowledgeRequestIn: t.typedef = ...
    AcknowledgeRequestOut: t.typedef = ...
    ListTopicsResponseIn: t.typedef = ...
    ListTopicsResponseOut: t.typedef = ...
    SubscriptionIn: t.typedef = ...
    SubscriptionOut: t.typedef = ...
    PublishResponseIn: t.typedef = ...
    PublishResponseOut: t.typedef = ...

class FuncList:
    projectsTopicsGetIamPolicy: t.func = ...
    projectsTopicsPublish: t.func = ...
    projectsTopicsCreate: t.func = ...
    projectsTopicsGet: t.func = ...
    projectsTopicsPatch: t.func = ...
    projectsTopicsSetIamPolicy: t.func = ...
    projectsTopicsList: t.func = ...
    projectsTopicsTestIamPermissions: t.func = ...
    projectsTopicsDelete: t.func = ...
    projectsTopicsSubscriptionsList: t.func = ...
    projectsTopicsSnapshotsList: t.func = ...
    projectsSubscriptionsAcknowledge: t.func = ...
    projectsSubscriptionsDelete: t.func = ...
    projectsSubscriptionsSetIamPolicy: t.func = ...
    projectsSubscriptionsPull: t.func = ...
    projectsSubscriptionsModifyPushConfig: t.func = ...
    projectsSubscriptionsGet: t.func = ...
    projectsSubscriptionsList: t.func = ...
    projectsSubscriptionsModifyAckDeadline: t.func = ...
    projectsSubscriptionsDetach: t.func = ...
    projectsSubscriptionsCreate: t.func = ...
    projectsSubscriptionsTestIamPermissions: t.func = ...
    projectsSubscriptionsGetIamPolicy: t.func = ...
    projectsSubscriptionsPatch: t.func = ...
    projectsSubscriptionsSeek: t.func = ...
    projectsSnapshotsSetIamPolicy: t.func = ...
    projectsSnapshotsList: t.func = ...
    projectsSnapshotsCreate: t.func = ...
    projectsSnapshotsGet: t.func = ...
    projectsSnapshotsDelete: t.func = ...
    projectsSnapshotsTestIamPermissions: t.func = ...
    projectsSnapshotsGetIamPolicy: t.func = ...
    projectsSnapshotsPatch: t.func = ...
    projectsSchemasGet: t.func = ...
    projectsSchemasTestIamPermissions: t.func = ...
    projectsSchemasRollback: t.func = ...
    projectsSchemasDelete: t.func = ...
    projectsSchemasCommit: t.func = ...
    projectsSchemasValidateMessage: t.func = ...
    projectsSchemasListRevisions: t.func = ...
    projectsSchemasSetIamPolicy: t.func = ...
    projectsSchemasDeleteRevision: t.func = ...
    projectsSchemasCreate: t.func = ...
    projectsSchemasGetIamPolicy: t.func = ...
    projectsSchemasValidate: t.func = ...
    projectsSchemasList: t.func = ...

class Import:
    types: TypeList = ...
    functions: FuncList = ...

def import_pubsub() -> Import: ...
