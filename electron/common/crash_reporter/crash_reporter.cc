// Copyright (c) 2013 GitHub, Inc.
// Use of this source code is governed by the MIT license that can be
// found in the LICENSE file.

#include "electron/common/crash_reporter/crash_reporter.h"

#include "electron/browser/browser.h"
#include "electron/common/atom_version.h"
#include "base/command_line.h"
#include "base/files/file_util.h"
#include "base/strings/string_split.h"
#include "base/strings/string_number_conversions.h"
#include "content/public/common/content_switches.h"

namespace crash_reporter {

CrashReporter::CrashReporter() {
  auto cmd = base::CommandLine::ForCurrentProcess();
  is_browser_ = cmd->GetSwitchValueASCII(switches::kProcessType).empty();
}

CrashReporter::~CrashReporter() {
}

void CrashReporter::Start(const std::string& product_name,
                          const std::string& company_name,
                          const std::string& submit_url,
                          bool auto_submit,
                          bool skip_system_crash_handler,
                          const StringMap& extra_parameters) {
  SetUploadParameters(extra_parameters);

  InitBreakpad(product_name, ATOM_VERSION_STRING, company_name, submit_url,
               auto_submit, skip_system_crash_handler);
}

void CrashReporter::SetUploadParameters(const StringMap& parameters) {
  upload_parameters_ = parameters;
  upload_parameters_["process_type"] = is_browser_ ? "browser" : "renderer";

  // Setting platform dependent parameters.
  SetUploadParameters();
}

std::vector<CrashReporter::UploadReportResult>
CrashReporter::GetUploadedReports(const std::string& path) {
  std::string file_content;
  std::vector<CrashReporter::UploadReportResult> result;
  if (base::ReadFileToString(base::FilePath::FromUTF8Unsafe(path),
        &file_content)) {
    std::vector<std::string> reports = base::SplitString(
        file_content, "\n", base::TRIM_WHITESPACE, base::SPLIT_WANT_NONEMPTY);
    for (const std::string& report : reports) {
      std::vector<std::string> report_item = base::SplitString(
          report, ",", base::TRIM_WHITESPACE, base::SPLIT_WANT_NONEMPTY);
      int report_time = 0;
      if (report_item.size() >= 2 && base::StringToInt(report_item[0],
            &report_time)) {
        result.push_back(CrashReporter::UploadReportResult(report_time,
            report_item[1]));
      }
    }
  }
  return result;
}

void CrashReporter::InitBreakpad(const std::string& product_name,
                                 const std::string& version,
                                 const std::string& company_name,
                                 const std::string& submit_url,
                                 bool auto_submit,
                                 bool skip_system_crash_handler) {
}

void CrashReporter::SetUploadParameters() {
}

#if defined(OS_MACOSX) && defined(MAS_BUILD)
// static
CrashReporter* CrashReporter::GetInstance() {
  static CrashReporter crash_reporter;
  return &crash_reporter;
}
#endif

}  // namespace crash_reporter
