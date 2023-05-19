from typegraph import t
from box import Box
from typegraph.importers.base.importer import Import
from typegraph.runtimes.http import HTTPRuntime


def import_language() -> Import:
    language = HTTPRuntime("https://language.googleapis.com/")

    renames = {
        "ErrorResponse": "_language_1_ErrorResponse",
        "PartOfSpeechIn": "_language_2_PartOfSpeechIn",
        "PartOfSpeechOut": "_language_3_PartOfSpeechOut",
        "AnalyzeSentimentRequestIn": "_language_4_AnalyzeSentimentRequestIn",
        "AnalyzeSentimentRequestOut": "_language_5_AnalyzeSentimentRequestOut",
        "AnnotateTextResponseIn": "_language_6_AnnotateTextResponseIn",
        "AnnotateTextResponseOut": "_language_7_AnnotateTextResponseOut",
        "FeaturesIn": "_language_8_FeaturesIn",
        "FeaturesOut": "_language_9_FeaturesOut",
        "AnalyzeSyntaxResponseIn": "_language_10_AnalyzeSyntaxResponseIn",
        "AnalyzeSyntaxResponseOut": "_language_11_AnalyzeSyntaxResponseOut",
        "AnalyzeEntitySentimentResponseIn": "_language_12_AnalyzeEntitySentimentResponseIn",
        "AnalyzeEntitySentimentResponseOut": "_language_13_AnalyzeEntitySentimentResponseOut",
        "AnnotateTextRequestIn": "_language_14_AnnotateTextRequestIn",
        "AnnotateTextRequestOut": "_language_15_AnnotateTextRequestOut",
        "SentimentIn": "_language_16_SentimentIn",
        "SentimentOut": "_language_17_SentimentOut",
        "DocumentIn": "_language_18_DocumentIn",
        "DocumentOut": "_language_19_DocumentOut",
        "StatusIn": "_language_20_StatusIn",
        "StatusOut": "_language_21_StatusOut",
        "AnalyzeEntitiesResponseIn": "_language_22_AnalyzeEntitiesResponseIn",
        "AnalyzeEntitiesResponseOut": "_language_23_AnalyzeEntitiesResponseOut",
        "AnalyzeEntitiesRequestIn": "_language_24_AnalyzeEntitiesRequestIn",
        "AnalyzeEntitiesRequestOut": "_language_25_AnalyzeEntitiesRequestOut",
        "V1ModelIn": "_language_26_V1ModelIn",
        "V1ModelOut": "_language_27_V1ModelOut",
        "TokenIn": "_language_28_TokenIn",
        "TokenOut": "_language_29_TokenOut",
        "TextSpanIn": "_language_30_TextSpanIn",
        "TextSpanOut": "_language_31_TextSpanOut",
        "DependencyEdgeIn": "_language_32_DependencyEdgeIn",
        "DependencyEdgeOut": "_language_33_DependencyEdgeOut",
        "ClassifyTextRequestIn": "_language_34_ClassifyTextRequestIn",
        "ClassifyTextRequestOut": "_language_35_ClassifyTextRequestOut",
        "V2ModelIn": "_language_36_V2ModelIn",
        "V2ModelOut": "_language_37_V2ModelOut",
        "AnalyzeSyntaxRequestIn": "_language_38_AnalyzeSyntaxRequestIn",
        "AnalyzeSyntaxRequestOut": "_language_39_AnalyzeSyntaxRequestOut",
        "SentenceIn": "_language_40_SentenceIn",
        "SentenceOut": "_language_41_SentenceOut",
        "EntityMentionIn": "_language_42_EntityMentionIn",
        "EntityMentionOut": "_language_43_EntityMentionOut",
        "ClassifyTextResponseIn": "_language_44_ClassifyTextResponseIn",
        "ClassifyTextResponseOut": "_language_45_ClassifyTextResponseOut",
        "EntityIn": "_language_46_EntityIn",
        "EntityOut": "_language_47_EntityOut",
        "ClassificationCategoryIn": "_language_48_ClassificationCategoryIn",
        "ClassificationCategoryOut": "_language_49_ClassificationCategoryOut",
        "AnalyzeEntitySentimentRequestIn": "_language_50_AnalyzeEntitySentimentRequestIn",
        "AnalyzeEntitySentimentRequestOut": "_language_51_AnalyzeEntitySentimentRequestOut",
        "AnalyzeSentimentResponseIn": "_language_52_AnalyzeSentimentResponseIn",
        "AnalyzeSentimentResponseOut": "_language_53_AnalyzeSentimentResponseOut",
        "ClassificationModelOptionsIn": "_language_54_ClassificationModelOptionsIn",
        "ClassificationModelOptionsOut": "_language_55_ClassificationModelOptionsOut",
    }

    types = {}
    types["ErrorResponse"] = t.struct(
        {"code": t.integer(), "message": t.string(), "status": t.string()}
    ).named(renames["ErrorResponse"])
    types["PartOfSpeechIn"] = t.struct(
        {
            "mood": t.string().optional(),
            "form": t.string().optional(),
            "number": t.string().optional(),
            "tag": t.string().optional(),
            "reciprocity": t.string().optional(),
            "voice": t.string().optional(),
            "case": t.string().optional(),
            "proper": t.string().optional(),
            "gender": t.string().optional(),
            "tense": t.string().optional(),
            "person": t.string().optional(),
            "aspect": t.string().optional(),
        }
    ).named(renames["PartOfSpeechIn"])
    types["PartOfSpeechOut"] = t.struct(
        {
            "mood": t.string().optional(),
            "form": t.string().optional(),
            "number": t.string().optional(),
            "tag": t.string().optional(),
            "reciprocity": t.string().optional(),
            "voice": t.string().optional(),
            "case": t.string().optional(),
            "proper": t.string().optional(),
            "gender": t.string().optional(),
            "tense": t.string().optional(),
            "person": t.string().optional(),
            "aspect": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["PartOfSpeechOut"])
    types["AnalyzeSentimentRequestIn"] = t.struct(
        {
            "encodingType": t.string().optional(),
            "document": t.proxy(renames["DocumentIn"]),
        }
    ).named(renames["AnalyzeSentimentRequestIn"])
    types["AnalyzeSentimentRequestOut"] = t.struct(
        {
            "encodingType": t.string().optional(),
            "document": t.proxy(renames["DocumentOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AnalyzeSentimentRequestOut"])
    types["AnnotateTextResponseIn"] = t.struct(
        {
            "tokens": t.array(t.proxy(renames["TokenIn"])).optional(),
            "entities": t.array(t.proxy(renames["EntityIn"])).optional(),
            "sentences": t.array(t.proxy(renames["SentenceIn"])).optional(),
            "categories": t.array(
                t.proxy(renames["ClassificationCategoryIn"])
            ).optional(),
            "language": t.string().optional(),
            "documentSentiment": t.proxy(renames["SentimentIn"]).optional(),
        }
    ).named(renames["AnnotateTextResponseIn"])
    types["AnnotateTextResponseOut"] = t.struct(
        {
            "tokens": t.array(t.proxy(renames["TokenOut"])).optional(),
            "entities": t.array(t.proxy(renames["EntityOut"])).optional(),
            "sentences": t.array(t.proxy(renames["SentenceOut"])).optional(),
            "categories": t.array(
                t.proxy(renames["ClassificationCategoryOut"])
            ).optional(),
            "language": t.string().optional(),
            "documentSentiment": t.proxy(renames["SentimentOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AnnotateTextResponseOut"])
    types["FeaturesIn"] = t.struct(
        {
            "extractEntitySentiment": t.boolean().optional(),
            "extractSyntax": t.boolean().optional(),
            "classifyText": t.boolean().optional(),
            "extractDocumentSentiment": t.boolean().optional(),
            "extractEntities": t.boolean().optional(),
            "classificationModelOptions": t.proxy(
                renames["ClassificationModelOptionsIn"]
            ).optional(),
        }
    ).named(renames["FeaturesIn"])
    types["FeaturesOut"] = t.struct(
        {
            "extractEntitySentiment": t.boolean().optional(),
            "extractSyntax": t.boolean().optional(),
            "classifyText": t.boolean().optional(),
            "extractDocumentSentiment": t.boolean().optional(),
            "extractEntities": t.boolean().optional(),
            "classificationModelOptions": t.proxy(
                renames["ClassificationModelOptionsOut"]
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["FeaturesOut"])
    types["AnalyzeSyntaxResponseIn"] = t.struct(
        {
            "tokens": t.array(t.proxy(renames["TokenIn"])).optional(),
            "sentences": t.array(t.proxy(renames["SentenceIn"])).optional(),
            "language": t.string().optional(),
        }
    ).named(renames["AnalyzeSyntaxResponseIn"])
    types["AnalyzeSyntaxResponseOut"] = t.struct(
        {
            "tokens": t.array(t.proxy(renames["TokenOut"])).optional(),
            "sentences": t.array(t.proxy(renames["SentenceOut"])).optional(),
            "language": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AnalyzeSyntaxResponseOut"])
    types["AnalyzeEntitySentimentResponseIn"] = t.struct(
        {
            "entities": t.array(t.proxy(renames["EntityIn"])).optional(),
            "language": t.string().optional(),
        }
    ).named(renames["AnalyzeEntitySentimentResponseIn"])
    types["AnalyzeEntitySentimentResponseOut"] = t.struct(
        {
            "entities": t.array(t.proxy(renames["EntityOut"])).optional(),
            "language": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AnalyzeEntitySentimentResponseOut"])
    types["AnnotateTextRequestIn"] = t.struct(
        {
            "document": t.proxy(renames["DocumentIn"]),
            "features": t.proxy(renames["FeaturesIn"]),
            "encodingType": t.string().optional(),
        }
    ).named(renames["AnnotateTextRequestIn"])
    types["AnnotateTextRequestOut"] = t.struct(
        {
            "document": t.proxy(renames["DocumentOut"]),
            "features": t.proxy(renames["FeaturesOut"]),
            "encodingType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AnnotateTextRequestOut"])
    types["SentimentIn"] = t.struct(
        {"magnitude": t.number().optional(), "score": t.number().optional()}
    ).named(renames["SentimentIn"])
    types["SentimentOut"] = t.struct(
        {
            "magnitude": t.number().optional(),
            "score": t.number().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SentimentOut"])
    types["DocumentIn"] = t.struct(
        {
            "type": t.string(),
            "gcsContentUri": t.string().optional(),
            "content": t.string().optional(),
            "language": t.string().optional(),
        }
    ).named(renames["DocumentIn"])
    types["DocumentOut"] = t.struct(
        {
            "type": t.string(),
            "gcsContentUri": t.string().optional(),
            "content": t.string().optional(),
            "language": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DocumentOut"])
    types["StatusIn"] = t.struct(
        {
            "code": t.integer().optional(),
            "message": t.string().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
        }
    ).named(renames["StatusIn"])
    types["StatusOut"] = t.struct(
        {
            "code": t.integer().optional(),
            "message": t.string().optional(),
            "details": t.array(t.struct({"_": t.string().optional()})).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["StatusOut"])
    types["AnalyzeEntitiesResponseIn"] = t.struct(
        {
            "language": t.string().optional(),
            "entities": t.array(t.proxy(renames["EntityIn"])).optional(),
        }
    ).named(renames["AnalyzeEntitiesResponseIn"])
    types["AnalyzeEntitiesResponseOut"] = t.struct(
        {
            "language": t.string().optional(),
            "entities": t.array(t.proxy(renames["EntityOut"])).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AnalyzeEntitiesResponseOut"])
    types["AnalyzeEntitiesRequestIn"] = t.struct(
        {
            "document": t.proxy(renames["DocumentIn"]),
            "encodingType": t.string().optional(),
        }
    ).named(renames["AnalyzeEntitiesRequestIn"])
    types["AnalyzeEntitiesRequestOut"] = t.struct(
        {
            "document": t.proxy(renames["DocumentOut"]),
            "encodingType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AnalyzeEntitiesRequestOut"])
    types["V1ModelIn"] = t.struct({"_": t.string().optional()}).named(
        renames["V1ModelIn"]
    )
    types["V1ModelOut"] = t.struct(
        {"error": t.proxy(renames["ErrorResponse"]).optional()}
    ).named(renames["V1ModelOut"])
    types["TokenIn"] = t.struct(
        {
            "lemma": t.string().optional(),
            "dependencyEdge": t.proxy(renames["DependencyEdgeIn"]).optional(),
            "partOfSpeech": t.proxy(renames["PartOfSpeechIn"]).optional(),
            "text": t.proxy(renames["TextSpanIn"]).optional(),
        }
    ).named(renames["TokenIn"])
    types["TokenOut"] = t.struct(
        {
            "lemma": t.string().optional(),
            "dependencyEdge": t.proxy(renames["DependencyEdgeOut"]).optional(),
            "partOfSpeech": t.proxy(renames["PartOfSpeechOut"]).optional(),
            "text": t.proxy(renames["TextSpanOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TokenOut"])
    types["TextSpanIn"] = t.struct(
        {"content": t.string().optional(), "beginOffset": t.integer().optional()}
    ).named(renames["TextSpanIn"])
    types["TextSpanOut"] = t.struct(
        {
            "content": t.string().optional(),
            "beginOffset": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["TextSpanOut"])
    types["DependencyEdgeIn"] = t.struct(
        {"label": t.string().optional(), "headTokenIndex": t.integer().optional()}
    ).named(renames["DependencyEdgeIn"])
    types["DependencyEdgeOut"] = t.struct(
        {
            "label": t.string().optional(),
            "headTokenIndex": t.integer().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["DependencyEdgeOut"])
    types["ClassifyTextRequestIn"] = t.struct(
        {
            "classificationModelOptions": t.proxy(
                renames["ClassificationModelOptionsIn"]
            ).optional(),
            "document": t.proxy(renames["DocumentIn"]),
        }
    ).named(renames["ClassifyTextRequestIn"])
    types["ClassifyTextRequestOut"] = t.struct(
        {
            "classificationModelOptions": t.proxy(
                renames["ClassificationModelOptionsOut"]
            ).optional(),
            "document": t.proxy(renames["DocumentOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ClassifyTextRequestOut"])
    types["V2ModelIn"] = t.struct(
        {"contentCategoriesVersion": t.string().optional()}
    ).named(renames["V2ModelIn"])
    types["V2ModelOut"] = t.struct(
        {
            "contentCategoriesVersion": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["V2ModelOut"])
    types["AnalyzeSyntaxRequestIn"] = t.struct(
        {
            "encodingType": t.string().optional(),
            "document": t.proxy(renames["DocumentIn"]),
        }
    ).named(renames["AnalyzeSyntaxRequestIn"])
    types["AnalyzeSyntaxRequestOut"] = t.struct(
        {
            "encodingType": t.string().optional(),
            "document": t.proxy(renames["DocumentOut"]),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AnalyzeSyntaxRequestOut"])
    types["SentenceIn"] = t.struct(
        {
            "text": t.proxy(renames["TextSpanIn"]).optional(),
            "sentiment": t.proxy(renames["SentimentIn"]).optional(),
        }
    ).named(renames["SentenceIn"])
    types["SentenceOut"] = t.struct(
        {
            "text": t.proxy(renames["TextSpanOut"]).optional(),
            "sentiment": t.proxy(renames["SentimentOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["SentenceOut"])
    types["EntityMentionIn"] = t.struct(
        {
            "type": t.string().optional(),
            "text": t.proxy(renames["TextSpanIn"]).optional(),
            "sentiment": t.proxy(renames["SentimentIn"]).optional(),
        }
    ).named(renames["EntityMentionIn"])
    types["EntityMentionOut"] = t.struct(
        {
            "type": t.string().optional(),
            "text": t.proxy(renames["TextSpanOut"]).optional(),
            "sentiment": t.proxy(renames["SentimentOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EntityMentionOut"])
    types["ClassifyTextResponseIn"] = t.struct(
        {"categories": t.array(t.proxy(renames["ClassificationCategoryIn"])).optional()}
    ).named(renames["ClassifyTextResponseIn"])
    types["ClassifyTextResponseOut"] = t.struct(
        {
            "categories": t.array(
                t.proxy(renames["ClassificationCategoryOut"])
            ).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ClassifyTextResponseOut"])
    types["EntityIn"] = t.struct(
        {
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "mentions": t.array(t.proxy(renames["EntityMentionIn"])).optional(),
            "sentiment": t.proxy(renames["SentimentIn"]).optional(),
            "salience": t.number().optional(),
            "type": t.string().optional(),
        }
    ).named(renames["EntityIn"])
    types["EntityOut"] = t.struct(
        {
            "name": t.string().optional(),
            "metadata": t.struct({"_": t.string().optional()}).optional(),
            "mentions": t.array(t.proxy(renames["EntityMentionOut"])).optional(),
            "sentiment": t.proxy(renames["SentimentOut"]).optional(),
            "salience": t.number().optional(),
            "type": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["EntityOut"])
    types["ClassificationCategoryIn"] = t.struct(
        {"confidence": t.number().optional(), "name": t.string().optional()}
    ).named(renames["ClassificationCategoryIn"])
    types["ClassificationCategoryOut"] = t.struct(
        {
            "confidence": t.number().optional(),
            "name": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ClassificationCategoryOut"])
    types["AnalyzeEntitySentimentRequestIn"] = t.struct(
        {
            "document": t.proxy(renames["DocumentIn"]),
            "encodingType": t.string().optional(),
        }
    ).named(renames["AnalyzeEntitySentimentRequestIn"])
    types["AnalyzeEntitySentimentRequestOut"] = t.struct(
        {
            "document": t.proxy(renames["DocumentOut"]),
            "encodingType": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AnalyzeEntitySentimentRequestOut"])
    types["AnalyzeSentimentResponseIn"] = t.struct(
        {
            "sentences": t.array(t.proxy(renames["SentenceIn"])).optional(),
            "documentSentiment": t.proxy(renames["SentimentIn"]).optional(),
            "language": t.string().optional(),
        }
    ).named(renames["AnalyzeSentimentResponseIn"])
    types["AnalyzeSentimentResponseOut"] = t.struct(
        {
            "sentences": t.array(t.proxy(renames["SentenceOut"])).optional(),
            "documentSentiment": t.proxy(renames["SentimentOut"]).optional(),
            "language": t.string().optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["AnalyzeSentimentResponseOut"])
    types["ClassificationModelOptionsIn"] = t.struct(
        {
            "v2Model": t.proxy(renames["V2ModelIn"]).optional(),
            "v1Model": t.proxy(renames["V1ModelIn"]).optional(),
        }
    ).named(renames["ClassificationModelOptionsIn"])
    types["ClassificationModelOptionsOut"] = t.struct(
        {
            "v2Model": t.proxy(renames["V2ModelOut"]).optional(),
            "v1Model": t.proxy(renames["V1ModelOut"]).optional(),
            "error": t.proxy(renames["ErrorResponse"]).optional(),
        }
    ).named(renames["ClassificationModelOptionsOut"])

    functions = {}
    functions["documentsAnalyzeSentiment"] = language.post(
        "v1/documents:classifyText",
        t.struct(
            {
                "classificationModelOptions": t.proxy(
                    renames["ClassificationModelOptionsIn"]
                ).optional(),
                "document": t.proxy(renames["DocumentIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ClassifyTextResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["documentsAnalyzeSyntax"] = language.post(
        "v1/documents:classifyText",
        t.struct(
            {
                "classificationModelOptions": t.proxy(
                    renames["ClassificationModelOptionsIn"]
                ).optional(),
                "document": t.proxy(renames["DocumentIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ClassifyTextResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["documentsAnnotateText"] = language.post(
        "v1/documents:classifyText",
        t.struct(
            {
                "classificationModelOptions": t.proxy(
                    renames["ClassificationModelOptionsIn"]
                ).optional(),
                "document": t.proxy(renames["DocumentIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ClassifyTextResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["documentsAnalyzeEntitySentiment"] = language.post(
        "v1/documents:classifyText",
        t.struct(
            {
                "classificationModelOptions": t.proxy(
                    renames["ClassificationModelOptionsIn"]
                ).optional(),
                "document": t.proxy(renames["DocumentIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ClassifyTextResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["documentsAnalyzeEntities"] = language.post(
        "v1/documents:classifyText",
        t.struct(
            {
                "classificationModelOptions": t.proxy(
                    renames["ClassificationModelOptionsIn"]
                ).optional(),
                "document": t.proxy(renames["DocumentIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ClassifyTextResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )
    functions["documentsClassifyText"] = language.post(
        "v1/documents:classifyText",
        t.struct(
            {
                "classificationModelOptions": t.proxy(
                    renames["ClassificationModelOptionsIn"]
                ).optional(),
                "document": t.proxy(renames["DocumentIn"]),
                "auth": t.string().optional(),
            }
        ),
        t.proxy(renames["ClassifyTextResponseOut"]),
        auth_token_field="auth",
        content_type="application/json",
    )

    return Import(
        importer="language", renames=renames, types=Box(types), functions=Box(functions)
    )
