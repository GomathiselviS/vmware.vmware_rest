#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright: (c) 2021, Ansible Project
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# template: header.j2
# This module is autogenerated using the ansible.content_builder.
# See: https://github.com/ansible-community/ansible.content_builder
from __future__ import absolute_import, division, print_function

__metaclass__ = type


DOCUMENTATION = r"""
module: vcenter_vm_hardware_boot
short_description: Updates the boot-related settings of a virtual machine.
description: Updates the boot-related settings of a virtual machine.
options:
    delay:
        description:
        - Delay in milliseconds before beginning the firmware boot process when the
            virtual machine is powered on.  This delay may be used to provide a time
            window for users to connect to the virtual machine console and enter BIOS
            setup mode.
        type: int
    efi_legacy_boot:
        description:
        - Flag indicating whether to use EFI legacy boot mode.
        type: bool
    enter_setup_mode:
        description:
        - Flag indicating whether the firmware boot process should automatically enter
            setup mode the next time the virtual machine boots.  Note that this flag
            will automatically be reset to false once the virtual machine enters setup
            mode.
        type: bool
    network_protocol:
        choices:
        - IPV4
        - IPV6
        description:
        - The C(network_protocol) defines the valid network boot protocols supported
            when booting a virtual machine with {@link Type#EFI} firmware over the
            network.
        type: str
    retry:
        description:
        - Flag indicating whether the virtual machine should automatically retry the
            boot process after a failure.
        type: bool
    retry_delay:
        description:
        - Delay in milliseconds before retrying the boot process after a failure;
            applicable only when {@link Info#retry} is true.
        type: int
    session_timeout:
        description:
        - 'Timeout settings for client session. '
        - 'The maximal number of seconds for the whole operation including connection
            establishment, request sending and response. '
        - The default value is 300s.
        type: float
        version_added: 2.1.0
    state:
        choices:
        - present
        default: present
        description: []
        type: str
    type:
        choices:
        - BIOS
        - EFI
        description:
        - The C(type) defines the valid firmware types for a virtual machine.
        type: str
    vcenter_hostname:
        description:
        - The hostname or IP address of the vSphere vCenter
        - If the value is not specified in the task, the value of environment variable
            C(VMWARE_HOST) will be used instead.
        required: true
        type: str
    vcenter_password:
        description:
        - The vSphere vCenter password
        - If the value is not specified in the task, the value of environment variable
            C(VMWARE_PASSWORD) will be used instead.
        required: true
        type: str
    vcenter_rest_log_file:
        description:
        - 'You can use this optional parameter to set the location of a log file. '
        - 'This file will be used to record the HTTP REST interaction. '
        - 'The file will be stored on the host that run the module. '
        - 'If the value is not specified in the task, the value of '
        - environment variable C(VMWARE_REST_LOG_FILE) will be used instead.
        type: str
    vcenter_username:
        description:
        - The vSphere vCenter username
        - If the value is not specified in the task, the value of environment variable
            C(VMWARE_USER) will be used instead.
        required: true
        type: str
    vcenter_validate_certs:
        default: true
        description:
        - Allows connection when SSL certificates are not valid. Set to C(false) when
            certificates are not trusted.
        - If the value is not specified in the task, the value of environment variable
            C(VMWARE_VALIDATE_CERTS) will be used instead.
        type: bool
    vm:
        description:
        - Virtual machine identifier. This parameter is mandatory.
        required: true
        type: str
author:
- Ansible Cloud Team (@ansible-collections)
version_added: 2.0.0
requirements:
- vSphere 7.0.2 or greater
- python >= 3.6
- aiohttp
notes:
- Tested on vSphere 7.0.2
"""

EXAMPLES = r"""
- name: Look up the VM called test_vm1 in the inventory
  register: search_result
  vmware.vmware_rest.vcenter_vm_info:
    filter_names:
    - test_vm1

- name: Collect information about a specific VM
  vmware.vmware_rest.vcenter_vm_info:
    vm: '{{ search_result.value[0].vm }}'
  register: test_vm1_info

- name: Change a VM boot parameters
  vmware.vmware_rest.vcenter_vm_hardware_boot:
    vm: '{{ test_vm1_info.id }}'
    efi_legacy_boot: true
    type: EFI
  register: _result
"""

RETURN = r"""
"""

# This structure describes the format of the data expected by the end-points
PAYLOAD_FORMAT = {
    "update": {
        "query": {},
        "body": {
            "delay": "delay",
            "efi_legacy_boot": "efi_legacy_boot",
            "enter_setup_mode": "enter_setup_mode",
            "network_protocol": "network_protocol",
            "retry": "retry",
            "retry_delay": "retry_delay",
            "type": "type",
        },
        "path": {"vm": "vm"},
    }
}  # pylint: disable=line-too-long

import json  # pylint: disable=unused-import
import socket  # pylint: disable=unused-import
from ansible.module_utils.basic import env_fallback

try:
    from ansible_collections.cloud.common.plugins.module_utils.turbo.exceptions import (
        EmbeddedModuleFailure,
    )
    from ansible_collections.cloud.common.plugins.module_utils.turbo.module import (
        AnsibleTurboModule as AnsibleModule,
    )

    AnsibleModule.collection_name = "vmware.vmware_rest"
except ImportError:
    from ansible.module_utils.basic import AnsibleModule

