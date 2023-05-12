from typegraph import t

class TypeList:
    ErrorResponse: t.typedef = ...
    LighthouseCategoryV5In: t.typedef = ...
    LighthouseCategoryV5Out: t.typedef = ...
    TimingIn: t.typedef = ...
    TimingOut: t.typedef = ...
    PagespeedApiLoadingExperienceV5In: t.typedef = ...
    PagespeedApiLoadingExperienceV5Out: t.typedef = ...
    LighthouseAuditResultV5In: t.typedef = ...
    LighthouseAuditResultV5Out: t.typedef = ...
    PagespeedApiPagespeedResponseV5In: t.typedef = ...
    PagespeedApiPagespeedResponseV5Out: t.typedef = ...
    CategoriesIn: t.typedef = ...
    CategoriesOut: t.typedef = ...
    AuditRefsIn: t.typedef = ...
    AuditRefsOut: t.typedef = ...
    StackPackIn: t.typedef = ...
    StackPackOut: t.typedef = ...
    CategoryGroupV5In: t.typedef = ...
    CategoryGroupV5Out: t.typedef = ...
    ConfigSettingsIn: t.typedef = ...
    ConfigSettingsOut: t.typedef = ...
    PagespeedVersionIn: t.typedef = ...
    PagespeedVersionOut: t.typedef = ...
    RuntimeErrorIn: t.typedef = ...
    RuntimeErrorOut: t.typedef = ...
    I18nIn: t.typedef = ...
    I18nOut: t.typedef = ...
    BucketIn: t.typedef = ...
    BucketOut: t.typedef = ...
    EnvironmentIn: t.typedef = ...
    EnvironmentOut: t.typedef = ...
    LhrEntityIn: t.typedef = ...
    LhrEntityOut: t.typedef = ...
    RendererFormattedStringsIn: t.typedef = ...
    RendererFormattedStringsOut: t.typedef = ...
    LighthouseResultV5In: t.typedef = ...
    LighthouseResultV5Out: t.typedef = ...
    UserPageLoadMetricV5In: t.typedef = ...
    UserPageLoadMetricV5Out: t.typedef = ...

class FuncList:
    pagespeedapiRunpagespeed: t.func = ...

class Import:
    types: TypeList = ...
    functions: FuncList = ...

def import_pagespeedonline() -> Import: ...
