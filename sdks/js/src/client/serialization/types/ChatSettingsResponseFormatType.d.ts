/**
 * This file was auto-generated by Fern from our API Definition.
 */
import * as serializers from "..";
import * as JulepApi from "../../api";
import * as core from "../../core";
export declare const ChatSettingsResponseFormatType: core.serialization.Schema<serializers.ChatSettingsResponseFormatType.Raw, JulepApi.ChatSettingsResponseFormatType>;
export declare namespace ChatSettingsResponseFormatType {
    type Raw = "text" | "json_object";
}