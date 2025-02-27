#!/usr/bin/env python3
# python >= 3.4

import os
from common.header_checker import HeaderChecker

#--------------------------------------------------------------------------------------------------
#                                            CONFIG
#--------------------------------------------------------------------------------------------------
FREERTOS_IGNORED_EXTENSIONS = [
    '.1',
    '.ASM',
    '.C',
    '.DSW',
    '.G_C',
    '.H',
    '.Hbp',
    '.IDE',
    '.LIB',
    '.Opt',
    '.PC',
    '.PRM',
    '.TXT',
    '.URL',
    '.UVL',
    '.Uv2',
    '.a',
    '.ac',
    '.am',
    '.atsln',
    '.atstart',
    '.atsuo',
    '.bash',
    '.bat',
    '.bbl',
    '.bit',
    '.board',
    '.bsb',
    '.bsdl',
    '.bts',
    '.ccxml',
    '.cdkproj',
    '.cdkws',
    '.cfg',
    '.cgp',
    '.checksum',
    '.cmake',
    '.cmd',
    '.config',
    '.cpp',
    '.cproj',
    '.cproject',
    '.crun',
    '.css',
    '.csv',
    '.custom_argvars',
    '.cxx',
    '.cydwr',
    '.cyprj',
    '.cysch',
    '.dat',
    '.datas',
    '.db',
    '.dbgdt',
    '.dep',
    '.dni',
    '.dnx',
    '.doc',
    '.dox',
    '.doxygen',
    '.ds',
    '.dsk',
    '.dtd',
    '.dts',
    '.elf',
    '.emProject',
    '.env_conf',
    '.ewd',
    '.ewp',
    '.ewt',
    '.eww',
    '.exe',
    '.filters',
    '.flash',
    '.fmt',
    '.ftl',
    '.gdb',
    '.gif',
    '.gise',
    '.gld',
    '.gpdsc',
    '.gui',
    '.h_from_toolchain',
    '.hdf',
    '.hdp',
    '.hex',
    '.hist',
    '.history',
    '.hsf',
    '.htm',
    '.html',
    '.hwc',
    '.hwl',
    '.hwp',
    '.hws',
    '.hzp',
    '.hzs',
    '.i',
    '.icf',
    '.ide',
    '.idx',
    '.in',
    '.inc',
    '.include',
    '.index',
    '.inf',
    '.ini',
    '.init',
    '.ipcf',
    '.ise',
    '.jlink',
    '.json',
    '.la',
    '.launch',
    '.lcf',
    '.ld',
    '.lds',
    '.lib',
    '.lk1',
    '.lkr',
    '.lm',
    '.lo',
    '.lock',
    '.lsl',
    '.lst',
    '.m4',
    '.mac',
    '.make',
    '.map',
    '.mbt',
    '.mcp',
    '.mcpar',
    '.mcs',
    '.mcw',
    '.md',
    '.mdm',
    '.mem',
    '.mhs',
    '.mk',
    '.mk1',
    '.mmi',
    '.mrt',
    '.mss',
    '.mtpj',
    '.nav',
    '.ntrc_log',
    '.opa',
    '.opb',
    '.opc',
    '.opl',
    '.opt',
    '.opv',
    '.out',
    '.pack',
    '.par',
    '.patch',
    '.pbd',
    '.pdsc',
    '.pe',
    '.pem',
    '.pgs',
    '.pl',
    '.plg',
    '.png',
    '.prc',
    '.pref',
    '.prefs',
    '.prj',
    '.project',
    '.properties',
    '.ps1',
    '.ptf',
    '.py',
    '.r79',
    '.rapp',
    '.rc',
    '.reggroups',
    '.reglist',
    '.resc',
    '.resources',
    '.rom',
    '.rprj',
    '.s',
    '.s79',
    '.s82',
    '.s90',
    '.sc',
    '.scf',
    '.scfg',
    '.script',
    '.sct',
    '.scvd',
    '.session',
    '.sfr',
    '.sh',
    '.shtml',
    '.sig',
    '.sln',
    '.spec',
    '.sprj',
    '.stf',
    '.stg',
    '.suo',
    '.sup',
    '.svg',
    '.tags',
    '.tcl',
    '.tdt',
    '.template',
    '.tgt',
    '.tps',
    '.tra',
    '.tree',
    '.tws',
    '.txt',
    '.ucf',
    '.url',
    '.user',
    '.ut',
    '.uvmpw',
    '.uvopt',
    '.uvoptx',
    '.uvproj',
    '.uvprojx',
    '.vcproj',
    '.vcxproj',
    '.version',
    '.webserver',
    '.wpj',
    '.wsdt',
    '.wsp',
    '.wspos',
    '.wsx',
    '.x',
    '.xbcd',
    '.xcl',
    '.xise',
    '.xml',
    '.xmp',
    '.xmsgs',
    '.xsl',
    '.yml',
    '.md',
    '.zip'
]

