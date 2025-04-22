import argparse 
from face_search.face_cropper import crop_faces_and_save 
from face_search.face_matcher import match_target_face

def main():
    parser = argparse.ArgumentParser(description="Face tool CLI: crop or match")
    subparsers = parser.add_subparsers(dest="command", required=True)

    crop_parser = subparsers.add_parser("crop", help="Crop faces")
    crop_parser.add_argument("--image", required=True)
    crop_parser.add_argument("--output_dir", default="./storage")

    matcher_parser = subparsers.add_parser("match", help="Match target face")
    matcher_parser.add_argument("--target", required=True)
    matcher_parser.add_argument("--storage", default="./storage")
    matcher_parser.add_argument("--tolerance", type=float, default=0.3)

    args = parser.parse_args()

    if args.command == "crop":
        result = crop_faces_and_save(args.image, args.output_dir)
        for path in result:
            print(path)
    elif args.command == "match":
        result = match_target_face(args.target, args.storage, args.tolerance)
        for r in result:
            print(f"{r['matched_file']} (distance: {r['distance']:.4f})")

if __name__ == "__main__":
    main()
