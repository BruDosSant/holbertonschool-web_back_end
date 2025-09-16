import ClassRoom from "./0-classroom";
export default function initializeRooms() {
    const messi = new ClassRoom(19);
    const messi2 = new ClassRoom(20);
    const messi3 = new ClassRoom(34);
    return [messi, messi2, messi3];
}