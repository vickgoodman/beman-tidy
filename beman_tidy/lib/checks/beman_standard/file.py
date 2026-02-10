#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0 WITH LLVM-exception

from ..base.base_check import BaseCheck
from ..system.registry import register_beman_standard_check

# [file.*] checks category.
# All checks in this file extend the FileBaseCheck class.
#
# Note: FileBaseCheck is not a registered check!


@register_beman_standard_check("file.license_id")
class FileLicenseIDCheck(BaseCheck):
	def __init__(self, repo_info, beman_standard_check_config):
		super().__init__(repo_info, beman_standard_check_config)

	def check(self):
		# 1. get the License so I can get the correct SPDX
		# 2. Figure out which files can contain a comment
		# 3. Figure out which type of comment
		#   3.1 C/C++ "//"
		#   3.2 Scripts "#"
		#   3.3 Markdown "<!-- SPDX... -->"

		# 1. License - 2 possibilities:
		# SPDX-License-Identifier: Apache-2.0 WITH LLVM-exception
		# SPDX-License-Identifier: BSL-1.0

		# Get type of LICENSE to get SPDX License Expression
		license_path = self.repo_path / "LICENSE"

		if not license_path.exists():
			self.log("No LICENSE")
			return False

		with license_path.open() as f:
			license_text = f.read()

		spdx_identifier = "SPDX-License-Identifier: "
		if "Boost" in license_text:
			spdx_identifier += "BSL-1.0"
		elif "Apache" in license_text:
			spdx_identifier += "Apache-2.0 WITH LLVM-exception"
		else:
			self.log("Incorrect LICENSE")
			return False

		# get files

		pass

	def fix(self):
		pass


# TODO file.test_names


# TODO file.license_id


# TODO file.copyright
