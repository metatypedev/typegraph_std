from typegraph import t

class TypeList:
    ErrorResponse: t.typedef = ...
    EmptyIn: t.typedef = ...
    EmptyOut: t.typedef = ...
    ListBucketsResponseIn: t.typedef = ...
    ListBucketsResponseOut: t.typedef = ...
    GoogleFirebaseStorageControlplaneV1alphaMigrateLocationDestructivelyMetadataIn: t.typedef = (
        ...
    )
    GoogleFirebaseStorageControlplaneV1alphaMigrateLocationDestructivelyMetadataOut: t.typedef = (
        ...
    )
    GoogleFirebaseStorageControlplaneV1betaMigrateLocationDestructivelyMetadataIn: t.typedef = (
        ...
    )
    GoogleFirebaseStorageControlplaneV1betaMigrateLocationDestructivelyMetadataOut: t.typedef = (
        ...
    )
    RemoveFirebaseRequestIn: t.typedef = ...
    RemoveFirebaseRequestOut: t.typedef = ...
    BucketIn: t.typedef = ...
    BucketOut: t.typedef = ...
    AddFirebaseRequestIn: t.typedef = ...
    AddFirebaseRequestOut: t.typedef = ...

class FuncList:
    projectsBucketsAddFirebase: t.func = ...
    projectsBucketsRemoveFirebase: t.func = ...
    projectsBucketsGet: t.func = ...
    projectsBucketsList: t.func = ...

class Import:
    types: TypeList = ...
    functions: FuncList = ...

def import_firebasestorage() -> Import: ...
