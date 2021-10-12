// Copyright (c) 2019 The RPG Core developers
// Distributed under the MIT software license, see the accompanying
// file COPYING or http://www.opensource.org/licenses/mit-license.php.
#ifndef X21S_H
#define X21S_H

#ifdef __cplusplus
extern "C" {
#endif

#include <stdint.h>

void x21s_hash(const char* input, char* output, uint32_t len);

#ifdef __cplusplus
}
#endif

#endif