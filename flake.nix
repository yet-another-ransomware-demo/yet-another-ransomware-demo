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
        targetPkgs = pkgs: with pkgs; [
          (python310.withPackages (ps: with ps; [
            tkinter
            cryptography
            rsa
            virtualenv
          ]))
          tcl
          gnumake
          zlib
          libGL
          glib
          stdenv.cc.cc
        ];
        profile = ''
        '';
      };
    in
    {
      devShells.${system}.default = fhs.env;
    };
}


