{
    "targets": [
        {
            "target_name": "multihashing",
            "sources": [
                "algos/multihashing.cc",
                "algos/allium.c",
                "algos/bcrypt.c",
                "algos/blake.c",
                "algos/blake2s.c",
                "algos/boolberry.cc",
                "algos/c11.c",
                "algos/cryptonote/cryptonight.c",
                "algos/cryptonote/cryptonight_fast.c",
                "algos/cryptonote/cryptonight_lite.c",
                "algos/cryptonote/cryptonight_dark.c",
                "algos/cryptonote/cryptonight_dark_lite.c",
                "algos/cryptonote/cryptonight_soft_shell.c",
                "algos/cryptonote/cryptonight_turtle.c",
                "algos/cryptonote/cryptonight_turtle_lite.c",
                "algos/fresh.c",
                "algos/fugue.c",
                "algos/gost.c",
                "algos/gr.c",
                "algos/groestl.c",
                "algos/hefty1.c",
                "algos/hsr14.c",
                "algos/keccak.c",
                "algos/lbry.c",
                "algos/Lyra2.c",
                "algos/Lyra2RE.c",
                "algos/Lyra2REV2.c",
                "algos/Lyra2REV3.c",
                "algos/Lyra2Z.c",
                "algos/lyra2z16m330.c",
                "algos/lyra2z330.c",
                "algos/m7.c",
                "algos/magimath.c",
                "algos/minotaur.c",
                "algos/neoscrypt.c",
                "algos/nist5.c",
                "algos/odo.cc",
                "algos/phi1612.c",
                "algos/quark.c",
                "algos/qubit.c",
                "algos/scryptjane.c",
                "algos/scryptn.c",
                "algos/sha1.c",
                "algos/sha256d.c",
                "algos/shavite3.c",
                "algos/skein.c",
                "algos/skunk.c",
                "algos/sm3.c",
                "algos/Sponge.c",
                "algos/tribus.c",
                "algos/whirlpoolx.c",
                "algos/x11.c",
                "algos/x13.c",
                "algos/x15.c",
                "algos/x16r.c",
                "algos/x16rt.c",
                "algos/x17.c",
                "algos/x21s.c",
                "algos/xevan.c",
                "algos/zr5.c",
                "algos/sha3/aes_helper.c",
                "algos/sha3/hamsi.c",
                "algos/sha3/KeccakP-800-reference.c",
                "algos/sha3/sph_haval.c",
                "algos/sha3/sph_hefty1.c",
                "algos/sha3/sph_fugue.c",
                "algos/sha3/sph_blake.c",
                "algos/sha3/sph_blake2s.c",
                "algos/sha3/sph_bmw.c",
                "algos/sha3/sph_cubehash.c",
                "algos/sha3/sph_echo.c",
                "algos/sha3/sph_gost.c",
                "algos/sha3/sph_groestl.c",
                "algos/sha3/sph_jh.c",
                "algos/sha3/sph_keccak.c",
                "algos/sha3/sph_luffa.c",
                "algos/sha3/sph_shavite.c",
                "algos/sha3/sph_simd.c",
                "algos/sha3/sph_skein.c",
                "algos/sha3/sph_whirlpool.c",
                "algos/sha3/sph_shabal.c",
                "algos/sha3/sph_ripemd.c",
                "algos/sha3/sph_sha2.c",
                "algos/sha3/sph_sha2big.c",
                "algos/sha3/sph_tiger.c",
                "algos/sph/sph_cubehash.h", 
                "algos/sph/sph_echo.h",
                "algos/sph/sph_fungue.h",
                "algos/sph/sph_gost.h",
                "algos/sph/sph_jh.h",
                "algos/sph/sph_skein.h",
                "algos/yescrypt/sha256_Y.c",
                "algos/yescrypt/yescrypt-best.c",
                "algos/yescrypt/yescryptcommon.c",
                "algos/crypto/aesb.c",
                "algos/crypto/c_blake256.c",
                "algos/crypto/c_groestl.c",
                "algos/crypto/c_jh.c",
                "algos/crypto/c_keccak.c",
                "algos/crypto/c_skein.c",
                "algos/crypto/hash.c",
                "algos/crypto/oaes_lib.c",
                "algos/crypto/odocrypt.cpp",
                "algos/crypto/wild_keccak.cpp"
            ],
            'conditions': [
                ['OS=="linux"',
                  {
                    'link_settings': {
                      'libraries': [
                        '-lgmp'
                      ]
                    }
                  }
                ],
                ['OS=="mac"',
                  {
                    'link_settings': {
                      'libraries': [
                        '-lgmp'
                      ]
                    }
                  }
                ],
                ['OS=="win"',
                  {
                    'link_settings': {
                      'libraries': [
                        '-lgmp.lib'
                      ],
                    }
                  }
                ]
              ],
            "include_dirs": [
                "algos/crypto"
            ],
            "cflags_cc": [
                "-std=c++0x"
            ],
        }
    ]
}
