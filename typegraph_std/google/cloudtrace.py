from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime
from typegraph import t
from box import Box


def import_cloudtrace():
    cloudtrace = HTTPRuntime("https://cloudtrace.googleapis.com/")

    renames = {
        "ErrorResponse": "_cloudtrace_1_ErrorResponse",
        "BatchWriteSpansRequestIn": "_cloudtrace_2_BatchWriteSpansRequestIn",
        "BatchWriteSpansRequestOut": "_cloudtrace_3_BatchWriteSpansRequestOut",
        "AttributesIn": "_cloudtrace_4_AttributesIn",
        "AttributesOut": "_cloudtrace_5_AttributesOut",
        "TruncatableStringIn": "_cloudtrace_6_TruncatableStringIn",
        "TruncatableStringOut": "_cloudtrace_7_TruncatableStringOut",
        "LinkIn": "_cloudtrace_8_LinkIn",
        "LinkOut": "_cloudtrace_9_LinkOut",
        "TimeEventsIn": "_cloudtrace_10_TimeEventsIn",
        "TimeEventsOut": "_cloudtrace_11_TimeEventsOut",
        "TimeEventIn": "_cloudtrace_12_TimeEventIn",
        "TimeEventOut": "_cloudtrace_13_TimeEventOut",
        "MessageEventIn": "_cloudtrace_14_MessageEventIn",
        "MessageEventOut": "_cloudtrace_15_MessageEventOut",
        "StackFrameIn": "_cloudtrace_16_StackFrameIn",
        "StackFrameOut": "_cloudtrace_17_StackFrameOut",
        "AnnotationIn": "_cloudtrace_18_AnnotationIn",
        "AnnotationOut": "_cloudtrace_19_AnnotationOut",
        "StackFramesIn": "_cloudtrace_20_StackFramesIn",
        "StackFramesOut": "_cloudtrace_21_StackFramesOut",
        "AttributeValueIn": "_cloudtrace_22_AttributeValueIn",
        "AttributeValueOut": "_cloudtrace_23_AttributeValueOut",
        "LinksIn": "_cloudtrace_24_LinksIn",
        "LinksOut": "_cloudtrace_25_LinksOut",
        "EmptyIn": "_cloudtrace_26_EmptyIn",
        "EmptyOut": "_cloudtrace_27_EmptyOut",
        "ModuleIn": "_cloudtrace_28_ModuleIn",
        "ModuleOut": "_cloudtrace_29_ModuleOut",
        "SpanIn": "_cloudtrace_30_SpanIn",
        "SpanOut": "_cloudtrace_31_SpanOut",
        "StackTraceIn": "_cloudtrace_32_StackTraceIn",
        "StackTraceOut": "_cloudtrace_33_StackTraceOut",
        "StatusIn": "_cloudtrace_34_StatusIn",
        "StatusOut": "_cloudtrace_35_StatusOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["BatchWriteSpansRequestIn"] = t.struct(
        {"spans": t.array(t.proxy(renames["SpanIn"]))}
    ).named(renames["BatchWriteSpansRequestIn"])
    types["BatchWriteSpansRequestOut"] = t.struct(
        {
            "spans": t.array(t.proxy(renames["SpanOut"])),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["BatchWriteSpansRequestOut"])
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
    types["LinkIn"] = t.struct(
        {
            "attributes": t.proxy(renames["AttributesIn"]).optional(),
            "spanId": t.string().optional(),
            "traceId": t.string().optional(),
            "type": t.string().optional(),
        }
    ).named(renames["LinkIn"])
    types["LinkOut"] = t.struct(
        {
            "attributes": t.proxy(renames["AttributesOut"]).optional(),
            "spanId": t.string().optional(),
            "traceId": t.string().optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["LinkOut"])
    types["TimeEventsIn"] = t.struct(
        {
            "timeEvent": t.array(t.proxy(renames["TimeEventIn"])).optional(),
            "droppedMessageEventsCount": t.integer().optional(),
            "droppedAnnotationsCount": t.integer().optional(),
        }
    ).named(renames["TimeEventsIn"])
    types["TimeEventsOut"] = t.struct(
        {
            "timeEvent": t.array(t.proxy(renames["TimeEventOut"])).optional(),
            "droppedMessageEventsCount": t.integer().optional(),
            "droppedAnnotationsCount": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TimeEventsOut"])
    types["TimeEventIn"] = t.struct(
        {
            "messageEvent": t.proxy(renames["MessageEventIn"]).optional(),
            "time": t.string().optional(),
            "annotation": t.proxy(renames["AnnotationIn"]).optional(),
        }
    ).named(renames["TimeEventIn"])
    types["TimeEventOut"] = t.struct(
        {
            "messageEvent": t.proxy(renames["MessageEventOut"]).optional(),
            "time": t.string().optional(),
            "annotation": t.proxy(renames["AnnotationOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TimeEventOut"])
    types["MessageEventIn"] = t.struct(
        {
            "id": t.string().optional(),
            "uncompressedSizeBytes": t.string().optional(),
            "compressedSizeBytes": t.string().optional(),
            "type": t.string().optional(),
        }
    ).named(renames["MessageEventIn"])
    types["MessageEventOut"] = t.struct(
        {
            "id": t.string().optional(),
            "uncompressedSizeBytes": t.string().optional(),
            "compressedSizeBytes": t.string().optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["MessageEventOut"])
    types["StackFrameIn"] = t.struct(
        {
            "loadModule": t.proxy(renames["ModuleIn"]).optional(),
            "fileName": t.proxy(renames["TruncatableStringIn"]).optional(),
            "lineNumber": t.string().optional(),
            "functionName": t.proxy(renames["TruncatableStringIn"]).optional(),
            "originalFunctionName": t.proxy(renames["TruncatableStringIn"]).optional(),
            "sourceVersion": t.proxy(renames["TruncatableStringIn"]).optional(),
            "columnNumber": t.string().optional(),
        }
    ).named(renames["StackFrameIn"])
    types["StackFrameOut"] = t.struct(
        {
            "loadModule": t.proxy(renames["ModuleOut"]).optional(),
            "fileName": t.proxy(renames["TruncatableStringOut"]).optional(),
            "lineNumber": t.string().optional(),
            "functionName": t.proxy(renames["TruncatableStringOut"]).optional(),
            "originalFunctionName": t.proxy(renames["TruncatableStringOut"]).optional(),
            "sourceVersion": t.proxy(renames["TruncatableStringOut"]).optional(),
            "columnNumber": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StackFrameOut"])
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
    types["EmptyIn"] = t.struct({"_": t.string().optional()}).named(renames["EmptyIn"])
    types["EmptyOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["EmptyOut"])
    types["ModuleIn"] = t.struct(
        {
            "buildId": t.proxy(renames["TruncatableStringIn"]).optional(),
            "module": t.proxy(renames["TruncatableStringIn"]).optional(),
        }
    ).named(renames["ModuleIn"])
    types["ModuleOut"] = t.struct(
        {
            "buildId": t.proxy(renames["TruncatableStringOut"]).optional(),
            "module": t.proxy(renames["TruncatableStringOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ModuleOut"])
    types["SpanIn"] = t.struct(
        {
            "displayName": t.proxy(renames["TruncatableStringIn"]),
            "status": t.proxy(renames["StatusIn"]).optional(),
            "timeEvents": t.proxy(renames["TimeEventsIn"]).optional(),
            "name": t.string(),
            "attributes": t.proxy(renames["AttributesIn"]).optional(),
            "spanId": t.string(),
            "endTime": t.string(),
            "stackTrace": t.proxy(renames["StackTraceIn"]).optional(),
            "sameProcessAsParentSpan": t.boolean().optional(),
            "startTime": t.string(),
            "spanKind": t.string().optional(),
            "links": t.proxy(renames["LinksIn"]).optional(),
            "parentSpanId": t.string().optional(),
            "childSpanCount": t.integer().optional(),
        }
    ).named(renames["SpanIn"])
    types["SpanOut"] = t.struct(
        {
            "displayName": t.proxy(renames["TruncatableStringOut"]),
            "status": t.proxy(renames["StatusOut"]).optional(),
            "timeEvents": t.proxy(renames["TimeEventsOut"]).optional(),
            "name": t.string(),
            "attributes": t.proxy(renames["AttributesOut"]).optional(),
            "spanId": t.string(),
            "endTime": t.string(),
            "stackTrace": t.proxy(renames["StackTraceOut"]).optional(),
            "sameProcessAsParentSpan": t.boolean().optional(),
            "startTime": t.string(),
            "spanKind": t.string().optional(),
            "links": t.proxy(renames["LinksOut"]).optional(),
            "parentSpanId": t.string().optional(),
            "childSpanCount": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SpanOut"])
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
    types["StatusIn"] = t.struct(
        {
            "message": t.string().optional(),
            "code": t.integer().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
        }
    ).named(renames["StatusIn"])
    types["StatusOut"] = t.struct(
        {
            "message": t.string().optional(),
            "code": t.integer().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StatusOut"])

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
                "displayName": t.proxy(renames["TruncatableStringIn"]),
                "status": t.proxy(renames["StatusIn"]).optional(),
                "timeEvents": t.proxy(renames["TimeEventsIn"]).optional(),
                "attributes": t.proxy(renames["AttributesIn"]).optional(),
                "spanId": t.string(),
                "endTime": t.string(),
                "stackTrace": t.proxy(renames["StackTraceIn"]).optional(),
                "sameProcessAsParentSpan": t.boolean().optional(),
                "startTime": t.string(),
                "spanKind": t.string().optional(),
                "links": t.proxy(renames["LinksIn"]).optional(),
                "parentSpanId": t.string().optional(),
                "childSpanCount": t.integer().optional(),
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
