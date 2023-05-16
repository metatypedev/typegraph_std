from typegraph import t
from box import Box
from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime


def import_cloudtrace() -> Import:
    cloudtrace = HTTPRuntime("https://cloudtrace.googleapis.com/")

    renames = {
        "ErrorResponse": "_cloudtrace_1_ErrorResponse",
        "StackFrameIn": "_cloudtrace_2_StackFrameIn",
        "StackFrameOut": "_cloudtrace_3_StackFrameOut",
        "TruncatableStringIn": "_cloudtrace_4_TruncatableStringIn",
        "TruncatableStringOut": "_cloudtrace_5_TruncatableStringOut",
        "MessageEventIn": "_cloudtrace_6_MessageEventIn",
        "MessageEventOut": "_cloudtrace_7_MessageEventOut",
        "StackFramesIn": "_cloudtrace_8_StackFramesIn",
        "StackFramesOut": "_cloudtrace_9_StackFramesOut",
        "BatchWriteSpansRequestIn": "_cloudtrace_10_BatchWriteSpansRequestIn",
        "BatchWriteSpansRequestOut": "_cloudtrace_11_BatchWriteSpansRequestOut",
        "TimeEventIn": "_cloudtrace_12_TimeEventIn",
        "TimeEventOut": "_cloudtrace_13_TimeEventOut",
        "EmptyIn": "_cloudtrace_14_EmptyIn",
        "EmptyOut": "_cloudtrace_15_EmptyOut",
        "LinkIn": "_cloudtrace_16_LinkIn",
        "LinkOut": "_cloudtrace_17_LinkOut",
        "TimeEventsIn": "_cloudtrace_18_TimeEventsIn",
        "TimeEventsOut": "_cloudtrace_19_TimeEventsOut",
        "SpanIn": "_cloudtrace_20_SpanIn",
        "SpanOut": "_cloudtrace_21_SpanOut",
        "AttributeValueIn": "_cloudtrace_22_AttributeValueIn",
        "AttributeValueOut": "_cloudtrace_23_AttributeValueOut",
        "LinksIn": "_cloudtrace_24_LinksIn",
        "LinksOut": "_cloudtrace_25_LinksOut",
        "StackTraceIn": "_cloudtrace_26_StackTraceIn",
        "StackTraceOut": "_cloudtrace_27_StackTraceOut",
        "AnnotationIn": "_cloudtrace_28_AnnotationIn",
        "AnnotationOut": "_cloudtrace_29_AnnotationOut",
        "StatusIn": "_cloudtrace_30_StatusIn",
        "StatusOut": "_cloudtrace_31_StatusOut",
        "AttributesIn": "_cloudtrace_32_AttributesIn",
        "AttributesOut": "_cloudtrace_33_AttributesOut",
        "ModuleIn": "_cloudtrace_34_ModuleIn",
        "ModuleOut": "_cloudtrace_35_ModuleOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["StackFrameIn"] = t.struct(
        {
            "loadModule": t.proxy(renames["ModuleIn"]).optional(),
            "columnNumber": t.string().optional(),
            "lineNumber": t.string().optional(),
            "originalFunctionName": t.proxy(renames["TruncatableStringIn"]).optional(),
            "sourceVersion": t.proxy(renames["TruncatableStringIn"]).optional(),
            "fileName": t.proxy(renames["TruncatableStringIn"]).optional(),
            "functionName": t.proxy(renames["TruncatableStringIn"]).optional(),
        }
    ).named(renames["StackFrameIn"])
    types["StackFrameOut"] = t.struct(
        {
            "loadModule": t.proxy(renames["ModuleOut"]).optional(),
            "columnNumber": t.string().optional(),
            "lineNumber": t.string().optional(),
            "originalFunctionName": t.proxy(renames["TruncatableStringOut"]).optional(),
            "sourceVersion": t.proxy(renames["TruncatableStringOut"]).optional(),
            "fileName": t.proxy(renames["TruncatableStringOut"]).optional(),
            "functionName": t.proxy(renames["TruncatableStringOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StackFrameOut"])
    types["TruncatableStringIn"] = t.struct(
        {"value": t.string().optional(), "truncatedByteCount": t.integer().optional()}
    ).named(renames["TruncatableStringIn"])
    types["TruncatableStringOut"] = t.struct(
        {
            "value": t.string().optional(),
            "truncatedByteCount": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TruncatableStringOut"])
    types["MessageEventIn"] = t.struct(
        {
            "uncompressedSizeBytes": t.string().optional(),
            "id": t.string().optional(),
            "compressedSizeBytes": t.string().optional(),
            "type": t.string().optional(),
        }
    ).named(renames["MessageEventIn"])
    types["MessageEventOut"] = t.struct(
        {
            "uncompressedSizeBytes": t.string().optional(),
            "id": t.string().optional(),
            "compressedSizeBytes": t.string().optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MessageEventOut"])
    types["StackFramesIn"] = t.struct(
        {
            "droppedFramesCount": t.integer().optional(),
            "frame": t.array(t.proxy(renames["StackFrameIn"])).optional(),
        }
    ).named(renames["StackFramesIn"])
    types["StackFramesOut"] = t.struct(
        {
            "droppedFramesCount": t.integer().optional(),
            "frame": t.array(t.proxy(renames["StackFrameOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StackFramesOut"])
    types["BatchWriteSpansRequestIn"] = t.struct(
        {"spans": t.array(t.proxy(renames["SpanIn"]))}
    ).named(renames["BatchWriteSpansRequestIn"])
    types["BatchWriteSpansRequestOut"] = t.struct(
        {
            "spans": t.array(t.proxy(renames["SpanOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchWriteSpansRequestOut"])
    types["TimeEventIn"] = t.struct(
        {
            "time": t.string().optional(),
            "messageEvent": t.proxy(renames["MessageEventIn"]).optional(),
            "annotation": t.proxy(renames["AnnotationIn"]).optional(),
        }
    ).named(renames["TimeEventIn"])
    types["TimeEventOut"] = t.struct(
        {
            "time": t.string().optional(),
            "messageEvent": t.proxy(renames["MessageEventOut"]).optional(),
            "annotation": t.proxy(renames["AnnotationOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TimeEventOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["LinkIn"] = t.struct(
        {
            "type": t.string().optional(),
            "attributes": t.proxy(renames["AttributesIn"]).optional(),
            "spanId": t.string().optional(),
            "traceId": t.string().optional(),
        }
    ).named(renames["LinkIn"])
    types["LinkOut"] = t.struct(
        {
            "type": t.string().optional(),
            "attributes": t.proxy(renames["AttributesOut"]).optional(),
            "spanId": t.string().optional(),
            "traceId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LinkOut"])
    types["TimeEventsIn"] = t.struct(
        {
            "droppedMessageEventsCount": t.integer().optional(),
            "droppedAnnotationsCount": t.integer().optional(),
            "timeEvent": t.array(t.proxy(renames["TimeEventIn"])).optional(),
        }
    ).named(renames["TimeEventsIn"])
    types["TimeEventsOut"] = t.struct(
        {
            "droppedMessageEventsCount": t.integer().optional(),
            "droppedAnnotationsCount": t.integer().optional(),
            "timeEvent": t.array(t.proxy(renames["TimeEventOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TimeEventsOut"])
    types["SpanIn"] = t.struct(
        {
            "sameProcessAsParentSpan": t.boolean().optional(),
            "displayName": t.proxy(renames["TruncatableStringIn"]),
            "childSpanCount": t.integer().optional(),
            "timeEvents": t.proxy(renames["TimeEventsIn"]).optional(),
            "attributes": t.proxy(renames["AttributesIn"]).optional(),
            "spanKind": t.string().optional(),
            "startTime": t.string(),
            "status": t.proxy(renames["StatusIn"]).optional(),
            "spanId": t.string(),
            "stackTrace": t.proxy(renames["StackTraceIn"]).optional(),
            "links": t.proxy(renames["LinksIn"]).optional(),
            "name": t.string(),
            "parentSpanId": t.string().optional(),
            "endTime": t.string(),
        }
    ).named(renames["SpanIn"])
    types["SpanOut"] = t.struct(
        {
            "sameProcessAsParentSpan": t.boolean().optional(),
            "displayName": t.proxy(renames["TruncatableStringOut"]),
            "childSpanCount": t.integer().optional(),
            "timeEvents": t.proxy(renames["TimeEventsOut"]).optional(),
            "attributes": t.proxy(renames["AttributesOut"]).optional(),
            "spanKind": t.string().optional(),
            "startTime": t.string(),
            "status": t.proxy(renames["StatusOut"]).optional(),
            "spanId": t.string(),
            "stackTrace": t.proxy(renames["StackTraceOut"]).optional(),
            "links": t.proxy(renames["LinksOut"]).optional(),
            "name": t.string(),
            "parentSpanId": t.string().optional(),
            "endTime": t.string(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SpanOut"])
    types["AttributeValueIn"] = t.struct(
        {
            "boolValue": t.boolean().optional(),
            "intValue": t.string().optional(),
            "stringValue": t.proxy(renames["TruncatableStringIn"]).optional(),
        }
    ).named(renames["AttributeValueIn"])
    types["AttributeValueOut"] = t.struct(
        {
            "boolValue": t.boolean().optional(),
            "intValue": t.string().optional(),
            "stringValue": t.proxy(renames["TruncatableStringOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AttributeValueOut"])
    types["LinksIn"] = t.struct(
        {
            "droppedLinksCount": t.integer().optional(),
            "link": t.array(t.proxy(renames["LinkIn"])).optional(),
        }
    ).named(renames["LinksIn"])
    types["LinksOut"] = t.struct(
        {
            "droppedLinksCount": t.integer().optional(),
            "link": t.array(t.proxy(renames["LinkOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LinksOut"])
    types["StackTraceIn"] = t.struct(
        {
            "stackFrames": t.proxy(renames["StackFramesIn"]).optional(),
            "stackTraceHashId": t.string().optional(),
        }
    ).named(renames["StackTraceIn"])
    types["StackTraceOut"] = t.struct(
        {
            "stackFrames": t.proxy(renames["StackFramesOut"]).optional(),
            "stackTraceHashId": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StackTraceOut"])
    types["AnnotationIn"] = t.struct(
        {
            "description": t.proxy(renames["TruncatableStringIn"]).optional(),
            "attributes": t.proxy(renames["AttributesIn"]).optional(),
        }
    ).named(renames["AnnotationIn"])
    types["AnnotationOut"] = t.struct(
        {
            "description": t.proxy(renames["TruncatableStringOut"]).optional(),
            "attributes": t.proxy(renames["AttributesOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AnnotationOut"])
    types["StatusIn"] = t.struct(
        {
            "message": t.string().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "code": t.integer().optional(),
        }
    ).named(renames["StatusIn"])
    types["StatusOut"] = t.struct(
        {
            "message": t.string().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "code": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StatusOut"])
    types["AttributesIn"] = t.struct(
        {
            "droppedAttributesCount": t.integer().optional(),
            "attributeMap": t.struct({"_": t.string().optional()}).optional(),
        }
    ).named(renames["AttributesIn"])
    types["AttributesOut"] = t.struct(
        {
            "droppedAttributesCount": t.integer().optional(),
            "attributeMap": t.struct({"_": t.string().optional()}).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AttributesOut"])
    types["ModuleIn"] = t.struct(
        {
            "module": t.proxy(renames["TruncatableStringIn"]).optional(),
            "buildId": t.proxy(renames["TruncatableStringIn"]).optional(),
        }
    ).named(renames["ModuleIn"])
    types["ModuleOut"] = t.struct(
        {
            "module": t.proxy(renames["TruncatableStringOut"]).optional(),
            "buildId": t.proxy(renames["TruncatableStringOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ModuleOut"])

    functions = {}
    functions["projectsTracesBatchWrite"] = cloudtrace.post(
        "v2/{name}/traces:batchWrite",
        t.struct(
            {
                "name": t.string(),
                "spans": t.array(t.proxy(renames["SpanIn"])),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["EmptyOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["projectsTracesSpansCreateSpan"] = cloudtrace.post(
        "v2/{name}",
        t.struct(
            {
                "name": t.string(),
                "sameProcessAsParentSpan": t.boolean().optional(),
                "displayName": t.proxy(renames["TruncatableStringIn"]),
                "childSpanCount": t.integer().optional(),
                "timeEvents": t.proxy(renames["TimeEventsIn"]).optional(),
                "attributes": t.proxy(renames["AttributesIn"]).optional(),
                "spanKind": t.string().optional(),
                "startTime": t.string(),
                "status": t.proxy(renames["StatusIn"]).optional(),
                "spanId": t.string(),
                "stackTrace": t.proxy(renames["StackTraceIn"]).optional(),
                "links": t.proxy(renames["LinksIn"]).optional(),
                "parentSpanId": t.string().optional(),
                "endTime": t.string(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SpanOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="cloudtrace",
        renames=renames,
        types=Box(types),
        functions=Box(functions),
    )