FREERTOS_IGNORED_PATTERNS = [
    r'.*\.git.*',
    r'.*mbedtls_config\.h.*',
    r'.*mbedtls_config\.h.*',
    r'.*CMSIS.*',
    r'.*/Nordic_Code/*',
    r'.*/ST_Code/*',
    r'.*/makefile',
    r'.*/Makefile',
    r'.*/printf-stdarg\.c.*',
    r'.*/startup.*',
    r'.*/Startup.*',
    r'.*/trcConfig\.h.*',
    r'.*/trcConfig\.c.*',
    r'.*/trcSnapshotConfig\.h.*',
    r'.*/trcKernelPortConfig\.h.*',
    r'.*/MicroZed_hw_platform.*',
    r'.*/ThirdParty/.*',
    r'FreeRTOS\-Plus/Demo/Common/WinPCap/.*',
    r'FreeRTOS\-Plus/Source/FreeRTOS-Plus-Trace/.*',
    r'FreeRTOS-Plus/Demo/FreeRTOS_Plus_CLI_with_Trace_Windows_Simulator/Trace_Recorder_Configuration/.*',
    r'FreeRTOS/Demo/lwIP_AVR32_UC3/.*',
    r'FreeRTOS/Demo/Tensilica_Simulator_Xplorer_XCC/.*',
    r'FreeRTOS/Demo/CORTEX_LM3S102_GCC/makedefs',
    r'FreeRTOS/Demo/AVR32_UC3/FreeRTOSConfig.h',
    r'FreeRTOS/Demo/RX700_RX72N_EnvisionKit_GCC_e2studio/src/smc_gen/.*',
    r'FreeRTOS/Demo/RX700_RX72N_EnvisionKit_IAR_e2studio_EWRX/src/smc_gen/.*',
    r'FreeRTOS/Demo/RX700_RX72N_EnvisionKit_Renesas_e2studio_CS\+/src/smc_gen/.*'
]

FREERTOS_IGNORED_FILES = [
    '.cproject',
    '.project',
    'fyi-another-way-to-ignore-file.txt',
    'mbedtls_config.h',
    'requirements.txt',
    'run-cbmc-proofs.py',
    '.editorconfig',
    'lcovrc',
    'htif.c', 'htif.h',
    'ethernetif.c',
    'platform.c',
    'platform.h',
    'platform_config.h',
    'FreeRTOS_asm_vectors.S',
    'interrupt_vector.s',
    'reg_test.S',
    'gdbinit'
]

FREERTOS_HEADER = [
    '/*\n',
    ' * FreeRTOS V202112.00\n',
    ' * Copyright (C) 2020 Amazon.com, Inc. or its affiliates.  All Rights Reserved.\n',
    ' *\n',
    ' * Permission is hereby granted, free of charge, to any person obtaining a copy of\n',
    ' * this software and associated documentation files (the "Software"), to deal in\n',
    ' * the Software without restriction, including without limitation the rights to\n',
    ' * use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of\n',
    ' * the Software, and to permit persons to whom the Software is furnished to do so,\n',
    ' * subject to the following conditions:\n',
    ' *\n',
    ' * The above copyright notice and this permission notice shall be included in all\n',
    ' * copies or substantial portions of the Software.\n',
    ' *\n',
    ' * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR\n',
    ' * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS\n',
    ' * FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR\n',
    ' * COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER\n',
    ' * IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN\n',
    ' * CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.\n',
    ' *\n',
    ' * https://www.FreeRTOS.org\n',
    ' * https://github.com/FreeRTOS\n',
    ' *\n',
    ' */\n',
]

FREERTOS_COPYRIGHT_REGEX = r"^( *(\/\*|\*|#|\/\/))? Copyright \(C\) 20\d\d Amazon.com, Inc. or its affiliates.  All Rights Reserved\.( \*\/)?$"

def main():
    parser = HeaderChecker.configArgParser()
    args   = parser.parse_args()

    # Configure the checks then run
    checker = HeaderChecker(FREERTOS_HEADER, copyright_regex=FREERTOS_COPYRIGHT_REGEX)
    checker.ignoreExtension(*FREERTOS_IGNORED_EXTENSIONS)
    checker.ignorePattern(*FREERTOS_IGNORED_PATTERNS)
    checker.ignoreFile(*FREERTOS_IGNORED_FILES)
    checker.ignoreFile(os.path.split(__file__)[-1])

    rc = checker.processArgs(args)
    if rc:
        checker.showHelp(__file__)

    return rc

if __name__ == '__main__':
    exit(main())

