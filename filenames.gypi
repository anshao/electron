{
  'variables': {
    'app_sources': [
      'electron/app/atom_main.cc',
      'electron/app/atom_main.h',
    ],
    'bundle_sources': [
      'electron/browser/resources/mac/atom.icns',
    ],
    'js_sources': [
      'lib/browser/api/app.js',
      'lib/browser/api/auto-updater.js',
      'lib/browser/api/auto-updater/auto-updater-native.js',
      'lib/browser/api/auto-updater/auto-updater-win.js',
      'lib/browser/api/auto-updater/squirrel-update-win.js',
      'lib/browser/api/browser-window.js',
      'lib/browser/api/content-tracing.js',
      'lib/browser/api/dialog.js',
      'lib/browser/api/exports/electron.js',
      'lib/browser/api/global-shortcut.js',
      'lib/browser/api/ipc.js',
      'lib/browser/api/ipc-main.js',
      'lib/browser/api/menu.js',
      'lib/browser/api/menu-item.js',
      'lib/browser/api/navigation-controller.js',
      'lib/browser/api/power-monitor.js',
      'lib/browser/api/power-save-blocker.js',
      'lib/browser/api/protocol.js',
      'lib/browser/api/session.js',
      'lib/browser/api/screen.js',
      'lib/browser/api/tray.js',
      'lib/browser/api/web-contents.js',
      'lib/browser/chrome-extension.js',
      'lib/browser/desktop-capturer.js',
      'lib/browser/guest-view-manager.js',
      'lib/browser/guest-window-manager.js',
      'lib/browser/init.js',
      'lib/browser/objects-registry.js',
      'lib/browser/rpc-server.js',
      'lib/common/api/callbacks-registry.js',
      'lib/common/api/clipboard.js',
      'lib/common/api/crash-reporter.js',
      'lib/common/api/deprecate.js',
      'lib/common/api/deprecations.js',
      'lib/common/api/exports/electron.js',
      'lib/common/api/native-image.js',
      'lib/common/api/shell.js',
      'lib/common/init.js',
      'lib/common/reset-search-paths.js',
      'lib/renderer/chrome-api.js',
      'lib/renderer/init.js',
      'lib/renderer/inspector.js',
      'lib/renderer/override.js',
      'lib/renderer/web-view/guest-view-internal.js',
      'lib/renderer/web-view/web-view.js',
      'lib/renderer/web-view/web-view-attributes.js',
      'lib/renderer/web-view/web-view-constants.js',
      'lib/renderer/api/desktop-capturer.js',
      'lib/renderer/api/exports/electron.js',
      'lib/renderer/api/ipc.js',
      'lib/renderer/api/ipc-renderer.js',
      'lib/renderer/api/remote.js',
      'lib/renderer/api/screen.js',
      'lib/renderer/api/web-frame.js',
    ],
    'js2c_sources': [
      'lib/common/asar.js',
      'lib/common/asar_init.js',
    ],
    'lib_sources': [
      'electron/app/atom_content_client.cc',
      'electron/app/atom_content_client.h',
      'electron/app/atom_main_delegate.cc',
      'electron/app/atom_main_delegate.h',
      'electron/app/atom_main_delegate_mac.mm',
      'electron/app/node_main.cc',
      'electron/app/node_main.h',
      'electron/app/uv_task_runner.cc',
      'electron/app/uv_task_runner.h',
      'electron/browser/api/atom_api_app.cc',
      'electron/browser/api/atom_api_app.h',
      'electron/browser/api/atom_api_auto_updater.cc',
      'electron/browser/api/atom_api_auto_updater.h',
      'electron/browser/api/atom_api_content_tracing.cc',
      'electron/browser/api/atom_api_cookies.cc',
      'electron/browser/api/atom_api_cookies.h',
      'electron/browser/api/atom_api_debugger.cc',
      'electron/browser/api/atom_api_debugger.h',
      'electron/browser/api/atom_api_desktop_capturer.cc',
      'electron/browser/api/atom_api_desktop_capturer.h',
      'electron/browser/api/atom_api_download_item.cc',
      'electron/browser/api/atom_api_download_item.h',
      'electron/browser/api/atom_api_dialog.cc',
      'electron/browser/api/atom_api_global_shortcut.cc',
      'electron/browser/api/atom_api_global_shortcut.h',
      'electron/browser/api/atom_api_menu.cc',
      'electron/browser/api/atom_api_menu.h',
      'electron/browser/api/atom_api_menu_views.cc',
      'electron/browser/api/atom_api_menu_views.h',
      'electron/browser/api/atom_api_menu_mac.h',
      'electron/browser/api/atom_api_menu_mac.mm',
      'electron/browser/api/atom_api_power_monitor.cc',
      'electron/browser/api/atom_api_power_monitor.h',
      'electron/browser/api/atom_api_power_save_blocker.cc',
      'electron/browser/api/atom_api_power_save_blocker.h',
      'electron/browser/api/atom_api_protocol.cc',
      'electron/browser/api/atom_api_protocol.h',
      'electron/browser/api/atom_api_screen.cc',
      'electron/browser/api/atom_api_screen.h',
      'electron/browser/api/atom_api_session.cc',
      'electron/browser/api/atom_api_session.h',
      'electron/browser/api/atom_api_tray.cc',
      'electron/browser/api/atom_api_tray.h',
      'electron/browser/api/atom_api_web_contents.cc',
      'electron/browser/api/atom_api_web_contents.h',
      'electron/browser/api/atom_api_web_request.cc',
      'electron/browser/api/atom_api_web_request.h',
      'electron/browser/api/atom_api_web_view_manager.cc',
      'electron/browser/api/atom_api_window.cc',
      'electron/browser/api/atom_api_window.h',
      'electron/browser/api/event.cc',
      'electron/browser/api/event.h',
      'electron/browser/api/event_emitter.cc',
      'electron/browser/api/event_emitter.h',
      'electron/browser/api/trackable_object.cc',
      'electron/browser/api/trackable_object.h',
      'electron/browser/api/frame_subscriber.cc',
      'electron/browser/api/frame_subscriber.h',
      'electron/browser/api/save_page_handler.cc',
      'electron/browser/api/save_page_handler.h',
      'electron/browser/auto_updater.cc',
      'electron/browser/auto_updater.h',
      'electron/browser/auto_updater_mac.mm',
      'electron/browser/atom_access_token_store.cc',
      'electron/browser/atom_access_token_store.h',
      'electron/browser/atom_browser_client.cc',
      'electron/browser/atom_browser_client.h',
      'electron/browser/atom_browser_context.cc',
      'electron/browser/atom_browser_context.h',
      'electron/browser/atom_download_manager_delegate.cc',
      'electron/browser/atom_download_manager_delegate.h',
      'electron/browser/atom_browser_main_parts.cc',
      'electron/browser/atom_browser_main_parts.h',
      'electron/browser/atom_browser_main_parts_mac.mm',
      'electron/browser/atom_browser_main_parts_posix.cc',
      'electron/browser/atom_javascript_dialog_manager.cc',
      'electron/browser/atom_javascript_dialog_manager.h',
      'electron/browser/atom_permission_manager.cc',
      'electron/browser/atom_permission_manager.h',
      'electron/browser/atom_quota_permission_context.cc',
      'electron/browser/atom_quota_permission_context.h',
      'electron/browser/atom_resource_dispatcher_host_delegate.cc',
      'electron/browser/atom_resource_dispatcher_host_delegate.h',
      'electron/browser/atom_speech_recognition_manager_delegate.cc',
      'electron/browser/atom_speech_recognition_manager_delegate.h',
      'electron/browser/bridge_task_runner.cc',
      'electron/browser/bridge_task_runner.h',
      'electron/browser/browser.cc',
      'electron/browser/browser.h',
      'electron/browser/browser_linux.cc',
      'electron/browser/browser_mac.mm',
      'electron/browser/browser_win.cc',
      'electron/browser/browser_observer.h',
      'electron/browser/common_web_contents_delegate.cc',
      'electron/browser/common_web_contents_delegate.h',
      'electron/browser/javascript_environment.cc',
      'electron/browser/javascript_environment.h',
      'electron/browser/login_handler.cc',
      'electron/browser/login_handler.h',
      'electron/browser/mac/atom_application.h',
      'electron/browser/mac/atom_application.mm',
      'electron/browser/mac/atom_application_delegate.h',
      'electron/browser/mac/atom_application_delegate.mm',
      'electron/browser/native_window.cc',
      'electron/browser/native_window.h',
      'electron/browser/native_window_views_win.cc',
      'electron/browser/native_window_views.cc',
      'electron/browser/native_window_views.h',
      'electron/browser/native_window_mac.h',
      'electron/browser/native_window_mac.mm',
      'electron/browser/native_window_observer.h',
      'electron/browser/net/asar/asar_protocol_handler.cc',
      'electron/browser/net/asar/asar_protocol_handler.h',
      'electron/browser/net/asar/url_request_asar_job.cc',
      'electron/browser/net/asar/url_request_asar_job.h',
      'electron/browser/net/atom_cert_verifier.cc',
      'electron/browser/net/atom_cert_verifier.h',
      'electron/browser/net/atom_network_delegate.cc',
      'electron/browser/net/atom_network_delegate.h',
      'electron/browser/net/atom_ssl_config_service.cc',
      'electron/browser/net/atom_ssl_config_service.h',
      'electron/browser/net/atom_url_request_job_factory.cc',
      'electron/browser/net/atom_url_request_job_factory.h',
      'electron/browser/net/http_protocol_handler.cc',
      'electron/browser/net/http_protocol_handler.h',
      'electron/browser/net/js_asker.cc',
      'electron/browser/net/js_asker.h',
      'electron/browser/net/url_request_async_asar_job.cc',
      'electron/browser/net/url_request_async_asar_job.h',
      'electron/browser/net/url_request_string_job.cc',
      'electron/browser/net/url_request_string_job.h',
      'electron/browser/net/url_request_buffer_job.cc',
      'electron/browser/net/url_request_buffer_job.h',
      'electron/browser/net/url_request_fetch_job.cc',
      'electron/browser/net/url_request_fetch_job.h',
      'electron/browser/node_debugger.cc',
      'electron/browser/node_debugger.h',
      'electron/browser/ui/accelerator_util.cc',
      'electron/browser/ui/accelerator_util.h',
      'electron/browser/ui/accelerator_util_mac.mm',
      'electron/browser/ui/accelerator_util_views.cc',
      'electron/browser/ui/atom_menu_model.cc',
      'electron/browser/ui/atom_menu_model.h',
      'electron/browser/ui/cocoa/atom_menu_controller.h',
      'electron/browser/ui/cocoa/atom_menu_controller.mm',
      'electron/browser/ui/file_dialog.h',
      'electron/browser/ui/file_dialog_gtk.cc',
      'electron/browser/ui/file_dialog_mac.mm',
      'electron/browser/ui/file_dialog_win.cc',
      'electron/browser/ui/message_box.h',
      'electron/browser/ui/message_box_gtk.cc',
      'electron/browser/ui/message_box_mac.mm',
      'electron/browser/ui/message_box_win.cc',
      'electron/browser/ui/tray_icon.cc',
      'electron/browser/ui/tray_icon.h',
      'electron/browser/ui/tray_icon_gtk.cc',
      'electron/browser/ui/tray_icon_gtk.h',
      'electron/browser/ui/tray_icon_cocoa.h',
      'electron/browser/ui/tray_icon_cocoa.mm',
      'electron/browser/ui/tray_icon_observer.h',
      'electron/browser/ui/tray_icon_win.cc',
      'electron/browser/ui/views/frameless_view.cc',
      'electron/browser/ui/views/frameless_view.h',
      'electron/browser/ui/views/global_menu_bar_x11.cc',
      'electron/browser/ui/views/global_menu_bar_x11.h',
      'electron/browser/ui/views/menu_bar.cc',
      'electron/browser/ui/views/menu_bar.h',
      'electron/browser/ui/views/menu_delegate.cc',
      'electron/browser/ui/views/menu_delegate.h',
      'electron/browser/ui/views/menu_layout.cc',
      'electron/browser/ui/views/menu_layout.h',
      'electron/browser/ui/views/native_frame_view.cc',
      'electron/browser/ui/views/native_frame_view.h',
      'electron/browser/ui/views/submenu_button.cc',
      'electron/browser/ui/views/submenu_button.h',
      'electron/browser/ui/views/win_frame_view.cc',
      'electron/browser/ui/views/win_frame_view.h',
      'electron/browser/ui/win/atom_desktop_window_tree_host_win.cc',
      'electron/browser/ui/win/atom_desktop_window_tree_host_win.h',
      'electron/browser/ui/win/message_handler_delegate.cc',
      'electron/browser/ui/win/message_handler_delegate.h',
      'electron/browser/ui/win/notify_icon_host.cc',
      'electron/browser/ui/win/notify_icon_host.h',
      'electron/browser/ui/win/notify_icon.cc',
      'electron/browser/ui/win/notify_icon.h',
      'electron/browser/ui/win/taskbar_host.cc',
      'electron/browser/ui/win/taskbar_host.h',
      'electron/browser/ui/x/window_state_watcher.cc',
      'electron/browser/ui/x/window_state_watcher.h',
      'electron/browser/ui/x/x_window_utils.cc',
      'electron/browser/ui/x/x_window_utils.h',
      'electron/browser/web_contents_permission_helper.cc',
      'electron/browser/web_contents_permission_helper.h',
      'electron/browser/web_contents_preferences.cc',
      'electron/browser/web_contents_preferences.h',
      'electron/browser/web_dialog_helper.cc',
      'electron/browser/web_dialog_helper.h',
      'electron/browser/web_view_guest_delegate.cc',
      'electron/browser/web_view_guest_delegate.h',
      'electron/browser/web_view_manager.cc',
      'electron/browser/web_view_manager.h',
      'electron/browser/window_list.cc',
      'electron/browser/window_list.h',
      'electron/browser/window_list_observer.h',
      'electron/common/api/api_messages.h',
      'electron/common/api/atom_api_asar.cc',
      'electron/common/api/atom_api_clipboard.cc',
      'electron/common/api/atom_api_crash_reporter.cc',
      'electron/common/api/atom_api_id_weak_map.cc',
      'electron/common/api/atom_api_id_weak_map.h',
      'electron/common/api/atom_api_native_image.cc',
      'electron/common/api/atom_api_native_image.h',
      'electron/common/api/atom_api_native_image_mac.mm',
      'electron/common/api/atom_api_shell.cc',
      'electron/common/api/atom_api_v8_util.cc',
      'electron/common/api/atom_bindings.cc',
      'electron/common/api/atom_bindings.h',
      'electron/common/api/event_emitter_caller.cc',
      'electron/common/api/event_emitter_caller.h',
      'electron/common/api/locker.cc',
      'electron/common/api/locker.h',
      'electron/common/api/object_life_monitor.cc',
      'electron/common/api/object_life_monitor.h',
      'electron/common/asar/archive.cc',
      'electron/common/asar/archive.h',
      'electron/common/asar/asar_util.cc',
      'electron/common/asar/asar_util.h',
      'electron/common/asar/scoped_temporary_file.cc',
      'electron/common/asar/scoped_temporary_file.h',
      'electron/common/atom_command_line.cc',
      'electron/common/atom_command_line.h',
      'electron/common/atom_constants.cc',
      'electron/common/atom_constants.h',
      'electron/common/common_message_generator.cc',
      'electron/common/common_message_generator.h',
      'electron/common/crash_reporter/crash_reporter.cc',
      'electron/common/crash_reporter/crash_reporter.h',
      'electron/common/crash_reporter/crash_reporter_linux.cc',
      'electron/common/crash_reporter/crash_reporter_linux.h',
      'electron/common/crash_reporter/crash_reporter_mac.h',
      'electron/common/crash_reporter/crash_reporter_mac.mm',
      'electron/common/crash_reporter/crash_reporter_win.cc',
      'electron/common/crash_reporter/crash_reporter_win.h',
      'electron/common/crash_reporter/linux/crash_dump_handler.cc',
      'electron/common/crash_reporter/linux/crash_dump_handler.h',
      'electron/common/crash_reporter/win/crash_service.cc',
      'electron/common/crash_reporter/win/crash_service.h',
      'electron/common/crash_reporter/win/crash_service_main.cc',
      'electron/common/crash_reporter/win/crash_service_main.h',
      'electron/common/draggable_region.cc',
      'electron/common/draggable_region.h',
      'electron/common/google_api_key.h',
      'electron/common/id_weak_map.cc',
      'electron/common/id_weak_map.h',
      'electron/common/keyboard_util.cc',
      'electron/common/keyboard_util.h',
      'electron/common/mouse_util.cc',
      'electron/common/mouse_util.h',
      'electron/common/linux/application_info.cc',
      'electron/common/native_mate_converters/accelerator_converter.cc',
      'electron/common/native_mate_converters/accelerator_converter.h',
      'electron/common/native_mate_converters/blink_converter.cc',
      'electron/common/native_mate_converters/blink_converter.h',
      'electron/common/native_mate_converters/callback.cc',
      'electron/common/native_mate_converters/callback.h',
      'electron/common/native_mate_converters/content_converter.cc',
      'electron/common/native_mate_converters/content_converter.h',
      'electron/common/native_mate_converters/file_path_converter.h',
      'electron/common/native_mate_converters/gfx_converter.cc',
      'electron/common/native_mate_converters/gfx_converter.h',
      'electron/common/native_mate_converters/gurl_converter.h',
      'electron/common/native_mate_converters/image_converter.cc',
      'electron/common/native_mate_converters/image_converter.h',
      'electron/common/native_mate_converters/net_converter.cc',
      'electron/common/native_mate_converters/net_converter.h',
      'electron/common/native_mate_converters/string16_converter.h',
      'electron/common/native_mate_converters/v8_value_converter.cc',
      'electron/common/native_mate_converters/v8_value_converter.h',
      'electron/common/native_mate_converters/value_converter.cc',
      'electron/common/native_mate_converters/value_converter.h',
      'electron/common/node_bindings.cc',
      'electron/common/node_bindings.h',
      'electron/common/node_bindings_linux.cc',
      'electron/common/node_bindings_linux.h',
      'electron/common/node_bindings_mac.cc',
      'electron/common/node_bindings_mac.h',
      'electron/common/node_bindings_win.cc',
      'electron/common/node_bindings_win.h',
      'electron/common/node_includes.h',
      'electron/common/options_switches.cc',
      'electron/common/options_switches.h',
      'electron/common/platform_util.h',
      'electron/common/platform_util_linux.cc',
      'electron/common/platform_util_mac.mm',
      'electron/common/platform_util_win.cc',
      'electron/renderer/api/atom_api_renderer_ipc.cc',
      'electron/renderer/api/atom_api_spell_check_client.cc',
      'electron/renderer/api/atom_api_spell_check_client.h',
      'electron/renderer/api/atom_api_web_frame.cc',
      'electron/renderer/api/atom_api_web_frame.h',
      'electron/renderer/atom_render_view_observer.cc',
      'electron/renderer/atom_render_view_observer.h',
      'electron/renderer/atom_renderer_client.cc',
      'electron/renderer/atom_renderer_client.h',
      'electron/renderer/guest_view_container.cc',
      'electron/renderer/guest_view_container.h',
      'electron/renderer/node_array_buffer_bridge.cc',
      'electron/renderer/node_array_buffer_bridge.h',
      'electron/utility/atom_content_utility_client.cc',
      'electron/utility/atom_content_utility_client.h',
      'chromium_src/chrome/browser/browser_process.cc',
      'chromium_src/chrome/browser/browser_process.h',
      'chromium_src/chrome/browser/chrome_process_finder_win.cc',
      'chromium_src/chrome/browser/chrome_process_finder_win.h',
      'chromium_src/chrome/browser/chrome_notification_types.h',
      'chromium_src/chrome/browser/extensions/global_shortcut_listener.cc',
      'chromium_src/chrome/browser/extensions/global_shortcut_listener.h',
      'chromium_src/chrome/browser/extensions/global_shortcut_listener_mac.mm',
      'chromium_src/chrome/browser/extensions/global_shortcut_listener_mac.h',
      'chromium_src/chrome/browser/extensions/global_shortcut_listener_x11.cc',
      'chromium_src/chrome/browser/extensions/global_shortcut_listener_x11.h',
      'chromium_src/chrome/browser/extensions/global_shortcut_listener_win.cc',
      'chromium_src/chrome/browser/extensions/global_shortcut_listener_win.h',
      'chromium_src/chrome/browser/media/desktop_media_list.h',
      'chromium_src/chrome/browser/media/desktop_media_list_observer.h',
      'chromium_src/chrome/browser/media/native_desktop_media_list.cc',
      'chromium_src/chrome/browser/media/native_desktop_media_list.h',
      'chromium_src/chrome/browser/printing/print_job.cc',
      'chromium_src/chrome/browser/printing/print_job.h',
      'chromium_src/chrome/browser/printing/print_job_manager.cc',
      'chromium_src/chrome/browser/printing/print_job_manager.h',
      'chromium_src/chrome/browser/printing/print_job_worker.cc',
      'chromium_src/chrome/browser/printing/print_job_worker.h',
      'chromium_src/chrome/browser/printing/print_job_worker_owner.cc',
      'chromium_src/chrome/browser/printing/print_job_worker_owner.h',
      'chromium_src/chrome/browser/printing/print_view_manager_base.cc',
      'chromium_src/chrome/browser/printing/print_view_manager_base.h',
      'chromium_src/chrome/browser/printing/print_view_manager_basic.cc',
      'chromium_src/chrome/browser/printing/print_view_manager_basic.h',
      'chromium_src/chrome/browser/printing/print_view_manager_observer.h',
      'chromium_src/chrome/browser/printing/printer_query.cc',
      'chromium_src/chrome/browser/printing/printer_query.h',
      'chromium_src/chrome/browser/printing/printing_message_filter.cc',
      'chromium_src/chrome/browser/printing/printing_message_filter.h',
      'chromium_src/chrome/browser/printing/print_preview_message_handler.cc',
      'chromium_src/chrome/browser/printing/print_preview_message_handler.h',
      'chromium_src/chrome/browser/process_singleton_posix.cc',
      'chromium_src/chrome/browser/process_singleton_win.cc',
      'chromium_src/chrome/browser/process_singleton.h',
      'chromium_src/chrome/browser/renderer_host/pepper/chrome_browser_pepper_host_factory.cc',
      'chromium_src/chrome/browser/renderer_host/pepper/chrome_browser_pepper_host_factory.h',
      'chromium_src/chrome/browser/renderer_host/pepper/monitor_finder_mac.h',
      'chromium_src/chrome/browser/renderer_host/pepper/monitor_finder_mac.mm',
      'chromium_src/chrome/browser/renderer_host/pepper/pepper_broker_message_filter.cc',
      'chromium_src/chrome/browser/renderer_host/pepper/pepper_broker_message_filter.h',
      'chromium_src/chrome/browser/renderer_host/pepper/pepper_flash_browser_host.cc',
      'chromium_src/chrome/browser/renderer_host/pepper/pepper_flash_browser_host.h',
      'chromium_src/chrome/browser/renderer_host/pepper/pepper_flash_clipboard_message_filter.cc',
      'chromium_src/chrome/browser/renderer_host/pepper/pepper_flash_clipboard_message_filter.h',
      'chromium_src/chrome/browser/renderer_host/pepper/pepper_flash_drm_host.cc',
      'chromium_src/chrome/browser/renderer_host/pepper/pepper_flash_drm_host.h',
      'chromium_src/chrome/browser/renderer_host/pepper/pepper_isolated_file_system_message_filter.cc',
      'chromium_src/chrome/browser/renderer_host/pepper/pepper_isolated_file_system_message_filter.h',
      'chromium_src/chrome/browser/renderer_host/pepper/widevine_cdm_message_filter.cc',
      'chromium_src/chrome/browser/renderer_host/pepper/widevine_cdm_message_filter.h',
      'chromium_src/chrome/browser/speech/tts_controller.h',
      'chromium_src/chrome/browser/speech/tts_controller_impl.cc',
      'chromium_src/chrome/browser/speech/tts_controller_impl.h',
      'chromium_src/chrome/browser/speech/tts_linux.cc',
      'chromium_src/chrome/browser/speech/tts_mac.mm',
      'chromium_src/chrome/browser/speech/tts_message_filter.cc',
      'chromium_src/chrome/browser/speech/tts_message_filter.h',
      'chromium_src/chrome/browser/speech/tts_platform.cc',
      'chromium_src/chrome/browser/speech/tts_platform.h',
      'chromium_src/chrome/browser/speech/tts_win.cc',
      'chromium_src/chrome/browser/ui/browser_dialogs.h',
      'chromium_src/chrome/browser/ui/cocoa/color_chooser_mac.mm',
      'chromium_src/chrome/browser/ui/views/color_chooser_aura.cc',
      'chromium_src/chrome/browser/ui/views/color_chooser_aura.h',
      'chromium_src/chrome/browser/ui/views/frame/global_menu_bar_registrar_x11.cc',
      'chromium_src/chrome/browser/ui/views/frame/global_menu_bar_registrar_x11.h',
      'chromium_src/chrome/common/chrome_constants.cc',
      'chromium_src/chrome/common/chrome_constants.h',
      'chromium_src/chrome/common/chrome_paths.cc',
      'chromium_src/chrome/common/chrome_paths.h',
      'chromium_src/chrome/common/chrome_paths_internal.h',
      'chromium_src/chrome/common/chrome_paths_linux.cc',
      'chromium_src/chrome/common/chrome_paths_mac.mm',
      'chromium_src/chrome/common/chrome_paths_win.cc',
      'chromium_src/chrome/common/chrome_utility_messages.h',
      'chromium_src/chrome/common/pref_names.cc',
      'chromium_src/chrome/common/pref_names.h',
      'chromium_src/chrome/common/print_messages.cc',
      'chromium_src/chrome/common/print_messages.h',
      'chromium_src/chrome/common/tts_messages.h',
      'chromium_src/chrome/common/tts_utterance_request.cc',
      'chromium_src/chrome/common/tts_utterance_request.h',
      'chromium_src/chrome/common/widevine_cdm_messages.h',
      'chromium_src/chrome/common/widevine_cdm_constants.cc',
      'chromium_src/chrome/common/widevine_cdm_constants.h',
      'chromium_src/chrome/renderer/media/chrome_key_systems.cc',
      'chromium_src/chrome/renderer/media/chrome_key_systems.h',
      'chromium_src/chrome/renderer/pepper/chrome_renderer_pepper_host_factory.cc',
      'chromium_src/chrome/renderer/pepper/chrome_renderer_pepper_host_factory.h',
      'chromium_src/chrome/renderer/pepper/pepper_flash_font_file_host.cc',
      'chromium_src/chrome/renderer/pepper/pepper_flash_font_file_host.h',
      'chromium_src/chrome/renderer/pepper/pepper_flash_fullscreen_host.cc',
      'chromium_src/chrome/renderer/pepper/pepper_flash_fullscreen_host.h',
      'chromium_src/chrome/renderer/pepper/pepper_flash_menu_host.cc',
      'chromium_src/chrome/renderer/pepper/pepper_flash_menu_host.h',
      'chromium_src/chrome/renderer/pepper/pepper_flash_renderer_host.cc',
      'chromium_src/chrome/renderer/pepper/pepper_flash_renderer_host.h',
      'chromium_src/chrome/renderer/pepper/pepper_helper.cc',
      'chromium_src/chrome/renderer/pepper/pepper_helper.h',
      'chromium_src/chrome/renderer/pepper/pepper_shared_memory_message_filter.cc',
      'chromium_src/chrome/renderer/pepper/pepper_shared_memory_message_filter.h',
      'chromium_src/chrome/renderer/printing/print_web_view_helper.cc',
      'chromium_src/chrome/renderer/printing/print_web_view_helper_linux.cc',
      'chromium_src/chrome/renderer/printing/print_web_view_helper_mac.mm',
      'chromium_src/chrome/renderer/printing/print_web_view_helper_pdf_win.cc',
      'chromium_src/chrome/renderer/printing/print_web_view_helper.h',
      'chromium_src/chrome/renderer/spellchecker/spellcheck_worditerator.cc',
      'chromium_src/chrome/renderer/spellchecker/spellcheck_worditerator.h',
      'chromium_src/chrome/renderer/tts_dispatcher.cc',
      'chromium_src/chrome/renderer/tts_dispatcher.h',
      'chromium_src/chrome/utility/utility_message_handler.h',
      'chromium_src/extensions/browser/app_window/size_constraints.cc',
      'chromium_src/extensions/browser/app_window/size_constraints.h',
      'chromium_src/extensions/common/url_pattern.cc',
      'chromium_src/extensions/common/url_pattern.h',
      'chromium_src/library_loaders/libspeechd_loader.cc',
      'chromium_src/library_loaders/libspeechd.h',
      'chromium_src/net/test/embedded_test_server/stream_listen_socket.cc',
      'chromium_src/net/test/embedded_test_server/stream_listen_socket.h',
      'chromium_src/net/test/embedded_test_server/tcp_listen_socket.cc',
      'chromium_src/net/test/embedded_test_server/tcp_listen_socket.h',
      '<@(native_mate_files)',
      '<(SHARED_INTERMEDIATE_DIR)/atom_natives.h',
    ],
    'lib_sources_win': [
      'chromium_src/chrome/browser/ui/views/color_chooser_dialog.cc',
      'chromium_src/chrome/browser/ui/views/color_chooser_dialog.h',
      'chromium_src/chrome/browser/ui/views/color_chooser_win.cc',
      'chromium_src/chrome/browser/printing/pdf_to_emf_converter.cc',
      'chromium_src/chrome/browser/printing/pdf_to_emf_converter.h',
      'chromium_src/chrome/utility/printing_handler_win.cc',
      'chromium_src/chrome/utility/printing_handler_win.h',
    ],
    'framework_sources': [
      'electron/app/atom_library_main.h',
      'electron/app/atom_library_main.mm',
    ],
    'locales': [
      'am', 'ar', 'bg', 'bn', 'ca', 'cs', 'da', 'de', 'el', 'en-GB',
      'en-US', 'es-419', 'es', 'et', 'fa', 'fi', 'fil', 'fr', 'gu', 'he',
      'hi', 'hr', 'hu', 'id', 'it', 'ja', 'kn', 'ko', 'lt', 'lv',
      'ml', 'mr', 'ms', 'nb', 'nl', 'pl', 'pt-BR', 'pt-PT', 'ro', 'ru',
      'sk', 'sl', 'sr', 'sv', 'sw', 'ta', 'te', 'th', 'tr', 'uk',
      'vi', 'zh-CN', 'zh-TW',
    ],
    'conditions': [
      ['OS=="win"', {
        'app_sources': [
          'electron/browser/resources/win/resource.h',
          'electron/browser/resources/win/atom.ico',
          'electron/browser/resources/win/atom.rc',
          # Cursors.
          '<(libchromiumcontent_src_dir)/ui/resources/cursors/aliasb.cur',
          '<(libchromiumcontent_src_dir)/ui/resources/cursors/cell.cur',
          '<(libchromiumcontent_src_dir)/ui/resources/cursors/col_resize.cur',
          '<(libchromiumcontent_src_dir)/ui/resources/cursors/copy.cur',
          '<(libchromiumcontent_src_dir)/ui/resources/cursors/hand_grab.cur',
          '<(libchromiumcontent_src_dir)/ui/resources/cursors/hand_grabbing.cur',
          '<(libchromiumcontent_src_dir)/ui/resources/cursors/none.cur',
          '<(libchromiumcontent_src_dir)/ui/resources/cursors/pan_east.cur',
          '<(libchromiumcontent_src_dir)/ui/resources/cursors/pan_middle.cur',
          '<(libchromiumcontent_src_dir)/ui/resources/cursors/pan_north.cur',
          '<(libchromiumcontent_src_dir)/ui/resources/cursors/pan_north_east.cur',
          '<(libchromiumcontent_src_dir)/ui/resources/cursors/pan_north_west.cur',
          '<(libchromiumcontent_src_dir)/ui/resources/cursors/pan_south.cur',
          '<(libchromiumcontent_src_dir)/ui/resources/cursors/pan_south_east.cur',
          '<(libchromiumcontent_src_dir)/ui/resources/cursors/pan_south_west.cur',
          '<(libchromiumcontent_src_dir)/ui/resources/cursors/pan_west.cur',
          '<(libchromiumcontent_src_dir)/ui/resources/cursors/row_resize.cur',
          '<(libchromiumcontent_src_dir)/ui/resources/cursors/vertical_text.cur',
          '<(libchromiumcontent_src_dir)/ui/resources/cursors/zoom_in.cur',
          '<(libchromiumcontent_src_dir)/ui/resources/cursors/zoom_out.cur',
        ],
      }],  # OS=="win"
    ],
  },
}