# pylint: disable=unused-import
from ansible_collections.vmware.vmware_rest.plugins.module_utils.vmware_rest import (
    build_full_device_list,
    exists,
    gen_args,
    get_device_info,
    get_subdevice_type,
    list_devices,
    open_session,
    prepare_payload,
    update_changed_flag,
    session_timeout,
)


def prepare_argument_spec():
    argument_spec = {
        "vcenter_hostname": dict(
            type="str",
            required=True,
            fallback=(env_fallback, ["VMWARE_HOST"]),
        ),
        "vcenter_username": dict(
            type="str",
            required=True,
            fallback=(env_fallback, ["VMWARE_USER"]),
        ),
        "vcenter_password": dict(
            type="str",
            required=True,
            no_log=True,
            fallback=(env_fallback, ["VMWARE_PASSWORD"]),
        ),
        "vcenter_validate_certs": dict(
            type="bool",
            required=False,
            default=True,
            fallback=(env_fallback, ["VMWARE_VALIDATE_CERTS"]),
        ),
        "vcenter_rest_log_file": dict(
            type="str",
            required=False,
            fallback=(env_fallback, ["VMWARE_REST_LOG_FILE"]),
        ),
        "session_timeout": dict(
            type="float",
            required=False,
            fallback=(env_fallback, ["VMWARE_SESSION_TIMEOUT"]),
        ),
    }

    argument_spec["delay"] = {"type": "int"}
    argument_spec["efi_legacy_boot"] = {"type": "bool"}
    argument_spec["enter_setup_mode"] = {"type": "bool"}
    argument_spec["network_protocol"] = {"type": "str", "choices": ["IPV4", "IPV6"]}
    argument_spec["retry"] = {"type": "bool"}
    argument_spec["retry_delay"] = {"type": "int"}
    argument_spec["state"] = {
        "type": "str",
        "choices": ["present"],
        "default": "present",
    }
    argument_spec["type"] = {"type": "str", "choices": ["BIOS", "EFI"]}
    argument_spec["vm"] = {"required": True, "type": "str"}

    return argument_spec


async def main():
    required_if = list([])

    module_args = prepare_argument_spec()
    module = AnsibleModule(
        argument_spec=module_args, required_if=required_if, supports_check_mode=True
    )
    if not module.params["vcenter_hostname"]:
        module.fail_json("vcenter_hostname cannot be empty")
    if not module.params["vcenter_username"]:
        module.fail_json("vcenter_username cannot be empty")
    if not module.params["vcenter_password"]:
        module.fail_json("vcenter_password cannot be empty")
    try:
        session = await open_session(
            vcenter_hostname=module.params["vcenter_hostname"],
            vcenter_username=module.params["vcenter_username"],
            vcenter_password=module.params["vcenter_password"],
            validate_certs=module.params["vcenter_validate_certs"],
            log_file=module.params["vcenter_rest_log_file"],
        )
    except EmbeddedModuleFailure as err:
        module.fail_json(err.get_message())
    result = await entry_point(module, session)
    module.exit_json(**result)


# template: default_module.j2
def build_url(params):
    return ("https://{vcenter_hostname}" "/api/vcenter/vm/{vm}/hardware/boot").format(
        **params
    )


async def entry_point(module, session):
    if module.params["state"] == "present":
        if "_create" in globals():
            operation = "create"
        else:
            operation = "update"
    elif module.params["state"] == "absent":
        operation = "delete"
    else:
        operation = module.params["state"]

    func = globals()["_" + operation]

    return await func(module.params, session)


async def _update(params, session):
    payload = prepare_payload(params, PAYLOAD_FORMAT["update"])
    _url = ("https://{vcenter_hostname}" "/api/vcenter/vm/{vm}/hardware/boot").format(
        **params
    )
    async with session.get(_url, **session_timeout(params)) as resp:
        _json = await resp.json()
        if "value" in _json:
            value = _json["value"]
        else:  # 7.0.2 and greater
            value = _json
        for k, v in value.items():
            if k in payload:
                if isinstance(payload[k], dict) and isinstance(v, dict):
                    to_delete = True
                    for _k in list(payload[k].keys()):
                        if payload[k][_k] != v.get(_k):
                            to_delete = False
                    if to_delete:
                        del payload[k]
                elif payload[k] == v:
                    del payload[k]
                elif payload[k] == {}:
                    del payload[k]

        if payload == {} or payload == {"spec": {}}:
            # Nothing has changed
            if "value" not in _json:  # 7.0.2
                _json = {"value": _json}
            _json["id"] = params.get("None")
            return await update_changed_flag(_json, resp.status, "get")
    async with session.patch(_url, json=payload, **session_timeout(params)) as resp:
        try:
            if resp.headers["Content-Type"] == "application/json":
                _json = await resp.json()
        except KeyError:
            _json = {}
        if "value" not in _json:  # 7.0.2
            _json = {"value": _json}

        # e.g: content_configuration
        if not _json and resp.status == 204:
            async with session.get(_url, **session_timeout(params)) as resp_get:
                _json_get = await resp_get.json()
                if _json_get:
                    _json = _json_get

        _json["id"] = params.get("None")
        return await update_changed_flag(_json, resp.status, "update")


if __name__ == "__main__":
    import asyncio

    current_loop = asyncio.get_event_loop_policy().get_event_loop()
    current_loop.run_until_complete(main())
