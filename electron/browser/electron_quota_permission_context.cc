// Copyright (c) 2015 GitHub, Inc.
// Use of this source code is governed by the MIT license that can be
// found in the LICENSE file.

#include "electron/browser/electron_quota_permission_context.h"

#include "storage/common/quota/quota_types.h"

namespace electron {

ElectronQuotaPermissionContext::ElectronQuotaPermissionContext() {
}

ElectronQuotaPermissionContext::~ElectronQuotaPermissionContext() {
}

void ElectronQuotaPermissionContext::RequestQuotaPermission(
    const content::StorageQuotaParams& params,
    int render_process_id,
    const PermissionCallback& callback) {
  callback.Run(response::QUOTA_PERMISSION_RESPONSE_ALLOW);
}

}  // namespace electron