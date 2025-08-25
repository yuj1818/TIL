import { getAllEvents } from '@/dummy-data';
import EventList from '@/components/events/event-list';
import EventSearch from '@/components/events/event-search';
import { useRouter } from 'next/router';

function AllEventsPage() {
  const router = useRouter();
  const events = getAllEvents();

  function findEventsHandler(year, month) {
    router.push(`/events/${year}/${month}`);
  }

  return (
    <div>
      <EventSearch onSearch={findEventsHandler} />
      <EventList items={events} />
    </div>
  );
}

export default AllEventsPage;
