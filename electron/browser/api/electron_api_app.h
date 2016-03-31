// Copyright (c) 2013 GitHub, Inc.
// Use of this source code is governed by the MIT license that can be
// found in the LICENSE file.

#ifndef ELECTRON_BROWSER_API_ELECTRON_API_APP_H_
#define ELECTRON_BROWSER_API_ELECTRON_API_APP_H_

#include <string>

#include "electron/browser/api/event_emitter.h"
#include "electron/browser/electron_browser_client.h"
#include "electron/browser/browser_observer.h"
#include "electron/common/native_mate_converters/callback.h"
#include "chrome/browser/process_singleton.h"
#include "content/public/browser/gpu_data_manager_observer.h"
#include "native_mate/handle.h"

namespace base {
class FilePath;
}

namespace mate {
class Arguments;
}

namespace electron {

namespace api {

class App : public ElectronBrowserClient::Delegate,
            public mate::EventEmitter,
            public BrowserObserver,
            public content::GpuDataManagerObserver {
 public:
  static mate::Handle<App> Create(v8::Isolate* isolate);

 protected:
  App();
  virtual ~App();

  // BrowserObserver:
  void OnBeforeQuit(bool* prevent_default) override;
  void OnWillQuit(bool* prevent_default) override;
  void OnWindowAllClosed() override;
  void OnQuit() override;
  void OnOpenFile(bool* prevent_default, const std::string& file_path) override;
  void OnOpenURL(const std::string& url) override;
  void OnActivate(bool has_visible_windows) override;
  void OnWillFinishLaunching() override;
  void OnFinishLaunching() override;
  void OnLogin(LoginHandler* login_handler) override;

  // content::ContentBrowserClient:
  void AllowCertificateError(
      content::WebContents* web_contents,
      int cert_error,
      const net::SSLInfo& ssl_info,
      const GURL& request_url,
      content::ResourceType resource_type,
      bool overridable,
      bool strict_enforcement,
      bool expired_previous_decision,
      const base::Callback<void(bool)>& callback,
      content::CertificateRequestResultType* request) override;
  void SelectClientCertificate(
      content::WebContents* web_contents,
      net::SSLCertRequestInfo* cert_request_info,
      scoped_ptr<content::ClientCertificateDelegate> delegate) override;

  // content::GpuDataManagerObserver:
  void OnGpuProcessCrashed(base::TerminationStatus exit_code) override;

#if defined(OS_MACOSX)
  void OnPlatformThemeChanged() override;
#endif

  // mate::Wrappable:
  mate::ObjectTemplateBuilder GetObjectTemplateBuilder(
      v8::Isolate* isolate) override;

 private:
  // Get/Set the pre-defined path in PathService.
  base::FilePath GetPath(mate::Arguments* args, const std::string& name);
  void SetPath(mate::Arguments* args,
               const std::string& name,
               const base::FilePath& path);

  void SetDesktopName(const std::string& desktop_name);
  void AllowNTLMCredentialsForAllDomains(bool should_allow);
  bool MakeSingleInstance(
      const ProcessSingleton::NotificationCallback& callback);
  std::string GetLocale();

#if defined(OS_WIN)
  bool IsAeroGlassEnabled();
#endif

  scoped_ptr<ProcessSingleton> process_singleton_;

  DISALLOW_COPY_AND_ASSIGN(App);
};

}  // namespace api

}  // namespace electron

#endif  // ELECTRON_BROWSER_API_ELECTRON_API_APP_H_