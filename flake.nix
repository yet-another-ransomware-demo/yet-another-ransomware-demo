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
          pkgs.python311
          pkgs.virtualenv
          pkgs.gnumake
          pkgs.zlib
        ];
        profile = ''
          source venv/bin/activate
        '';
      };
    in
    {
      devShells.${system}.default = fhs.env;
    };
}


