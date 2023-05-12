from typegraph.runtimes.http import HTTPRuntime
from typegraph.importers.base.importer import Import
from typegraph import t
from box import Box


def import_cloudtrace() -> Import:
    cloudtrace = HTTPRuntime("https://cloudtrace.googleapis.com/")

    renames = {
        "ErrorResponse": "_cloudtrace_1_ErrorResponse",
        "ModuleIn": "_cloudtrace_2_ModuleIn",
        "ModuleOut": "_cloudtrace_3_ModuleOut",
        "StackFramesIn": "_cloudtrace_4_StackFramesIn",
        "StackFramesOut": "_cloudtrace_5_StackFramesOut",
        "TimeEventsIn": "_cloudtrace_6_TimeEventsIn",
        "TimeEventsOut": "_cloudtrace_7_TimeEventsOut",
        "TimeEventIn": "_cloudtrace_8_TimeEventIn",
        "TimeEventOut": "_cloudtrace_9_TimeEventOut",
        "StackTraceIn": "_cloudtrace_10_StackTraceIn",
        "StackTraceOut": "_cloudtrace_11_StackTraceOut",
        "StackFrameIn": "_cloudtrace_12_StackFrameIn",
        "StackFrameOut": "_cloudtrace_13_StackFrameOut",
        "LinksIn": "_cloudtrace_14_LinksIn",
        "LinksOut": "_cloudtrace_15_LinksOut",
        "SpanIn": "_cloudtrace_16_SpanIn",
        "SpanOut": "_cloudtrace_17_SpanOut",
        "TruncatableStringIn": "_cloudtrace_18_TruncatableStringIn",
        "TruncatableStringOut": "_cloudtrace_19_TruncatableStringOut",
        "EmptyIn": "_cloudtrace_20_EmptyIn",
        "EmptyOut": "_cloudtrace_21_EmptyOut",
        "AttributesIn": "_cloudtrace_22_AttributesIn",
        "AttributesOut": "_cloudtrace_23_AttributesOut",
        "AttributeValueIn": "_cloudtrace_24_AttributeValueIn",
        "AttributeValueOut": "_cloudtrace_25_AttributeValueOut",
        "LinkIn": "_cloudtrace_26_LinkIn",
        "LinkOut": "_cloudtrace_27_LinkOut",
        "StatusIn": "_cloudtrace_28_StatusIn",
        "StatusOut": "_cloudtrace_29_StatusOut",
        "MessageEventIn": "_cloudtrace_30_MessageEventIn",
        "MessageEventOut": "_cloudtrace_31_MessageEventOut",
        "AnnotationIn": "_cloudtrace_32_AnnotationIn",
        "AnnotationOut": "_cloudtrace_33_AnnotationOut",
        "BatchWriteSpansRequestIn": "_cloudtrace_34_BatchWriteSpansRequestIn",
        "BatchWriteSpansRequestOut": "_cloudtrace_35_BatchWriteSpansRequestOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
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
    types["StackFramesIn"] = t.struct(
        {
            "frame": t.array(t.proxy(renames["StackFrameIn"])).optional(),
            "droppedFramesCount": t.integer().optional(),
        }
    ).named(renames["StackFramesIn"])
    types["StackFramesOut"] = t.struct(
        {
            "frame": t.array(t.proxy(renames["StackFrameOut"])).optional(),
            "droppedFramesCount": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StackFramesOut"])
    types["TimeEventsIn"] = t.struct(
        {
            "droppedAnnotationsCount": t.integer().optional(),
            "droppedMessageEventsCount": t.integer().optional(),
            "timeEvent": t.array(t.proxy(renames["TimeEventIn"])).optional(),
        }
    ).named(renames["TimeEventsIn"])
    types["TimeEventsOut"] = t.struct(
        {
            "droppedAnnotationsCount": t.integer().optional(),
            "droppedMessageEventsCount": t.integer().optional(),
            "timeEvent": t.array(t.proxy(renames["TimeEventOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TimeEventsOut"])
    types["TimeEventIn"] = t.struct(
        {
            "time": t.string().optional(),
            "annotation": t.proxy(renames["AnnotationIn"]).optional(),
            "messageEvent": t.proxy(renames["MessageEventIn"]).optional(),
        }
    ).named(renames["TimeEventIn"])
    types["TimeEventOut"] = t.struct(
        {
            "time": t.string().optional(),
            "annotation": t.proxy(renames["AnnotationOut"]).optional(),
            "messageEvent": t.proxy(renames["MessageEventOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TimeEventOut"])
    types["StackTraceIn"] = t.struct(
        {
            "stackTraceHashId": t.string().optional(),
            "stackFrames": t.proxy(renames["StackFramesIn"]).optional(),
        }
    ).named(renames["StackTraceIn"])
    types["StackTraceOut"] = t.struct(
        {
            "stackTraceHashId": t.string().optional(),
            "stackFrames": t.proxy(renames["StackFramesOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StackTraceOut"])
    types["StackFrameIn"] = t.struct(
        {
            "sourceVersion": t.proxy(renames["TruncatableStringIn"]).optional(),
            "loadModule": t.proxy(renames["ModuleIn"]).optional(),
            "functionName": t.proxy(renames["TruncatableStringIn"]).optional(),
            "lineNumber": t.string().optional(),
            "columnNumber": t.string().optional(),
            "originalFunctionName": t.proxy(renames["TruncatableStringIn"]).optional(),
            "fileName": t.proxy(renames["TruncatableStringIn"]).optional(),
        }
    ).named(renames["StackFrameIn"])
    types["StackFrameOut"] = t.struct(
        {
            "sourceVersion": t.proxy(renames["TruncatableStringOut"]).optional(),
            "loadModule": t.proxy(renames["ModuleOut"]).optional(),
            "functionName": t.proxy(renames["TruncatableStringOut"]).optional(),
            "lineNumber": t.string().optional(),
            "columnNumber": t.string().optional(),
            "originalFunctionName": t.proxy(renames["TruncatableStringOut"]).optional(),
            "fileName": t.proxy(renames["TruncatableStringOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StackFrameOut"])
    types["LinksIn"] = t.struct(
        {
            "link": t.array(t.proxy(renames["LinkIn"])).optional(),
            "droppedLinksCount": t.integer().optional(),
        }
    ).named(renames["LinksIn"])
    types["LinksOut"] = t.struct(
        {
            "link": t.array(t.proxy(renames["LinkOut"])).optional(),
            "droppedLinksCount": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LinksOut"])
    types["SpanIn"] = t.struct(
        {
            "attributes": t.proxy(renames["AttributesIn"]).optional(),
            "links": t.proxy(renames["LinksIn"]).optional(),
            "status": t.proxy(renames["StatusIn"]).optional(),
            "endTime": t.string(),
            "spanId": t.string(),
            "parentSpanId": t.string().optional(),
            "displayName": t.proxy(renames["TruncatableStringIn"]),
            "childSpanCount": t.integer().optional(),
            "startTime": t.string(),
            "sameProcessAsParentSpan": t.boolean().optional(),
            "stackTrace": t.proxy(renames["StackTraceIn"]).optional(),
            "timeEvents": t.proxy(renames["TimeEventsIn"]).optional(),
            "name": t.string(),
            "spanKind": t.string().optional(),
        }
    ).named(renames["SpanIn"])
    types["SpanOut"] = t.struct(
        {
            "attributes": t.proxy(renames["AttributesOut"]).optional(),
            "links": t.proxy(renames["LinksOut"]).optional(),
            "status": t.proxy(renames["StatusOut"]).optional(),
            "endTime": t.string(),
            "spanId": t.string(),
            "parentSpanId": t.string().optional(),
            "displayName": t.proxy(renames["TruncatableStringOut"]),
            "childSpanCount": t.integer().optional(),
            "startTime": t.string(),
            "sameProcessAsParentSpan": t.boolean().optional(),
            "stackTrace": t.proxy(renames["StackTraceOut"]).optional(),
            "timeEvents": t.proxy(renames["TimeEventsOut"]).optional(),
            "name": t.string(),
            "spanKind": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SpanOut"])
    types["TruncatableStringIn"] = t.struct(
        {"truncatedByteCount": t.integer().optional(), "value": t.string().optional()}
    ).named(renames["TruncatableStringIn"])
    types["TruncatableStringOut"] = t.struct(
        {
            "truncatedByteCount": t.integer().optional(),
            "value": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TruncatableStringOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
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
    types["AttributeValueIn"] = t.struct(
        {
            "intValue": t.string().optional(),
            "boolValue": t.boolean().optional(),
            "stringValue": t.proxy(renames["TruncatableStringIn"]).optional(),
        }
    ).named(renames["AttributeValueIn"])
    types["AttributeValueOut"] = t.struct(
        {
            "intValue": t.string().optional(),
            "boolValue": t.boolean().optional(),
            "stringValue": t.proxy(renames["TruncatableStringOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AttributeValueOut"])
    types["LinkIn"] = t.struct(
        {
            "spanId": t.string().optional(),
            "traceId": t.string().optional(),
            "attributes": t.proxy(renames["AttributesIn"]).optional(),
            "type": t.string().optional(),
        }
    ).named(renames["LinkIn"])
    types["LinkOut"] = t.struct(
        {
            "spanId": t.string().optional(),
            "traceId": t.string().optional(),
            "attributes": t.proxy(renames["AttributesOut"]).optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LinkOut"])
    types["StatusIn"] = t.struct(
        {
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "code": t.integer().optional(),
            "message": t.string().optional(),
        }
    ).named(renames["StatusIn"])
    types["StatusOut"] = t.struct(
        {
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "code": t.integer().optional(),
            "message": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StatusOut"])
    types["MessageEventIn"] = t.struct(
        {
            "uncompressedSizeBytes": t.string().optional(),
            "compressedSizeBytes": t.string().optional(),
            "id": t.string().optional(),
            "type": t.string().optional(),
        }
    ).named(renames["MessageEventIn"])
    types["MessageEventOut"] = t.struct(
        {
            "uncompressedSizeBytes": t.string().optional(),
            "compressedSizeBytes": t.string().optional(),
            "id": t.string().optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MessageEventOut"])
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
    types["BatchWriteSpansRequestIn"] = t.struct(
        {"spans": t.array(t.proxy(renames["SpanIn"]))}
    ).named(renames["BatchWriteSpansRequestIn"])
    types["BatchWriteSpansRequestOut"] = t.struct(
        {
            "spans": t.array(t.proxy(renames["SpanOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchWriteSpansRequestOut"])

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
                "attributes": t.proxy(renames["AttributesIn"]).optional(),
                "links": t.proxy(renames["LinksIn"]).optional(),
                "status": t.proxy(renames["StatusIn"]).optional(),
                "endTime": t.string(),
                "spanId": t.string(),
                "parentSpanId": t.string().optional(),
                "displayName": t.proxy(renames["TruncatableStringIn"]),
                "childSpanCount": t.integer().optional(),
                "startTime": t.string(),
                "sameProcessAsParentSpan": t.boolean().optional(),
                "stackTrace": t.proxy(renames["StackTraceIn"]).optional(),
                "timeEvents": t.proxy(renames["TimeEventsIn"]).optional(),
                "spanKind": t.string().optional(),
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
