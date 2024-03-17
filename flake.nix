{
  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
  };

  outputs = { self, nixpkgs }:
    let
      system = "x86_64-linux";
      pkgs = nixpkgs.legacyPackages.${system};
      fhs = pkgs.buildFHSUserEnv {
        name = "fhs-shell";
        targetPkgs = pkgs: [
          (pkgs.python311.withPackages (ps: with ps; [
            tkinter
            cryptography
            rsa
          ]))
          pkgs.gnumake
          pkgs.zlib
          pkgs.libGL
          pkgs.glib
          pkgs.stdenv.cc.cc
        ];
        profile = ''
        '';
      };
    in
    {
      devShells.${system}.default = fhs.env;
    };
}


