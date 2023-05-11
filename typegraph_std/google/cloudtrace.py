from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from typegraph import effects
from typegraph import TypeGraph


def import_cloudtrace() -> Import:
    cloudtrace = HTTPRuntime("https://cloudtrace.googleapis.com/")

    renames = {
        "ErrorResponse": "_cloudtrace_1_ErrorResponse",
        "AttributeValueIn": "_cloudtrace_2_AttributeValueIn",
        "AttributeValueOut": "_cloudtrace_3_AttributeValueOut",
        "ModuleIn": "_cloudtrace_4_ModuleIn",
        "ModuleOut": "_cloudtrace_5_ModuleOut",
        "TimeEventsIn": "_cloudtrace_6_TimeEventsIn",
        "TimeEventsOut": "_cloudtrace_7_TimeEventsOut",
        "BatchWriteSpansRequestIn": "_cloudtrace_8_BatchWriteSpansRequestIn",
        "BatchWriteSpansRequestOut": "_cloudtrace_9_BatchWriteSpansRequestOut",
        "TruncatableStringIn": "_cloudtrace_10_TruncatableStringIn",
        "TruncatableStringOut": "_cloudtrace_11_TruncatableStringOut",
        "StatusIn": "_cloudtrace_12_StatusIn",
        "StatusOut": "_cloudtrace_13_StatusOut",
        "MessageEventIn": "_cloudtrace_14_MessageEventIn",
        "MessageEventOut": "_cloudtrace_15_MessageEventOut",
        "SpanIn": "_cloudtrace_16_SpanIn",
        "SpanOut": "_cloudtrace_17_SpanOut",
        "StackTraceIn": "_cloudtrace_18_StackTraceIn",
        "StackTraceOut": "_cloudtrace_19_StackTraceOut",
        "TimeEventIn": "_cloudtrace_20_TimeEventIn",
        "TimeEventOut": "_cloudtrace_21_TimeEventOut",
        "AnnotationIn": "_cloudtrace_22_AnnotationIn",
        "AnnotationOut": "_cloudtrace_23_AnnotationOut",
        "EmptyIn": "_cloudtrace_24_EmptyIn",
        "EmptyOut": "_cloudtrace_25_EmptyOut",
        "StackFramesIn": "_cloudtrace_26_StackFramesIn",
        "StackFramesOut": "_cloudtrace_27_StackFramesOut",
        "LinksIn": "_cloudtrace_28_LinksIn",
        "LinksOut": "_cloudtrace_29_LinksOut",
        "LinkIn": "_cloudtrace_30_LinkIn",
        "LinkOut": "_cloudtrace_31_LinkOut",
        "AttributesIn": "_cloudtrace_32_AttributesIn",
        "AttributesOut": "_cloudtrace_33_AttributesOut",
        "StackFrameIn": "_cloudtrace_34_StackFrameIn",
        "StackFrameOut": "_cloudtrace_35_StackFrameOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["AttributeValueIn"] = t.struct(
        {
            "boolValue": t.boolean().optional(),
            "stringValue": t.proxy(renames["TruncatableStringIn"]).optional(),
            "intValue": t.string().optional(),
        }
    ).named(renames["AttributeValueIn"])
    types["AttributeValueOut"] = t.struct(
        {
            "boolValue": t.boolean().optional(),
            "stringValue": t.proxy(renames["TruncatableStringOut"]).optional(),
            "intValue": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AttributeValueOut"])
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
    types["TimeEventsIn"] = t.struct(
        {
            "droppedMessageEventsCount": t.integer().optional(),
            "timeEvent": t.array(t.proxy(renames["TimeEventIn"])).optional(),
            "droppedAnnotationsCount": t.integer().optional(),
        }
    ).named(renames["TimeEventsIn"])
    types["TimeEventsOut"] = t.struct(
        {
            "droppedMessageEventsCount": t.integer().optional(),
            "timeEvent": t.array(t.proxy(renames["TimeEventOut"])).optional(),
            "droppedAnnotationsCount": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TimeEventsOut"])
    types["BatchWriteSpansRequestIn"] = t.struct(
        {"spans": t.array(t.proxy(renames["SpanIn"]))}
    ).named(renames["BatchWriteSpansRequestIn"])
    types["BatchWriteSpansRequestOut"] = t.struct(
        {
            "spans": t.array(t.proxy(renames["SpanOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchWriteSpansRequestOut"])
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
    types["StatusIn"] = t.struct(
        {
            "code": t.integer().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "message": t.string().optional(),
        }
    ).named(renames["StatusIn"])
    types["StatusOut"] = t.struct(
        {
            "code": t.integer().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "message": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StatusOut"])
    types["MessageEventIn"] = t.struct(
        {
            "uncompressedSizeBytes": t.string().optional(),
            "id": t.string().optional(),
            "type": t.string().optional(),
            "compressedSizeBytes": t.string().optional(),
        }
    ).named(renames["MessageEventIn"])
    types["MessageEventOut"] = t.struct(
        {
            "uncompressedSizeBytes": t.string().optional(),
            "id": t.string().optional(),
            "type": t.string().optional(),
            "compressedSizeBytes": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MessageEventOut"])
    types["SpanIn"] = t.struct(
        {
            "spanKind": t.string().optional(),
            "links": t.proxy(renames["LinksIn"]).optional(),
            "stackTrace": t.proxy(renames["StackTraceIn"]).optional(),
            "startTime": t.string(),
            "endTime": t.string(),
            "timeEvents": t.proxy(renames["TimeEventsIn"]).optional(),
            "parentSpanId": t.string().optional(),
            "childSpanCount": t.integer().optional(),
            "sameProcessAsParentSpan": t.boolean().optional(),
            "name": t.string(),
            "displayName": t.proxy(renames["TruncatableStringIn"]),
            "attributes": t.proxy(renames["AttributesIn"]).optional(),
            "spanId": t.string(),
            "status": t.proxy(renames["StatusIn"]).optional(),
        }
    ).named(renames["SpanIn"])
    types["SpanOut"] = t.struct(
        {
            "spanKind": t.string().optional(),
            "links": t.proxy(renames["LinksOut"]).optional(),
            "stackTrace": t.proxy(renames["StackTraceOut"]).optional(),
            "startTime": t.string(),
            "endTime": t.string(),
            "timeEvents": t.proxy(renames["TimeEventsOut"]).optional(),
            "parentSpanId": t.string().optional(),
            "childSpanCount": t.integer().optional(),
            "sameProcessAsParentSpan": t.boolean().optional(),
            "name": t.string(),
            "displayName": t.proxy(renames["TruncatableStringOut"]),
            "attributes": t.proxy(renames["AttributesOut"]).optional(),
            "spanId": t.string(),
            "status": t.proxy(renames["StatusOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SpanOut"])
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
    types["AnnotationIn"] = t.struct(
        {
            "attributes": t.proxy(renames["AttributesIn"]).optional(),
            "description": t.proxy(renames["TruncatableStringIn"]).optional(),
        }
    ).named(renames["AnnotationIn"])
    types["AnnotationOut"] = t.struct(
        {
            "attributes": t.proxy(renames["AttributesOut"]).optional(),
            "description": t.proxy(renames["TruncatableStringOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AnnotationOut"])
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
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
    types["LinkIn"] = t.struct(
        {
            "traceId": t.string().optional(),
            "attributes": t.proxy(renames["AttributesIn"]).optional(),
            "spanId": t.string().optional(),
            "type": t.string().optional(),
        }
    ).named(renames["LinkIn"])
    types["LinkOut"] = t.struct(
        {
            "traceId": t.string().optional(),
            "attributes": t.proxy(renames["AttributesOut"]).optional(),
            "spanId": t.string().optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LinkOut"])
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
    types["StackFrameIn"] = t.struct(
        {
            "originalFunctionName": t.proxy(renames["TruncatableStringIn"]).optional(),
            "functionName": t.proxy(renames["TruncatableStringIn"]).optional(),
            "fileName": t.proxy(renames["TruncatableStringIn"]).optional(),
            "lineNumber": t.string().optional(),
            "columnNumber": t.string().optional(),
            "sourceVersion": t.proxy(renames["TruncatableStringIn"]).optional(),
            "loadModule": t.proxy(renames["ModuleIn"]).optional(),
        }
    ).named(renames["StackFrameIn"])
    types["StackFrameOut"] = t.struct(
        {
            "originalFunctionName": t.proxy(renames["TruncatableStringOut"]).optional(),
            "functionName": t.proxy(renames["TruncatableStringOut"]).optional(),
            "fileName": t.proxy(renames["TruncatableStringOut"]).optional(),
            "lineNumber": t.string().optional(),
            "columnNumber": t.string().optional(),
            "sourceVersion": t.proxy(renames["TruncatableStringOut"]).optional(),
            "loadModule": t.proxy(renames["ModuleOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StackFrameOut"])

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
                "spanKind": t.string().optional(),
                "links": t.proxy(renames["LinksIn"]).optional(),
                "stackTrace": t.proxy(renames["StackTraceIn"]).optional(),
                "startTime": t.string(),
                "endTime": t.string(),
                "timeEvents": t.proxy(renames["TimeEventsIn"]).optional(),
                "parentSpanId": t.string().optional(),
                "childSpanCount": t.integer().optional(),
                "sameProcessAsParentSpan": t.boolean().optional(),
                "displayName": t.proxy(renames["TruncatableStringIn"]),
                "attributes": t.proxy(renames["AttributesIn"]).optional(),
                "spanId": t.string(),
                "status": t.proxy(renames["StatusIn"]).optional(),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["SpanOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="cloudtrace", renames=renames, types=types, functions=functions
    )
